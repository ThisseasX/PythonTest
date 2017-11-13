# ~~~~~~~~~~~~~~~~~~~~~~~~~
# this program is about the "double arrow print" homework

# this is not the right answer, just some approaches
# more like food for thought

# I advise you strongly to check my code AFTER
# you have tried to solve it by yourselves

# please comment me and correct me, I am neither smart nor smartass

# the goal is to print a double arrow on our terminal
# i approach the subject from different views
# starting from the easiest to the hardest that I can think of

# instead of spaces " ", I am going to use dots "."
# just to make the code read friendly
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# written and tested on IDLE
# ~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~
# approach 1
# this is the simplest approach ever, I just print each line
# ~~~~~~~~~~~~~~~~~~~~~~~~~

# print("....*..........*....")
# print("...**..........**...")
# print("..***..........***..")
# print(".******************.")
# print("********************")
# print(".******************.")
# print("..***..........***..")
# print("...**..........**...")
# print("....*..........*....")

# comments on the 1st approach
# luckily, dots and asterisks take the same space on printing screen
# I think that it is missing some math

# ~~~~~~~~~~~~~~~~~~~~~~~~~
# approach 2
# a bit more complex than approach 1 but still simple
# ~~~~~~~~~~~~~~~~~~~~~~~~~

# print(4 * "." + 1 * "*" + 10 * "." + 1 * "*" + 4 * ".")
# print(3 * "." + 2 * "*" + 10 * "." + 2 * "*" + 3 * ".")
# print(2 * "." + 3 * "*" + 10 * "." + 3 * "*" + 2 * ".")
# print(1 * "." + 4 * "*" + 10 * "*" + 4 * "*" + 1 * ".")
# print(0 * "." + 5 * "*" + 10 * "*" + 5 * "*" + 0 * ".")
# print(1 * "." + 4 * "*" + 10 * "*" + 4 * "*" + 1 * ".")
# print(2 * "." + 3 * "*" + 10 * "." + 3 * "*" + 2 * ".")
# print(3 * "." + 2 * "*" + 10 * "." + 2 * "*" + 3 * ".")
# print(4 * "." + 1 * "*" + 10 * "." + 1 * "*" + 4 * ".")

# comments on the second approach
# I start recognising some patterns here
# I mean after printing the middle line(5th)
# everything is the same, just in reverse order
# I think I should make the math more advanced
# maybe ask the user to give me some data

# ~~~~~~~~~~~~~~~~~~~~~~~~~
# approach 3
# ask the user to provide data
# ~~~~~~~~~~~~~~~~~~~~~~~~~

#################################################
#####THIS IS A VERY BAD APPROACH, RUN IT BY #####
#####       LENGTH = 40 , HEIGHT = 11       #####
#################################################

# print("Hello user, I am your arrowbot for today")
# I convert the variables to float type just because
# I divide them and I am not sure how python manages
# division of an integer
length = int(input("length of chars for the double arrow? > "))
height = int(input("height of chars for the double arrow? > "))

# I noticed that I can "cut" the arrow in 3 parts
# The left arrow, the backbone and the right arrow
# lucky for me the code is read line to line


# I did this because the 2 arrows take the same space in every line
# and the backbone twice this space
varL = int(length / 4)

# the arrow consist by an odd number of lines
varH = int(height / 2)

# each line can be transformed as an equation of strings and numbers
# instead of 9 lines of prints, I wrote 9 lines of a forloop
# because I want my arrow to be "dynamic" and userdefined
for i in range(1, int(height)):
    if i > (varH + 1) or i < (varH - 1):
        char = "."
    else:
        char = "*"
    if i <= varH:
        print((varL - i) * "." + i * "*" + 2 * varL * char + i * "*" + (varL - i) * ".")
    else:
        print(i * "." + (varL - i) * "*" + 2 * varL * char + (varL - i) * "*" + i * ".")

print("\n"*100)

# comments on the third approach
# IT WAS A BAD IDEA TO DO A LOT OF STUFF TOGETHER
# I really had a hard time to manage the variable types
# and the user input at the same time
# this approach has lots of logical errors
# and works only for certain numbers
# where there is NO CONTROL over the user input
# AT LEAST THE MATH WORK, sometimes :(
# I had really a hard time, lucky for me google and stackoverflow are working

# ~~~~~~~~~~~~~~~~~~~~~~~~~
# approach 4
# control the user data input
# ~~~~~~~~~~~~~~~~~~~~~~~~~

# questions from approach 3
# how do I control the user input?
# i need to make sure user inputs only integer numbers
# also there should be a control over the numbers user enters
# length should be at least 4 times + 1 over the height??
"""
#####################################################
####### THIS IS THE FUNCTION DEFINING SECTION #######
#######  I STRONGLY ADVICE TO READ THIS PART  #######
####### AFTER UNDERSTANDING THE FOLLOWING CODE#######
#####################################################

def arrowmaker(dots, asterisks):
    arrowstring = dots * "." + asterisks * "*"
    return arrowstring


def bbmaker(length, char):
    bbstring = length * char
    return bbstring


#####################################################
#####################################################
#####################################################
#####################################################

# control the user input, it should be Integer only
# do not panic, just thank stackoverflow.com
while True:
    userHeight = input("Dear user please provide a height! > ")
    try:
        height = int(userHeight)
        break
    except ValueError:
        print("This is not an integer number")

# print("1height is: ", height)  #for debugging
# in case user puts a negative number we force it to positive
if height < 0:
    height = - height
# height must be an odd number
if height % 2 == 0:
    height += 1
# print("2height is: ", height) #for debugging

length = int((height - 1) * 4)
lengthbb = int(length / 2)
lengtha = int(length / 4)
for i in range(1, height + 1):
    # print((height+1)/2)
    if i < (int((height + 1) / 2) - 1) or i > (int((height + 1) / 2) + 1):
        char = "."
    else:
        char = "*"

    if i <= int((height + 1) / 2):
        c = lengtha - i
        d = i
    else:
        c = i - 2
        d = lengtha - i + 2

    str1 = arrowmaker(c, d)
    str2 = bbmaker(lengthbb, char)
    str3 = str1[::-1]
    print(str1 + str2 + str3)
"""
