## Instalation
> pip install -r requirements.txt
## Run
> flask run
## Basic authentication is required in POST, PUT and DELETE
  - Login: **username**
  - Pass: **password**
## Routes
  > flask routes
  - GET
    - Retrieve all values
      > localhost:5000/todo/getall
    - Retrive a one specific fruit by id identification
      > localhost:5000/todo/getvalue/1
  - POST
    - Register a new value
      > {'fruit':'tomato'} <br/> localhost:5000/todo/insert
  - PUT
    - Uptade a specific value
      > {'fruit':'blueberry'} <br/> localhost:5000/todo/update/1
  - DELETE
    - Delete a specific value
      > localhost:5000/todo/delete/3
