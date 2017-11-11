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

while True:
    whitespace = input("Please input whitespace length: ")
    try:
        whitespace = int(whitespace)
        break
    except ValueError:
        print("-- Please input a valid number --")

while True:
    edge_height = input("Please input edge height: ")
    try:
        edge_height = int(edge_height)
        break
    except ValueError:
        print("-- Please input a valid number --")

while True:
    center_height = input("Please input central height: ")
    try:
        center_height = int(center_height)
        break
    except ValueError:
        print("-- Please input a valid number --")

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
        print(create_row(index).center(max_length))
        if ascend:
            index += 1
        else:
            index -= 1

        if index == peak:
            ascend = False


create_arrow()
