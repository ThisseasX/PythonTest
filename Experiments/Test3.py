# while True:
#     try:
#         whitespace = int(input("Please input whitespace length: "))
#         # whitespace = int(whitespace)
#         break
#     except ValueError:
#         print("-- Please input a valid number --")
#
# print(whitespace + 2)

# while True:
#     x = input("Enter a number: ")
#     if x.isdecimal():
#         break
#     else:
#         print("LOL")

# x = "#"
# y = "#"
#
# print(x.isdecimal())
# print(x.isdigit())
# print(x.isnumeric())

count_wrong_value = 0
while True:
    x = input("Enter a, b or c: ")
    if x == 'a':
        print("You entered a")
        break
    if x == 'b':
        print("You entered b")
        break
    if x == 'c':
        print("You entered c")
        break
    else:
        print("Wrong value. Try again...")

print("You pressed the wrong key", count_wrong_value, "times")
