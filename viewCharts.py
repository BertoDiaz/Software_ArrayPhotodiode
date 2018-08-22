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

from PyQt5.QtWidgets import QDesktopWidget, QGridLayout, QGroupBox, QDialog
from PyQt5.QtChart import QChartView, QChart, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class ViewCharts(QDialog):

    def __init__(self, parent):
        super().__init__(parent)

        """Put the dialog window on top and block all windows."""
        self.setWindowModality(Qt.ApplicationModal)

        self.charts = []
        self.chartsView = []
        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        for i in range(0, 16):
            self.charts.append(QChart())
            self.chartsView.append(QChartView(self.charts[i]))

        self.layoutGrid = QGridLayout(self)

        self.chartsBoxLayout = QGroupBox("Charts")

        self.chartsLayout = QGridLayout(self)

        self.resize(1200, 800)
        self.centerWindowOnScreen()
        self.setWindowTitle('Graphs')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self):
        self.layoutGrid.addWidget(self.setChartGroup(), 0, 0)

    def setChartGroup(self):
        i = 0
        r = 0
        # for i in range(0, 16):
        while i < 16:

            for k in range(0, 3):
                if (i+k) < 16:
                    self.chartsLayout.addWidget(self.chartsView[i+k], r, k)

            i += 3
            r += 1

        self.resize(1500, 875)
        self.centerWindowOnScreen()

        self.chartsBoxLayout.setStyleSheet("QGroupBox {"
                                           "border: 2px outset #948682;"
                                           "border-radius: 5px;"
                                           "margin-top: 7px;"
                                           "}"
                                           "QGroupBox:title {"
                                           "top: -7 ex;"
                                           "left: 10px;"
                                           "}")

        self.chartsBoxLayout.setLayout(self.chartsLayout)

        return self.chartsBoxLayout

    def setCharts(self):
        m = 1

        for i in range(0, 16):
            self.chartsView[i].setRenderHint(QPainter.Antialiasing)
            self.charts[i].legend().setVisible(False)
            self.charts[i].legend().setAlignment(Qt.AlignBottom)
            self.charts[i].setTitle("Photodiode " + str(m))
            self.charts[i].setAnimationOptions(QChart.AllAnimations)

            self.chartsView[i].show()

            m += 1

    def setChartsFilter(self):
        m = 1

        for i in range(0, 16):
            self.chartsView[i].setRenderHint(QPainter.Antialiasing)
            self.charts[i].legend().setVisible(False)
            self.charts[i].legend().setAlignment(Qt.AlignBottom)
            self.charts[i].setTitle("Photodiode " + str(m))
            self.charts[i].setAnimationOptions(QChart.AllAnimations)

            self.chartsView[i].show()

            m += 1
