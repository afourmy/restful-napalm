from flask import Flask
from flask_restful import Resource, Api
from napalm import get_network_driver
from os.path import abspath, dirname
from sys import path

path_app = dirname(abspath(__file__))
if path_app not in path:
    path.append(path_app)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
api = Api(app)
username = 'cisco'
password = 'cisco'


class RestfulNapalm(Resource):
    def get(self, ip_address, os, getter):
        try:
            driver = get_network_driver(os)
            with driver(ip_address, username, password) as device:
                device.open()
                getter = getattr(device, getter)
            return getter
        except Exception as e:
            return str(e)


api.add_resource(
    RestfulNapalm,
    '/<string:ip_address>/<string:os>/<string:getter>'
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
