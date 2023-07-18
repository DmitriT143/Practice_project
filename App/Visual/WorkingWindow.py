import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from App.Working.Functions import prepare_input_line, initial_roll


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

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("HistoryArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("HistoryAreaWidgetContents")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 1, 1, 1)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.RollButton.clicked.connect(lambda: self.roll())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def roll(self):
        print('Clicity Clakity')
        input = str(self.RollInputLine.text())
        prepare_input_line(input)
#        initial_roll(1,10)  # ToDo: make it take input from input line
#        self.RollInputLine.setText('')  # Todo: It MAY export default roll like 12d8+5
        return

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Roller"))
        self.RollButton.setText(_translate("MainWindow", "Make Roll"))
        self.pushButton.setText(_translate("MainWindow", "ReRoll"))
        self.pushButton_3.setText(_translate("MainWindow", "ReRoll"))
        self.RollInputLine.setText('4d6+12')


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = RollerWindow()
ui.__init__()
MainWindow.show()
sys.exit(app.exec_())
