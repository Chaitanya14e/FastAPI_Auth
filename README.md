# FastAPI Auth API

A secure authentication API built with FastAPI and Supabase Auth.

## Features

- User signup with Supabase Auth
- User login with JWT access tokens
- Protected API routes
- JWT verification using Supabase
- Reusable FastAPI authentication dependency
- Logout endpoint
- Swagger UI with Bearer authentication
- Public and protected routes

## Tech Stack

- Python
- FastAPI
- Supabase Auth
- PostgreSQL through Supabase
- JWT
- Swagger / OpenAPI

## Project Structure

```text
auth-api/
│
├── app/
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── protected_routes.py
│   │
│   ├── auth_dependency.py
│   ├── main.py
│   ├── schemas.py
│   └── __init__.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md