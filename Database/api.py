from db_query import *
from db_insert import *
from db_update import *
from db_delete import *
import json

from flask import Flask, request
app = Flask(__name__)

@app.route('/restaurant', methods=['GET', 'POST', 'PUT', 'DELETE'])
def restaurant():
    if request.method == 'GET':
        id = None
        if 'id' in request.args:
            id = request.args['id']
        return json.dumps(query_restaurant(id))
    elif request.method == 'POST':
        f = request.form
        insert_restaurant(f['name'], f['username'], f['passhash'], f['address'], f['phone'], f['gps_loc'])
        return "Valid"
    elif request.method == 'PUT':
        f = {key:value[0] for key,value in dict(request.form).items()}
        update_restaurant(int(request.args['id']), f)
        return "Valid"
    elif request.method == 'DELETE':
        id = None
        if 'id' in request.args:
            id = request.args['id']
        delete_restaurant(int(id))
        return "Valid"

    return 'not implemented'

@app.route('/menu', methods=['GET', 'POST', 'PUT', 'DELETE'])
def menu():
    if request.method == 'GET':
        id = None
        rid = None

        if 'id' in request.args:
            id = request.args['id']
        if 'rid' in request.args:
            rid = request.args['rid']

        return json.dumps(query_menu(id, rid))
    elif request.method == 'POST':
        f = request.form
        insert_menu_item(f['name'], f['price'], f['rid'])
        return 'VALID'
    elif request.method == 'PUT':
        f = {key:value[0] for key,value in dict(request.form).items()}
        update_menu_item(int(request.args['id']), f)
        return "Valid"
    elif request.method == 'DELETE':
        id = None
        if 'id' in request.args:
            id = request.args['id']
        delete_menu(int(id))
        return "Valid"
    return 'not implemented'

@app.route('/profile', methods=['GET', 'POST', 'PUT', 'DELETE'])
def profile():
    if request.method == 'GET':
        id = None
        username = None

        if 'id' in request.args:
            id = request.args['id']
        if 'username' in request.args:
            username = request.args['username']

        return json.dumps(query_profile(id, username))
    elif request.method == 'POST':
        f = request.form
        insert_profile(f['username'], f['passhash'])
        return 'VALID'
    elif request.method == 'DELETE':
        id = None
        if 'id' in request.args:
            id = request.args['id']
        delete_profile(int(id))
        return "Valid"
    return 'not implemented'

@app.route('/order', methods=['GET', 'POST', 'PUT', 'DELETE'])
def order():
    if request.method == 'GET':
        id = None
        rid = None
        pid = None

        if 'id' in request.args:
            id = request.args['id']
        if 'rid' in request.args:
            rid = request.args['rid']
        if 'pid' in request.args:
            pid = request.args['pid']

        return json.dumps(query_order(id, rid, pid))
    elif request.method == 'POST':
        f = request.form
        mids = f['mids'].split(',')
        insert_order(f['status'], f['detail'], f['rid'], f['pid'], mids)
    elif request.method == 'PUT':
        f = request.form
        update_order(int(request.args['id']), f['status'])
        return "Valid"
    elif request.method == 'DELETE':
        id = None
        if 'id' in request.args:
            id = request.args['id']
        delete_order(int(id))
        return "Valid"
    return 'not implemented'

@app.route('/alert', methods=['GET', 'POST', 'PUT', 'DELETE'])
def alert():
    if request.method == 'GET':
        id = None
        rid = None
        pid = None
        status = None

        if 'id' in request.args:
            id = request.args['id']
        if 'rid' in request.args:
            rid = request.args['rid']
        if 'pid' in request.args:
            pid = request.args['pid']
        if 'status' in request.args:
            status = request.args['status']

        return json.dumps(query_alert(id, rid, pid, status))
    elif request.method == 'POST':
        f = request.form
        insert_alert(f['status'], f['detail'], f['rid'], f['pid'])
    elif request.method == 'PUT':
        f = request.form
        update_alert(int(request.args['id']), f['status'])
        return "Valid"
    elif request.method == 'DELETE':
        id = None
        if 'id' in request.args:
            id = request.args['id']
        delete_alert(int(id))
        return "Valid"
    return 'not implemented'

if __name__ == "__main__":
    app.run()