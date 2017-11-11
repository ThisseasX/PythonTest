test = [1, "dog", (("tost", "tost1"), ("test", "test1")), 'c', 4, 'cat']


def mysort(eleme):
    if type(eleme) == int:
        return str(eleme)
    else:
        return eleme


print(test[2][0][1])
# print(c)
# print(test.count(self))
