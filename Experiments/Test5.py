i = [("1", "2"), ("2", "1"), ("3", "4"), ("6", "7")]

i[2] = ("9", "9")

name = input("Name: ")
adt = input("ADT: ")
new_tuple = (name, adt)
i.append(new_tuple)
i.sort()
print(i)
