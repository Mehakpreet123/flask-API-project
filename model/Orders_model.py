import mysql.connector
import json

class orders_model:
    def __init__(self):
        try:
            #connection establish
            self.con= mysql.connector.connect(host="localhost",user="root",password="1234Ab@cd",database="flask_db")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("some eror")


    def order_getall_model(self):
        #business logic
        self.cur.execute("SELECT * FROM orders")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        
        
    def order_addone_model(self,data):
        self.cur.execute(f"INSERT INTO orders(customer_id,order_date,total_amount) VALUES ('{data['customer_id']}','{data['order_date']}','{data['total_amount']}')")
        return "Order added successfully"
    

    def order_update_model(self,data):
        self.cur.execute(f"UPDATE orders SET customer_id='{data['customer_id']}',order_date='{data['order_date']}',total_amount='{data['total_amount']}' WHERE order_id={data['order_id']}")
        if self.cur.rowcount>0:
            return "order updated successfully"
        else:
            return "Nothing to update"
        
        
    def order_delete_model(self,id):
        self.cur.execute(f"DELETE FROM orders WHERE order_id IN {id}")
        if self.cur.rowcount>0:
            return "Order deleted successfully"
        else:
            return "Nothing to Delete"
