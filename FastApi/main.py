from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import Session
from pydantic import BaseModel

from typing import List
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    email= Column(String , unique=True, index=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

#CREATE

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str

    class Config:
        from_attributes = True


@app.post("/user/", response_model=UserResponse)
def create_user(user: UserCreate, db :Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#READ

@app.get("/user/",response_model=List[UserResponse])
def read_users(skip:int =0, limit:int = 10, db:Session=Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.get("/user/{user_id}",response_model=UserResponse)
def read_users(user_id:int , db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        return HTTPException(status_code=404, detail="User not found")
    return user

#UPDATE

class UserUpdate(BaseModel):
    name:Optional[str] = None
    email:Optional[str] = None


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id:int , user:UserUpdate, db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.name = user.name if user.name is not None else db_user.name
    db_user.email = user.email if user.email is not None else db_user.email
    db.commit()
    db.refresh(db_user)
    return db_user


#DELETE

@app.delete("/user/{user_id}", response_model=UserResponse)
def del_user(user_id:int , db: Session=Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code= 404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return db_user