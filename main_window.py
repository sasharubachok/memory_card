from PyQt5.QtWidgets import (
    QWidget,
      QPushButton,
        QLabel ,
        QRadioButton,
        QButtonGroup,
          QGroupBox,
            QRadioButton,
              QVBoxLayout,
                QHBoxLayout,
                  QSpinBox) 
from PyQt5.QtCore import Qt
card_width, card_height = 600, 500 #початкові розміри вікна "картка"  
win_card =QWidget() 
win_card.resize(card_width, card_height)  
win_card.move(300, 300)
win_card.setWindowTitle('Memory card') 

menu_bth = QPushButton("Відпочити") 
rest_bth = QPushButton("ВІдпочити") 
time_box = QSpinBox() 
time_box.setValue(50) 
time_Ib = QLabel("хвилин")
line1 = QHBoxLayout() 
line1.addWidget(menu_bth) 
line1.addStretch(1) 
line1.addWidget(rest_bth) 
line1.addWidget(time_box) 
line1.addWidget(time_Ib) 





bth1 = QRadioButton("1") 
bth2 = QRadioButton ("2") 
bth3 = QRadioButton ("3") 
bth4 = QRadioButton ("4") 
radioGroupBox = QGroupBox("Варіанти відповідей:") 
radioGroup = QButtonGroup()
radioGroup.addButton(bth1)
radioGroup.addButton(bth2)
radioGroup.addButton(bth3)
radioGroup.addButton(bth4) 

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout() 
layout_ans1.addWidget(bth1) 
layout_ans1.addWidget(bth2) 
layout_ans2.addWidget(bth3) 
layout_ans2.addWidget(bth4)
layout_ans_main = QVBoxLayout()
layout_ans_main.addLayout (layout_ans1)
layout_ans_main.addLayout (layout_ans2) 
radioGroupBox.setLayout(layout_ans_main) 


andGroupBox = GroupBox("Результат") 
lb_resuit = QLabel("Правильно!") 
ib_correct = QLabel("Правильна відповідь тут") 
layout_result = QVBoxLayout()
layout_result.addWidget(lb_result, alighment=Qt.AlighTop) 
layout_result.addWidget(lb_correct, alignment=Qt.AligCenter, strench=2
ansGroupbox.setLayout(layout_result) 
ansGroupbox.hide()


question = QLabel("питання тут") 

checkBth =QPushButton("Перевірити") 
checkBth.cliced.connect(show_result)
main_line = QVBoxLayout( ) 
main_line.addLayout(line1) 

main_line.addWidget(question, strench=1,aligment=Qt.AlignHCenter)
main_line.addWidget(radioGroupBox, stretch=1) 
main_line.addWidget(checkBth,stretch=1) 

win_card.setLayout(main_line) 
def show_result(): 
  radio   