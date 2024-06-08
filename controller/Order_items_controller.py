from app import app 
 # first app is file name app.py second is variable app in that file
from model.Order_items_model import order_items_model
from flask import request
obj=order_items_model()
@app.route("/order_items/getall",methods=["POST","GET"]) # to handle req at endpoint

def order_items_getall_controller():
    return obj.order_items_getall_model()


@app.route("/order_items/addone",methods=["POST","GET"]) 
def order_items_addone_controller():
    return obj.order_items_addone_model(request.form)


@app.route("/order_items/update",methods=["PUT"]) 
def order_items_update_controller():
    return obj.order_items_update_model(request.form)


@app.route("/order_items/delete/<id>",methods=["DELETE"]) 
def order_items_delete_controller(id):
    return obj.order_items_delete_model(id)