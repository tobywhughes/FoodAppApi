import sqlite3
from connect import db_connect
#from sql import *
from db_query import *


@db_connect
def update_restaurant(id, changes, connection, cursor):
    if id is None or changes is None:
        raise ValueError
    cursor.execute(build_update('restaurant', changes.keys()), tuple(list(changes.values()) + [id]))

@db_connect
def update_menu_item(id, changes, connection, cursor):
    if id is None or changes is None:
        raise ValueError
    cursor.execute(build_update('menu_item', changes.keys()), tuple(list(changes.values()) + [id]))
    
@db_connect
def update_order(id, status, connection, cursor):
    if id is None or status is None:
        raise ValueError
    cursor.execute(build_update('order_parent', ['status']), (status, id))

@db_connect
def update_alert(id, status, connection, cursor):
    if id is None or status is None:
        raise ValueError
    cursor.execute(build_update('alerts', ['status']), (status, id))

if __name__ == "__main__":
    update_alert(1, 'Y')
    print(query_alert(1, None, None, None))