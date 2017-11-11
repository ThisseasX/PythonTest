age = 0


def print_age():
    global age
    age = input("How old are you? ")

    if age.isnumeric():
        if int(age) < 14:
            print("You are younger than me")
        elif 14 < int(age) < 30:
            print("You are older than me")
        else:
            print("You are way too old")
    else:
<<<<<<< HEAD

=======
>>>>>>> 4cccf3a80cd12fa09a54943bbfd70447975923d2
        print("That's not a number")


print_age()
print(age)
