from flask import Flask

app = Flask(__name__)

app.config.from_object('config.Develop')




# routes
from flask import render_template

@app.route('/')
def index():
    return render_template('pages/home.html')
