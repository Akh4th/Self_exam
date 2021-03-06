import re
import random
from datetime import datetime, timedelta
import time
import os
from os import name

global counter, num, skipped, errors1, asked, page
counter = 0
num = 0
skipped = 0
errors1 = 0
asked = []

# Customization Area
amount = 125  # Amount of questions for the test
file_name = 'quiz.txt'  # File to read the test from
time_limit = 2  # Time limit in hours
time_limit2 = 30  # Time limit in minutes
score_limit = 80  # Minimum percents to pass the test

# Settings
file = open(file_name, 'r')
d1 = file.read()
file.close()
d2 = str(d1)
pages = d2.count('NO.')
time1 = datetime.now()
date = time1.strftime('%D:')
hour = time1.strftime('%H:%M:%S')
end_time = format(time1 + timedelta(hours=time_limit, minutes=time_limit2), '%H:%M')
min_quest = int((score_limit*amount)/100)
time.sleep(3)

# Clears old answers files if existed
while counter == 0:
    open('wrong_answer.txt', 'w').close()
    open('correct_answers.txt', 'w').close()
    time.sleep(1)
    counter += 1


# Splitting random questions from text file and their answers
def split():
    print(f'Question {counter}/{amount} - ends at {end_time}')
    paging()
    x = re.split("\n\n", d2)
    question = x[page-1]
    x3 = question.splitlines()[-1]
    correct = x3[-1]
    print(question[:-9])
    answer = input('\nEnter your answer or type "skip" -> ').upper()

    def answer_check():
        global counter
        if answer == correct:
            quest1 = str(page + 1)
            ans_time = datetime.now()
            ans_date = ans_time.strftime('%D:')
            ans_hour = ans_time.strftime('%H:%M:%S')
            print('Thats correct !\n')
            right = open('correct_answers.txt', 'a')
            right.write(f'{ans_date} - {ans_hour} : Correct answer on question number : {quest1} \n')
            right.close()
            counter += 1
            clock()
            time.sleep(1)
        elif answer == "done" or answer == "Done" or answer == "DONE":
            done()
        elif answer == "skip" or answer == "Skip" or answer == "SKIP":
            global skipped
            skipped += 1
            clear()
            clock()
            return
        else:
            quest1 = str(page + 1)
            ans_time = datetime.now()
            ans_date = ans_time.strftime('%D:')
            ans_hour = ans_time.strftime('%H:%M:%S')
            print(f'Incorrect answer ! \nThe correct answer is {correct} \n')
            wrong = open('wrong_answer.txt', 'a')
            wrong.write(f'{ans_date} - {ans_hour} : Incorrect answer on question number : {quest1} \n')
            wrong.close()
            res = open('results.txt', 'a')
            res.write(f'Selected answer : {answer} \n {x[page]} \n\n')
            res.close()
            counter += 1
            clock()
            time.sleep(2)

    answer_check()


# Avoiding
# \duplication on questions number
def paging():
    global page
    page = random.randint(1, pages)
    if page in asked:
        print('Duplication found, changing question...')
        paging()
    else:
        asked.append(page)
        return page


# Checks if time limit has passed
def clock():
    global counter
    time_check = datetime.now().strftime('%H:%M')
    if time_check == end_time:
        print('Your time is up !')
        counter = amount
        time.sleep(1)
    else:
        return


# Clear console
def clear():
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Function for finishing the test at any point
def done():
    clear()
    answers = int(len(open('correct_answers.txt', 'r').readlines()))
    wrongs = int(len(open('wrong_answer.txt', 'r').readlines()))
    total = answers + wrongs
    if total != amount and wrongs > 0:
        percentage = ((answers * 100) / total)
        print(f'Your exam is over !\nTotal questions : {total}\nCorrect answers : {answers}\nWrong answers : {wrongs}\nSkipped questions : {skipped}\nSuccess rate of {percentage}%')
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
    elif errors1 >= 3:
        print(f'Your exam has been stopped !\nCorrect answers : {answers}\nWrong answers : {wrongs}\nSkipped questions : {skipped}\nSuccess rate of {(answers*100)/amount}%')
        quit()
    else:
        percentage = ((answers * 100) / amount)
        if percentage > score_limit:
            print(f'You have successfully passed the exam !\nCorrect answers : {answers}\nWrong answers : {wrongs}\nSkipped questions : {skipped}\nSuccess rate of {percentage}%')
            res = open('results.txt', 'a')
            res.write('****************************************\n')
            res.write(f'{date}{hour} : {percentage} percents with {answers} correct answers out of {total}.\n ')
            res.write('****************************************\n\n')
            res.close()
            time.sleep(5)
            quit()
        else:
            print(f'You have failed the exam !\nCorrect answers : {answers}\nWrong answers : {wrongs}\nSkipped questions : {skipped}\nSuccess rate of {percentage}%')
            res = open('results.txt', 'a')
            res.write('****************************************\n')
            res.write(f'{date}{hour} : {percentage} percents with {answers} correct answers out of {total}.\n ')
            res.write('****************************************\n\n')
            res.close()
            time.sleep(5)
            quit()


def run():
    print(f"Welcome user. Type 'done' whenever you want to quit.\nTo complete this test you'll have {time_limit}:{time_limit2} hours ({end_time}).\nIn order to pass the test you'll have to get {score_limit}% from {amount} questions ({min_quest} questions).\n")
    while counter <= amount:
        clear()
        try:
            split()
        except IndexError or ValueError or IOError as exp:
            while errors1 < 3:
                errors1 += 1
                print(f'{exp} error occurred...\nTrying again...')
                time.sleep(2)
                pass
            else:
                print('3 Errors were recorded, aborting...\n')
                time.sleep(2)
                done()
    else:
        done()


if __name__ == "__main__":
    run()
