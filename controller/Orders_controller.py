from app import app 
 # first app is file name app.py second is variable app in that file
from model.Orders_model import orders_model
from flask import request
obj=orders_model()
@app.route("/order/getall",methods=["POST","GET"]) # to handle req at endpoint

def order_getall_controller():
    return obj.order_getall_model()


@app.route("/order/addone",methods=["POST","GET"]) 
def order_addone_controller():
    return obj.order_addone_model(request.form)


@app.route("/order/update",methods=["PUT"]) 
def order_update_controller():
    return obj.order_update_model(request.form)


@app.route("/order/delete/<id>",methods=["DELETE"]) 
def order_delete_controller(id):
    return obj.order_delete_model(id)