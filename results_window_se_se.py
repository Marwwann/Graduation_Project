# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results_window_se_se.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Results_window_se_se(object):
    def setupUi(self, Results_window_se_se):
        Results_window_se_se.setObjectName("Results_window_se_se")
        Results_window_se_se.resize(549, 206)
        self.centralwidget = QtWidgets.QWidget(Results_window_se_se)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        Results_window_se_se.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Results_window_se_se)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 21))
        self.menubar.setObjectName("menubar")
        Results_window_se_se.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Results_window_se_se)
        self.statusbar.setObjectName("statusbar")
        Results_window_se_se.setStatusBar(self.statusbar)

        self.retranslateUi(Results_window_se_se)
        QtCore.QMetaObject.connectSlotsByName(Results_window_se_se)

    def retranslateUi(self, Results_window_se_se):
        _translate = QtCore.QCoreApplication.translate
        Results_window_se_se.setWindowTitle(_translate("Results_window_se_se", "Table of Results"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Results_window_se_se", "CL="))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Results_window_se_se", "CL"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Results_window_se_se", "Av"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Results_window_se_se", "BW"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Results_window_se_se", "GBW"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Results_window_se_se", "UGF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results_window_se_se = QtWidgets.QMainWindow()
    ui = Ui_Results_window_se_se()
    ui.setupUi(Results_window_se_se)
    Results_window_se_se.show()
    sys.exit(app.exec_())
