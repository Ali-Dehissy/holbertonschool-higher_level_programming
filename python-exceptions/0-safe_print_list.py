#!/usr/bin/python3
"""safeprint"""


def safe_print_list(my_list=[], x=0):
        i, j = 0, 0
            try:
                        for i in range(x):
                                        print("{}".format(my_list[i]), end="")
                                                    j = j + 1
                                                        except IndexError as err:
                                                                    pass
                                                                    finally:
                                                                                print()
                                                                                    return (j)
