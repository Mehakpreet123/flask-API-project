import mysql.connector
import json

class order_items_model:
    def __init__(self):
        try:
            #connection establish
            self.con= mysql.connector.connect(host="localhost",user="root",password="1234Ab@cd",database="flask_db")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("some error")


    def order_items_getall_model(self):
        #business logic
        self.cur.execute("SELECT * FROM order_items")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        
        
    def order_items_addone_model(self,data):
        self.cur.execute(f"INSERT INTO order_items(order_id,product_id,quantity,unit_price) VALUES ('{data['order_id']}','{data['product_id']}','{data['quantity']}','{data['unit_price']}')")
        return "Order items added successfully"
    

    def order_items_update_model(self,data):
        self.cur.execute(f"UPDATE order_items  SET order_id='{data['order_id']}',product_id='{data['product_id']}',quantity='{data['quantity']}',unit_price='{data['unit_price']}' WHERE order_items_id={data['order_items_id']}")
        if self.cur.rowcount>0:
            return "order items updated successfully"
        else:
            return "Nothing to update"
        
        
    def order_items_delete_model(self,id):
        self.cur.execute(f"DELETE FROM order_items WHERE order_item_id IN {id}")
        if self.cur.rowcount>0:
            return "order items deleted successfully"
        else:
            return "Nothing to Delete"
