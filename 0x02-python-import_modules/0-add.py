#!/usr/bin/python3

exec(open("./add_0.py").read())
a = 1
b = 2

add(a, b)

print("<{:d}> + <{:d}> = <{:d}>".format(a, b, add(a, b)))
