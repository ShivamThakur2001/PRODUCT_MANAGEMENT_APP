import sqlite3
connection = sqlite3.connect("PRODUCT.db")
cursor = connection.cursor()
command = "CREATE TABLE IF NOT EXISTS register_info(name VARCHAR2(50),email VARCHAR2(20),mobile INTEGER(12),password VARCHAR2(10))"
cursor.execute(command)
command = "CREATE TABLE IF NOT EXISTS add_product(product_name VARCHAR2(20),brand_name VARCHAR2(20),product_category VARCHAR2(20),product_price INTEGER,product_sku INTEGER,product_use VARCHAR2(100),product_description VARCHAR2(500))"
cursor.execute(command)
command = "CREATE TABLE IF NOT EXISTS delete_product(deleted_name VARCHAR2(50),deleted_brand VARCHAR2(10),deleted_reason VARCHAR2(500))"
cursor.execute(command)
command = "CREATE TABLE IF NOT EXISTS order_product(order_id INTEGER,order_name VARCHAR2(20),order_brand VARCHAR2(20),order_category VARCHAR2(20),order_quantity VARCHAR2(20),order_price INTEGER, total_price INTEGER)"
cursor.execute(command)
connection.commit()
connection.close()