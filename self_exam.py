import re
import random
from datetime import datetime
import time
import os
from os import name

file = open('quiz.txt', 'r')
d1 = file.read()
file.close()
d2 = str(d1)
pages = d2.count('NO.')
print("Welcome user. Type 'done' whenever you want to quit.\n")
time1 = datetime.now()
date = time1.strftime('%D:')
hour = time1.strftime('%H:%M:%S')
global counter, num
counter = 0
num = 0

# Clears old answers files if existed
while counter == 0:
    open('wrong_answer.txt', 'w').close()
    open('correct_answers.txt', 'w').close()
    time.sleep(1)
    counter += 1


# Splitting random questions from text file and their answers
def split():
    print(f'Question {counter}/125')
    page = random.randint(1, pages)
    x = re.split("\n\n", d2)
    question = x[page]
    x3 = question.splitlines()[-1]
    correct = x3[-1]
    print(question[:-9])
    answer = input('\nEnter your answer or type "skip" -> ').upper()

    def answer_check():
        global counter
        if answer == correct:
            quest1 = str(page)
            ans_time = datetime.now()
            ans_date = ans_time.strftime('%D:')
            ans_hour = ans_time.strftime('%H:%M:%S')
            print('Thats correct !\n')
            right = open('correct_answers.txt', 'a')
            right.write(ans_date + " - " + ans_hour + ' Correct answer question number : ' + quest1 + "\n")
            right.close()
            counter += 1
            clock()
            time.sleep(1)
        elif answer == "done" or answer == "Done" or answer == "DONE":
            done()
        elif answer == "skip" or answer == "Skip" or answer == "SKIP":
            clear()
            clock()
            return
        else:
            quest1 = str(page)
            ans_time = datetime.now()
            ans_date = ans_time.strftime('%D:')
            ans_hour = ans_time.strftime('%H:%M:%S')
            print('Incorrect answer !\nThe correct answer is ' + correct + '\n')
            wrong = open('wrong_answer.txt', 'a')
            wrong.write(ans_date + " - " + ans_hour + ' Incorrect answer question number : ' + quest1 + "\n")
            wrong.close()
            res = open('results.txt', 'a')
            res.write('Selected answer : '+answer+'\n'+x[page]+'\n\n')
            res.close()
            counter += 1
            clock()
            time.sleep(2)
    answer_check()


# Checks if time limit has passed (2 hours)
def clock():
    global counter
    time_check = datetime.now()
    hour_check = time_check.strftime('%H:%M:%S')
    new_time = hour_check.split(':')
    new_hour = new_time[0]
    new_min = new_time[1]
    old_time = hour.split(':')
    old_hour = old_time[0]
    old_min = old_time[1]
    test_time = int(old_hour)+2
    if new_hour == test_time and new_min == old_min:
        counter = 125
    else:
        return


# Clear console every iteration
def clear():
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# After exam has ended one reason or another user will be asked
# if he desires to use previous function (score())
def done():
    clear()
    answers = int(len(open('correct_answers.txt', 'r').readlines()))
    wrongs = int(len(open('wrong_answer.txt', 'r').readlines()))
    total = answers+wrongs
    if total != 125 and wrongs > 0:
        percentage = ((answers * 100) / total)
        print(f'Your exam is over !\nYou have {answers} right answers and {wrongs} wrong answers out of {total} questions and {percentage}% of success.')
        res = open('results.txt', 'a')
        res.write('****************************************\n')
        res.write(f'{date}{hour} : {percentage} percents with {answers} correct answers out of {total}.\n ')
        res.write('****************************************\n\n')
        res.close()
        time.sleep(5)
        quit()
    elif total == 0:
        print('Good luck next time !')
        quit()
    else:
        percentage = ((answers * 100) / 125)
        if percentage < 66.666:
            print(f'You have successfully passed the exam !\nYou have {answers} right answers and {wrongs} wrong answers.\n{percentage}% of success.')
            res = open('results.txt', 'a')
            res.write('****************************************\n')
            res.write(f'{date}{hour} : {percentage} percents with {answers} correct answers out of {total}.\n ')
            res.write('****************************************\n\n')
            res.close()
            time.sleep(5)
            quit()
        else:
            print(f'You have failed the exam ! \nYou have {answers} right answers and {wrongs} wrongs answers out of {total} questions.\n{percentage}% of success.')
            res = open('results.txt', 'a')
            res.write('****************************************\n')
            res.write(f'{date}{hour} : {percentage} percents with {answers} correct answers out of {total}.\n ')
            res.write('****************************************\n\n')
            res.close()
            time.sleep(5)
            quit()


while counter <= 125:
    clear()
    split()
else:
    done()
