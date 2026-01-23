# Shiplify - Courier Management System

A Django-based Courier Management System (CMS) designed to help manage courier deliveries, track packages, and maintain inventory stock.

## 🌐 Live Demo

**Live Application:** [https://shiplify-render.onrender.com/](https://shiplify-render.onrender.com/)

## 📖 Description

Shiplify is a web-based courier management system built with Django that provides a comprehensive solution for managing courier services. The application includes user authentication, courier tracking, and inventory management features.

## ✨ Features

- **User Authentication System**
  - User registration and login
  - Password reset functionality
  - Secure authentication with Django's built-in authentication system

- **Courier Management**
  - Track courier deliveries
  - Record package information (name, service, package number, date received)
  - Search and filter courier records
  - Paginated courier listing

- **Stock Management**
  - Inventory tracking system
  - Track item categories and quantities
  - Record receive and issue transactions
  - Monitor stock levels with reorder level alerts
  - Export data to CSV

- **Admin Dashboard**
  - Django admin interface for managing all data
  - User management capabilities

## 🛠️ Technology Stack

- **Backend Framework:** Django 5.1.7
- **Database:** SQLite (development), PostgreSQL (production via dj-database-url)
- **Web Server:** Gunicorn 23.0.0
- **Frontend Styling:** 
  - Bootstrap 4 & Bootstrap 5
  - Django Crispy Forms for form rendering
- **Other Libraries:**
  - BeautifulSoup4 for web scraping
  - psycopg2-binary for PostgreSQL support

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rohitisavailable/shiplify-render.git
   cd shiplify-render
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📱 Usage

1. **Login/Register**
   - Visit the home page and login with your credentials
   - New users can register through the registration page

2. **Managing Couriers**
   - Navigate to the main page to view all courier records
   - Use the search functionality to find specific packages
   - View paginated results for better organization

3. **Admin Functions**
   - Access the admin panel at `/admin/`
   - Manage users, couriers, and stock items
   - Configure system settings

## 📂 Project Structure

```
shiplify-render/
├── CMS/                  # Main Django project settings
│   ├── settings.py      # Project configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── couriermanage/       # Courier management app
│   ├── models.py        # Courier data models
│   ├── views.py         # Courier views
│   └── templates/       # Courier templates
├── users/               # User authentication app
│   ├── models.py        # Stock/User models
│   ├── views.py         # User views
│   └── templates/       # User templates
├── static/              # Static files (CSS, JS, images)
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## 🔐 Security Notes

- Change the `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` properly
- Use environment variables for sensitive data

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is available for educational and personal use.

## 👨‍💻 Author

**Rohit**
- GitHub: [@Rohitisavailable](https://github.com/Rohitisavailable)

## 🔗 Links

- **GitHub Repository:** [https://github.com/Rohitisavailable/shiplify-render](https://github.com/Rohitisavailable/shiplify-render)
- **Live Demo:** [https://shiplify-render.onrender.com/](https://shiplify-render.onrender.com/)
