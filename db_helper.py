import mysql.connector


cnx = mysql.connector.connect(
    host="localhost",  # e.g., "localhost" or "your-db-server.com"
    user="root",  # e.g., "root"
    password="8133",  # e.g., "password"
    database="pandeyji_eatery"  # e.g., "orders_db"
)


def get_order_status(order_id: int) -> str:
    cursor = cnx.cursor()  # Returns results as a dictionary
    query = "SELECT status FROM order_tracking WHERE order_id = %s"

    # Executing the SQL query
    cursor.execute(query, (order_id,))

    # Fetching the result
    result = cursor.fetchone()

    cursor.close()

    if result is not None:
        return result[0]  # Extract status from the result
    else:
        return None


#     except Error as e:
#         return f"Error: {e}"
#
#     finally:
#         # Closing the database connection
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#
#
# # Example usage
# order_id = 123  # Replace with the actual order_id you want to query
# status = get_order_status(order_id)
# print(f"Order ID {order_id} status: {status}")
def get_next_order_id():
    cursor = cnx.cursor()

    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()

    if result is None:
        return 1
    else:
        return result + 1


def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = cnx.cursor()
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))
        cnx.commit()
        cursor.close()

        print('Order item inserted Successfully')
        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        cnx.rollback()
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()

        return -1


def get_total_order_price(order_id):
    cursor = cnx.cursor()
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    result = cursor.fetchone()[0]
    cursor.close()
    return result


def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    cnx.commit()
    cursor.close()
