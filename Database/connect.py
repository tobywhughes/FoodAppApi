import sqlite3
DATABASE_FILE = 'database.db'


def db_connect(func_):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        kwargs['connection'] = connection
        kwargs['cursor'] = cursor
        ret_val = func_(*args, **kwargs)
        connection.commit()
        connection.close()
        return ret_val

    return wrapper