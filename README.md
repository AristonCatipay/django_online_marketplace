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

### Install Dependencies

Install Pipenv

```bash
pip install pipenv
```

Activate Virtual Environment

```bash
pipenv shell
```

Make sure you have `Python 3.11`
Go to [Python 11](https://www.python.org/downloads/release/python-3119/)
If you have multiple installation of python. Choose the python 11.

```bash
pipenv --python path\to\python.exe
```

Install Dependencies

```bash
pipenv install
```

Migrate

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
