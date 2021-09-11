#!/usr/bin/env python

from random import randint
from time import localtime, mktime

# How long the user will have to answer each problem.
time_limit = 15

# Initialize the number of problems and the score.
count = 0
right = 0

# Describe the program and let the user decide when to begin.
print ('''
******************* Math practice ********************

There will be both addition and subtraction problems.
Answer each problem by typing the answer and pressing
the Return or Enter key. To get credit, you have to
answer in %d seconds.

Press the 'q' key when you want to quit.
''' % time_limit)

input('Ready? Press Return or Enter to begin. ')
print

#
while True:
    count += 1

    # Choose three numbers so that a + b = c, with c from 10 to 20.
    c = randint(10,20)
    b = randint(0,c)
    a = c - b

    # Choose whether to give an addition (a + b = c)
    # or subtraction (c - b = a) problem.
    if randint(0, 1) == 0:
        # Addition.
        problem = '%d + %d = ' % (a, b)
        correct_answer = c
    else:
        # Subtraction.
        problem = '%d - %d = ' % (c, b)
        correct_answer = a

    # Show the problem and get the answer. Time it.
    start_time = mktime(localtime())
    user_answer = input('%3d.   ' % count + problem)
    end_time = mktime(localtime())

    # Break out of the loop when the user wants to quit.
    if user_answer.lower() == 'q':
        count -= 1      # the last problem doesn't count
        break

    # Answers that took too long are counted wrong.
    if end_time - start_time > time_limit:
        print ('       Too long!')
        continue

    # Check the answer and mark it right or wrong. Because user_answer
    # is a string, it has to be converted to an integer first. If the
    # answer doesn't look like an integer, it's wrong.
    try:
        if int(user_answer) == correct_answer:
            right += 1
            print ('       Right!')
        else:
            print ('       No, %s%d' % (problem, correct_answer))
    except:
        print ('       %s?   %s%d' % (user_answer, problem, correct_answer))

# Let the user know the final score.
print ("\n       You got %d right out of %d." % (right, count)),
if right == count:
    print ("Perfect!")
