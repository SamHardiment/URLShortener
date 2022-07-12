from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os


## app :)
app = Flask(__name__)

##  Code block to connect sql db to heroku
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title="Home")


if __name__ == "__main__":
    app.run(debug=True)
