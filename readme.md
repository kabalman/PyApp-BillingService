# AdditionalBillingService REST Api

This is built with Flask, Flask-RESTful, Flask-SQLAlchemy, psycopg2, sqlalchemy

additem:

curl -X POST @parameters.json http://URL/additem

Description:

This will execute a stored procedure on the postgres db to add a new chargeable item

Parameters:

ITEMCODE: Item code of the chargable item
CF_SERVICE_ID: the cloudforms service id of the service that added the new chargeable item
HOSTNAME: the hostname of the service that added the new chargeable item


Delete:

curl -X POST @parameters.json http://URL/enditem

Description:

This will execute a stored procedure on the postgres db to end a chargeable item

Parameters:

ITEMCODE: Item code of the chargable item
CF_SERVICE_ID: the cloudforms service id of the service that ended the chargeable item
HOSTNAME: the hostname of the service that ended the chargeable item