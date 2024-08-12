
## Overview
The project is structured in a modular way, with separate apps for `books` and `authors`.

## Requirements
- Python 3.8+ (Recommended Python:3.9.6)
- Django 4.2+
- Relational DB e.g Postgres

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AbrarMustafa/DataScienceSpotter.git
cd DataScienceSpotter
```

### 2. Create a Virtual Environment
If using VSCode’s default command palette, the virtual environment will be created as `.venv`. To activate it:

- **On macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```
- **On Windows:**
  ```bash
  .venv\Scripts\activate
  ```

### 3. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Set Up the Database
Run the following commands to create the database and apply migrations:
```bash
python manage.py migrate
```

### 5. Create a Superuser
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Testing
To run the tests for the project:
```bash
python manage.py test
```

## Directory Structure
```
DataScienceSpotter/
├── books/                  # Books app
├── authors/                # Authors app
├── DataScienceSpotter/     # Main project configuration
├── .venv/                  # Virtual environment
├── manage.py               # Django's CLI utility
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Deployment
For deploying to a production environment, refer to the Django documentation for guidance on:
- Setting `DEBUG = False`
- Configuring allowed hosts
- Database settings
- Static and media files

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to contribute to this project by submitting a pull request or opening an issue.

---

This README now reflects the `.venv` folder used for the virtual environment setup in VSCode.