questions = "Username", "Password"
correct_answers = "thiss", "123"
errors = [0, 0]
correct_username = False
correct_password = False


def correct_answer(i):
    if i == 0:
        global correct_username
        correct_username = True
    else:
        global correct_password
        correct_password = True
        print("Welcome to my program!")


def is_error_limit_reached():
    if errors[0] >= 3 or errors[1] >= 3:
        return True
    return False


def add_error(i):
    errors[i] += 1
    if is_error_limit_reached():
        print("-- Wrong too many times. Bye! --")
        return True
    else:
        print("-- Wrong {0}. Try again! --".format(questions[i]))
        return False


def request_input(i):
    while not correct_username or not correct_password:
        if is_error_limit_reached():
            break

        if input("{0}: ".format(questions[i])) == correct_answers[i]:
            correct_answer(i)
            break
        else:
            add_error(i)


# 0 for Username, 1 for Password
request_input(0)
request_input(1)
