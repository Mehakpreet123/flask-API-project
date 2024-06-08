import mysql.connector
import json

class p_categories_model:
    def __init__(self):
        try:
            #connection establish
            self.con= mysql.connector.connect(host="localhost",user="root",password="1234Ab@cd",database="flask_db")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("some eror")


    def p_categories_getall_model(self):
        #business logic
        self.cur.execute("SELECT * FROM categories")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        
        
    def p_categories_addone_model(self,data):
        self.cur.execute(f"INSERT INTO categories(name) VALUES ('{data['name']}')")
        return "Product category added successfully"
    

    def p_categories_update_model(self,data):
        self.cur.execute(f"UPDATE categories SET name='{data['name']}' WHERE category_id={data['category_id']}")
        if self.cur.rowcount>0:
            return "product category updated successfully"
        else:
            return "Nothing to update"
        
        
    def p_categories_delete_model(self,id):
        self.cur.execute(f"DELETE FROM categories WHERE category_id IN {id}")
        if self.cur.rowcount>0:
            return "product category deleted successfully"
        else:
            return "Nothing to Delete"