# Todo List Application

A modern, feature-rich todo list web application built with Django. Manage your tasks efficiently with an intuitive user interface.

## Features

- ✅ Create, read, update, and delete tasks
- ✅ Mark tasks as complete or incomplete
- ✅ View task creation dates and times
- ✅ Beautiful, responsive UI with gradient design
- ✅ Mobile-friendly interface
- ✅ User authentication (Django admin)
- ✅ Real-time task statistics

## Tech Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (default) / PostgreSQL (optional)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Modern gradient design with responsive layout

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Paban-Bhandari/todo_list.git
   cd todo_list
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Todo List: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Usage

### Creating Tasks
- Navigate to the todo list homepage
- Enter your task title in the input field
- Click "Add" to create the task

### Managing Tasks
- **Mark Complete**: Click the "Done" button to mark a task as complete
- **Edit**: Click "Edit" to modify task details
- **Delete**: Click "Delete" to remove a task

### Viewing Statistics
- Task statistics are displayed at the top showing total tasks and completed count

## Project Structure

```
todo_list/
├── manage.py                 # Django management script
├── requirements.txt         # Project dependencies
├── db.sqlite3              # SQLite database
├── staticfiles/            # Compiled static files
├── todolist/               # Main project directory
│   ├── settings.py         # Django settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── tasks/                  # Todo app
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Admin configuration
│   ├── migrations/        # Database migrations
│   ├── static/
│   │   └── tasks/
│   │       └── styles.css # Application styling
│   └── templates/
│       └── tasks/
│           ├── base.html              # Base template
│           ├── task_list.html         # Task list view
│           ├── task_form.html         # Task form
│           └── task_confirm_delete.html # Delete confirmation
└── staticfiles/           # Compiled admin static files
```

## Database

### SQLite (Default)
The project uses SQLite by default. The database file is `db.sqlite3`.

### PostgreSQL (Optional)
To use PostgreSQL:

1. Update `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'todo_db',
           'USER': 'your_db_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

2. Install PostgreSQL adapter:
   ```bash
   pip install psycopg2-binary
   ```

## Configuration

### Settings
Key settings in `todolist/settings.py`:
- `DEBUG = True` - Development mode (set to False in production)
- `ALLOWED_HOSTS = ['*']` - Modify for production
- `DATABASES` - Database configuration
- `INSTALLED_APPS` - Registered applications

### Environment Variables (Optional)
Create a `.env` file for sensitive settings:
```
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
```

## API Routes

### Task URLs
- `GET /` - View all tasks
- `GET /task/<id>/` - View task details
- `POST /task/create/` - Create a new task
- `GET /task/<id>/edit/` - Edit task form
- `POST /task/<id>/edit/` - Update task
- `POST /task/<id>/delete/` - Delete task
- `GET /task/<id>/toggle/` - Toggle task completion

## Admin Panel

Access the Django admin at `/admin/` with your superuser credentials to:
- Manage tasks directly
- Create/edit users
- View application statistics
- Manage permissions

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

## Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Update `ALLOWED_HOSTS` with your domain
3. Set a secure `SECRET_KEY`
4. Use a production database (PostgreSQL recommended)
5. Configure static files serving
6. Set up HTTPS/SSL
7. Use a production WSGI server (Gunicorn, uWSGI)

### Example Deployment with Gunicorn
```bash
pip install gunicorn
gunicorn todolist.wsgi:application --bind 0.0.0.0:8000
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Troubleshooting

### Django Not Found
```bash
# Make sure virtual environment is activated and packages are installed
source venv/bin/activate
pip install -r requirements.txt
```

### Database Errors
```bash
# Reset migrations
python manage.py migrate tasks zero
python manage.py migrate
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --clear --noinput
```

### CSRF Token Error
- Refresh the form page after logging in
- Ensure cookies are enabled in your browser

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created by [Paban Bhandari](https://github.com/Paban-Bhandari)

## Support

For support, email bhandaripawan841@gmail.com or open an issue on GitHub.

## Changelog

### Version 1.0.0
- Initial release
- Basic CRUD operations for tasks
- Beautiful UI with gradient design
- Mobile responsive layout
- Task statistics display

---

**Happy todo-ing! 📝✅**
