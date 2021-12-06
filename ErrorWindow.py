# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ErrorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorWindow(object):
    def setupUi(self, ErrorWindow):
        ErrorWindow.setObjectName("ErrorWindow")
        ErrorWindow.resize(467, 201)
        self.centralwidget = QtWidgets.QWidget(ErrorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ErrorLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.verticalLayout_3.addWidget(self.ErrorLabel)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ErrorMsg = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMsg.setFont(font)
        self.ErrorMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorMsg.setObjectName("ErrorMsg")
        self.verticalLayout.addWidget(self.ErrorMsg)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ErrorMsg2 = QtWidgets.QLabel(self.centralwidget)
        self.ErrorMsg2.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorMsg2.setObjectName("ErrorMsg2")
        self.verticalLayout_5.addWidget(self.ErrorMsg2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setObjectName("CloseButton")
        self.verticalLayout_6.addWidget(self.CloseButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        ErrorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ErrorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 21))
        self.menubar.setObjectName("menubar")
        ErrorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ErrorWindow)
        self.statusbar.setObjectName("statusbar")
        ErrorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ErrorWindow)
        QtCore.QMetaObject.connectSlotsByName(ErrorWindow)

    def retranslateUi(self, ErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        ErrorWindow.setWindowTitle(_translate("ErrorWindow", "Error"))
        self.ErrorLabel.setText(_translate("ErrorWindow", "ERROR"))
        self.ErrorMsg.setText(_translate("ErrorWindow", "Invalid Input Format"))
        self.ErrorMsg2.setText(_translate("ErrorWindow", "For more information about the input format, please refer to the help tab."))
        self.CloseButton.setText(_translate("ErrorWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorWindow = QtWidgets.QMainWindow()
    ui = Ui_ErrorWindow()
    ui.setupUi(ErrorWindow)
    ErrorWindow.show()
    sys.exit(app.exec_())
