import re
import random
from datetime import datetime


file = open('quiz.txt', 'r')
d1 = file.read()
file.close()
d2 = str(d1)
print("Welcome user. Type 'done' whenever you want to quit.\n")
time = datetime.now()
date = time.strftime('%D')
hour = time.strftime(':%H:%M:%S')
global counter
counter = 1

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
            right = open('correct_answers.txt','a')
            right.write(date+" - "+hour+' Correct answer question number : '+str(page)+"\n")
            right.close()
            counter += 1
        elif answer == "done" or answer == "Done" or answer == "DONE":
            print('See you later !')
            quit()
        else:
            print('Incorrect answer !\nThe correct answer is '+correct+'\n')
            wrong = open('wrong_answer.txt', 'a')
            wrong.write(date+" - "+hour+' Incorrect answer question number : '+str(page)+"\n")
            counter += 1
    answer_check()


while counter <= 125:
    split()
else:
    answers = int(len(open('correct_answers.txt', 'r').readlines()))
    wrongs = int(len(open('wrong_answer.txt', 'r').readlines()))
    percentage = (answers*125)/100
    print(f'You have finished to exam !\nYou have {answers} right answers and {wrongs} wrong answers.\n{percentage}% of succes.')
