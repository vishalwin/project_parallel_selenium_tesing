import mysql.connector

def get_login_data():
    conn  = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database ="saucedemodb"
    )
    
    cursor = conn.cursor()
    
    query = "select username, password from login_users where username like 'standard_user'" 
    
    cursor.execute(query)
    
    data= cursor.fetchone()
    conn.close()
    
    return data 
       