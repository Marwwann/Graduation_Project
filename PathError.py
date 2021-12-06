# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PathError.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BrowseValidation(object):
    def setupUi(self, BrowseValidation):
        BrowseValidation.setObjectName("BrowseValidation")
        BrowseValidation.resize(420, 175)
        self.centralwidget = QtWidgets.QWidget(BrowseValidation)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.InsertPatLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.InsertPatLabel.setFont(font)
        self.InsertPatLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InsertPatLabel.setObjectName("InsertPatLabel")
        self.verticalLayout.addWidget(self.InsertPatLabel)
        self.CloseButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton2.setObjectName("CloseButton2")
        self.verticalLayout.addWidget(self.CloseButton2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        BrowseValidation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BrowseValidation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        BrowseValidation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BrowseValidation)
        self.statusbar.setObjectName("statusbar")
        BrowseValidation.setStatusBar(self.statusbar)

        self.retranslateUi(BrowseValidation)
        QtCore.QMetaObject.connectSlotsByName(BrowseValidation)

    def retranslateUi(self, BrowseValidation):
        _translate = QtCore.QCoreApplication.translate
        BrowseValidation.setWindowTitle(_translate("BrowseValidation", "Path Missing"))
        self.InsertPatLabel.setText(_translate("BrowseValidation", "PATH MISSING"))
        self.CloseButton2.setText(_translate("BrowseValidation", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BrowseValidation = QtWidgets.QMainWindow()
    ui = Ui_BrowseValidation()
    ui.setupUi(BrowseValidation)
    BrowseValidation.show()
    sys.exit(app.exec_())
