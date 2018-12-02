def build_select(table, wheres):
    s = "SELECT * FROM " + table
    for where in wheres:
        s += " WHERE " + where + " = ?"
    return s

def build_update(table, changes):
    s = "UPDATE " + table + " SET"
    for change in changes:
        s += " " + change + " = ?"
    s += " WHERE id = ?"

    return s

def build_insert(table, fields):
    s = "INSERT INTO " + table + "("
    s += ", ".join(fields)
    s += ") VALUES ("
    s += ", ".join(['?'] * len(fields))
    s += ")"
    return s

def create_return_dict(cursor):
    result = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]
    return [{col_names[i]: item[i] for i in range(len(col_names))} for item in result]

if __name__ == "__main__":
    print(build_select('abc', ['a', 'b', 'c']))