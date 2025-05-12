package com.CRUDapi.app.rest.Repo;

import org.springframework.data.jpa.repository.JpaRepository;

import com.CRUDapi.app.rest.Models.User;

public interface UserRepo extends JpaRepository<User, Long> {

}
