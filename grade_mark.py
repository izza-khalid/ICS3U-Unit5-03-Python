#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: November 2019
# This program tells percentage from level


def grade_level(mark):
    # this function tells percentage from level

    # process
    if mark == 0:
        mark = 25
    elif mark == 1:
        mark = 55
    elif mark == 2:
        mark = 65
    elif mark == 3:
        mark = 75
    elif mark == 4:
        mark = 90

    return mark


def main():
    # this function just calls other functions

    # input
    print("Let's find the percentage of your level (Not more than 4!)")
    mark = int(input("Enter your level: "))

    # call functions
    final_percentage = grade_level(mark)

    # output
    print("Your percentage is {0}%".format(final_percentage))


if __name__ == "__main__":
    main()
