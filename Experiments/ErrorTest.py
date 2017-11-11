Age = input("How old is he?")
while True:
    if Age.isnumeric():
        Age = float(Age)

    if Age > 13 or Age < 19:
        print("He's a teenager")
    else:
        print("He's not a teenager")
