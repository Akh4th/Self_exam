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
print("Welcome user. Type 'done' whenever you want to quit.\n")
time1 = datetime.now()
date = time1.strftime('%D')
hour = time1.strftime(':%H:%M:%S')
global counter
counter = 0


while counter == 0:
    open('wrong_answer.txt', 'w').close()
    open('correct_answers.txt', 'w').close()
    time.sleep(3)
    counter += 1


def split():
    print(f'Question {counter}/125')
    page = random.randint(1, 720)
    x = re.split("\n\n", d2)
    question = x[page]
    x3 = question.splitlines()[-1]
    correct = x3[-1]
    print(question[:-9])
    answer = input('\nEnter your answer or type "skip" -> ').upper()

    def answer_check():
        global counter
        if answer == correct:
            print('Thats correct !\n')
            right = open('correct_answers.txt', 'a')
            right.write(date + " - " + hour + ' Correct answer question number : ' + str(page) + "\n")
            right.close()
            counter += 1
            time.sleep(1)
        elif answer == "done" or answer == "Done" or answer == "DONE":
            answers1 = int(len(open('correct_answers.txt', 'r').readlines()))
            percentage1 = ((answers1 * 100) / (counter - 1))
            done1 = input(
                f'You have done {answers1} right answers out of {counter - 1} questions.\nYour success rate is {percentage1}%.\nType YES in order to get score file. ').upper()
            if done1 == 'YES':
                print('results.txt has your wrong questions.')
                score()
            else:
                quit()
        elif answer == "skip" or answer == "Skip" or answer == "SKIP":
            clear()
            return
        else:
            print('Incorrect answer !\nThe correct answer is ' + correct + '\n')
            wrong = open('wrong_answer.txt', 'a')
            wrong.write(date + " - " + hour + ' Incorrect answer question number : ' + str(page) + "\n")
            wrong.close()
            counter += 1
            time.sleep(2)

    answer_check()


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
            print(x2[quest_number])
            new.write("\n\n" + x2[quest_number])
            num += 1
            new.close()
        else:
            quit()


while counter <= 125:
    clear()
    split()
else:
    answers = int(len(open('correct_answers.txt', 'r').readlines()))
    wrongs = int(len(open('wrong_answer.txt', 'r').readlines()))
    percentage = ((answers * 100) / 125)
    done = input(
        f'You have finished to exam !\nYou have {answers} right answers and {wrongs} wrong answers.\n{percentage}% of success.\nType yes to get results file').upper()
    if done == 'YES':
        score()
    else:
        quit()
