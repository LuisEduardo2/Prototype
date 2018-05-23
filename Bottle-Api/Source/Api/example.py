from bottle import route, Bottle, response, request, auth_basic
from json import dumps, load

def returnJson(data={},code=200):
    response.content_type='application/json'
    response.status = code
    return dumps(data)

#basic http authentication (username and password)
def checklogin(username, password):
    if (username,password) == ('username','password'):
        return True
    return False #return status code 401

data = [
    {
        'id':1,
        'fruit':'pineapple'
    },{
        'id':2,
        'fruit':'watermelon'
    },{
        'id':3,
        'fruit':'strawberry'
    } ]

app = Bottle()


@app.route('/getall', method=['GET'])
def get_values():
    return returnJson({'values':data})


@app.route('/getvalue/<id:int>', method=['GET'])
def get_value(id):
    value = [value for value in data if value['id'] == id]
    if len(value) == 0:
        return returnJson({"message":"values not found"},404)
    return returnJson({'values':value})


'CREATE A UNIQUE VALUE, BASIC AUTHORIZATION (username and password) IS REQUIRED'
#username and password authentication is required
@app.route('/insert', method=['POST'])
@auth_basic(checklogin)
def create_value():
    if not request.json or not 'fruit' in request.json:
        return returnJson({"message":"values not found"},404)
    newdata = {
        'id': data[-1]['id'] + 1,
        'fruit': request.json['fruit']
    }
    data.append(newdata)
    return returnJson({'Success':'values ​​added successfully'},201)


'UPDATE A SPECIFIC VALUE, BASIC AUTHORIZATION (username and password) IS REQUIRED'
#username and password authentication is required
@app.route('/update/<id:int>', method=['PUT'])
@auth_basic(checklogin)
def update_values(id):
    if not request.json or not 'fruit' in request.json:
        return returnJson({"message":"values not found"},404)
    for index,value in enumerate(data):
        if value['id'] == id:
            data[index]['fruit'] = request.json['fruit']
            return returnJson(value,200)
    return returnJson({"message":"values not found"},404)


'DELETE A SPECIFIC VALUE, BASIC AUTHORIZATION (username and password) IS REQUIRED'
#username and password authentication is required
@app.route('/delete/<id:int>', method=['DELETE'])
@auth_basic(checklogin)
def delete_values(id):
    for index,value in enumerate(data):
        if value['id'] == id:
            return returnJson(data.pop(id), 200)
    return returnJson({"message":"values not found"},200)