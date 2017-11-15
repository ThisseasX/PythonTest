def is_divisible_by(x, divisor):
    print(int(x / divisor))
    print(int(x / divisor) * divisor)
    return print(int(x / divisor) * divisor == x)


def is_divisible_by2(x, divisor):
    print(int(x % divisor))
    return print(int(x % divisor) == 0)


x = 3000
while x > 0.5:
    print(x)
    x = x / 2

is_divisible_by(10, 3)
is_divisible_by2(10, 3)
