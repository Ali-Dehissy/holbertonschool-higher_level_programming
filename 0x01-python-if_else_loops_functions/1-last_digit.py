#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number % 10 == 1
if number > 5:
    print(number, "and is greater than 5")
if number == 0:
    print(number, "and is 0")
if ((number < 6) != 0):
    print(number, "and is less than 6 and not 0")

