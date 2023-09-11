from question_model import QuizObjMaker
from quiz_brain import QuizBrain
from data import animal_data
import os

os.system('cls')
all_object_list = []
for one_object in animal_data:
    question = one_object["question"]
    answer = one_object["answer"]
    all_object_list.append(QuizObjMaker(question, answer))

quiz = QuizBrain(all_object_list)
while quiz.still_question():
    quiz.next_question()
    quiz.right_question()

print(f"Vyhodnocení kvízu:\nUhádl jsi {quiz.right_count} otázek z celkem {quiz.obj_count}")