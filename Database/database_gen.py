from pathlib import Path
import sqlite3
import sys, os

DATABASE_FILE = 'database.db'
SCHEMA_FILE = 'schema.sql'
TEMP_GENERATION_FILE = 'temp.json'

def create_database_from_file(filename, schemaname, regen = False):
    if Path(filename).is_file():
        if regen:
            os.remove(filename)
        else:
            raise FileExistsError

    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    with open(schemaname, 'r') as schema_file:
        lines = schema_file.readlines()
    
    for line in lines:
        print(line)
        cursor.execute(line)

    connection.commit()
    connection.close()


def fill_database_with_temp_data_with_json(filename):
    pass

if __name__ == '__main__':
    regen = False
    if len(sys.argv) == 2:
        if sys.argv[1] == 'regen':
            regen = True
    create_database_from_file(DATABASE_FILE, SCHEMA_FILE, regen)
    fill_database_with_temp_data_with_json(TEMP_GENERATION_FILE)
