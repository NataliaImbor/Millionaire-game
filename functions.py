from colorama import Fore, init
from variables import Question, df, objects, points, money, used_questions, flaga1, flaga2, flaga3, your_money
import random
import pandas as pd

init()
def create_objects():
    data_frame = pd.DataFrame(df)
    for index, row in df.iterrows():
        obj = Question(row['Question'], row['Correct'], row['Category'], [row['b1'], row['b2'], row['b3']], row['hint'])
        objects.append(obj)
    return objects


def choose_category():
    categories = df['Category'].tolist()
    categories = list(set(categories))
    category1 = random.choice(categories)
    category2 = random.choice(categories)
    while (category1 == category2):
        category2 = random.choice(categories)
    print(Fore.BLUE + "Choose category\n1."+category1+"\n2."+category2)
    your_category = input()
    while (your_category != '1' and your_category != '2'):
        print(Fore.RED + "Bad choice, choose number 1 or 2")
        your_category = input()
    if (your_category == '1'):
        your_category = category1
    elif (your_category == '2'):
        your_category = category2
    return your_category

def choose_answer():
    your_answer = input()
    return your_answer


def count_points():
    global money, points
    if (points == 1 or points == 2):
        money = 1000 * points
    elif (points == 3 or points == 4):
        money = 2000 + 5000 * (points - 2)
    elif (points == 5):
        money = 12000 + 12000
    elif (points == 6):
        money = 24000 + 26000
    elif (points == 7 or points == 8):
        money = 50000 + (points - 6) * 100000
    elif (points == 9 or points == 10):
        money = 250000 + (points - 8) * 150000
    elif (points == 11 or points == 12):
        money = 550000 + (points - 10) * 225000
    return money


def quaranted_amount():
    money = count_points()
    if (points == 1 or points == 5 or points == 8):
        print(Fore.YELLOW + "If you want you can finish this game now with the money you've won so far, decide, what do you want to do (write 1 or 2).\n"
              "1.I want to keep playing.\n2. I want to finish this game.")
        decision = input()
        if (decision == '1'):
            print(Fore.YELLOW + "Great decision, you're still in the game:)\nChoose the correct answer:")
        elif (decision == '2'):
            print(Fore.YELLOW + "That's a pity, that you're finishing this game, but you won much money! We'll be happy to make a transfer for PLN "+str(money))
            exit()


def check_answer(your_answer, answers, correct_answer):
    if (your_answer == 'A' or your_answer == 'a'):
        your_answer = answers[0]
    elif (your_answer == 'B' or your_answer == 'b'):
        your_answer = answers[1]
    elif (your_answer == 'C' or your_answer == 'c'):
        your_answer = answers[2]
    elif (your_answer == 'D' or your_answer == 'd'):
        your_answer = answers[3]

    if (your_answer == correct_answer):
        return True
    else:
        return False


def answer(answers, correct_answer):
    global your_money
    print("Write your answer")
    your_answer = choose_answer()
    values = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']

    while (your_answer not in values):
        print(Fore.YELLOW + "There's no answer like this, try again!\nChoose answer again:")
        your_answer = choose_answer()


    if (check_answer(your_answer, answers, correct_answer) == True):
        print(Fore.GREEN + "Congratulations, that's good answer")
        global points
        points+=1
        your_money = count_points()
        print(Fore.GREEN + "You have PLN "+str(your_money)+" on your account.")
    else:
        print(Fore.RED + "That's bad answer, you must finish this game. You won PLN " + str(your_money))
        exit()

