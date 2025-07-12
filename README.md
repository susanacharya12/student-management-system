# 🎓 Student Management System (CRUD) – Django

![Django](https://img.shields.io/badge/Django-5.2-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A simple Student Management System built using Django and SQLite3.  
It provides an admin-friendly interface to **Create, Read, Update, and Delete (CRUD)** student records and includes basic data visualization using Chart.js to display grade-wise distribution.

---

## 🚀 Features

- Add, update, and delete student records
- View all student records in a list
- Simple and responsive UI using Django Templates
- Grade distribution chart using Chart.js
- Admin panel for backend control

---

## 📁 Project Directory Structure

```plaintext
student-management-system/
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
├── db.sqlite3
├── student_mgmt/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── students/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   └── templates/
│       └── students/
│           ├── student_list.html
│           ├── student_form.html
│           └── student_confirm_delete.html


⚙️ Setup Instructions

1. Clone the Repository
git clone https://github.com/susanacharya12/student-management-system.git
cd student-management-system

2. Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Optional)
python manage.py createsuperuser

6. Start the Development Server
python manage.py runserver


📊 Data Visualization

The dashboard includes a simple bar chart showing the number of students per grade using Chart.js.

🛠️ Technologies Used

Backend: Django 5.2
Frontend: HTML5, CSS3, Chart.js
Database: SQLite3
Tools: Git, GitHub, PyCharm

📄 License

This project is licensed under the MIT License.
