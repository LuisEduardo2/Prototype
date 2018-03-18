from flask import Flask, jsonify

from Api.example import example

app = Flask(__name__)
app.register_blueprint(example)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)