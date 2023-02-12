# напиши тут код основної програми та першого екрануm
nlmn
from memo_card_layout import*
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer 
from random import shuffle 
from memo_data import* 
from memo_edit_layout import* 
from memo_main_layout import * 


main_width, main_height = 1000, 450 
card_width, card_height = 600, 500 
time_unit = 1000   



text_wrong = 'Невірно'
text_correct = 'Вірно'

questions_listmodel = QuestionListModel() 
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
frm_card = 0
win_card = QWidget()
win_main = QWidget()
timer = QTimer() 
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3) 

def testlist():
    
    frm = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
    questions_listmodel.form_list.append(frm)
    frm = Question('Дім', 'house', 'horse', 'hurry', 'hour')
    questions_listmodel.form_list.append(frm)
    frm = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Question('Число', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)

def set_card():
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layout_card)


def set_main():
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle('Список запитань')
    win_main.setLayout(layout_main)

def show_random():
    global frm_card 
    frm_card = random_AnswerCheck(questions_listmodel, lb_Question, radio_list, lb_Correct, lb_Result)
    frm_card.show() 
    show_question() 

def click_OK():
    if btn_OK.text() != 'Наступне питання':
        frm_card.check()
        show_result()
    else:
        show_random()

def back_to_menu():
    win_card.hide()
    win_main.showNormal()

def start_test():
    show_random()
    win_card.show()
    win_main.showMinimized()

def add_form():
    questions_listmodel.insertRows() 
    last = questions_listmodel.rowCount(0) - 1       
    index = questions_listmodel.index(last)
    list_questions.setCurrentIndex(index) 
    edit_question(index)    
    txt_Question.setFocus(Qt.TabFocusReason)  
                                             

def edit_question(index):
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()

def del_form():
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())

def sleep_card():
    win_card.hide()
    timer.setInterval(time_unit * box_Minutes.value() )
    timer.start()
    
def connects():
    list_questions.setModel(questions_listmodel) 
    btn_start.clicked.connect(start_test)  
    btn_OK.clicked.connect(click_OK) 
    btn_Menu.clicked.connect(back_to_menu)    
    list_questions.clicked.connect(edit_question)
    btn_add.clicked.connect(add_form) 
    btn_delete.clicked.connect(del_form) 
    timer.timeout.connect(show_card) 
    btn_Sleep.clicked.connect(sleep_card) 

def show_card():
    win_card.show()
    timer.stop()


testlist()
set_card()
set_main()
connects()

win_main.show()
app.exec_()
