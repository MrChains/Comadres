from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return '<p>Hello!<p>'


@app.route('/puesto/<int:post_id>')
def show_post(post_id):
    puesto = post_id
    return render_template('puesto.html', puesto=puesto)
