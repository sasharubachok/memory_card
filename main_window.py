from PYQt5.Qtwidgets import QWidget.QPushButton, QLabel 
card_width, card_height = 600, 500 #початкові розміри вікна "картка"  

win_card =Qwidget() 
win_card.resize(card_widgh, card_height)  
win_card.move(300, 300)
win_card.setWindowTitle('Memory card') 

menu_bth = QPushButton("Відпочити") 
rest_bth = QPushButton("ВІдпочити") 
time_box = QSpinbox() 
time_box.set_value(50) 
time_Ib = QLabel("хвилин")
line1 = QHboxLayout() 
line1.addwidget(menu_bth) 
line1.addStrech(1) 
line1.addwidget(rest_bth) 
line1.addwidget(time_box) 
line1.addwidget(time_Ib) 



main_line = QVBoxLayout( )