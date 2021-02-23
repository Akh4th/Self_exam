import os, time
import self_exam
run = 1
choices = ['M', 'F', 'A', 'H', 'P', 'DONE', 'RUN']


def amount():
    a = int(input('Please enter amount of questions for the exam -> '))
    if a > open('quiz.txt', 'r').read().count('NO.'):
        print('Incorrect amount of questions.')
    else:
        self_exam.amount = a
        print(f'The questions amount was changed to {a}\n')
        time.sleep(1)


def file():
    f = str(input('Please enter the file name includes .txt -> '))
    if os.path.exists(f):
        self_exam.file_name = f
        print(f'The exams file name was changed to {f}\n')
        time.sleep(1)
    else:
        print(f'{f} Was not found, please try again.')


def hours():
    h = int(input('Please enter your exams time limit (In hours) -> '))
    if h > 24:
        print('Incorrect hours amount, please try again.')
    else:
        self_exam.time_limit = h
        print(f'Time limit was changed to {h} hours\n')
        time.sleep(1)


def minutes():
    m = int(input('Please enter your exams time limit (In minutes) - >'))
    if m > 60:
        print('Incorrect minutes amount, please try again.')
    else:
        self_exam.time_limit2 = m
        print(f'Time limit was changed to {m} minutes\n')
        print(self_exam.time_limit2)
        time.sleep(1)


def percents():
    p = int(input('Please enter the minimum percents needed to pass the exam -> '))
    if p > 100:
        print('Incorrect percents, please try again.')
    else:
        self_exam.score_limit = p
        print(f'Minimum percents to successfully pass the exam are {p}\n')
        time.sleep(1)


while run:
    print(f"Hello user and welcome to 'Self_exam' Configuration file.\nIn order to stop configuring please try 'done' whenever you're done\nType 'Run' whenever you'd like to start the exam with the new configurations.\n")
    time.sleep(1)
    print("To change to amount of questions please type 'A'")
    time.sleep(1)
    print("To change the file name please type 'F'")
    time.sleep(1)
    print("To change the hours amount please type 'H'")
    time.sleep(1)
    print("To change the minutes amount please type 'M'")
    time.sleep(1)
    print("To change the minimum percents please type 'P'")
    time.sleep(1)
    hello = input('\nPlease enter your choice ---> ').upper()
    if hello == 'A':
        amount()
    elif hello == 'F':
        file()
    elif hello == 'H':
        hours()
    elif hello == 'M':
        minutes()
    elif hello == 'P':
        percents()
    elif hello == 'DONE':
        run = 0
    elif hello == 'RUN':
        self_exam.run()
    elif hello not in choices:
        print('Wrong choice, please try again.')
        time.sleep(1)
else:
    print('Good luck on your exam !')
    quit()