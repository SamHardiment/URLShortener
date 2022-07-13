from flask import Flask, render_template
from werkzeug import exceptions
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


############# ERROR STUFF

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('errors/404.html', title="404 Error"), 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return render_template('errors/400.html', title="400 Error"), 400

@app.errorhandler(exceptions.MethodNotAllowed)
def handle_405(err):
    return render_template('errors/405.html', title="405 Error"), 405

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('errors/500.html', title="500 Error"), 500

if __name__ == "__main__":
    app.run(debug=True)
