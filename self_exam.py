import re
import random
from datetime import datetime
import time

file = open('quiz.txt', 'r')
d1 = file.read()
file.close()
d2 = str(d1)
print("Welcome user. Type 'done' whenever you want to quit.\n")
time1 = datetime.now()
date = time1.strftime('%D')
hour = time1.strftime(':%H:%M:%S')
global counter
counter = 1
open('wrong_answer.txt', 'w').close()
open('correct_answers.txt', 'w').close()


def split():
    print(f'Question {counter}/125')
    page = random.randint(1, 720)
    x = re.split("\n\n", d2)
    question = x[page]
    x3 = question.splitlines()[-1]
    correct = x3[-1]
    print(question[:-9])
    answer = input('\nPlease enter your answer ').upper()

    def answer_check():
        global counter
        if answer == correct:
            print('Thats correct !\n')
            right = open('correct_answers.txt', 'a')
            right.write(date + " - " + hour + ' Correct answer question number : ' + str(page) + "\n")
            right.close()
            counter += 1
        elif answer == "done" or answer == "Done" or answer == "DONE":
            answers1 = int(len(open('correct_answers.txt', 'r').readlines()))
            percentage1 = (answers1 * counter) / 100
            print(f'You have done {answers1} right answers out of {counter} questions.\nYour success rate is {percentage1}. See you next time !')
            time.sleep(5)
            open('wrong_answer.txt', 'w').close()
            open('correct_answers.txt', 'w').close()
            quit()
        else:
            print('Incorrect answer !\nThe correct answer is ' + correct + '\n')
            wrong = open('wrong_answer.txt', 'a')
            wrong.write(date + " - " + hour + ' Incorrect answer question number : ' + str(page) + "\n")
            counter += 1

    answer_check()


while counter <= 125:
    split()
else:
    answers = int(len(open('correct_answers.txt', 'r').readlines()))
    wrongs = int(len(open('wrong_answer.txt', 'r').readlines()))
    percentage = (answers * 125) / 100
    print(f'You have finished to exam !\nYou have {answers} right answers and {wrongs} wrong answers.\n{percentage}% of success.')
    time.sleep(5)
    open('wrong_answer.txt', 'w').close()
    open('correct_answers.txt', 'w').close()
    quit()
