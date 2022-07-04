#!/usr/bin/python

def print_list_integer(my_list=[]):
    """Prints integers in a list"""
    for j in range(len(my_list)):
        print("{:d}".format(my_list[j]))
