"""
Copyright (C) 2018  Heriberto J. Díaz Luis-Ravelo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from view import View
from viewChart import ViewChart
from viewCharts import ViewCharts
from PyQt5.QtWidgets import QApplication
from PyQt5.QtChart import QLineSeries
from PyQt5.QtCore import Qt
from functools import partial
from scipy import signal
import sys
import csv
import datetime


class Controller:
    def __init__(self):

        self.timeStart = []
        self.valueStart = []
        self.timeTrigger = []
        self.valueTrigger = []
        self.timeSensor = []
        self.valueSensor = []
        self.changesStart = []
        self.changesTrigger = []
        self.dataSensor = []
        self.photodiode_1 = []
        self.photodiode_2 = []
        self.photodiode_3 = []
        self.photodiode_4 = []
        self.photodiode_5 = []
        self.photodiode_6 = []
        self.photodiode_7 = []
        self.photodiode_8 = []
        self.photodiode_9 = []
        self.photodiode_10 = []
        self.photodiode_11 = []
        self.photodiode_12 = []
        self.photodiode_13 = []
        self.photodiode_14 = []
        self.photodiode_15 = []
        self.photodiode_16 = []
        self.photodiodes = []
        # self.photodiodeFiltered = None
        self.lenghtPhotodiode = None
        self.colors = [Qt.blue, Qt.red, Qt.green, Qt.darkMagenta, Qt.darkYellow]
        self.fileLoaded = False

        self.view = View(None)
        self.viewChart = ViewChart(None)
        self.viewCharts = ViewCharts(None)

        self.view.mainWindow()

        self.view.show()

        self.run()

    def run(self):

        self.view.btnExit.clicked.connect(self.exit_App)
        self.view.btnLoadFile.clicked.connect(self.loadFile)

        for i in range(0, 5):
            self.view.btnPhotodiodes[i].clicked.connect(partial(self.btnPhotodiode, n=i))
            self.view.btnPhotodiodeFilter[i].clicked.connect(partial(self.btnPhotodiodeFilter, n=i))

        self.view.btnPhotodiodes[5].clicked.connect(self.btnAllPhotodiodes)
        self.view.btnPhotodiodeFilter[5].clicked.connect(self.btnFilterAll)
        self.view.btnSaveFile.clicked.connect(self.saveDataSensor)

    def loadFile(self):
        loadFile = self.view.setLoadFile()
        iSensor = 0
        iStart = 0
        iTrigger = 0
        i = 0

        if loadFile != "":
            self.view.editPathFile.setText(loadFile)

            fileName = open(loadFile, 'r')

            with fileName:
                reader = csv.reader(fileName, delimiter=',')

                for row in reader:
                    if i == 2:
                        nameColumn = row
                        for l in range(0, len(nameColumn)):
                            if nameColumn[l].find('Sensor') != -1:
                                iSensor = l

                            elif nameColumn[l].find('Start') != -1:
                                iStart = l

                            elif nameColumn[l].find('Trigger') != -1:
                                iTrigger = l

                    elif i > 3:

                        self.timeStart.append(float(row[iStart-1]))
                        self.valueStart.append(float(row[iStart]))
                        self.timeTrigger.append(float(row[iTrigger-1]))
                        self.valueTrigger.append(float(row[iTrigger]))
                        self.timeSensor.append(float(row[iSensor-1]))
                        self.valueSensor.append(float(row[iSensor]))

                    i += 1

                self.getDataSensor()

        else:
            pass

    def btnPhotodiode(self, n):
        self.lenghtPhotodiode = len(self.photodiodes[n])

        x = list(range(len(self.photodiodes[n])))
        self.addDataChart(x, self.photodiodes[n], "Photodiode " + str(n+1), color=Qt.blue)

        self.viewChart.mainWindow()

        self.viewChart.show()

        self.viewChart.setChart(n)

        self.viewChart.exec_()

    def btnAllPhotodiodes(self):
        for i in range(0, 5):
            x = list(range(len(self.photodiodes[i])))
            self.addDataCharts(x, self.photodiodes[i], "Photodiode " + str(i+1), i, color=self.colors[i])

        self.viewCharts.mainWindow()

        self.viewCharts.show()

        self.viewCharts.setCharts()

        self.viewCharts.exec_()

    def addDataCharts(self, xdata, ydata, name_label, m, color=None):
        curve = QLineSeries()
        pen = curve.pen()

        if color is not None:
            pen.setColor(color)

        pen.setWidthF(0.1)
        curve.setPen(pen)
        curve.setUseOpenGL(True)

        for i in range(0, len(xdata)):
            curve.append(xdata[i], ydata[i])

        curve.setName(name_label)

        self.viewCharts.charts[m].removeAllSeries()
        self.viewCharts.charts[m].addSeries(curve)
        self.viewCharts.charts[m].createDefaultAxes()

    def addMultipleDataCharts(self, xdata, ydata):
        for m in range(0, 5):
            curve_1 = QLineSeries()
            curve_2 = QLineSeries()
            pen_1 = curve_1.pen()
            pen_2 = curve_2.pen()

            pen_1.setColor(Qt.darkCyan)
            pen_2.setColor(self.colors[m])

            pen_1.setWidthF(0.1)
            curve_1.setPen(pen_1)
            curve_1.setUseOpenGL(True)
            pen_2.setWidthF(0.1)
            curve_2.setPen(pen_2)
            curve_2.setUseOpenGL(True)

            for i in range(0, len(xdata)):
                curve_1.append(xdata[i], ydata[m][i])
                curve_2.append(xdata[i], self.photodiodes[m][i])

            curve_1.setName("Filtered")
            curve_2.setName("Without Filter")

            self.viewCharts.charts[m].removeAllSeries()
            self.viewCharts.charts[m].addSeries(curve_1)
            self.viewCharts.charts[m].addSeries(curve_2)
            self.viewCharts.charts[m].createDefaultAxes()

    def addDataChart(self, xdata, ydata, name_label, color=None):
        curve = QLineSeries()
        pen = curve.pen()

        if color is not None:
            pen.setColor(color)

        pen.setWidthF(0.1)
        curve.setPen(pen)
        curve.setUseOpenGL(True)

        for i in range(0, len(xdata)):
            curve.append(xdata[i], ydata[i])

        curve.setName(name_label)

        self.viewChart.chart.removeAllSeries()
        self.viewChart.chart.addSeries(curve)

        self.viewChart.axisX.setTitleText("Samples")
        self.viewChart.axisY.setTitleText("Voltage")
        self.viewChart.axisX.setTickCount(1)
        self.viewChart.axisY.setTickCount(1)
        self.viewChart.axisX.setRange(0, self.lenghtPhotodiode)
        self.viewChart.axisY.setRange(-5, 5)

        self.viewChart.chart.addAxis(self.viewChart.axisX, Qt.AlignBottom)
        self.viewChart.chart.addAxis(self.viewChart.axisY, Qt.AlignLeft)
        self.viewChart.chart.setAxisX(self.viewChart.axisX, curve)
        self.viewChart.chart.setAxisY(self.viewChart.axisY, curve)

        curve.attachAxis(self.viewChart.axisX)
        curve.attachAxis(self.viewChart.axisY)

    def addMultipleDataChart(self, xdata, ydata_1, ydata_2, name_label_1, name_label_2, color_1=None, color_2=None):
        curve_1 = QLineSeries()
        curve_2 = QLineSeries()
        pen_1 = curve_1.pen()
        pen_2 = curve_2.pen()

        if color_1 is not None:
            pen_1.setColor(color_1)

        if color_2 is not None:
            pen_2.setColor(color_2)

        pen_1.setWidthF(0.1)
        curve_1.setPen(pen_1)
        curve_1.setUseOpenGL(True)
        pen_2.setWidthF(0.1)
        curve_2.setPen(pen_2)
        curve_2.setUseOpenGL(True)

        for i in range(0, len(xdata)):
            curve_1.append(xdata[i], ydata_1[i])
            curve_2.append(xdata[i], ydata_2[i])

        curve_1.setName(name_label_1)
        curve_2.setName(name_label_2)

        self.viewChart.chart.removeAllSeries()
        self.viewChart.chart.addSeries(curve_1)
        self.viewChart.chart.addSeries(curve_2)

        minValue_1 = min(ydata_1)
        minValue_2 = min(ydata_2)
        minValue = min([minValue_1, minValue_2])
        maxValue_1 = max(ydata_1)
        maxValue_2 = max(ydata_2)
        maxValue = max([maxValue_1, maxValue_2])

        self.viewChart.axisX.setTitleText("Samples")
        self.viewChart.axisY.setTitleText("Voltage")
        self.viewChart.axisX.setTickCount(1)
        self.viewChart.axisY.setTickCount(1)
        self.viewChart.axisX.setRange(0, len(xdata))
        self.viewChart.axisY.setRange(minValue-0.3, maxValue+0.3)

        self.viewChart.chart.addAxis(self.viewChart.axisX, Qt.AlignBottom)
        self.viewChart.chart.addAxis(self.viewChart.axisY, Qt.AlignLeft)
        self.viewChart.chart.setAxisX(self.viewChart.axisX, curve_1)
        self.viewChart.chart.setAxisY(self.viewChart.axisY, curve_1)
        self.viewChart.chart.setAxisX(self.viewChart.axisX, curve_2)
        self.viewChart.chart.setAxisY(self.viewChart.axisY, curve_2)

        curve_1.attachAxis(self.viewChart.axisX)
        curve_1.attachAxis(self.viewChart.axisY)
        curve_2.attachAxis(self.viewChart.axisX)
        curve_2.attachAxis(self.viewChart.axisY)

    def getDataSensor(self):
        iStart = 0
        dataSensorDict = []
        nSensor = 0

        while iStart < len(self.valueStart)-1:
            if self.valueStart[iStart] > 1:
                self.changesStart.append(iStart)

                iTrigger = iStart
                nTrigger = 0

                while nTrigger < 16:
                    if self.valueTrigger[iTrigger] > 1:
                        self.changesTrigger.append(iTrigger)

                        if (iTrigger + 5) < len(self.valueSensor):
                            dataSensorDict.append(self.valueSensor[self.changesTrigger[nSensor] + 5])

                            nSensor += 1

                        else:
                            nTrigger = 50

                        iTrigger += 10
                        nTrigger += 1

                    iTrigger += 1

                if nTrigger < 20:
                    self.dataSensor.append(dataSensorDict)
                    dataSensorDict = []

                iStart += 10

            iStart += 1

        for i in range(0, len(self.dataSensor)):
            self.photodiode_1.append(self.dataSensor[i][15])
            self.photodiode_2.append(self.dataSensor[i][14])
            self.photodiode_3.append(self.dataSensor[i][13])
            self.photodiode_4.append(self.dataSensor[i][12])
            self.photodiode_5.append(self.dataSensor[i][11])
            self.photodiode_6.append(self.dataSensor[i][10])
            self.photodiode_7.append(self.dataSensor[i][9])
            self.photodiode_8.append(self.dataSensor[i][8])
            self.photodiode_9.append(self.dataSensor[i][7])
            self.photodiode_10.append(self.dataSensor[i][6])
            self.photodiode_11.append(self.dataSensor[i][5])
            self.photodiode_12.append(self.dataSensor[i][4])
            self.photodiode_13.append(self.dataSensor[i][3])
            self.photodiode_14.append(self.dataSensor[i][2])
            self.photodiode_15.append(self.dataSensor[i][1])
            self.photodiode_16.append(self.dataSensor[i][0])

        self.photodiodes.append(self.photodiode_1)
        self.photodiodes.append(self.photodiode_2)
        self.photodiodes.append(self.photodiode_3)
        self.photodiodes.append(self.photodiode_4)
        self.photodiodes.append(self.photodiode_5)
        self.photodiodes.append(self.photodiode_6)
        self.photodiodes.append(self.photodiode_7)
        self.photodiodes.append(self.photodiode_8)
        self.photodiodes.append(self.photodiode_9)
        self.photodiodes.append(self.photodiode_10)
        self.photodiodes.append(self.photodiode_11)
        self.photodiodes.append(self.photodiode_12)
        self.photodiodes.append(self.photodiode_13)
        self.photodiodes.append(self.photodiode_14)
        self.photodiodes.append(self.photodiode_15)
        self.photodiodes.append(self.photodiode_16)

        for i in range(0, 6):
            self.view.btnPhotodiodes[i].setEnabled(True)
            self.view.btnPhotodiodeFilter[i].setEnabled(True)

        self.view.btnSaveFile.setEnabled(True)

        self.fileLoaded = True

    def btnPhotodiodeFilter(self, n):
        b, a = signal.butter(1, 0.5)

        photodiodeFiltered = signal.filtfilt(b, a, self.photodiodes[n])

        lenghtPhotodiodeFiltered = len(photodiodeFiltered)

        x = list(range(lenghtPhotodiodeFiltered))
        self.addMultipleDataChart(x, photodiodeFiltered, self.photodiodes[n], "Photodiode " + str(n + 1) + " Filtered",
                                  "Photodiode " + str(n + 1), color_1=Qt.blue, color_2=Qt.red)
        # self.addDataChart(x, self.photodiodes[n], "Photodiode " + str(n + 1), color=Qt.green)

        self.viewChart.mainWindow()

        self.viewChart.show()

        self.viewChart.setChartFilter(n)

        self.viewChart.exec_()

    def btnFilterAll(self):
        photodiodeFiltered = []

        b, a = signal.butter(1, 0.5)

        for i in range(0, 5):
            photodiodeFiltered.append(signal.filtfilt(b, a, self.photodiodes[i]))

        lenghtPhotodiodeFiltered = len(photodiodeFiltered[0])

        x = list(range(lenghtPhotodiodeFiltered))
        self.addMultipleDataCharts(x, photodiodeFiltered)
        # self.addDataChart(x, self.photodiodes[n], "Photodiode " + str(n + 1), color=Qt.green)

        self.viewCharts.mainWindow()

        self.viewCharts.show()

        self.viewCharts.setChartsFilter()

        self.viewCharts.exec_()

    def saveDataSensor(self):
        myFileName = datetime.datetime.now().strftime("%d-%m-%Y") + "_measure.csv"
        fileName = self.view.setSaveFile(myFileName)

        if fileName != '':
            myData = [["Photodiode 1", "Photodiode 2", "Photodiode 3", "Photodiode 4", "Photodiode 5"]]

            for i in range(0, len(self.photodiodes[0])):
                myData.append([self.photodiodes[0][i], self.photodiodes[1][i], self.photodiodes[2][i],
                               self.photodiodes[3][i], self.photodiodes[4][i]])

            myFile = open(fileName, 'w')

            with myFile:
                writer = csv.writer(myFile)
                writer.writerows(myData)

            self.view.setMessageSaveSuccess()
            self.fileLoaded = False

        else:
            pass

    def exit_App(self):
        if self.fileLoaded:
            saveData = self.view.setMessageSave()

            if saveData:
                self.saveDataSensor()
                exitApp = self.view.setMessageExit()
            else:
                exitApp = self.view.setMessageExit()

        else:
            exitApp = self.view.setMessageExit()

        if exitApp:
            QApplication.quit()


if __name__ == '__main__':
    app = QApplication([])

    window = Controller()
    sys.exit(app.exec_())
