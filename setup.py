from flask import Flask
from controllers.auth import controller_endpoints
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import VARCHAR, DateTime, text



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://jonas:password@localhost:5432/jonas'
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory='config/db/postgres/migrations')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(VARCHAR(16), nullable=False)
    password = db.Column(VARCHAR(64), nullable=False)
    salt = db.Column(VARCHAR(64), nullable=False)
    created_at = db.Column(DateTime, nullable=False, server_default=text('NOW()'))
    updated_at = db.Column(DateTime, nullable=False, onupdate=text('NOW()'))
    deleted_at = db.Column(DateTime, nullable=False)


controller_endpoints(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)