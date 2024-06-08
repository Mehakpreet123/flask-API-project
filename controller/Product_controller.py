from app import app 
 # first app is file name app.py second is variable app in that file
from model.Product_model import product_model
from flask import request
obj=product_model()
@app.route("/product/getall",methods=["POST","GET"]) # to handle req at endpoint

def product_getall_controller():
    return obj.product_getall_model()


@app.route("/product/addone",methods=["POST","GET"]) 
def product_addone_controller():
    return obj.product_addone_model(request.form)


@app.route("/product/update",methods=["PUT"]) 
def product_update_controller():
    return obj.product_update_model(request.form)


@app.route("/product/delete/<id>",methods=["DELETE"]) 
def product_delete_controller(id):
    return obj.product_delete_model(id)