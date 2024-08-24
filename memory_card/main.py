#підключення модулю
from menu_window import *
from main_window import *


from random import choice, shuffle #виб. ранд. ел.зі списку \ переімуновує елементи списку
from time import sleep


class Qestion():
    def __init__(self, qestion, answer, wrong_answer1, wrong_answer2, wrong_answer3,):
        self.qestion = qestion 
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.actual = True
        self.attempts = 0
        self.correct = 0 

    def got_right(self):

        self.attempts +=1
        self.correct +=1

    def got_wrong(self):
        self.attempts +=1
# питання

q1 = Qestion('Що завжди піднімається, але ніколи не опускається?','Вік','Сонце','Ніч','День')
q2 = Qestion('Що має коріння, але не росте, має листя, але не зелена, має стовбур, але не дерево?','Книга','Дерево','Двері','Стіл')
q3 = Qestion('Що має велику силу, але є лише кілька грамів ваги?','Слово','Сонце','Ніч','День')
q4 = Qestion('Що завжди піднімається, але ніколи не опускається?','Вік','Сонце','Ніч','День')
q5 = Qestion('Що завжди піднімається, але ніколи не опускається?','Вік','Сонце','Ніч','День')
q6 = Qestion('Що завжди піднімається, але ніколи не опускається?','Вік','Сонце','Ніч','День')
q7 = Qestion('Що завжди піднімається, але ніколи не опускається?','Вік','Сонце','Ніч','День')
q8 = Qestion('Що завжди піднімається, але ніколи не опускається?','Вік','Сонце','Ніч','День')
q9 = Qestion('Що завжди піднімається, але ніколи не опускається?','Вік','Сонце','Ніч','День')
q10 = Qestion('Що завжди піднімається, але ніколи не опускається?','Вік','Сонце','Ніч','День')


radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
question = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,]

def new_question():
    global cur_question
    cur_question = choice(question)

    lb_Question.setText(cur_question.qestion)
    lb_Correct.setText(cur_question.answer)

    shuffle(radio_list)

def rest():
    main_win.hide()
    n = box_Minutes.value() = 60
    sleep(n)
    main_win.show

def show_menu():
    menu_win.show()
    main_win.hide()

def back_menu():
    menu_win.hide()
    main_win.show()

def clear():
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()

new_question()

btn_Menu.clicked.connect(show_menu)
btn_back.clicked.connect(show_menu)
btn_clear.clicked.connect(show_menu)
btn_Sleep.clicked.connect(show_menu)

main_win.show()
app.exec_()