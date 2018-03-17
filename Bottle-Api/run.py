from bottle import run, Bottle, response
from json import dumps
from Api.example import app

root = Bottle()

@root.error(404)
def error404(error):
    response.content_type='application/json'
    return dumps({'Error':'Not Found'})

@root.error(401)
def error404(error):
    response.content_type='application/json'
    return dumps({'Error':'Unauthorized access'})

if __name__ == '__main__':
    root.merge(app)
    run(root,
        host='0.0.0.0',port=80,
        debug=True,
        reloader=True
    )