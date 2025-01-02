import mysql.connector

connection = mysql.connector.connect(
            host="localhost",         
            user="root",      
            password="***",  
            database="pandeyji_eatery"   
        )

def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = connection.cursor()
        
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))
        connection.commit()
        
        cursor.close()
        return 1
    
    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        connection.rollback()
        
        return -1
    
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
        
        return -1
    
    
def get_total_order_price(order_id):
    cursor = connection.cursor()
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    return result

def insert_order_tracking(order_id, status):
    cursor = connection.cursor()
    
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))
    
    connection.commit()
    cursor.close()


def get_next_order_id():
    cursor = connection.cursor()
    
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    
    if result is None:
        return 1
    else:
        return result + 1


def get_order_status(order_id):
    cursor = connection.cursor()
    
    query = "SELECT status FROM order_tracking WHERE order_id = %s"
    cursor.execute(query, (order_id,))
    result = cursor.fetchone()
    
    cursor.close()
    
    if result is not None:
        return result[0]
    else:
        return None
            
   
    