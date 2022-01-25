#!/usr/bin/env python3

# Created by: Ketia Gaelle  Kaze
# Created on: Jan. 20, 2022
# This program asks the user for a mark level
# and returns its middle percentage.

# this function uses a switch case statement to
# determine the middle percentage of a mark level
def calc_mark(level):
    levels = {
        "4+": "Level {} has a middle percentage of 98%".format(level),
        "4": "Level {} has a middle percentage of 91%".format(level),
        "4-": "Level {} has a middle percentage of 83%".format(level),
        "3+": "Level {} has a middle percentage of 78%".format(level),
        "3": "Level {} has a middle percentage of 75%".format(level),
        "3-": "Level {} has a middle percentage of 71%".format(level),
        "2+": "Level {} has a middle percentage of 68%".format(level),
        "2": "Level {} has a middle percentage of 65%".format(level),
        "2-": "Level {} has a middle percentage of 61%".format(level),
        "1+": "Level {} has a middle percentage of 58%".format(level),
        "1": "Level {} has a middle percentage of 55%".format(level),
        "1-": "Level {} has a middle percentage of 51%".format(level),
        "R": "Level {} has a middle percentage of 25%".format(level),
    }
    return levels.get(level, -1)


# this function gets input from the user
# and calls the other function
def main():
    # get input from the user
    level_user = input("Enter the level you want to convert to a %: ")
    print("")

    # assign variable to function call that gives return value
    percentage = calc_mark(level_user)

    # displays results to user
    if calc_mark(level_user) == -1:
        print("{} is not a valid input!".format(level_user))
    else:
        print(percentage)


if __name__ == "__main__":
    main()
