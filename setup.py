from flask import Flask
from controllers.auth import controller_endpoints
from models.user import conn

app = Flask(__name__)
controller_endpoints(app)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)