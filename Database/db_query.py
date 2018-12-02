import sqlite3
from connect import db_connect
from sql import *

@db_connect
def query_restaurant(id, connection, cursor):
    if id is not None:
        execute_string = build_select('restaurant', ['id'])
        cursor.execute(execute_string, (id,))
    else:
        execute_string = build_select('restaurant', [])
        cursor.execute(execute_string)
    return create_return_dict(cursor)

@db_connect
def query_menu(id, rid, connection, cursor):
    if id is None and rid is None:
        execute_string = build_select('menu_item', [])
        cursor.execute(execute_string)
    else:
        n_ = []
        t_ = []
        if id is not None:
            n_.append('id')
            t_.append(id)
        if rid is not None:
            n_.append('rid')
            t_.append(rid)
        execute_string = build_select('menu_item', n_)
        cursor.execute(execute_string, t_)
    return create_return_dict(cursor)


@db_connect
def query_profile(id, username, connection, cursor):
    if id is None and username is None:
        execute_string = build_select('profile', [])
        cursor.execute(execute_string)
    else:
        n_ = []
        t_ = []
        if id is not None:
            n_.append('id')
            t_.append(id)
        if username is not None:
            n_.append('username')
            t_.append(username)
        execute_string = build_select('profile', n_)
        cursor.execute(execute_string, t_)
    return create_return_dict(cursor)

@db_connect
def query_order(id, rid, pid, connection, cursor):
    table_name = "order_parent JOIN order_element ON order_element.oid = order_parent.id"
    if id is None and rid is None and pid is None:
        execute_string = build_select(table_name, [])
        cursor.execute(execute_string)
    else:
        n_ = []
        t_ = []
        if id is not None:
            n_.append('order_parent.id')
            t_.append(id)
        if rid is not None:
            n_.append('rid')
            t_.append(rid)
        if pid is not None:
            n_.append('pid')
            t_.append(pid)
        execute_string = build_select(table_name, n_)
        cursor.execute(execute_string, t_)
    return create_return_dict(cursor)

@db_connect
def query_alert(id, rid, pid, status, connection, cursor):
    if id is None and rid is None and pid is None and status is None:
        execute_string = build_select('alerts', [])
        cursor.execute(execute_string)
    else:
        n_ = []
        t_ = []
        if id is not None:
            n_.append('id')
            t_.append(id)
        if rid is not None:
            n_.append('rid')
            t_.append(rid)
        if pid is not None:
            n_.append('pid')
            t_.append(pid)
        if status is not None:
            n_.append('status')
            t_.append(status)
        execute_string = build_select('alerts', n_)
        cursor.execute(execute_string, t_)
    return create_return_dict(cursor)

    

if __name__ == "__main__":
    #print(query_restaurant(None))
    #print(query_menu(None, None))
    print(query_alert(None, None, 1, None))
