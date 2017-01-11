#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_args` -- Arguing with the functions
=========================================

LAB_ARGS Learning Objective: Learn to modify, receive, and work with arguments to function.
::

 a. Create a function that accepts any number of positional arguments and
    keyword arguments and prints the argument values out to the screen.

 b. Create a function that takes in any number of positional arguments, turns
    those arguments into keyword arguments using "arg#" for the keyword names,
    and calls the print function you wrote in a.

 c. Write a validation function that takes in a variable number of positional
    arguments.  Validate that all the arguments passed in are integers and are
    greater than 0.  If the arguments validate, call the print function, if an
    argument doesn't validate raise a ValueError.

"""


# PART A
def part_a(*args, **kwargs):
    for ii in args: print(ii)
    for ii in kwargs: print(kwargs[ii])


# PART B
def part_b(*args):
    bargs = dict()
    count = 0
    for ii in args:
        bargs["arg" + str(count)] = ii
        count += 1
    part_a(**bargs)


# PART C
def part_c(*args):
    for ii in args:
        if not isinstance(ii, int):
            raise ValueError("'{}' is not int".format(ii))
        if not ii >= 0:
            raise ValueError("'{}' is not greater than 0".format(ii))
        print(ii)
