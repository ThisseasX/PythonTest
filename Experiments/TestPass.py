prompts = ["Username", "Password"]

correct = "nikos", "spyros00"

errors = [0, 0]


def check_errors():
    if errors[0] >= 3 or errors[1] >= 3:
        return True
    return False


def count_error(i):
    global errors

    if errors[i] >= 3:
        print("Wrong too many times. Bye!")
        return True

    errors[i] += 1
    print("Wrong {0}. Try again!".format(prompts[i]))
    return False


def request_input(i):
    while True:
        if check_errors():
            break
        user_input = input("{0}: ".format(prompts[i]))
        if user_input != correct[i]:
            count_error(i)
            continue
        else:
            break


request_input(0)
request_input(1)
