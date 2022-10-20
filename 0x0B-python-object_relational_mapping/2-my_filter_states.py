#!/usr/bin/python3
"""
This python script lists all states from the database hbtn_0e_0_usa
that equal the state name that was passed
"""


import MySQLdb


def select_state():
    """
    This method lists all the states in the table that start with
    the given state name
    """
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE binary'{}' ORDER BY id"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    select_state()
