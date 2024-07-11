### 1. Creating a Virtual Environment

First of all, it is a recommended practice to use a virtual environment to isolate project dependencies. Here is how to do this using `venv`:

#### Windows:

``bash
# Create a new virtual environment in the 'myproject_env' folder
python -m venv myproject_env

# Activate the virtual environment
myproject_env\Scriptsactivate
```

#### macOS/Linux:

``bash
# Create a new virtual environment in the 'myproject_env' folder
python3 -m venv myproject_env

# Activate the virtual environment
source myproject_env/bin/activate
```

### 2. Installing Dependencies

After activating the virtual environment, you can install the project dependencies listed in the file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Creating a New Django Project

We create a new Django project called `myproject`:

```bash
django-admin startproject myproject
cd myproject
```

### 4. Database Configuration

Edit the database settings in the file `myproject/settings.py` to configure the database you want to use (e.g. SQLite, PostgreSQL, MySQL).

```python
# settings.py

DATABASES = {
    default': {
        ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 5. Applying Initial Migrations

Applies initial migrations to create database tables:

```bash
python manage.py migrate
```

### 6. Creating the Admin Account

Create a superuser to access Django's admin interface:

```bash
python manage.py createsuperuser
```

Follow the instructions to create a username, email address, and password for the admin account.

### 7. Starting the Development Server

Finally, start the development server to check that everything is configured correctly:

```bash
python manage.py runserver
```

You can now access your Django project at ``http://127.0.0.1:8000/` and the administration interface at ``http://127.0.0.1:8000/admin/`.
