
from . import app, request
from .modules import db_utils as DBU

DB = DBU.DB_API()

@app.route("/get_clients_dept", methods=["GET"])
def get_clients_dept():
    return DB.get_clients_dept()

@app.route("/get_client/<id>", methods=["GET"])
def get_client(id:str):
    return DB.get_client(id)

@app.route("/create_client",  methods=["POST"])
def create_client():
    '''
    ussage:  http://127.0.0.1:8080/create_client?cust_id=value&first_name=value&last_name=value&company_name=value&address=value&city=value&state=value&zip=value&phone1=value&&phone2=value&email=value
    '''
    args = request.args.lists()
    return DB.create_client(args)

@app.route("/update_client_attr/<id>",  methods=["POST"])
def update_client_attr(id:str):
    '''
    ussage = http://127.0.0.1:8080/update_client_attr/id?column=value&insert=value
    '''
    column = request.args.get('column')
    insert = request.args.get('insert')
    return DB.update_client_attr(id,column,insert)

@app.route("/delete_client/<id>", methods=["POST"])
def delete_client(id:str):
    return DB.delete_client(id)