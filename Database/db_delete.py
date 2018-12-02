import sqlite3
from connect import db_connect
#from sql import *
from db_query import *

@db_connect
def delete_restaurant(id, connection, cursor):
    if id is None:
        raise ValueError
    cursor.execute('DELETE FROM restaurant WHERE id = ?', (id, ))
    cursor.execute('DELETE FROM menu_item WHERE rid = ?', (id, ))
    delete_order_by_rid(id, connection, cursor)
    cursor.execute('DELETE FROM alerts WHERE rid = ?', (id, ))

@db_connect
def delete_menu(id, connection, cursor):
    if id is None:
        raise ValueError
    cursor.execute('DELETE FROM menu_item WHERE id = ?', (id, ))

@db_connect
def delete_profile(id, connection, cursor):
    if id is None:
        raise ValueError
    cursor.execute('DELETE FROM profile WHERE id = ?', (id, ))
    delete_order_by_pid(id, connection, cursor)
    cursor.execute('DELETE FROM alerts WHERE pid = ?', (id, ))

@db_connect
def delete_order(id, connection, cursor):
    if id is None:
        raise ValueError
    cursor.execute('DELETE FROM order_parent WHERE id = ?', (id, ))
    cursor.execute('DELETE FROM order_element WHERE mid = ?', (id, ))

def delete_order_by_rid(id, connection, cursor):
    if id is None:
        raise ValueError
    cursor.execute('SELECT id FROM order_parent WHERE rid = ?', (id, ))
    oids = [oid[0] for oid in cursor.fetchall()]
    cursor.execute('DELETE FROM order_parent WHERE rid = ?', (id, ))
    for oid in oids:
        cursor.execute('DELETE FROM order_element WHERE oid = ?', (oid, ))

def delete_order_by_pid(id, connection, cursor):
    if id is None:
        raise ValueError
    cursor.execute('SELECT id FROM order_parent WHERE pid = ?', (id, ))
    oids = [oid[0] for oid in cursor.fetchall()]
    cursor.execute('DELETE FROM order_parent WHERE rid = ?', (id, ))
    for oid in oids:
        cursor.execute('DELETE FROM order_element WHERE oid = ?', (oid, ))

@db_connect
def delete_alert(id, connection, cursor):
    if id is None:
        raise ValueError
    cursor.execute('DELETE FROM alerts WHERE id = ?', (id, ))


if __name__ == "__main__":
    #insert_order('ABC', 'asdasdffB', 2, 1, [1, 1, 2])
    delete_order(3)
    print(query_order(None, None, None))
    #update_alert(1, 'Y')
    #print(query_alert(1, None, None, None))