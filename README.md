# CRM Project

## Introduction
This CRM project is a system for managing customers, products, employees, and task boards. The system uses Django REST Framework to provide APIs and JWT for authentication.

## Installation

### Requirements
- Python 3.x
- Django
- Other required packages listed in `requirements.txt`

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone git@github.com:dung050509/crm_project.git
   cd crm_project
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
4. **Apply migrations:**
    ```bash
    python manage.py migrate
5. **Run the server:**
    ```bash
    python manage.py runserver

## Usage
### Accessing the Admin Page
#### Visit http://localhost:8000/admin/ to manage data.

### Accessing the API Documentation
#### Visit http://localhost:8000/api/swagger/ to view the API documentation.

### Important Endpoints
#### /api/register/: Register a new user.

#### /api/token/: Log in and obtain a JWT token.

#### /api/token/refresh/: Refresh the JWT token.

### Contribution
#### If you want to contribute to this project, please fork the repository and submit a pull request.

### Security
#### Make sure not to push sensitive information such as secret keys or configuration files to GitHub.

### Contact
#### If you have any questions, please contact me at vudungtb00@gmail.com.