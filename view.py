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

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QMessageBox, QProgressBar, QLabel, QFileDialog
from PyQt5.QtWidgets import QDesktopWidget, QHBoxLayout, QGridLayout, QGroupBox, QLineEdit


class View(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.btnPhotodiodes = []
        self.btnPhotodiodeFilter = []

        for i in range(0, 5):
            self.btnPhotodiodes.append(QPushButton("Photodiode " + str(i+1)))
            self.btnPhotodiodes[i].setEnabled(False)

            self.btnPhotodiodeFilter.append(QPushButton("Filter"))
            self.btnPhotodiodeFilter[i].setEnabled(False)

        self.btnPhotodiodes.append(QPushButton("All Photodiodes"))
        self.btnPhotodiodes[5].setEnabled(False)

        self.btnPhotodiodeFilter.append(QPushButton("Filter All"))
        self.btnPhotodiodeFilter[5].setEnabled(False)

        self.btnLoadFile = QPushButton('Load File')
        self.btnSaveFile = QPushButton('Save Data')
        self.btnExit = QPushButton('Exit')

        self.btnSaveFile.setEnabled(False)

        self.labelPathFile = QLabel("Path File:")
        self.editPathFile = QLineEdit()

        self.layoutGrid = QGridLayout(self)

        self.loadFileBoxLayout = QGroupBox("Load File")
        self.buttonsBoxLayout = QGroupBox("Photodiodes")

        self.loadFileLayout = QHBoxLayout(self)
        self.buttonsLayout = QGridLayout(self)

        self.resize(600, 300)
        self.centerWindowOnScreen()
        self.setWindowTitle('PREDICT')

    def centerWindowOnScreen(self):
        windowGeometry = self.frameGeometry()
        desktopWidget = QDesktopWidget().availableGeometry().center()
        windowGeometry.moveCenter(desktopWidget)
        self.move(windowGeometry.topLeft())

    def mainWindow(self):
        self.layoutGrid.addWidget(self.setLoadFileGroup(), 0, 2, 2, 4)
        self.layoutGrid.addWidget(self.setButtonsGroup(), 0, 0, 1, 2)
        self.layoutGrid.addWidget(self.btnSaveFile, 1, 0)
        self.layoutGrid.addWidget(self.btnExit, 1, 1)

    def setButtonsGroup(self):
        for i in range(0, 6):
            self.buttonsLayout.addWidget(self.btnPhotodiodes[i], i, 0)
            self.buttonsLayout.addWidget(self.btnPhotodiodeFilter[i], i, 1)

        self.buttonsBoxLayout.setStyleSheet("QGroupBox {"
                                            "border: 2px outset #948682;"
                                            "border-radius: 5px;"
                                            "margin-top: 7px;"
                                            "}"
                                            "QGroupBox:title {"
                                            "top: -7 ex;"
                                            "left: 10px;"
                                            "}")
        self.buttonsBoxLayout.setLayout(self.buttonsLayout)

        return self.buttonsBoxLayout

    def setLoadFileGroup(self):
        self.loadFileLayout.addWidget(self.labelPathFile)
        self.loadFileLayout.addWidget(self.editPathFile)
        self.loadFileLayout.addWidget(self.btnLoadFile)

        """
            Different border style:
                - dotted
                - dashed
                - solid
                - double
                - groove
                - ridge
                - inset
                - outset
                - none
                - hidden
        """

        self.loadFileBoxLayout.setStyleSheet("QGroupBox {"
                                             "border: 2px outset #948682;"
                                             "border-radius: 5px;"
                                             "margin-top: 7px;"
                                             "}"
                                             "QGroupBox:title {"
                                             "top: -7 ex;"
                                             "left: 10px;"
                                             "}")
        self.loadFileBoxLayout.setLayout(self.loadFileLayout)

        return self.loadFileBoxLayout

    def setLoadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "/home/Documents/ ", "*.csv")

        return fileName

    def setSaveFile(self, myNameFile):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "/home/Documents/" + myNameFile, "*.csv")

        return fileName

    def setMessageSaveSuccess(self):
        succesSave = QMessageBox.information(self, "Success", "The data saved successfully.",
                                             QMessageBox.Ok, QMessageBox.Ok)

    def setMessageSave(self):
        saveData = QMessageBox.question(self, "Question", "Do you want to save the data?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if saveData == QMessageBox.Yes:
            return True

        else:
            return False

    def setMessageExit(self):
        exitApp = QMessageBox.question(self, "Question", "Are you sure you want to quit?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if exitApp == QMessageBox.Yes:
            return True

        else:
            return False
