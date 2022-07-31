# Ozon Price Checker

:cityscape: :cityscape: :cityscape:

A Price Checker/Tracker for [OZON.ru](ozon.ru). Gets data from their consumer API. No proxies were used so the access to the API might be blocked after you do too many requests. But you get unblocked quickly enough.

User Interface written in Russian, comments written in English.

## Preview

![ozon_checker_1](https://user-images.githubusercontent.com/86254474/159653407-562ca01a-0a84-4e09-89cc-19566a6480b4.png)

## Instructions

1. Clone this repository
2. Start a new Virtualenv, activate it, type in console `pip install -r requirements.txt`
3. Run the Django Server by typing in console `python manage.py runserver`

## Technologies 

Frontend: CSS, Bootstrap 5.1, a bit of JS.

Backend: Django 4.0 and Requests library.

Database: SQLite.

## To Do/To Add

- [x] Update delete confirm template; 

- [x] Add cancel functionality to delete; 

- [x] Add a discounted items list page/modal; 
