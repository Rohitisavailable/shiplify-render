# Shiplify

Shiplify is a Django courier-management application for tracking incoming packages and keeping collection teams organized. The public home page explains the product, while authenticated users get a focused package desk and administrators manage courier records through Django Admin.

## Live Application

- Public home: [shiplify-render.onrender.com](https://shiplify-render.onrender.com/)
- Repository: [github.com/Rohitisavailable/shiplify-render](https://github.com/Rohitisavailable/shiplify-render)

## Features

- Public logistics-focused home page with warehouse and shipping imagery
- User registration, login, logout, and password reset flows
- Authenticated package dashboard with pagination
- Package-number-only search
- Django Admin management for courier records
- Upcoming-features roadmap page linked beside the dashboard
- Responsive custom CSS UI with desktop and mobile layouts
- GitHub and LinkedIn profile links in the public home page
- WhiteNoise static-file serving for production

## Application Routes

| Route | Purpose | Access |
| --- | --- | --- |
| `/` | Public Shiplify home page | Public |
| `/login/` | User sign-in | Public |
| `/register/` | Create an account | Public |
| `/password-reset/` | Request a password reset | Public |
| `/main/` | Package dashboard and package-number search | Authenticated |
| `/upcoming/` | Upcoming features roadmap | Authenticated |
| `/about/` | Product information | Public |
| `/admin/` | Django administration | Staff |

## Technology

- Python 3.13
- Django 5.1.7
- SQLite for local development
- PostgreSQL through `dj-database-url` in production
- Gunicorn application server
- WhiteNoise for static assets
- Custom CSS in `static/css/app.css`
- PostgreSQL driver: `psycopg2-binary`

## Local Setup

```bash
git clone https://github.com/Rohitisavailable/shiplify-render.git
cd shiplify-render
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS or Linux
source .venv/bin/activate
```

Install dependencies, migrate the database, and collect static files:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
```

Create an administrator when needed:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Testing and Checks

Run the system checks and regression tests with:

```bash
python manage.py check
python manage.py test
```

The test suite covers public home and login routes, authentication redirects, package-number search, social links, and nullable stock values.

## Render Deployment

The repository includes `render.yaml`. Render uses these commands:

```bash
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
gunicorn CMS.wsgi:application
```

Production should set:

- `DJANGO_ENV=production`
- `SECRET_KEY` to a long random value
- `ALLOWED_HOSTS` to the deployed hostnames
- `DATABASE_URL` for PostgreSQL
- `EMAIL_BACKEND` and SMTP variables if email delivery is required

The local default email backend is the console backend so password-reset flows can be tested without placeholder SMTP credentials.

## Project Structure

```text
shiplify-render/
├── CMS/                         # Django project settings and URLs
├── couriermanage/               # Courier model, dashboard, admin, templates
├── users/                       # Registration, stock model, auth templates
├── static/                      # Source CSS and images
├── staticfiles/                 # Collected static assets
├── manage.py
├── render.yaml                  # Render build and start configuration
├── requirements.txt
└── README.md
```

## Author

Rohit Mahajan

- GitHub: [Rohitisavailable](https://github.com/Rohitisavailable)
- LinkedIn: [rohit-mahajan1202](https://www.linkedin.com/in/rohit-mahajan1202/)