def remove_two(answers, correct_answer):
    global your_money
    y1 = correct_answer
    y2 = random.choice(answers)
    while (y2 == y1):
        y2 = random.choice(answers)

    print(Fore.BLUE + y1)
    new_answers = []
    new_answers.append(y1)
    new_answers.append(y2)
    random.shuffle(new_answers)
    print(Fore.BLUE + "A. "+ new_answers[0] + "\nB. " + new_answers[1])
    your_answer = choose_answer()

    def check_answer_lifebuoy():
        nonlocal your_answer
        values = ['A', 'a', 'B', 'b']
        while (your_answer not in values):
            print(Fore.YELLOW + "There's no answer like this, try again!\nChoose answer again:")
            your_answer = choose_answer()

        if (your_answer == 'A' or your_answer == 'a'):
            your_answer = new_answers[0]
        elif (your_answer == 'B' or your_answer == 'b'):
            your_answer = new_answers[1]

        if (your_answer == correct_answer):
            return True
        else:
            return False

    if (check_answer_lifebuoy() == True):
        print(Fore.GREEN + "Congratulations, that's good answer")
        global points
        points += 1
        your_money = count_points()
        print(Fore.GREEN + "You have PLN " + str(your_money) + " on your account.")
    else:
        print(Fore.RED + "That's bad answer, you must finish this game. You won PLN " + str(your_money))
        exit()

def change_question(correct_questions):
    q = random.choice(correct_questions)
    print(Fore.BLUE + q)
    global used_questions
    used_questions.append(q)
    print(used_questions)
    answers = [obj.bad_answers for obj in objects if obj.question == q]
    answers.append(list(obj.correct_answer for obj in objects if obj.question == q))
    answers = sum(answers, [])
    correct_answer = answers[3]
    random.shuffle(answers)
    print(Fore.BLUE + "A. " + answers[0] + "\nB. " + answers[1] + "\nC. " + answers[2] + "\nD. " + answers[3])
    print(correct_answer)
    answer(answers, correct_answer)

def hint(questions, q, answers, correct_answer):
    your_hint = [obj.hint for obj in questions if obj.question == q]
    print(Fore.MAGENTA + your_hint[0])
    answer(answers, correct_answer)

def choose_question():
    objects = create_objects()
    while(True):
        your_category = choose_category()
        questions = [obj for obj in objects if obj.category == your_category]
        while (len(questions) == 0):
            print(Fore.RED + "There's not any more questions in this category, choose another category.")
            your_category = choose_category()
            questions = [obj for obj in objects if obj.category == your_category]
        correct_questions = [obj.question for obj in questions]
        q = random.choice(correct_questions)
        print(Fore.BLUE + q)
        quaranted_amount()
        global used_questions
        used_questions.append(q)
        answers = [obj.bad_answers for obj in objects if obj.question == q]
        answers.append(list(obj.correct_answer for obj in objects if obj.question == q))
        answers = sum(answers, [])
        correct_answer = answers[3]
        random.shuffle(answers)
        print(Fore.BLUE + "A. "+answers[0]+"\nB. "+answers[1]+"\nC. "+answers[2]+"\nD. "+answers[3])
        print(correct_answer)

        global flaga1, flaga2, flaga3


        print(Fore.YELLOW + "If you want, you can use the so-called lifebuoy, but remember, you can use every one only one time. "
            "\nChoose which option you want to use."
            "\n1. I don't want to use lifebuoys.\n2. I want to use removing two wrong answers.\n"
            "3. I want to change question (it's possible question from the same category).\n"
              "4. I want to get a hint.")
        while(True):
            your_choice = input()
            while(your_choice != '1' and your_choice != '2' and your_choice != '3' and your_choice != '4'):
                print(Fore.RED + "Bad choice, choose number 1, 2, 3 or 4:")
                your_choice = input()
            if (your_choice == '1'):
                answer(answers, correct_answer)
                break
            elif (your_choice == '2' and not flaga1):
                remove_two(answers, correct_answer)
                flaga1 = True
                break
            elif (your_choice == '3' and not flaga2):
                change_question(correct_questions)
                flaga2 = True
                break
            elif (your_choice == '4' and not flaga3):
                print(Fore.YELLOW + "This is your hint: ")
                hint(questions, q, answers, correct_answer)
                flaga3 = True
                break
            else:
                print(Fore.RED + "Bad choice, this lifebuoy was already used, try again.")



        for obj in objects:
            if obj.question == q:
                objects.remove(obj)
                break

        if(len(used_questions) == 13 or your_money == 1000000):
            print(Fore.GREEN + "That was fanstastic game, you won main price - 1 000 000 PLN, CONGRATULATIONS!")
            exit()

