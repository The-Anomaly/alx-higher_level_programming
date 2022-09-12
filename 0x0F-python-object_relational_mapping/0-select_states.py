#!/usr/bin/python3
"""list all states from the database hbtn_0e_0usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(
        host=host, port=port, user=user,
        passwd=password, db=db)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
