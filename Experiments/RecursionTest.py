def factorial(n):
    if n == 100:
        return 100
    else:
        return n * factorial(n + 1)


def my_sum(n):
    if n == 1:
        return 1
    else:
        return n + (my_sum(n - 1))


def stars(n):
    print(("*" * n).center(n-1))
    if n == 1:
        return 1
    else:
        return stars(n - 1)


stars(10)
