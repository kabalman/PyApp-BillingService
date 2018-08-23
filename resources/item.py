from flask import request
from flask_restful import Resource
import psycopg2
from sqlalchemy import create_engine
import os
#Connection to allow application to communicate with postgres db - os variables are so we can pass in the connection detials via docker
engine = create_engine("postgresql://" + os.environ.get('PG_USER') + ":" + os.environ.get('PG_PASSWORD') + "@" + os.environ.get('PG_HOST') + "/" + os.environ.get('PG_DATABASE'))


#This processes the request data that is passed to the AddChargeableItem resource and then passes them as parameters into the stored procedure in the db and then executes the procedure
class AddChargeableItem(Resource):
    def post(self):
        data = request.get_json()
        connection = engine.raw_connection()
        try:
            cursor = connection.cursor()
            cursor.callproc("AddChargeableItem", [
                            data['ITEMCODE'], data['CF_SERVICE_ID'], data['HOSTNAME']])
            results = list(cursor.fetchall())
            cursor.close()
            connection.commit()
            return {"message": "Chargeable item added"}, 201
        except psycopg2.InternalError:
            return {"message": "This item is already active on the service/host"}, 400
        finally:
            connection.close()


#This processes the request data that is passed to the EndChargeableItem resource and then passes them as parameters into the stored procedure in the db and then executes the procedure
class EndChargeableItem(Resource):
    def post(self):
        data = request.get_json()
        connection = engine.raw_connection()
        try:
            cursor = connection.cursor()
            cursor.callproc("endChargeableItem", [
                            data['ITEMCODE'], data['CF_SERVICE_ID'], data['HOSTNAME']])
            results = list(cursor.fetchall())
            cursor.close()
            connection.commit()
            return {"message": "Chargeable item ended"}, 201
        except psycopg2.InternalError:
            return {"message": "This item is NOT active on the service/host"}, 400
        finally:
            connection.close()
