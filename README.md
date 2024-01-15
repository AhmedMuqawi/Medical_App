# Medical_App

# Medical App Structure

This repository contains a FastAPI-based application for managing medical information. Below is the directory structure and brief descriptions of each file/folder:
### Structure:
```
.
└── Medical_app
    ├── __init__.py  # Package initializer
    ├── medical_info.py  # selecting medical data
    ├── database.py  # Manages the database connection
    ├── main.py  # Entry point for FastAPI application
    ├── schemas.py  # Defines Pydantic models
    └── routers
        ├── __init__.py  # Initialization for the routers package
        ├── respiratory.py  # Routes for respiratory diseases
        ├── urinary.py  # Routes for urinary tract diseases
        ├── git.py  # Routes for gastrointestinal diseases
        ├── pediatric.py  # Routes for pediatric emergencies
        └── miscellaneous.py  # Routes for miscellaneous diseases
```
### File Descriptions:

- `medical_app/`: Root directory for the FastAPI application.
- `medical_app/__init__.py`: Empty file indicating it's a Python package.
- `medical_app/medical_info.py`: File containing functions for CRUD operations.
- `medical_app/database.py`: Manages the database connection.
- `medical_app/main.py`: Main entry point for the FastAPI application.
- `medical_app/schemas.py`: Defines Pydantic models for validation and serialization.
- `medical_app/routers/`: Directory containing different route handlers.
- `medical_app/routers/__init__.py`: Empty file indicating it's a Python package.
- `medical_app/routers/respiratory.py`: Routes related to respiratory diseases.
- `medical_app/routers/urinary.py`: Routes related to urinary tract diseases.
- `medical_app/routers/git.py`: Routes related to gastrointestinal diseases.
- `medical_app/routers/pediatric.py`: Routes related to pediatric emergencies.
- `medical_app/routers/miscellaneous.py`: Routes related to miscellaneous diseases.


 chmod +x MedicalInfoDB/import.sh
ahmed@pop-os:~/Desktop/learning python/medical_app/Medical_App$ ls -l MedicalInfoDB/import.sh
-rwxrwxr-x 1 ahmed ahmed 1104 Jan 14 23:14 MedicalInfoDB/import.sh

http://localhost/docs