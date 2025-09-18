# Django Project

A Django web application following a clean architecture pattern with separated concerns for better maintainability and scalability.

## Project Structure

```
django_project/
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database file
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
├── app/                        # Main application package
│   ├── __init__.py
│   ├── admin.py               # Django admin configuration
│   ├── apps.py                # Application configuration
│   ├── controllers/           # Request handlers (views)
│   │   ├── __init__.py
│   │   └── user_controller.py # User-related endpoints
│   ├── dtos/                  # Data Transfer Objects
│   │   ├── __init__.py
│   │   ├── common_dto.py      # Common data structures
│   │   └── user_dto.py        # User-related DTOs
│   ├── migrations/            # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py    # Initial database schema
│   ├── models/                # Database models
│   │   ├── __init__.py
│   │   └── user.py            # User model definition
│   ├── repositories/          # Data access layer
│   │   ├── __init__.py
│   │   └── user_repo.py       # User data operations
│   ├── services/              # Business logic layer
│   │   ├── __init__.py
│   │   └── user_service.py    # User business logic
│   └── utils/                 # Utility modules
│       ├── __init__.py
│       ├── exceptions.py      # Custom exceptions
│       └── response.py        # Response utilities
└── django_project/            # Django project configuration
    ├── __init__.py
    ├── asgi.py                # ASGI configuration
    ├── settings.py            # Django settings
    ├── urls.py                # URL routing
    └── wsgi.py                # WSGI configuration
```

## Architecture Overview

This project follows a layered architecture pattern to separate concerns and improve code organization:

### 1. Controllers Layer (`app/controllers/`)
- **Purpose**: Handle HTTP requests and responses
- **Responsibilities**: 
  - Parse incoming requests
  - Validate input data
  - Call appropriate services
  - Format responses
- **Files**: 
  - `user_controller.py` - Handles user-related HTTP endpoints

### 2. Services Layer (`app/services/`)
- **Purpose**: Contains business logic and orchestrates operations
- **Responsibilities**:
  - Implement business rules
  - Coordinate between repositories
  - Handle complex operations
- **Files**:
  - `user_service.py` - User business logic and operations

### 3. Repository Layer (`app/repositories/`)
- **Purpose**: Data access abstraction
- **Responsibilities**:
  - Database operations (CRUD)
  - Query optimization
  - Data persistence logic
- **Files**:
  - `user_repo.py` - User data access operations

### 4. Models Layer (`app/models/`)
- **Purpose**: Database schema definition
- **Responsibilities**:
  - Define database tables
  - Model relationships
  - Data validation rules
- **Files**:
  - `user.py` - User model definition

### 5. DTOs (Data Transfer Objects) (`app/dtos/`)
- **Purpose**: Data structure definitions for API communication
- **Responsibilities**:
  - Define request/response formats
  - Data serialization/deserialization
  - Input validation schemas
- **Files**:
  - `common_dto.py` - Shared data structures
  - `user_dto.py` - User-specific DTOs

### 6. Utilities (`app/utils/`)
- **Purpose**: Common utilities and helpers
- **Responsibilities**:
  - Custom exceptions
  - Response formatting
  - Helper functions
- **Files**:
  - `exceptions.py` - Custom exception classes
  - `response.py` - Response formatting utilities

## Getting Started

### Prerequisites
- Python 3.8+
- Django 5.2.3+

### Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Database

The project uses SQLite as the default database (`db.sqlite3`). The database file is automatically created when you run migrations.

## Development Guidelines

### Adding New Features

1. **Models**: Define your data structure in `app/models/`
2. **DTOs**: Create request/response schemas in `app/dtos/`
3. **Repository**: Implement data access in `app/repositories/`
4. **Service**: Add business logic in `app/services/`
5. **Controller**: Create API endpoints in `app/controllers/`

### Code Organization Principles

- **Single Responsibility**: Each layer has a specific purpose
- **Dependency Direction**: Controllers → Services → Repositories → Models
- **Separation of Concerns**: Business logic separate from data access
- **Testability**: Each layer can be unit tested independently

## Configuration

### Settings
Main Django settings are in `django_project/settings.py`:
- Database configuration
- Installed apps
- Middleware
- Static files
- Security settings

### URL Configuration
URL routing is defined in `django_project/urls.py`

## Contributing

1. Follow the existing architecture patterns
2. Add appropriate tests for new features
3. Update this README when adding new modules
4. Follow Python PEP 8 style guidelines

## License

This project is for educational/development purposes.