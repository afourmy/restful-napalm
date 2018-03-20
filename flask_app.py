from flask import Flask, render_template
from os.path import abspath, dirname
from sys import path

path_app = dirname(abspath(__file__))
if path_app not in path:
    path.append(path_app)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

@app.route('/')
def index():
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
