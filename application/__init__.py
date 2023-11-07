from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qisxltcl:KbRC4J5kGAurTbq5xLQlQyPG5FIQE00J@trumpet.db.elephantsql.com/qisxltcl'
db = SQLAlchemy(app)

from application import routes
