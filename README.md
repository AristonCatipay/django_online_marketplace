![HandMeDown](/readme_images/handmedown_desktop.png)
# HandMeDown - an Online Marketplace

HandMeDown is a Django website for an Online Marketplace where users can sell their preloved items.

## Run Locally

To use this application you have to clone this repository using git bash.

### Clone the repository
- Open the directory you want this application to be cloned. 
- Open git bash.

```bash
git clone https://github.com/AristonCatipay/django_online_marketplace.git
```

### Install Dependencies

Activate virtual environment
```bash
pipenv shell
```

Install Django
```bash
pipenv install django
```

Install MySQL Client
```bash
pipenv install mysqlclient
```

Install Pillow
```bash
pipenv install pillow
```

Install Tailwind
```bash
pipenv install django-tailwind
```

Install Django Tailwind Reload
```bash
pipenv install django-tailwind[reload]
```

Create a database named 'django_online_marketplace' 
using your RDMS of choice (in this case using XAMPP Server).

![Create_a_database](/readme_images/xampp_create_database.PNG)

Edit your database configuration in the settings.py.
![Database_Configuration](/readme_images/change_database_settings.png)

Migrate
```bash
python manage.py migrate
```

Start the server
```bash
python manage.py runserver
```

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)