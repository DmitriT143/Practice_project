import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from App.Working.Functions import input_to_response


class RollerWindow(object):
    def __init__(self):
        super(RollerWindow, self).__init__()
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.InputWidget = QtWidgets.QWidget(self.centralwidget)
        self.InputWidget.setObjectName("InputWidget")

        self.InputLayout = QtWidgets.QGridLayout(self.InputWidget)
        self.InputLayout.setObjectName("InputLayout")

        self.RollInputLine = QtWidgets.QLineEdit(self.InputWidget)
        self.RollInputLine.setObjectName("RollInputLine")
        self.InputLayout.addWidget(self.RollInputLine, 0, 0, 1, 1)

        self.RollButton = QtWidgets.QPushButton(self.InputWidget)
        self.RollButton.setObjectName("RollButton")
        self.InputLayout.addWidget(self.RollButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.InputWidget, 0, 0, 1, 1)

        # Current Block contains
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("HistoryArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("HistoryAreaWidgetContents")

        # Next Block contains AutoGenerated GridLayouts (Output -> Formula -> ReRoll Button)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuLine = QtWidgets.QMenu(self.menuSettings)
        self.menuLine.setObjectName("MenuLine")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.actionAnother_line = QtWidgets.QAction(MainWindow)
        self.actionAnother_line.setObjectName("actionAnother_line")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSubLine = QtWidgets.QAction(MainWindow)
        self.actionSubLine.setObjectName("actionSubLine")
        self.menuLine.addAction(self.actionSubLine)
        self.menuSettings.addAction(self.menuLine.menuAction())
        self.menuSettings.addAction(self.actionAnother_line)
        self.menubar.addAction(self.menuSettings.menuAction())

        for i in range(10):
            self.create_ten_reroll_positions(i)
            self.OutputRerollButton.clicked.connect(lambda ch, num=i: self.reroll(num))
        MainWindow.setCentralWidget(self.centralwidget)

        self.RollButton.clicked.connect(lambda: self.roll('roll',0))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_ten_reroll_positions(self, line):
        self.OutputRerollButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.OutputRerollButton.setObjectName(f"OutputRerollButton{line}")
        self.OutputResultLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.OutputResultLine.setObjectName("OutputResultLine")
        self.OutputFormulaLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.OutputFormulaLine.setObjectName(f'OutputFormulaLine_{line}')
        read_history = open("roll_history.txt", "r")
        saved_history = read_history.read()
        saved_history = saved_history.split(',')
        self.gridLayout_2.addWidget(self.OutputFormulaLine, int(line), 0, 1, 1)
        self.gridLayout_2.addWidget(self.OutputResultLine, int(line), 1, 1, 1)
        self.gridLayout_2.addWidget(self.OutputRerollButton, int(line), 2, 1, 1)
        self.OutputRerollButton.setText(QtCore.QCoreApplication.translate("MainWindow", 'ReRoll'))
        self.OutputResultLine.setText(QtCore.QCoreApplication.translate("MainWindow", f'{saved_history[2*line]}'))
        self.OutputFormulaLine.setText(QtCore.QCoreApplication.translate("MainWindow", f'{saved_history[2*line+1]}'))

        return

    def update_layout(self):
        for i in range(10):
            self.create_ten_reroll_positions(i)
            self.retranslateUi(MainWindow)
            self.OutputRerollButton.clicked.connect(lambda ch, num=i: self.reroll(num))
            MainWindow.setCentralWidget(self.centralwidget)
        print('Hello')

    def roll_add(self, added_roll, added_result):
        read_history = open("roll_history.txt", "r")
        print(added_roll, added_result)
        print(read_history)
        saved_history = read_history.read()
        add_history = open("roll_history.txt", "w")
        add_history.write(f'{added_result}' f', {added_roll}' f', {saved_history}')
        print(saved_history)

    def roll(self, start_type, line):
        if start_type == 'roll':
            input = str(self.RollInputLine.text())
        else:
            input = str(line)
        response = input_to_response(input)
        self.roll_add(response[0], response[1])
        self.RollInputLine.setText('4d6+12')
        self.update_layout()

    def reroll(self, num):
        read_history = open("roll_history.txt", "r")
        saved_history = read_history.read()
        saved_history = saved_history.split(',')
        current_line = str(f'{saved_history[2*num+1]}')
        self.roll('none',current_line)
        return current_line

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Roller"))
        self.RollButton.setText(_translate("MainWindow", "Make Roll"))
        self.pushButton.setText(_translate("MainWindow", "ReRoll"))
        self.RollInputLine.setText('4d6+12')
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuLine.setTitle(_translate("MainWindow", "Line"))
        self.actionAnother_line.setText(_translate("MainWindow", "Another line"))
        self.actionSubLine.setText(_translate("MainWindow", "SubLine"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = RollerWindow()
ui.__init__()
MainWindow.show()
sys.exit(app.exec_())
