#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)[-1]
if number > 5:
    print("last digit of {} is {} and is greater than 5".format(number, num))
if number == 0:
    print("last digit of {} is {} and is 0".format(number, num))
if ((number < 6) != 0):
    print("last digit of {} is {} and is less than 6 and not 0".format(number, num))
