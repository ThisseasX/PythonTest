my_list = ["Red", "Blue"]
s = input("Color plz: ").capitalize()
if not my_list.__contains__(s):
    my_list.append(s)

print(my_list)
