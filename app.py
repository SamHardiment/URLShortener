from flask import Flask, request, render_template, url_for, redirect
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
## Required for shorten_url func
import string
import os


## app :)
app = Flask(__name__)

##  Code block to connect sql db to heroku
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


class Urllist(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    long_url = db.Column("long_url", db.String(255))
    short_url = db.Column("short_url", db.String(50))

    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url

## Function for shortening url - hence the obvs function name
def shorten_url():
    # string.ascii_lowercase = abcdefghijklmnopqrstuvwxyz
    random_seqeuence = string.ascii_lowercase + string.digits
    while True:
        # random.choices is a method that reeturns a list wth randomly selected elements from a specifiied seqeuence
        # k is an integer that defines the length of the returned list
        random_string = random.choices(random_seqeuence, k=6)
        random_string = "".join(random_string)
        old_short_url = Urllist.query.filter_by(short_url=rand_letters).first()
        if not old_short_url:
            return random_string


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        url_input = request.form['urlInput']

        # Check if long url exists in db
        check_url = Urllist.query.filter_by(long_url=url_input).first()
        print(check_url)
        if check_url:
            #Redirect to url display of the long url and short url
            return redirect(url_for("short_url_handle", url=found_url.short_url), title="Short Url")
        else:
            short_url = shorten_url()
            # below adds long url and short url to the model
            new_url_set = Urls(url_input, short_url)
            # below adds new_url to the db
            db.session.add(new_url_set)
            # below saves the data
            db.session.commit()
            # redirect to webste
            return redirect(url_for("short_url_handle", url=short_url, title="Short Url"))
    else:
        return render_template('home.html', title="Home")

@app.route('/<url>')
def short_url_handle(url):
    url = Urllist.query.filter_by(short_url=url).first()
    print(url)
    return redirect(url.long_url)

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
