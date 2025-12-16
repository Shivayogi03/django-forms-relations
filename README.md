# Django Topic–Webpage–AccessRecord Project

This is a Django project demonstrating how to use **ModelForms** with
**OneToOne relationships** across multiple models and save them using
a **single HTML form**.

---

## 🚀 Features
- Django ModelForms
- OneToOneField relationships
- Single page registration form
- Manual foreign key assignment using `commit=False`
- CSRF protection

---

## 🧱 Models Structure
Topic → Webpage → AccessRecord

yaml
Copy code

- **Topic**
  - topic_name (Primary Key)

- **Webpage**
  - OneToOneField with Topic
  - name, url, email

- **AccessRecord**
  - OneToOneField with Webpage
  - author, date

---

## 🖥️ Technologies Used
- Python
- Django
- HTML
- SQLite (default Django DB)

---

## ⚙️ How to Run the Project

```bash
# Clone the repository
git clone https://github.com/your-username/django-topic-webpage-accessrecord.git

# Go inside the project
cd django-topic-webpage-accessrecord

# Create virtual environment (optional)
python -m venv env
env\Scripts\activate   # Windows
source env/bin/activate # Linux/Mac

# Install Django
pip install django

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver
📌 Learning Outcome
This project helps understand:

Django ModelForms

commit=False

Handling related models

Saving dependent models in correct order

