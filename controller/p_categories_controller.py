from app import app 
 # first app is file name app.py second is variable app in that file
from model.p_categories_model import p_categories_model
from flask import request
obj=p_categories_model()
@app.route("/p_categories/getall",methods=["POST","GET"]) # to handle req at endpoint

def p_categories_getall_controller():
    return obj.p_categories_getall_model()


@app.route("/p_categories/addone",methods=["POST","GET"]) 
def p_categories_addone_controller():
    return obj.p_categories_addone_model(request.form)


@app.route("/p_categories/update",methods=["PUT"]) 
def p_categories_update_controller():
    return obj.p_categories_update_model(request.form)


@app.route("/p_categories/delete/<id>",methods=["DELETE"]) 
def p_categories_delete_controller(id):
    return obj.p_categories_delete_model(id)