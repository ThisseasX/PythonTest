def repeat_string(count, string):
    result = ""
    for i in range(count):
        result += string
    return result


def left_arrow(row, width):
    if row < width:
        stars = row + 1
    else:
        stars = width * 2 + 1 - row
    return repeat_string(width + 1 - stars, " ") + repeat_string(stars, "*")


def right_arrow(row, width):
    if row < width:
        stars = row + 1
    else:
        stars = width * 2 + 1 - row
    return repeat_string(stars, '*') + repeat_string(width + 1 - stars, " ")


def shaft(row, height, length):
    if (row > height * 0.25) and (row < height * 0.75):
        string = repeat_string(length, "*")
    else:
        string = repeat_string(length, " ")
    return string


def arrow(width, length):
    for row in range(width * 2 + 1):
        print(left_arrow(row, width) +
              shaft(row, width * 2, length) +
              right_arrow(row, width))


arrow(11, 45)
