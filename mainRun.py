from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QRunnable, QThreadPool, QDir
import threading
import sys
from mainUi4 import Ui_main_window
import pyqtgraph as pg
# import sweep file
from GmIdKit import techsweep_run
import numpy as np
from math import ceil
import pickle
import re
import matplotlib.pyplot as plt
from GmIdKit.lookupMos import lookup
from dip_se_op import dip_se_op

class main_window(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self):
        # Create UI
        QtWidgets.QMainWindow.__init__(self)
        # initialize widgets
        self.initWidgets()
        Ui_main_window.setupUi(self, self)
        # init variables
        self.initVariables()
        # init and define constants
        self.defCons()
        # config Plots
        self.ConfigPlot()
        # connections
        self.connections()


    def ConfigPlot(self):
        self.plotGmIdwidget_1.plotItem.showGrid(True, True, 0.7)
        self.plotGmIdwidget_1.plotItem.setTitle('Fig.1 ')
        self.plotGmIdwidget_1.plotItem.setLabel('bottom', 'GM/ID', units='S')
        self.plotGmIdwidget_2.plotItem.showGrid(True, True, 0.7)
        self.plotGmIdwidget_2.plotItem.setTitle('Fig.2 ')
        self.plotGmIdwidget_2.plotItem.setLabel('bottom', 'GM/ID', units='S')
        self.plotGmIdwidget_3.plotItem.showGrid(True, True, 0.7)
        self.plotGmIdwidget_3.plotItem.setTitle('Fig.3 ')
        self.plotGmIdwidget_3.plotItem.setLabel('bottom', 'GM/ID', units='S')
        self.plotGmIdwidget_4.plotItem.showGrid(True, True, 0.7)
        self.plotGmIdwidget_4.plotItem.setTitle('Fig.4 ')
        self.plotGmIdwidget_4.plotItem.setLabel('bottom', 'GM/ID', units='S')
        self.redLinePen = pg.mkPen('r', width=1.5, style=QtCore.Qt.DashLine)
        self.greenLinePen = pg.mkPen('g', width=2.5, style=QtCore.Qt.SolidLine)
        self.blueLinePen = pg.mkPen('b', width=2.5, style=QtCore.Qt.SolidLine)
        self.magLinePen = pg.mkPen('m', width=2.5, style=QtCore.Qt.SolidLine)
        self.yellLinePen = pg.mkPen('y', width=2.5, style=QtCore.Qt.SolidLine)
        self.line1 = pg.InfiniteLine(angle=90, pen=self.redLinePen, movable=False)
        self.line2 = pg.InfiniteLine(angle=90, pen=self.redLinePen, movable=False)
        self.line3 = pg.InfiniteLine(angle=90, pen=self.redLinePen, movable=False)
        self.line4 = pg.InfiniteLine(angle=90, pen=self.redLinePen, movable=False)
        #self.plotGmIdwidget_1.addItem(self.line1, ignoreBounds=True)
        #self.plotGmIdwidget_2.addItem(self.line2, ignoreBounds=True)
        #self.plotGmIdwidget_3.addItem(self.line3, ignoreBounds=True)
        #self.plotGmIdwidget_4.addItem(self.line4, ignoreBounds=True)

    def initVariables(self):
        self.modelPath = ""
        self.loadedData = False
        self.LRangePlotGmId = [1]
        self.generatechartsError = False

    def defCons(self):
        print("define const")

    def initWidgets(self):
        print("init widgets")
        # change pyqtgraph setting
        pg.setConfigOption('background', 'w')


    def connections(self):
        # generate GmId charts tab
        # select model and ngSpice command
        self.browseModelbutton.clicked.connect(self.getModelPath)
        self.generatepushButton.clicked.connect(self.generateCharts)
        # connect line Edit to calculate size
        self.generateVGSLineEdit.textChanged.connect(self.calculateSize)
        self.generateVDSlineEdit.textChanged.connect(self.calculateSize)
        self.generateVBSlineEdit.textChanged.connect(self.calculateSize)
        self.generateLlineEdit.textChanged.connect(self.calculateSize)
        # load data Button
        self.browseDataPlotbutton.clicked.connect(self.getPlotDataPath)
        # plot connections
        self.plotGmIdComboBox1_1.currentTextChanged.connect(self.plotGmId1)
        self.plotGmIdComboBox1_2.currentTextChanged.connect(self.plotGmId1)
        self.plotGmIdComboBox1_3.currentTextChanged.connect(self.plotGmId1)

        self.plotGmIdComboBox2_1.currentTextChanged.connect(self.plotGmId2)
        self.plotGmIdComboBox2_2.currentTextChanged.connect(self.plotGmId2)
        self.plotGmIdComboBox2_3.currentTextChanged.connect(self.plotGmId2)

        self.plotGmIdComboBox3_1.currentTextChanged.connect(self.plotGmId3)
        self.plotGmIdComboBox3_2.currentTextChanged.connect(self.plotGmId3)
        self.plotGmIdComboBox3_3.currentTextChanged.connect(self.plotGmId3)

        self.plotGmIdComboBox4_1.currentTextChanged.connect(self.plotGmId4)
        self.plotGmIdComboBox4_2.currentTextChanged.connect(self.plotGmId4)
        self.plotGmIdComboBox4_3.currentTextChanged.connect(self.plotGmId4)
        # mouse
        #self.plotGmIdwidget_1.scene().sigMouseMoved.connect(self.MouseMoved1)
        #self.plotGmIdwidget_2.scene().sigMouseMoved.connect(self.MouseMoved2)
        #self.plotGmIdwidget_3.scene().sigMouseMoved.connect(self.MouseMoved3)
        #self.plotGmIdwidget_4.scene().sigMouseMoved.connect(self.MouseMoved4)
        #self.mainTabWidget.tabBarClicked.connect(self.windowSize)
        self.plotGmIdwidget_1.scene().sigMouseMoved.connect(self.onMouseMoved_1)
        self.plotGmIdwidget_2.scene().sigMouseMoved.connect(self.onMouseMoved_2)
        self.plotGmIdwidget_3.scene().sigMouseMoved.connect(self.onMouseMoved_3)
        self.plotGmIdwidget_4.scene().sigMouseMoved.connect(self.onMouseMoved_4)
        self.pushButton.clicked.connect(self.plot_dip_se_op)
        self.browse_netlist_button.clicked.connect(self.get_netlist_path)

    def windowSize(self):
        coord = self.geometry().getCoords()
        index = self.mainTabWidget.currentIndex()
        print(index)
        #print(self.mainTabWidget.currentChanged())
        if index == 0:
            self.setGeometry(coord[0], coord[1], 435, 345)
        elif index == 1:
            self.setGeometry(coord[0], coord[1], 754, 650)

    def getModelPath(self):
        self.modelPath = QFileDialog.getOpenFileName()[0]
        self.modelPathLineEdit.setText(self.modelPath)
        print(self.modelPath)

    def getPlotDataPath(self):
        self.plotDataPath = QFileDialog.getOpenFileName()[0]
        self.LoaDataPlotlineEdit.setText(self.plotDataPath)
        try:
            with open(self.plotDataPath, "rb") as f:
                self.mosData = pickle.load(f)
            self.loadedData = True
        except Exception as e:
            print(e)


    def generateCharts(self):
        self.generatechartsError = False
        self.checkForGeneratinParameters(self.generateLlineEdit, "L")
        self.checkForGeneratinParameters(self.generateVGSLineEdit, "V")
        self.checkForGeneratinParameters(self.generateVDSlineEdit, "V")
        self.checkForGeneratinParameters(self.generateVBSlineEdit, "V")
        if self.generatechartsError:
            return
        thread1 = generateChartThread(self)
        thread1.start()


    def getL(self, Larg):
        try:
            Larr=Larg.strip().split(" ")
            Lfinal= self.getSweepParameterRange(Larr[0])
        except:
            print("No L specified")
        for i in range(1, len(Larr)):
            Lfinal = np.concatenate(Lfinal, self.getSweepParameterRange(Larr[i]))
        return Lfinal


    # creat a arange from input lineEdit
    def getSweepParameterRange(self, Lstr):
        #print(Lstr, Lstr.split(":"))
        try:
            LList = []
            tempStr=Lstr.split(":")
            for i in tempStr:
                LList.append(float(i))
            return np.arange(LList[0], LList[2] + LList[1] - 0.0000000000000001, LList[1])
        except Exception as e:
            print("Error in Length Format", e)


    # get min max step from line edit
    def getSweepParameterArguments(self, paramStr):
        paramStr.replace(" ", "")
        try:
            paramList = [float(i) for i in paramStr.split(":")]
            return paramList
        except:0
        print("Error in Parameters Format")

    def calculateSize(self):
        try:
            LLength = len(self.getL(self.generateLlineEdit.text()))
            VBSLength = len(self.getSweepParameterRange(self.generateVBSlineEdit.text()))
            VDSLength = len(self.getSweepParameterRange(self.generateVDSlineEdit.text()))
            VGSLength = len(self.getSweepParameterRange(self.generateVGSLineEdit.text()))
            expectedSize = (LLength * VBSLength * VDSLength * VGSLength * 8 * 9)/(1024 * 1024)
            self.expectedSizelineEdit.setText("{0:4.4f}".format(expectedSize)+" MB")

        except:
            pass

    def checkForGeneratinParameters(self, genParamLineEdit, type):
        # check for invalid format
        self.isGenParameterInValidFormat(genParamLineEdit)
        # check for empty input
        self.isGenParameterEmpty(genParamLineEdit, type)
        # check for bad step , min and max values
        self.isGenPatameterHaveValueError(genParamLineEdit)


    def isGenParameterInValidFormat(self, genParamLineEdit):
        try:
            text = genParamLineEdit.text()
            numOfColon = len(re.findall(":", text))
            print(numOfColon)
            if len(re.findall("([0-9.]+:[0-9.]+:[0-9.]+)", text)) != numOfColon / 2 or numOfColon % 2 != 0:
                raise Exception("ERROR in input format ")

        except Exception as e:
            print(e)
            self.generatechartsError = True
            QMessageBox.Warning("ERROR", e)

    def isGenParameterEmpty(self, genParamLineEdit, type):
        if len(genParamLineEdit.text()) == 0 and type == "V":
            genParamLineEdit.setText("0:0.1:1")
        elif len(genParamLineEdit.text()) == 0 and type == "L":
            genParamLineEdit.setText("1:0.5:2")

    def isGenPatameterHaveValueError(self, genParamLineEdit): #value error is 0 step or max < min
        genParValues = self.getSweepParameterArguments(genParamLineEdit.text())
        if genParValues[1] == 0:
            QMessageBox.Warning(self, "ERROR", "invalid step value")
            print("Invalid Step Value, Can not be zero")
            self.generatechartsError = True
        if genParValues[2] < genParValues[0]:
            QMessageBox.Warning(self, "ERROR", "Maximum Value Should Be Higher Than Minimum Value")
            self.generatechartsError = True



    def plotGmId1(self):
        yaxies1 = self.plotGmIdComboBox1_1.currentText()
        yaxies2 = self.plotGmIdComboBox1_2.currentText()
        yaxies3 = self.plotGmIdComboBox1_3.currentText()
        if self.LRangPlot.text() != "":
            self.LRangePlotGmId = self.getL(self.LRangPlot.text())

        if yaxies1 != "------" and yaxies2 != "------" and yaxies3 != "------" and self.loadedData:
            yaxis = yaxies1 + yaxies2 + yaxies3
            self.plotGmIdwidget_1.plotItem.setLabel('left', yaxis)
            y = lookup(self.mosData, yaxis, "GM/ID", L=self.LRangePlotGmId, RANGE=np.arange(4, 25, 0.4))
            self.plotGmIdwidget_1.clear()
            for i in range(0, len(self.LRangePlotGmId)):
                x = pg.PlotDataItem(np.arange(4, 25, 0.4), y[i], pen=self.blueLinePen, clear=True)
                self.plotGmIdwidget_1.addItem(x)

            self.plotGmIdwidget_1.addItem(self.line1, ignoreBounds=True)
           # proxy_1 = pg.SignalProxy(plotGmIdwidget_1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

    def plotGmId2(self):
        yaxies1 = self.plotGmIdComboBox2_1.currentText()
        yaxies2 = self.plotGmIdComboBox2_2.currentText()
        yaxies3 = self.plotGmIdComboBox2_3.currentText()
        if self.LRangPlot.text() != "":
            self.LRangePlotGmId = self.getL(self.LRangPlot.text())

        if yaxies1 != "------" and yaxies2 != "------" and yaxies3 != "------" and self.loadedData:
            yaxis = yaxies1 + yaxies2 + yaxies3
            self.plotGmIdwidget_2.plotItem.setLabel('left', yaxis)
            y = lookup(self.mosData, yaxis, "GM/ID", L=self.LRangePlotGmId, RANGE=np.arange(4, 25, 0.4))
            self.plotGmIdwidget_2.clear()
            for i in range(0, len(self.LRangePlotGmId)):
                x = pg.PlotDataItem(np.arange(4, 25, 0.4), y[i], pen=self.greenLinePen, clear=True)
                self.plotGmIdwidget_2.addItem(x)

            self.plotGmIdwidget_2.addItem(self.line2, ignoreBounds=True)
          #  proxy_2 = pg.SignalProxy(plotGmIdwidget_2.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
    def plotGmId3(self):
        yaxies1 = self.plotGmIdComboBox3_1.currentText()
        yaxies2 = self.plotGmIdComboBox3_2.currentText()
        yaxies3 = self.plotGmIdComboBox3_3.currentText()
        if self.LRangPlot.text() != "":
            self.LRangePlotGmId = self.getL(self.LRangPlot.text())

        if yaxies1 != "------" and yaxies2 != "------" and yaxies3 != "------" and self.loadedData:
            yaxis = yaxies1 + yaxies2 + yaxies3
            self.plotGmIdwidget_3.plotItem.setLabel('left', yaxis)
            y = lookup(self.mosData, yaxis, "GM/ID", L=self.LRangePlotGmId, RANGE=np.arange(4, 25, 0.4))
            self.plotGmIdwidget_3.clear()
            for i in range(0, len(self.LRangePlotGmId)):
                x = pg.PlotDataItem(np.arange(4, 25, 0.4), y[i], pen=self.magLinePen, clear=True)
                self.plotGmIdwidget_3.addItem(x)

            self.plotGmIdwidget_3.addItem(self.line3, ignoreBounds=True)
           # proxy_3 = pg.SignalProxy(plotGmIdwidget_3.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
    def plotGmId4(self):
        yaxies1 = self.plotGmIdComboBox4_1.currentText()
        yaxies2 = self.plotGmIdComboBox4_2.currentText()
        yaxies3 = self.plotGmIdComboBox4_3.currentText()
        if self.LRangPlot.text() != "":
            self.LRangePlotGmId = self.getL(self.LRangPlot.text())

        if yaxies1 != "------" and yaxies2 != "------" and yaxies3 != "------" and self.loadedData:
            yaxis = yaxies1 + yaxies2 + yaxies3
            self.plotGmIdwidget_4.plotItem.setLabel('left', yaxis)
            y = lookup(self.mosData, yaxis, "GM/ID", L=self.LRangePlotGmId, RANGE=np.arange(4, 25, 0.4))
            self.plotGmIdwidget_4.clear()
            for i in range(0, len(self.LRangePlotGmId)):
                x = pg.PlotDataItem(np.arange(4, 25, 0.4), y[i], pen=self.yellLinePen, clear=True)
                self.plotGmIdwidget_4.addItem(x)

            self.plotGmIdwidget_4.addItem(self.line4, ignoreBounds=True)
           # proxy_4 = pg.SignalProxy(plotGmIdwidget_4.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
    #def MouseMoved1(self, evt):
      #  mousePointI = self.plotGmIdwidget_1.plotItem.vb.mapSceneToView(evt)
       # self.line1.setPos(mousePointI.x())
       # self.line2.setPos(mousePointI.x())
      #  self.line3.setPos(mousePointI.x())
       # self.line4.setPos(mousePointI.x())

  #  def MouseMoved2(self, evt):
     #   mousePointI = self.plotGmIdwidget_2.plotItem.vb.mapSceneToView(evt)
     #   self.line1.setPos(mousePointI.x())
      #  self.line2.setPos(mousePointI.x())
     #   self.line3.setPos(mousePointI.x())
      #  self.line4.setPos(mousePointI.x())

  #  def MouseMoved3(self, evt):
     #   mousePointI = self.plotGmIdwidget_3.plotItem.vb.mapSceneToView(evt)
     #   self.line1.setPos(mousePointI.x())
      #  self.line2.setPos(mousePointI.x())
      #  self.line3.setPos(mousePointI.x())
      #  self.line4.setPos(mousePointI.x())

  #  def MouseMoved4(self, evt):
     #   mousePointI = self.plotGmIdwidget_4.plotItem.vb.mapSceneToView(evt)
      #  self.line1.setPos(mousePointI.x())
     #   self.line2.setPos(mousePointI.x())
     #   self.line3.setPos(mousePointI.x())
     #   self.line4.setPos(mousePointI.x())

  #  def mouseMoved_1(evt):
   #     mousePoint = self.plotGmIdwidget_1.vb.mapSceneToView(evt[0])
    #    self.label.setText(
     #       "<span style='font-size: 14pt; color: black'> x = %0.2f, <span style='color: black'> y = %0.2f</span>" % (
      #      mousePoint.x(), mousePoint.y()))

   # def mouseMoved_2(evt):
    #    mousePoint = self.plotGmIdwidget_2.vb.mapSceneToView(evt[0])
     #   self.label.setText(
      #      "<span style='font-size: 14pt; color: white'> x = %0.2f, <span style='color: white'> y = %0.2f</span>" % (
       #     mousePoint.x(), mousePoint.y()))


   # def mouseMoved_3(evt):
    #    mousePoint = plotGmIdwidget_3.vb.mapSceneToView(evt[0])
     #   label.setText(
      #      "<span style='font-size: 14pt; color: white'> x = %0.2f, <span style='color: white'> y = %0.2f</span>" % (
       #     mousePoint.x(), mousePoint.y()))


   # def mouseMoved_4(evt):
    #    mousePoint = plotGmIdwidget_4.vb.mapSceneToView(evt[0])
     #   label.setText(
      #      "<span style='font-size: 14pt; color: black'> x = %0.2f, <span style='color: black'> y = %0.2f</span>" % (
       #     mousePoint.x(), mousePoint.y()))

    def onMouseMoved_1(self, point):
        p1 = self.plotGmIdwidget_1.plotItem.vb.mapSceneToView(point)
        #self.statusBar().showMessage("{}-{}".format(p1.x(), p1.y()))
        self.label_13.setText(
            "<span style='font-size: 8pt; color: black'> x = %0.2f, <span style='color: black'> y = %0.2f</span>" % (
            p1.x(), p1.y()))

    def onMouseMoved_2(self, point):
        p2 = self.plotGmIdwidget_2.plotItem.vb.mapSceneToView(point)

        self.label_15.setText(
            "<span style='font-size: 8pt; color: black'> x = %0.2f, <span style='color: black'> y = %0.2f</span>" % (
             p2.x(), p2.y()))
    def onMouseMoved_3(self, point):
        p3 = self.plotGmIdwidget_3.plotItem.vb.mapSceneToView(point)

        self.label_14.setText(
            "<span style='font-size: 8pt; color: black'> x = %0.2f, <span style='color: black'> y = %0.2f</span>" % (
            p3.x(), p3.y()))
    def onMouseMoved_4(self, point):
        p4 = self.plotGmIdwidget_4.plotItem.vb.mapSceneToView(point)

        self.label_16.setText(
            "<span style='font-size: 8pt; color: black'> x = %0.2f, <span style='color: black'> y = %0.2f</span>" % (
            p4.x(), p4.y()))

    def test(self):
        print("xxxx")

    def get_netlist_path(self):

        self.subckt_netlist = QFileDialog.getOpenFileName()[0]
        self.netlist_path_lineEdit.setText(self.subckt_netlist)
        return

    def get_cap(self):

        cap = self.Capacitance_lineEdit.text()
        capacitance = []
        if cap == '':
            capacitance.append('1f')

        else:
            range_flag = 0
            if re.search(':', cap):
                x = re.split(':', cap)
                range_flag = 1
            else:
                x = re.split('\s', cap)
                range_flag = 0

            if x[-1] == '':
                x.pop()

            if range_flag == 1:
                range_list = []
                for i in range(len(x)):
                    y = re.split('p', x[i])
                    y.pop()
                    range_list.append(y)
                pre_capacitance = np.arange(int(range_list[0][0]), int(range_list[2][0]), int(range_list[1][0]))

                for i in pre_capacitance:
                    capacitance.append(str(i) + 'p')
            else:
                capacitance = x
        print(capacitance)
        return capacitance




    def plot_dip_se_op(self):

        netlist = self.netlist_path_lineEdit.text()
        VDD_in = self.lineEdit_2.text()
        VINCM_in = self.VINCM_lineEdit.text()
        VIND_in = self.VIND_lineEdit.text()

        cap_in = self.get_cap()

        start_freq_in = self.start_freq_lineEdit.text()
        stop_freq_in = self.Stop_freq_lineEdit.text()
        no_points_in = self.Points_dec_lineEdit.text()

        color_list = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

        for i in range(len(cap_in)):

            results = dip_se_op(netlist, VDD_in, VINCM_in, VIND_in, cap_in[i], start_freq_in, stop_freq_in, no_points_in)
            plt.plot(results[6], results[7], color_list[i], label=f'C = {cap_in[i]} F')


        self.Gain_Result_label.setText(str(results[0])+str(results[1]))
        self.Bandwidth_result_label.setText(str(results[2])+str(results[3]))
        self.UGF_result_label.setText(str(results[4])+str(results[5]))

        plt.legend()
        plt.grid()
        plt.xscale('log')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain (dB)')
        plt.title('5T-OTA AC Analysis Using NG-Spice')
        plt.show()

class generateChartThread (threading.Thread):
   def __init__(self, w):
      threading.Thread.__init__(self)
      self.w = w

   def run(self):
      print ("Starting " + self.name+"\n")
      techsweep_run.generateCharts(self.w.logGenerateChartslabel, self.w.modelPath, self.w.ngSpiceCommandLineEdit.text(),
                                   self.w.getSweepParameterArguments(self.w.generateVGSLineEdit.text()),
                                   self.w.getSweepParameterArguments(self.w.generateVDSlineEdit.text()),
                                   self.w.getSweepParameterArguments(self.w.generateVBSlineEdit.text()),
                                   self.w.getL(self.w.generateLlineEdit.text()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = main_window()
    form.show()
    app.exec_()
