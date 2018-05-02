from flask import Flask, jsonify

from Api.example import example

application = Flask(__name__)
application.register_blueprint(example)

@application.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

''' 
#this runner still working, but it is no longer recommended for this and future flask versions
if __name__ == '__main__':
    application.run(host='0.0.0.0',port=5000,debug=True)
'''