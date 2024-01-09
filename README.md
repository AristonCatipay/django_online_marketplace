![HandMeDown](/readme_images/handmedown_desktop.png)
# HandMeDown - an Online Marketplace

HandMeDown is a Django-based website for an online marketplace where users can buy and sell pre-owned items. You can use the built-in front end using Django templates or interact with the system via API.

### Features
- User Authentication: Secure user registration and login functionalities.
- Item Management: Ability for users to add, edit, and delete items for sale.
- Search and Filters: Enables users to search for specific items and apply filters.
- Messaging App: Allows users to communicate the seller of the item with queries or questions.

## Run Locally

To use this application you have to clone this repository using git bash.

### Clone the repository
- Open the directory you want this application to be cloned. 
- Open git bash.

```bash
git clone https://github.com/AristonCatipay/django_online_marketplace.git
```

### Install Dependencies using `requirements.txt`
Install project dependencies
```bash
pip install -r requirements
```

### Install Dependencies manually
#### Note: If the `requirements.txt` is available you can skip this.

Activate virtual environment
```bash
pipenv shell
```

Install Django
```bash
pipenv install django
```

Install Django REST Framework
```bash
pipenv install djangorestframework
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

Start the server (Make sure your RDBMS is also running.)
```bash
python manage.py runserver
```

### Note: I want to add my own data and images. (Without dummy data and Stock Images)
- Go to `media` > `item_images` > Delete all stock images.
- Go to `media` > `profile_images` > Delete all stock images.


### Note: App with Dummy Data and Stock Images
If you want to see the full application with `dummy data` and `stock images` you can use the SQL file provided in the project named `django_online_marketplace.sql`.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)