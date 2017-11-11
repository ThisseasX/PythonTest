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
    ArrowTest.py
     
    This script prints a two-headed arrow
    pattern to the console.
"""

# The arrow's dimensions.
whitespace = 30  # Central whitespace - Can be filled with stars.
edge_height = 6  # Height of the edges where whitespace is needed.
center_height = 5  # Height of the central part where stars fill the whitespace.
peak = (edge_height + center_height + 1)  # The tip of the arrowheads.
max_length = peak * 2 + whitespace  # Maximum length, used for centering.


# Function that creates the space between the two arrowheads.
#
# If the loop is 6 rows away from the edge, fill with whitespace
# else fill with stars.
def fill_whitespace(i):
    if i > 6:
        return "*" * whitespace
    else:
        return " " * whitespace


# Function that returns a complete string that represents a single row.
def create_row(i):
    string = "*" * i
    string += fill_whitespace(i)
    string += "*" * i
    return string


# Function that creates the two-headed arrow.
def create_arrow():
    # This is the starting index for the loop representing
    # stars before and after the added whitespace.
    #
    # e.g. row 3 has 3 stars before the whitespace
    #      and 3 stars after.
    index = 1

    # This boolean starts at True as we ascend to the tip of the
    # arrowhead, at which point it reverts to False to allow
    # for the subsequent descent and mirroring of the pattern.
    ascend = True

    # Our loop that does all the work.
    while index > 0:
        # We center the entire arrow at the maximum
        # possible length, so that all the stars
        # are visible.
        print(create_row(index).center(max_length))

        # If we're before the peak, go upwards,
        # else go downwards.
        if ascend:
            index += 1
        else:
            index -= 1

        # If we have reached the tip of the arrowhead,
        # we begin descending.
        if index == peak:
            ascend = False


create_arrow()
