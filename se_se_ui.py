# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'se_se.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_se(object):
    def setupUi(self, MainWindow_se):
        MainWindow_se.setObjectName("MainWindow_se")
        MainWindow_se.resize(637, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow_se)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_paths_layout = QtWidgets.QVBoxLayout()
        self.input_paths_layout.setObjectName("input_paths_layout")
        self.Model_path_layout = QtWidgets.QHBoxLayout()
        self.Model_path_layout.setObjectName("Model_path_layout")
        self.Model_path_label_se_se = QtWidgets.QLabel(self.centralwidget)
        self.Model_path_label_se_se.setObjectName("Model_path_label_se_se")
        self.Model_path_layout.addWidget(self.Model_path_label_se_se)
        self.model_path_lineEdit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.model_path_lineEdit_se_se.setObjectName("model_path_lineEdit_se_se")
        self.Model_path_layout.addWidget(self.model_path_lineEdit_se_se)
        self.model_path_browse_button_se_se = QtWidgets.QPushButton(self.centralwidget)
        self.model_path_browse_button_se_se.setObjectName("model_path_browse_button_se_se")
        self.Model_path_layout.addWidget(self.model_path_browse_button_se_se)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.Model_path_layout.addItem(spacerItem)
        self.input_paths_layout.addLayout(self.Model_path_layout)
        self.Netlist_path_layout = QtWidgets.QHBoxLayout()
        self.Netlist_path_layout.setObjectName("Netlist_path_layout")
        self.netlist_path_label = QtWidgets.QLabel(self.centralwidget)
        self.netlist_path_label.setObjectName("netlist_path_label")
        self.Netlist_path_layout.addWidget(self.netlist_path_label)
        self.netlist_path_lineEdit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.netlist_path_lineEdit_se_se.setObjectName("netlist_path_lineEdit_se_se")
        self.Netlist_path_layout.addWidget(self.netlist_path_lineEdit_se_se)
        self.Netlist_path_browse_button_se_se = QtWidgets.QPushButton(self.centralwidget)
        self.Netlist_path_browse_button_se_se.setObjectName("Netlist_path_browse_button_se_se")
        self.Netlist_path_layout.addWidget(self.Netlist_path_browse_button_se_se)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.Netlist_path_layout.addItem(spacerItem1)
        self.input_paths_layout.addLayout(self.Netlist_path_layout)
        self.verticalLayout.addLayout(self.input_paths_layout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.Capacitive_load_layout = QtWidgets.QHBoxLayout()
        self.Capacitive_load_layout.setObjectName("Capacitive_load_layout")
        self.capacitive_load_label = QtWidgets.QLabel(self.centralwidget)
        self.capacitive_load_label.setObjectName("capacitive_load_label")
        self.Capacitive_load_layout.addWidget(self.capacitive_load_label)
        spacerItem3 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.Capacitive_load_layout.addItem(spacerItem3)
        self.Capacitive_load_lineedit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.Capacitive_load_lineedit_se_se.setObjectName("Capacitive_load_lineedit_se_se")
        self.Capacitive_load_layout.addWidget(self.Capacitive_load_lineedit_se_se)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.Capacitive_load_layout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.Capacitive_load_layout)
        self.VINCM_layout = QtWidgets.QHBoxLayout()
        self.VINCM_layout.setObjectName("VINCM_layout")
        self.supply_voltage_label = QtWidgets.QLabel(self.centralwidget)
        self.supply_voltage_label.setObjectName("supply_voltage_label")
        self.VINCM_layout.addWidget(self.supply_voltage_label)
        spacerItem5 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.VINCM_layout.addItem(spacerItem5)
        self.supply_voltage_lineedit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.supply_voltage_lineedit_se_se.setObjectName("supply_voltage_lineedit_se_se")
        self.VINCM_layout.addWidget(self.supply_voltage_lineedit_se_se)
        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.VINCM_layout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.VINCM_layout)
        self.supply_voltage_layout = QtWidgets.QHBoxLayout()
        self.supply_voltage_layout.setObjectName("supply_voltage_layout")
        self.VINCM_label = QtWidgets.QLabel(self.centralwidget)
        self.VINCM_label.setObjectName("VINCM_label")
        self.supply_voltage_layout.addWidget(self.VINCM_label)
        spacerItem7 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.supply_voltage_layout.addItem(spacerItem7)
        self.VINCM_lineedit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.VINCM_lineedit_se_se.setObjectName("VINCM_lineedit_se_se")
        self.supply_voltage_layout.addWidget(self.VINCM_lineedit_se_se)
        spacerItem8 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.supply_voltage_layout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.supply_voltage_layout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.Start_freq_layout = QtWidgets.QHBoxLayout()
        self.Start_freq_layout.setObjectName("Start_freq_layout")
        self.start_freq_label = QtWidgets.QLabel(self.centralwidget)
        self.start_freq_label.setObjectName("start_freq_label")
        self.Start_freq_layout.addWidget(self.start_freq_label)
        spacerItem10 = QtWidgets.QSpacerItem(94, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.Start_freq_layout.addItem(spacerItem10)
        self.start_freq_lineEdit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.start_freq_lineEdit_se_se.setObjectName("start_freq_lineEdit_se_se")
        self.Start_freq_layout.addWidget(self.start_freq_lineEdit_se_se)
        spacerItem11 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.Start_freq_layout.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.Start_freq_layout)
        self.stop_freq_layout = QtWidgets.QHBoxLayout()
        self.stop_freq_layout.setObjectName("stop_freq_layout")
        self.stop_freq_label = QtWidgets.QLabel(self.centralwidget)
        self.stop_freq_label.setObjectName("stop_freq_label")
        self.stop_freq_layout.addWidget(self.stop_freq_label)
        spacerItem12 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.stop_freq_layout.addItem(spacerItem12)
        self.stop_freq_lineEdit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.stop_freq_lineEdit_se_se.setObjectName("stop_freq_lineEdit_se_se")
        self.stop_freq_layout.addWidget(self.stop_freq_lineEdit_se_se)
        spacerItem13 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.stop_freq_layout.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.stop_freq_layout)
        self.no_of_points_layout = QtWidgets.QHBoxLayout()
        self.no_of_points_layout.setObjectName("no_of_points_layout")
        self.no_of_points_label = QtWidgets.QLabel(self.centralwidget)
        self.no_of_points_label.setObjectName("no_of_points_label")
        self.no_of_points_layout.addWidget(self.no_of_points_label)
        spacerItem14 = QtWidgets.QSpacerItem(32, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.no_of_points_layout.addItem(spacerItem14)
        self.no_of_points_lineedit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.no_of_points_lineedit_se_se.setObjectName("no_of_points_lineedit_se_se")
        self.no_of_points_layout.addWidget(self.no_of_points_lineedit_se_se)
        spacerItem15 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.no_of_points_layout.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.no_of_points_layout)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem16)
        self.message_layout = QtWidgets.QHBoxLayout()
        self.message_layout.setObjectName("message_layout")
        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setObjectName("message_label")
        self.message_layout.addWidget(self.message_label)
        self.verticalLayout.addLayout(self.message_layout)
        self.netlist_points_layout = QtWidgets.QGridLayout()
        self.netlist_points_layout.setObjectName("netlist_points_layout")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.netlist_points_layout.addItem(spacerItem17, 0, 2, 1, 1)
        self.ground_lineedit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.ground_lineedit_se_se.setObjectName("ground_lineedit_se_se")
        self.netlist_points_layout.addWidget(self.ground_lineedit_se_se, 0, 4, 1, 1)
        self.VOUT_lineedit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.VOUT_lineedit_se_se.setObjectName("VOUT_lineedit_se_se")
        self.netlist_points_layout.addWidget(self.VOUT_lineedit_se_se, 1, 4, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.netlist_points_layout.addItem(spacerItem18, 1, 5, 1, 1)
        self.VIN_lineedit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.VIN_lineedit_se_se.setObjectName("VIN_lineedit_se_se")
        self.netlist_points_layout.addWidget(self.VIN_lineedit_se_se, 1, 1, 1, 1)
        self.VDD_label = QtWidgets.QLabel(self.centralwidget)
        self.VDD_label.setObjectName("VDD_label")
        self.netlist_points_layout.addWidget(self.VDD_label, 0, 0, 1, 1)
        self.Ground_label = QtWidgets.QLabel(self.centralwidget)
        self.Ground_label.setObjectName("Ground_label")
        self.netlist_points_layout.addWidget(self.Ground_label, 0, 3, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.netlist_points_layout.addItem(spacerItem19, 0, 5, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.netlist_points_layout.addItem(spacerItem20, 1, 2, 1, 1)
        self.VINN_label = QtWidgets.QLabel(self.centralwidget)
        self.VINN_label.setObjectName("VINN_label")
        self.netlist_points_layout.addWidget(self.VINN_label, 1, 0, 1, 1)
        self.VINP_label = QtWidgets.QLabel(self.centralwidget)
        self.VINP_label.setObjectName("VINP_label")
        self.netlist_points_layout.addWidget(self.VINP_label, 1, 3, 1, 1)
        self.VDD_lineedit_se_se = QtWidgets.QLineEdit(self.centralwidget)
        self.VDD_lineedit_se_se.setObjectName("VDD_lineedit_se_se")
        self.netlist_points_layout.addWidget(self.VDD_lineedit_se_se, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.netlist_points_layout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem21, 1, 0, 1, 1)
        self.generate_and_plot_button_se_se = QtWidgets.QPushButton(self.centralwidget)
        self.generate_and_plot_button_se_se.setObjectName("generate_and_plot_button_se_se")
        self.gridLayout_2.addWidget(self.generate_and_plot_button_se_se, 2, 0, 1, 1)
        MainWindow_se.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_se)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_se.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_se)
        self.statusbar.setObjectName("statusbar")
        MainWindow_se.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_se)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_se)
        MainWindow_se.setTabOrder(self.model_path_lineEdit_se_se, self.model_path_browse_button_se_se)
        MainWindow_se.setTabOrder(self.model_path_browse_button_se_se, self.netlist_path_lineEdit_se_se)
        MainWindow_se.setTabOrder(self.netlist_path_lineEdit_se_se, self.Netlist_path_browse_button_se_se)
        MainWindow_se.setTabOrder(self.Netlist_path_browse_button_se_se, self.Capacitive_load_lineedit_se_se)
        MainWindow_se.setTabOrder(self.Capacitive_load_lineedit_se_se, self.supply_voltage_lineedit_se_se)
        MainWindow_se.setTabOrder(self.supply_voltage_lineedit_se_se, self.VINCM_lineedit_se_se)
        MainWindow_se.setTabOrder(self.VINCM_lineedit_se_se, self.start_freq_lineEdit_se_se)
        MainWindow_se.setTabOrder(self.start_freq_lineEdit_se_se, self.stop_freq_lineEdit_se_se)
        MainWindow_se.setTabOrder(self.stop_freq_lineEdit_se_se, self.no_of_points_lineedit_se_se)
        MainWindow_se.setTabOrder(self.no_of_points_lineedit_se_se, self.VDD_lineedit_se_se)
        MainWindow_se.setTabOrder(self.VDD_lineedit_se_se, self.ground_lineedit_se_se)
        MainWindow_se.setTabOrder(self.ground_lineedit_se_se, self.VIN_lineedit_se_se)
        MainWindow_se.setTabOrder(self.VIN_lineedit_se_se, self.VOUT_lineedit_se_se)
        MainWindow_se.setTabOrder(self.VOUT_lineedit_se_se, self.generate_and_plot_button_se_se)

    def retranslateUi(self, MainWindow_se):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_se.setWindowTitle(_translate("MainWindow_se", "Single Ended Input Single Ended Output OTA"))
        self.Model_path_label_se_se.setText(_translate("MainWindow_se", "Model Path"))
        self.model_path_lineEdit_se_se.setPlaceholderText(_translate("MainWindow_se", "Choose model file path"))
        self.model_path_browse_button_se_se.setText(_translate("MainWindow_se", "Browse"))
        self.netlist_path_label.setText(_translate("MainWindow_se", "Netlist Path"))
        self.netlist_path_lineEdit_se_se.setPlaceholderText(_translate("MainWindow_se", "Choose netlist path"))
        self.Netlist_path_browse_button_se_se.setText(_translate("MainWindow_se", "Browse"))
        self.capacitive_load_label.setText(_translate("MainWindow_se", "Capacitive Load Value"))
        self.Capacitive_load_lineedit_se_se.setPlaceholderText(_translate("MainWindow_se", "Default value = 1pF"))
        self.supply_voltage_label.setText(_translate("MainWindow_se", "Supply Voltage (VDD)"))
        self.VINCM_label.setText(_translate("MainWindow_se", "Input DC Voltage"))
        self.start_freq_label.setText(_translate("MainWindow_se", "Start Frequency"))
        self.stop_freq_label.setText(_translate("MainWindow_se", "Stop Frequency"))
        self.no_of_points_label.setText(_translate("MainWindow_se", "Number of Points per Decade"))
        self.message_label.setText(_translate("MainWindow_se", "Write the node names in your netlist of the following:"))
        self.VDD_label.setText(_translate("MainWindow_se", "VDD"))
        self.Ground_label.setText(_translate("MainWindow_se", "Ground"))
        self.VINN_label.setText(_translate("MainWindow_se", "VIN"))
        self.VINP_label.setText(_translate("MainWindow_se", "VOUT"))
        self.generate_and_plot_button_se_se.setText(_translate("MainWindow_se", "Generate and Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_se = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_se()
    ui.setupUi(MainWindow_se)
    MainWindow_se.show()
    sys.exit(app.exec_())