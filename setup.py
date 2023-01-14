from flask import Flask
import os
from controllers.auth import controller
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import VARCHAR, DateTime, text
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://'+os.getenv('POSTGRES_USER')+':'+os.getenv('POSTGRES_PASSWORD')+'@db:5432/jonas'
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory='config/db/postgres/migrations')

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(VARCHAR(16), nullable=False)
    password = db.Column(VARCHAR(64), nullable=False)
    salt = db.Column(VARCHAR(64), nullable=False)
    created_at = db.Column(DateTime, nullable=False, server_default=text('NOW()'))
    updated_at = db.Column(DateTime, nullable=False, onupdate=text('NOW()'))
    deleted_at = db.Column(DateTime, nullable=True)
    test = db.Column(VARCHAR(10), nullable=True)


controller(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)