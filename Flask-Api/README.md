## Instalation
> pip install -r requirements.txt
## Run
> python run.py
## Basic authentication is required in POST, PUT and DELETE
  - Login: **username**
  - Pass: **password**
## Routes
  - GET
    - Retrieve all values
      > localhost/todo/getall
    - Retrive a one specific fruit by id identification
      > localhost/todo/getvalue/1
  - POST
    - Register a new value
      > {'fruit':'tomato'} <br/> localhost/todo/insert
  - PUT
    - Uptade a specific value
      > {'fruit':'blueberry'} <br/> localhost/todo/update/1
  - DELETE
    - Delete a specific value
      > localhost/todo/delete/3
