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
hour = time1.strftime('%H:%M:%S')
global counter
counter = 0


while counter == 0:
    open('wrong_answer.txt', 'w').close()
    open('correct_answers.txt', 'w').close()
    time.sleep(1)
    counter += 1


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
            quest1 = int(page)
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
            quest1 = int(page)
            ans_time = datetime.now()
            ans_date = ans_time.strftime('%D:')
            ans_hour = ans_time.strftime('%H:%M:%S')
            print('Incorrect answer !\nThe correct answer is ' + correct + '\n')
            wrong = open('wrong_answer.txt', 'a')
            wrong.write(ans_date + " - " + ans_hour + ' Incorrect answer question number : ' + quest1 + "\n")
            wrong.close()
            counter += 1
            clock()
            time.sleep(2)

    answer_check()


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


def clear():
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


global num
num = 0


def score():
    file_lines1 = int(len(open('wrong_answer.txt', 'r').readlines()))
    if file_lines1 == 0:
        print('Nothing to show...')
        quit()
    else:
        global num
        file_lines = file_lines1 - 1
        while num <= file_lines:
            e = open('wrong_answer.txt', 'r').readlines()
            e2 = e[num]
            a, *b, c = e2.split()
            quest_number = int(c)-1
            new = open('results.txt', 'a+')
            x2 = re.split("\n\n", d2)
            new.write("\n\n" + x2[quest_number])
            num += 1
            new.close()
            quit()
        else:
            quit()


def done():
    answers = int(len(open('correct_answers.txt', 'r').readlines()))
    wrongs = int(len(open('wrong_answer.txt', 'r').readlines()))
    total = answers+wrongs
    if total != 125:
        percentage = ((answers * 100) / total)
        finished = input(f'Your time is up !\nYou have {answers} right answers and {wrongs} wrong answers.\n{percentage}% of success.\nType yes to get results file').upper()
        if finished == 'YES':
            score()
        else:
            quit()
    else:
        percentage = ((answers * 100) / 125)
        finished = input(f'You have finished to exam !\nYou have {answers} right answers and {wrongs} wrong answers.\n{percentage}% of success.\nType yes to get results file').upper()
        if finished == 'YES':
            score()
        else:
            quit()


while counter <= 125:
    clear()
    split()
else:
    done()
