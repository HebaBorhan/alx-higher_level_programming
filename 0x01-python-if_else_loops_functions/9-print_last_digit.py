#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        x = (number % 10)
        print(f"{x:d}", end='')
        return x

    elif number < 0:
        number = abs(number)
        x = (number % 10)
        print(f"{x:d}", end='')
        return x

    elif number == 0:
        print(f"0", end='')
        return 0
