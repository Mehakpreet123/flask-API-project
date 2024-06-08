from app import app 
 # first app is file name app.py second is variable app in that file
from model.user_model import user_model
from flask import request
obj=user_model()
@app.route("/user/getall",methods=["POST","GET"]) # to handle req at endpoint

def user_getall_controller():
    return obj.user_getall_model()


@app.route("/user/addone",methods=["POST","GET"]) 
def user_addone_controller():
    return obj.user_addone_model(request.form)


@app.route("/user/update",methods=["PUT"]) 
def user_update_controller():
    return obj.user_update_model(request.form)


@app.route("/user/delete/<id>",methods=["DELETE"]) 
def user_delete_controller(id):
    return obj.user_delete_model(id)