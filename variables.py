import pandas as pd
class Question:
    def __init__(self, question, correct_answer, category, bad_answers, hint):
        self.question = question
        self.correct_answer = correct_answer
        self.category = category
        self.bad_answers = bad_answers
        self.hint = hint

df = pd.read_excel('Zeszytt.xlsx')
points = 0
money = 0
objects = []
used_questions = []
flaga1, flaga2, flaga3 = False, False, False
your_money = 0