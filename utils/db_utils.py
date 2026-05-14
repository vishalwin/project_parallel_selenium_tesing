
from pymongo import MongoClient

def get_login_data():
    client = MongoClient(
        "mongodb://localhost:27017/"
    )
    
    db = client["saucedemodb"]
    
    collection = db["login_users"]
    
    user = collection.find_one()
    client.close()
    
    return user["username"], user["password"]



















# import mysql.connector

# def get_login_data():
#     conn  = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root",
#         database ="saucedemodb"
#     )
    
#     cursor = conn.cursor()
    
#     query = "select username, password from login_users where username like 'standard_user'" 
    
#     cursor.execute(query)
    
#     data= cursor.fetchone()
#     conn.close()
    
#     return data 
       