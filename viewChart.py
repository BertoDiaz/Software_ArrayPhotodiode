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


class ViewChart(QDialog):

    def __init__(self, parent):
        super().__init__(parent)

        """Put the dialog window on top and block all windows."""
        self.setWindowModality(Qt.ApplicationModal)

        self.chart = QChart()
        self.chartView = QChartView(self.chart)
        self.axisX = QValueAxis()
        self.axisY = QValueAxis()

        self.layoutGrid = QGridLayout(self)

        self.chartBoxLayout = QGroupBox("Chart")

        self.chartLayout = QGridLayout(self)

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
        self.chartLayout.addWidget(self.chartView, 0, 0)

        self.chartBoxLayout.setStyleSheet("QGroupBox {"
                                          "border: 2px outset #948682;"
                                          "border-radius: 5px;"
                                          "margin-top: 7px;"
                                          "}"
                                          "QGroupBox:title {"
                                          "top: -7 ex;"
                                          "left: 10px;"
                                          "}")

        self.chartBoxLayout.setLayout(self.chartLayout)

        return self.chartBoxLayout

    def setChart(self, n):
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.setTitle("Photodiode " + str(n+1))
        self.chart.setAnimationOptions(QChart.AllAnimations)

        self.chartView.show()

    def setChartFilter(self, n):
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.setTitle("Photodiode " + str(n+1) + " Filtered")
        self.chart.setAnimationOptions(QChart.AllAnimations)

        self.chartView.show()
