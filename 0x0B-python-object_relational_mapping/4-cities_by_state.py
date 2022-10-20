#!/usr/bin/python3
"""Module contains a script that will list states in a MySQL database"""
import MySQLdb
from sys import argv


def cities_by_state():
    """Takes in an argument and displays all values in
    the states table where name matches the argument"""

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3]
                         )

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities, states\
                    WHERE cities.state_id = states.id\
                    ORDER BY cities.id"
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    cities_by_state()
