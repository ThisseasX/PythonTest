##########################################
#                                        #
#            Date:  9 Nov 2017           #
#          Author:  Thiss                #
#                                        #
##########################################

"""
    Copyright 2017 Thisseas Xanthopoulos

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

"""
    ArrowTestWOC.py
     
    This script prints a two-headed arrow
    pattern to the console.
    
    WOC stands for WithOut Comments.
"""

from ClassExcercises.BaseColors import BaseColors


def request_input(prompt, min_=None, max_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
        except ValueError:
            print("-- Please input a valid number --")
            continue
        if max_ is not None and user_input > max_:
            print("Input must be less than or equal to %d" % max_)
        elif min_ is not None and user_input < min_:
            print("Input must be greater than or equal to %d." % min_)
        else:
            return user_input


restart = True

while restart:

    whitespace = request_input("Please input whitespace length: ", min_=0, max_=80)
    edge_height = request_input("Please input edge height: ", min_=1, max_=30)
    center_height = request_input("Please input central height: ", min_=1, max_=30)

    peak = (edge_height + center_height)
    max_length = peak * 2 + whitespace


    def fill_whitespace(n):
        if n > edge_height:
            return "*" * whitespace
        else:
            return " " * whitespace


    def create_row(n):
        string = "*" * n
        string += fill_whitespace(n)
        string += "*" * n
        return string


    def create_arrow():
        print("\n")

        index = 1
        ascend = True

        while index > 0:
            color_char_start = BaseColors.OKBLUE
            color_char_end = BaseColors.END
            color_char_length = len(color_char_start) + len(color_char_end)
            center = max_length + color_char_length
            seq = (color_char_start, create_row(index), color_char_end)

            row = "".join(seq)
            print(row.center(center))

            if ascend:
                index += 1
            else:
                index -= 1

            if index == peak:
                ascend = False

        print("\n")


    create_arrow()

    while True:
        x = input("Type 'x' to close or 'r' to restart: ")
        if x == 'x':
            restart = False
            break
        elif x == 'r':
            break
