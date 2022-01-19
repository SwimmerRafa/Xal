from crypt import methods
from . import app

@app.route("/get_clients", methods=["GET"])
def get_clients():
    return "Pass"

@app.route("/get_client/<id>", methods=["GET"])
def get_client(id:str):
    return f"{id}"

@app.route("/delete_client/<id>", methods=["POST"])
def delete_client(id:str):
    return "Pass"

@app.route("/update_client/<id>",  methods=["POST"])
def update_client(id:str):
    return "Pass"
