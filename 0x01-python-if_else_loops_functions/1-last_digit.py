#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    x = (number % 10)
    if x > 5:
        print(f"Last digit of {number:d} is {x:d} and is greater than 5")
    elif x == 0:
        print(f"Last digit of {number:d} is {x:d} and is 0")
    elif x < 6 and x != 0:
        print(f"Last digit of {number:d} is {x:d} and is less than 6 and not 0")

elif number < 0:
    number = abs(number)
    x = (number % 10)
    if x > 5 or (x < 6 and x != 0):
        print(f"Last digit of -{number:d} is -{x:d} and is less than 6 and not 0")
    elif x == 0:
        print(f"Last digit of -{number:d} is 0 and is 0")
