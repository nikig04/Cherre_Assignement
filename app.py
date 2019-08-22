from flask import Flask, request, jsonify
import os
import sqlite3

from sqlite3 import Error


app = Flask(__name__)

"""
   Create SQL connection to the DB in this project
   :return: con
"""
def sql_connection():
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR + "/sqlite/testdb.db")
        con = sqlite3.connect(db_path)
        print("Connection is established: Database is created in memory")
        return con

    except Error:
        print(Error)


"""
    Create a new table from other tables
    :param cur:
"""
def create_table(cur):

    cur.execute('CREATE TABLE IF NOT EXISTS frequent_browser AS select people.first_name, people.id, '
                'Count(people.first_name) from visits LEFT JOIN  people on visits.personId = people.id '
                'GROUP BY people.first_name ORDER BY Count(people.first_name) '
                'DESC LIMIT 10;')
    print("Table Created")


@app.route("/freqUser", methods=["POST"])
def get_user():
    conn = sql_connection()
    print("here")
    cur = conn.cursor();
    result = create_project(cur)
    return jsonify(result)

"""
    Function to query all from newly create DB
    param: cur
    return: result
"""
def create_project(cur):

    cur.execute('''SELECT * FROM frequent_browser''')
    all_rows = cur.fetchall()
    print('1):', all_rows)
    result = all_rows
    return result


if __name__ == '__main__':

    app.run(debug=True)

