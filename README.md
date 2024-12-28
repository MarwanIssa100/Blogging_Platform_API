# Blogging_Platform_API

## API Documentation

### User Registration
- **Endpoint:** `/api/register/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string",
    "bio": "string",
    "profile_pic": "string (optional)"
  }
  ```
- **Response:**
  - **201 Created:** User successfully registered
  - **400 Bad Request:** Validation errors

### User Login
- **Endpoint:** `/api/login/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**
  - **200 OK:** Successful login with token
  ```json
  {
    "username": "string",
    "token": "string"
  }
  ```
  - **400 Bad Request:** Invalid username or password

### User Profile Update
- **Endpoint:** `/api/profile/update/`
- **Method:** `PUT`
- **Headers:** 
  - `Authorization: Token your-token-here`
- **Request Body:**
  ```json
  {
    "bio": "string (optional)",
    "profile_pic": "string (optional)"
  }
  ```
- **Response:**
  - **200 OK:** Profile updated successfully
  - **400 Bad Request:** Validation errors

### User Logout
- **Endpoint:** `/api/logout/`
- **Method:** `POST`
- **Headers:** 
  - `Authorization: Token your-token-here`
- **Response:**
  - **200 OK:** Successfully logged out

### Blog Management
- **Create Blog**
  - **Endpoint:** `/api/blog/create/`
  - **Method:** `POST`
  - **Request Body:**
  ```json
  {
    "title": "string",
    "content": "string",
    "tags": ["string"],
    "category": "string"
  }
  ```
  - **Response:**
    - **201 Created:** Blog successfully created
    - **400 Bad Request:** Validation errors

- **Update Blog**
  - **Endpoint:** `/api/blog/update/{id}/`
  - **Method:** `PUT`
  - **Headers:** 
    - `Authorization: Token your-token-here`
  - **Request Body:**
  ```json
  {
    "title": "string (optional)",
    "content": "string (optional)",
    "tags": ["string (optional)"],
    "category": "string (optional)"
  }
  ```
  - **Response:**
    - **200 OK:** Blog updated successfully
    - **400 Bad Request:** Validation errors

- **Delete Blog**
  - **Endpoint:** `/api/blog/delete/{id}/`
  - **Method:** `DELETE`
  - **Headers:** 
    - `Authorization: Token your-token-here`
  - **Response:**
    - **204 No Content:** Blog deleted successfully
    - **404 Not Found:** Blog not found

**Delete Tags**
  - **Endpoint:** `/api/tag/delete/{id}/`
  - **Method:** `DELETE`
  - **Response:**
    - **204 No Content:** Tag deleted successfully
    - **404 Not Found:** Tag not found

    **Create Category**
  - **Endpoint:** `/api/category/create/`
  - **Method:** `POST`
  - **Request Body:**
  ```json
  {
    "name": "string"
  }
  ```
    - **Headers:** 
    - `Authentication: you'er not admin`
  - **Response:**
    - **201 Created:** Category successfully created
    - **400 Bad Request:** Validation errors
