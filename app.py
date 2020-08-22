"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from flask import Flask, request, g, render_template, Response
from FractalDatabase import GetDB
from controller import controller

app = Flask(__name__)


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

app.config['SECRET_KEY'] = 'cheekibreeki'
app.config['CORS_ORIGINS'] = "*"
app.config['CORS_HEADERS'] = ['Content-Type']
app.debug = True

app.register_blueprint(controller, url_prefix="/api")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

"""
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
"""
