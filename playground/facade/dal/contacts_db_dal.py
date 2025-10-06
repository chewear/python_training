import sqlite3

def get_db_connection():
    return sqlite3.connect("address_book.db")

def retrieve_contacts():
    sql = "select name, contact from contacts"
    cnn = get_db_connection()
    cursor = cnn.execute(sql)
    result = {
        "contacts": []
    }
        
    for row in cursor:
        result.get("contacts").append({
            "name" : row[0],
            "contact_number" : row[1]
        })
        
    return result
        
        