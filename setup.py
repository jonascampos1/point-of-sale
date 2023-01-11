from flask import Flask
from controllers.auth import controller_endpoints
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://jonas:password@localhost:5432/jonas'
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory='config/db/postgres/migrations')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

controller_endpoints(app)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)