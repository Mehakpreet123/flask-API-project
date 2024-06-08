import mysql.connector
import json

class user_model:
    def __init__(self):
        try:
            #connection establish
            self.con= mysql.connector.connect(host="localhost",user="root",password="1234Ab@cd",database="flask_db")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("some eror")


    def user_getall_model(self):
        #business logic
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        
        
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(Name,email,Phone) VALUES ('{data['Name']}','{data['email']}','{data['Phone']}')")
        return "User created successfully"
    

    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET Name='{data['Name']}',email='{data['email']}',Phone='{data['Phone']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return "user updated successfully"
        else:
            return "Nothing to update"
        
        
    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id IN {id}")
        if self.cur.rowcount>0:
            return "User deleted successfully"
        else:
            return "Nothing to Delete"
