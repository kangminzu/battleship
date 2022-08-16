import sys
from PyQt5.QtWidgets import *


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout=QVBoxLayout()
        
        #버튼 만들기
        btn = QPushButton("Click me")
        main_layout.addWidget(btn)
        
        self.setLayout(main_layout)
        self.resize(500,500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
