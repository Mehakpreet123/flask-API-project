import mysql.connector
import json

class product_model:
    def __init__(self):
        try:
            #connection establish
            self.con= mysql.connector.connect(host="localhost",user="root",password="1234Ab@cd",database="flask_db")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("some eror")


    def product_getall_model(self):
        #business logic
        self.cur.execute("SELECT * FROM products")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        
        
    def product_addone_model(self,data):
        self.cur.execute(f"INSERT INTO products(name,price,stock_quantity,category_id) VALUES ('{data['name']}','{data['price']}','{data['stock_quantity']}','{data['category_id']}')")
        return "Product added successfully"
    

    def product_update_model(self,data):
        self.cur.execute(f"UPDATE products SET name='{data['name']}',price='{data['price']}',stock_quantity='{data['stock_quantity']}',category_id='{data['category_id']}' WHERE product_id={data['product_id']}")
        if self.cur.rowcount>0:
            return "product updated successfully"
        else:
            return "Nothing to update"
        
        
    def product_delete_model(self,id):
        self.cur.execute(f"DELETE FROM products WHERE product_id IN {id}")
        if self.cur.rowcount>0:
            return "product deleted successfully"
        else:
            return "Nothing to Delete"