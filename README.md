# Medical_App

##App structure:
.
└── medical_app
    ├── __init__.py
    ├── crud
    │   ├── __init__.py
    │   └── medical.py  # Handling CRUD operations for medical data
    ├── database.py  # Handles the database connection
    ├── main.py  # Entry point for FastAPI application
    ├── models.py  # Defines the database models
    ├── schemas.py  # Defines Pydantic models for validation and serialization
    └── routers
        ├── __init__.py
        ├── respiratory.py
        ├── urinary.py
        ├── git.py
        ├── pediatric.py
        └── miscellaneous.py
