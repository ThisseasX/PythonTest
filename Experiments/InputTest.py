def test1():
    print("--before t1")
    a = input("Test1: ")
    print("A: ", a)
    print("--after t1\n")
    return a


def test2(test):
    print("**before t2")
    b = input("Test2: ")
    print("B: ", b)
    print("Test: ", test)
    print("**after t2\n")
    return b


print("FINAL PRINT", test2(test1()))

print("FINAL")
