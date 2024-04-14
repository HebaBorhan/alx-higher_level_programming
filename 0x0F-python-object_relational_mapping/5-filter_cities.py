#!/usr/bin/python3
"""takes in name of a state as argument & lists all cities of that state"""
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    state_name = (sys.argv[4],)
    cur.execute(query, state_name)

    cities = [row[0] for row in cur.fetchall()]
    print(', '.join(cities))

    cur.close()
    conn.close()
