#!/usr/bin/python3
if __name__ == "__main__":
    from sys import
    sum = 0

    for num in args:
        if not str(num).isdigit():
            return False
        else:
            sum += int(num)
    return sum
