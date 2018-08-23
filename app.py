from flask import Flask
from flask_restful import Api
from resources.item import AddChargeableItem, EndChargeableItem

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(AddChargeableItem, '/additem')
api.add_resource(EndChargeableItem, '/enditem')

if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0')
