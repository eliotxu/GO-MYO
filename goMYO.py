# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goMYO.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_goMYO(object):
    def setupUi(self, goMYO):
        goMYO.setObjectName("goMYO")
        goMYO.resize(1472, 992)
        self.funcArea = QtWidgets.QGroupBox(goMYO)
        self.funcArea.setGeometry(QtCore.QRect(1180, 0, 281, 101))
        self.funcArea.setObjectName("funcArea")
        self.gridLayoutWidget = QtWidgets.QWidget(self.funcArea)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.rssi_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.rssi_2.setFont(font)
        self.rssi_2.setObjectName("rssi_2")
        self.gridLayout.addWidget(self.rssi_2, 3, 0, 1, 1)
        self.betteryBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.betteryBar.setProperty("value", 25)
        self.betteryBar.setObjectName("betteryBar")
        self.gridLayout.addWidget(self.betteryBar, 3, 1, 1, 1)
        self.rssiBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.rssiBar.setProperty("value", 25)
        self.rssiBar.setObjectName("rssiBar")
        self.gridLayout.addWidget(self.rssiBar, 2, 1, 1, 1)
        self.rssi = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.rssi.setFont(font)
        self.rssi.setObjectName("rssi")
        self.gridLayout.addWidget(self.rssi, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(goMYO)
        self.groupBox.setGeometry(QtCore.QRect(10, 670, 1451, 311))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1431, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setObjectName("graph_layout")
        self.msgGroup = QtWidgets.QGroupBox(goMYO)
        self.msgGroup.setGeometry(QtCore.QRect(1180, 110, 281, 561))
        self.msgGroup.setObjectName("msgGroup")
        self.msgBrowser = QtWidgets.QTextBrowser(self.msgGroup)
        self.msgBrowser.setGeometry(QtCore.QRect(10, 20, 261, 531))
        self.msgBrowser.setObjectName("msgBrowser")
        self.TestGroup = QtWidgets.QGroupBox(goMYO)
        self.TestGroup.setEnabled(True)
        self.TestGroup.setGeometry(QtCore.QRect(10, 10, 1161, 671))
        self.TestGroup.setObjectName("TestGroup")
        self.LoadGroup = QtWidgets.QGroupBox(self.TestGroup)
        self.LoadGroup.setGeometry(QtCore.QRect(10, 20, 201, 111))
        self.LoadGroup.setObjectName("LoadGroup")
        self.connectBtn = QtWidgets.QPushButton(self.LoadGroup)
        self.connectBtn.setGeometry(QtCore.QRect(10, 70, 71, 31))
        self.connectBtn.setObjectName("connectBtn")
        self.disconnectBtn = QtWidgets.QPushButton(self.LoadGroup)
        self.disconnectBtn.setGeometry(QtCore.QRect(90, 70, 101, 31))
        self.disconnectBtn.setObjectName("disconnectBtn")
        self.init_Btn = QtWidgets.QPushButton(self.LoadGroup)
        self.init_Btn.setGeometry(QtCore.QRect(10, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.init_Btn.setFont(font)
        self.init_Btn.setObjectName("init_Btn")
        self.showGroup = QtWidgets.QGroupBox(self.TestGroup)
        self.showGroup.setGeometry(QtCore.QRect(490, 30, 231, 281))
        self.showGroup.setObjectName("showGroup")
        self.ok_Label = QtWidgets.QLabel(self.showGroup)
        self.ok_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.ok_Label.setText("")
        self.ok_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ok_Label.setObjectName("ok_Label")
        self.waveIn_Label = QtWidgets.QLabel(self.showGroup)
        self.waveIn_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.waveIn_Label.setText("")
        self.waveIn_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.waveIn_Label.setObjectName("waveIn_Label")
        self.waveOut_Label = QtWidgets.QLabel(self.showGroup)
        self.waveOut_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.waveOut_Label.setText("")
        self.waveOut_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.waveOut_Label.setObjectName("waveOut_Label")
        self.relax_Label = QtWidgets.QLabel(self.showGroup)
        self.relax_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.relax_Label.setText("")
        self.relax_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.relax_Label.setObjectName("relax_Label")
        self.six_Label = QtWidgets.QLabel(self.showGroup)
        self.six_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.six_Label.setText("")
        self.six_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.six_Label.setObjectName("six_Label")
        self.seven_Label = QtWidgets.QLabel(self.showGroup)
        self.seven_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.seven_Label.setText("")
        self.seven_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.seven_Label.setObjectName("seven_Label")
        self.abduct_Label = QtWidgets.QLabel(self.showGroup)
        self.abduct_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.abduct_Label.setText("")
        self.abduct_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.abduct_Label.setObjectName("abduct_Label")
        self.peace_Label = QtWidgets.QLabel(self.showGroup)
        self.peace_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.peace_Label.setText("")
        self.peace_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.peace_Label.setObjectName("peace_Label")
        self.white_Label = QtWidgets.QLabel(self.showGroup)
        self.white_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.white_Label.setText("")
        self.white_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.white_Label.setObjectName("white_Label")
        self.fist_Label = QtWidgets.QLabel(self.showGroup)
        self.fist_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.fist_Label.setText("")
        self.fist_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.fist_Label.setObjectName("fist_Label")
        self.adduct_Label = QtWidgets.QLabel(self.showGroup)
        self.adduct_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.adduct_Label.setText("")
        self.adduct_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.adduct_Label.setObjectName("adduct_Label")
        self.ring_Label = QtWidgets.QLabel(self.showGroup)
        self.ring_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.ring_Label.setText("")
        self.ring_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ring_Label.setObjectName("ring_Label")
        self.thumb_Label = QtWidgets.QLabel(self.showGroup)
        self.thumb_Label.setGeometry(QtCore.QRect(10, 20, 211, 251))
        self.thumb_Label.setText("")
        self.thumb_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.thumb_Label.setObjectName("thumb_Label")
        self.lcdTime = QtWidgets.QLCDNumber(self.TestGroup)
        self.lcdTime.setEnabled(True)
        self.lcdTime.setGeometry(QtCore.QRect(740, 260, 131, 51))
        self.lcdTime.setSmallDecimalPoint(True)
        self.lcdTime.setObjectName("lcdTime")
        self.timeUnit = QtWidgets.QLabel(self.TestGroup)
        self.timeUnit.setGeometry(QtCore.QRect(880, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timeUnit.setFont(font)
        self.timeUnit.setObjectName("timeUnit")
        self.gesturesGroup = QtWidgets.QGroupBox(self.TestGroup)
        self.gesturesGroup.setGeometry(QtCore.QRect(10, 320, 1141, 341))
        self.gesturesGroup.setObjectName("gesturesGroup")
        self.allPics_Label = QtWidgets.QLabel(self.gesturesGroup)
        self.allPics_Label.setGeometry(QtCore.QRect(10, 20, 1121, 311))
        self.allPics_Label.setText("")
        self.allPics_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.allPics_Label.setObjectName("allPics_Label")

        self.retranslateUi(goMYO)
        QtCore.QMetaObject.connectSlotsByName(goMYO)

    def retranslateUi(self, goMYO):
        _translate = QtCore.QCoreApplication.translate
        goMYO.setWindowTitle(_translate("goMYO", "Form"))
        self.funcArea.setTitle(_translate("goMYO", "Bar"))
        self.rssi_2.setText(_translate("goMYO", "BETTERY:"))
        self.rssi.setText(_translate("goMYO", "RSSI:"))
        self.groupBox.setTitle(_translate("goMYO", "sEMG"))
        self.msgGroup.setTitle(_translate("goMYO", "Info"))
        self.TestGroup.setTitle(_translate("goMYO", "Test"))
        self.LoadGroup.setTitle(_translate("goMYO", "Load Classifier"))
        self.connectBtn.setText(_translate("goMYO", "Connect"))
        self.disconnectBtn.setText(_translate("goMYO", "Disconnect"))
        self.init_Btn.setText(_translate("goMYO", "Init Classifier"))
        self.showGroup.setTitle(_translate("goMYO", "Predicted Gesture"))
        self.timeUnit.setText(_translate("goMYO", "Milli Second"))
        self.gesturesGroup.setTitle(_translate("goMYO", "Gesture Class"))
