import re
from msvcrt import getch

regex = re.compile('[^a-zA-Z]')

my_list = []


def input_color():
    while True:
        s = input("Choose a color: ").capitalize()
        if s == "Stop" or s == "S" or len(s) < 3:
            print_list()
            break
        else:
            read_line(s)


def print_list():
    if len(my_list) < 1:
        print("\nI have no favorite colors!", end="\n\n")
        return
    if len(my_list) == 1:
        print("\nMy favorite color is: {0}.".format(my_list[0]), end="\n\n")
    elif len(my_list) == 2:
        print("\nMy favorite colors are: {0} and {1}.".format(my_list[0], my_list[1]), end="\n\n")
    else:
        print("\nMy favorite colors are: ", end="")
        i = 0
        while i < len(my_list) - 1:
            print(my_list[i], end=", ")
            i += 1
        print("and", my_list[i], end=".\n\n")


def read_line(s):
    s = regex.sub(" ", s)
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i].capitalize()
        add_to_list(s[i])


def add_to_list(s):
    if len(s) > 2:
        if s not in my_list:
            my_list.append(s)
        else:
            print("-- Cannot add duplicate value: {0} --".format(s))


def ask_for_restart():
    while True:
        print("Press any key to close, or R for Restart.")
        key = ord(getch())
        if key == ord('r'):
            my_list.clear()
            print()
            input_color()
        else:
            break


def display_hint():
    print("\nHint: You can type 's' to stop at any time", end="\n\n")


display_hint()
input_color()
ask_for_restart()
