#!/usr/bin/python3
"""Module contains a script that will list states in a MySQL database"""
import MySQLdb
from sys import argv


def filter_cities():
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
    cur.execute("SELECT cities.name FROM cities\
                 LEFT JOIN states\
                 ON BINARY cities.state_id = states.id\
                 WHERE states.id = (SELECT id\
                                    FROM states\
                                    WHERE name = %s)\
                 ORDER BY cities.id", (name,)
                )
    rows = cur.fetchall()
    output = ''
    for row in rows:
        output += row[0] + ', '
    print(output[:-2])

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
