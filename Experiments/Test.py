print("Test, Τεστ")

x = "Τεστ"
y = " Test" * 3

z = input("What is your name? ")
w = input("What is your age ")

print(x, ",", y)
try:
    val = int(w)
    g = val + 30
    print("Hello ", z, ", I see you are ", int(g), " years old!")
except ValueError:
    print("That is not an int!")
