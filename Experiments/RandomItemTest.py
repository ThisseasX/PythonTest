from random import choice, randint

fruits = [("orange", "banana", "pear", "apple"),
          ("broccoli", "tomato", "potato", "celery"),
          ("tea", "beer", "juice", "coffee")]

print(choice(choice(fruits)))
print(fruits[randint(0, len(fruits) - 1)][randint(0, len(fruits) - 1)])

my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(my_list[0][0])
