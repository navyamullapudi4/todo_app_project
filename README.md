# Todo web app


This is a simple Django web app that let's a user create a todo item list and click the complete button to move it to completed item list.

## Demo
Hosted on AWS Lightsail
http://18.133.233.8:8000/

## Features

1. User signup
2. Create todo items
3. Users and todo lists are stored in database(Sqlite3)
4. Move todo item to completed list
5. Delete the todo item

![item list](doc_images/Currentitems.png?raw=true "Title")
![editing todo list](doc_images/Editingtodoitem.png?raw=true "Title")


## Getting Started


#### Prerequisites

1. Python 3.8 and pip
2. Django 3.1


#### Installing

```
pip3 install django

git clone git@github.com:navyamullapudi4/todo_app_project.git

cd todo_app_project

```

#### Running the application

`python3 manage.py runserver`

#### Running the tests

`python3 manage.py tests`



