#!/usr/bin/python3
"""Module contains a script that will list states in a MySQL database"""
import MySQLdb
from sys import argv


def my_safe_filter_states():
    """Takes in an argument and displays all values in
    the states table where name matches the argument"""

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3]
                         )

    cur = db.cursor()
    name = argv[4]
    cur.execute("SELECT * FROM states "
                "WHERE BINARY name = %s "
                "ORDER BY id", (name,)
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
