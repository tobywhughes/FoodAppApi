import sqlite3
from connect import db_connect
#from sql import *
from db_query import *

@db_connect
def insert_restaurant(name, username, passhash, address, phone, gps_loc, connection, cursor):
    #execute_string = 'INSERT INTO restaurant (name, username, passhash, address, phone, gps_location) VALUES (?, ?, ?, ?, ?, ?)'
    execute_tuple = (name, username, passhash, address, phone, gps_loc)
    cursor.execute(build_insert('restaurant', ['name', 'username', 'passhash', 'address', 'phone', 'gps_location']), execute_tuple)

@db_connect
def insert_menu_item(name, price, rid, description, connection, cursor):
    execute_tuple = (name,price,rid, description)
    cursor.execute(build_insert('menu_item', ['name', 'price', 'rid', 'description']), execute_tuple)

@db_connect
def insert_profile(username, passhash, email, dob, connection, cursor):
    execute_tuple = (username,passhash, email, dob)
    cursor.execute(build_insert('profile', ['username', 'passhash', 'email', 'dob']), execute_tuple)
    
@db_connect
def insert_order(status, detail, rid, pid, mids, connection, cursor):
    execute_tuple = (status, detail, rid, pid)
    cursor.execute(build_insert('order_parent', ['status', 'detail', 'rid', 'pid']), execute_tuple)
    cursor.execute('SELECT id FROM order_parent ORDER BY id DESC LIMIT 1')
    oid = cursor.fetchall()[0][0]
    for mid in mids:
        execute_tuple = (oid, mid)
        cursor.execute(build_insert('order_element', ['oid', 'mid']), execute_tuple)

@db_connect
def insert_alert(status, detail, rid, pid, connection, cursor):
    execute_tuple = (status, detail, rid, pid)
    cursor.execute(build_insert('alerts', ['status', 'detail', 'rid', 'pid']), execute_tuple)

if __name__ == "__main__":
    #insert_order('ABC', 'asdasdffB', 2, 1, [1, 1, 2])
    print(query_order(None, None, None))
    #update_alert(1, 'Y')
    #print(query_alert(1, None, None, None))
