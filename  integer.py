#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 16th Oct, 2026
# This program asks the user for an integer
# and checks whether the number is positive
# negative or equal to zero.
# It will display the result back to the user.


def main():
    # get the number from the user as an integer
    number = int(input("Enter an integer: "))

    # check if the number is positive, negative or equal to zero
    if number > 0:
        print("{0} your value is positive.".format(number))
    elif number < 0:
        print("{0} your value is negative.".format(number))
    else:
        print("{0} your value is equal to zero.".format(number))


if __name__ == "__main__":
    main()
