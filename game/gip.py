"""
This File Contains the code for the Git Game
Author: James Penales
"""
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QMessageBox



class Ui_StartWindow(object):
    """ This is the Start Window of the Application"""
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(597, 396)
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLbl = QtWidgets.QLabel(self.centralwidget)
        self.titleLbl.setGeometry(QtCore.QRect(190, 70, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(32)
        self.titleLbl.setFont(font)
        self.titleLbl.setObjectName("titleLbl")
        self.playBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow())
        self.playBtn.clicked.connect(StartWindow.close)
        self.playBtn.setGeometry(QtCore.QRect(210, 220, 151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(15, 157, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.playBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.playBtn.setFont(font)
        self.playBtn.setStyleSheet("background: #0F9D58; \n"
        "border: 0px solid black;\n"
        "color:white; \n"
        "border-radius: 10%;")
        self.playBtn.setAutoDefault(False)
        self.playBtn.setObjectName("playBtn")
        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 21))
        self.menubar.setObjectName("menubar")
        StartWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartWindow)
        self.statusbar.setObjectName("statusbar")
        StartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)


    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "MainWindow"))
        self.titleLbl.setText(_translate("StartWindow", "GipGame"))
        self.playBtn.setText(_translate("StartWindow", "Play"))

    def openWindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PlayerEntryWindow()
        self.ui.setupUi(self.window)
        self.window.show()


class Ui_PlayerEntryWindow(object):
    """ This Window is a form that gets the player's Name"""
    def setupUi(self, PlayerEntryWindow):
        PlayerEntryWindow.setObjectName("PlayerEntryWindow")
        PlayerEntryWindow.resize(245, 280)
        PlayerEntryWindow.setWindowTitle("GipGame")
        self.centralwidget = QtWidgets.QWidget(PlayerEntryWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.titleLbl = QtWidgets.QLabel(self.centralwidget)
        self.titleLbl.setGeometry(QtCore.QRect(60, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(18)
        self.titleLbl.setFont(font)
        self.titleLbl.setObjectName("titleLbl")
        self.p1EntryLbl = QtWidgets.QLabel(self.centralwidget)
        self.p1EntryLbl.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.p1EntryLbl.setObjectName("p1EntryLbl")
        self.p2EntryLbl = QtWidgets.QLabel(self.centralwidget)
        self.p2EntryLbl.setGeometry(QtCore.QRect(30, 140, 47, 13))
        self.p2EntryLbl.setObjectName("label_2")
        self.p1Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.p1Entry.setGeometry(QtCore.QRect(80, 110, 113, 20))
        self.p1Entry.setObjectName("p1Entry")
        self.p2Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.p2Entry.setGeometry(QtCore.QRect(80, 140, 113, 20))
        self.p2Entry.setObjectName("p2Entry")
        self.submitPlayerbtn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.submit())
        self.submitPlayerbtn.setGeometry(QtCore.QRect(120, 180, 75, 23))
        self.submitPlayerbtn.setObjectName("submitPlayerbtn")

        self.introLbl = QtWidgets.QLabel(self.centralwidget)
        self.introLbl.setGeometry(QtCore.QRect(70, 70, 91, 16))
        self.introLbl.setObjectName("introLbl")
        PlayerEntryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PlayerEntryWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 245, 21))
        self.menubar.setObjectName("menubar")
        PlayerEntryWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PlayerEntryWindow)
        self.statusbar.setObjectName("statusbar")
        PlayerEntryWindow.setStatusBar(self.statusbar)

        self.introLbl.setText("Hello and Welcome to Gip Game.")
        self.introLbl.adjustSize()
        self.retranslateUi(PlayerEntryWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayerEntryWindow)


    def retranslateUi(self, PlayerEntryWindow):
        _translate = QtCore.QCoreApplication.translate
        PlayerEntryWindow.setWindowTitle(_translate("PlayerEntryWindow", "MainWindow"))
        self.titleLbl.setText(_translate("PlayerEntryWindow", "GipGame"))
        self.p1EntryLbl.setText(_translate("PlayerEntryWindow", "Player 1"))
        self.p2EntryLbl.setText(_translate("PlayerEntryWindow", "Player 2"))
        self.submitPlayerbtn.setText(_translate("PlayerEntryWindow", "Submit"))

    def submit(self):
        if self.p1Entry.text() and self.p2Entry.text() != None:

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_GameWindow()
            self.ui.setupUi(self.window)
            self.setGameWindowText()
            self.p1Entry.clear()
            self.p2Entry.clear()
            self.window.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("GipGame")
            msg.setText("Error: Input is missing from one or both the entries")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()

    def setGameWindowText(self):
        p1 = self.p1Entry.text()
        p2 = self.p2Entry.text()
        self.ui.gameDialogLbl.setText(f"Hello {p1} and {p2}. Welcome to Gip Game. Press space,"
                                      f" or click continue to start playing")
        self.ui.gameDialogLbl.adjustSize()
        self.ui.p1namelbl.setText(f"{p1}'s Score:")
        self.ui.p2namelbl.setText(f":{p2}'s Score")


class Ui_GameWindow(object):
    """ This is the official Game Window"""
    def __init__(self):
        super().__init__()
        self.currentlyPlaying = False
        self.turnScore = 0

        self.introCount = 0 # I know this is a bad way to do it but i dont want to learn PyQT Threading sorry

    def setupUi(self, GameWindow):
        GameWindow.setObjectName("GameWindow")
        GameWindow.resize(697, 526)
        GameWindow.setWindowTitle("GipGame")
        self.centralwidget = QtWidgets.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLbl = QtWidgets.QLabel(self.centralwidget)
        self.titleLbl.setGeometry(QtCore.QRect(280, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(18)
        self.titleLbl.setFont(font)
        self.titleLbl.setObjectName("titleLbl")
        self.diceImg = QtWidgets.QLabel(self.centralwidget)
        self.diceImg.setGeometry(QtCore.QRect(310, 150, 71, 71))
        self.diceImg.setText("")
        self.diceImg.setPixmap(QtGui.QPixmap("../resources/img/d6.png"))
        self.diceImg.setScaledContents(True)
        self.diceImg.setObjectName("diceImg")
        self.gameDialogLbl = QtWidgets.QLabel(self.centralwidget)
        self.gameDialogLbl.setGeometry(QtCore.QRect(150, 400, 237, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gameDialogLbl.sizePolicy().hasHeightForWidth())
        self.gameDialogLbl.setSizePolicy(sizePolicy)
        self.gameDialogLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gameDialogLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.gameDialogLbl.setObjectName("gameDialogLbl")
        self.continueDialogBtn = QtWidgets.QPushButton(self.centralwidget)
        self.continueDialogBtn.setGeometry(QtCore.QRect(610, 450, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.continueDialogBtn.sizePolicy().hasHeightForWidth())
        self.continueDialogBtn.setSizePolicy(sizePolicy)
        self.continueDialogBtn.setFlat(True)
        self.continueDialogBtn.setObjectName("continueDialogBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 330, 591, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(163, 70, 20, 261))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(50, 60, 591, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(500, 70, 20, 261))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.p1Avatar = QtWidgets.QLabel(self.centralwidget)
        self.p1Avatar.setGeometry(QtCore.QRect(50, 80, 111, 111))
        self.p1Avatar.setText("")
        self.p1Avatar.setPixmap(QtGui.QPixmap("../resources/img/player2.jpg"))
        self.p1Avatar.setScaledContents(True)
        self.p1Avatar.setObjectName("p1Avatar")
        self.p2Avatar = QtWidgets.QLabel(self.centralwidget)
        self.p2Avatar.setGeometry(QtCore.QRect(520, 80, 111, 111))
        self.p2Avatar.setText("")
        self.p2Avatar.setPixmap(QtGui.QPixmap("../resources/img/player2.jpg"))
        self.p2Avatar.setScaledContents(True)
        self.p2Avatar.setObjectName("p2Avatar")
        self.rollDiceBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rollDiceBtn.setGeometry(QtCore.QRect(300, 280, 81, 31))
        self.rollDiceBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rollDiceBtn.setStyleSheet("background: #4285F4;\n"
        "color:white;\n"
        "border: 0px;\n"
        "border-radius: 10%;\n"
        "")
        self.rollDiceBtn.setObjectName("rollDiceBtn")
        self.diceLbl = QtWidgets.QLabel(self.centralwidget)
        self.diceLbl.setGeometry(QtCore.QRect(290, 240, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.diceLbl.setFont(font)
        self.diceLbl.setObjectName("diceLbl")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 210, 111, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.p1namelbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1namelbl.sizePolicy().hasHeightForWidth())
        self.p1namelbl.setSizePolicy(sizePolicy)
        self.p1namelbl.setObjectName("p1namelbl")
        self.horizontalLayout.addWidget(self.p1namelbl)
        self.p1scorelbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.p1scorelbl.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1scorelbl.sizePolicy().hasHeightForWidth())
        self.p1scorelbl.setSizePolicy(sizePolicy)
        self.p1scorelbl.setObjectName("p1scorelbl")
        self.horizontalLayout.addWidget(self.p1scorelbl)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(520, 200, 111, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.p2scorelbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2scorelbl.sizePolicy().hasHeightForWidth())
        self.p2scorelbl.setSizePolicy(sizePolicy)
        self.p2scorelbl.setObjectName("p2scorelbl")
        self.horizontalLayout_2.addWidget(self.p2scorelbl)
        self.p2namelbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.p2namelbl.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2namelbl.sizePolicy().hasHeightForWidth())
        self.p2namelbl.setSizePolicy(sizePolicy)
        self.p2namelbl.setObjectName("p2namelbl")
        self.horizontalLayout_2.addWidget(self.p2namelbl)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(290, 80, 101, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.turnscorelbl = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turnscorelbl.sizePolicy().hasHeightForWidth())
        self.turnscorelbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.turnscorelbl.setFont(font)
        self.turnscorelbl.setObjectName("turnscorelbl")
        self.horizontalLayout_3.addWidget(self.turnscorelbl)
        self.turnscorevalLbl = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turnscorevalLbl.sizePolicy().hasHeightForWidth())
        self.turnscorevalLbl.setSizePolicy(sizePolicy)
        self.turnscorevalLbl.setObjectName("turnscorevalLbl")
        self.horizontalLayout_3.addWidget(self.turnscorevalLbl)
        GameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        GameWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GameWindow)
        self.statusbar.setObjectName("statusbar")
        GameWindow.setStatusBar(self.statusbar)

        self.rollDiceBtn.setEnabled(False)

        self.retranslateUi(GameWindow)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)
        self.start()



    def retranslateUi(self, GameWindow):
        _translate = QtCore.QCoreApplication.translate
        GameWindow.setWindowTitle(_translate("GameWindow", "MainWindow"))
        self.titleLbl.setText(_translate("GameWindow", "GipGame"))
        self.gameDialogLbl.setText(_translate("GameWindow", "Hello Player 1 and Player 2, Welcome to Git Game"))
        self.continueDialogBtn.setText(_translate("GameWindow", "Continue >>"))
        self.continueDialogBtn.setShortcut(_translate("GameWindow", "Space"))
        self.rollDiceBtn.setText(_translate("GameWindow", "Roll Dice"))
        self.diceLbl.setText(_translate("GameWindow", ""))
        self.p1namelbl.setText(_translate("GameWindow", "Player1 Score:"))
        self.p1scorelbl.setText(_translate("GameWindow", "0"))
        self.p2scorelbl.setText(_translate("GameWindow", "0"))
        self.p2namelbl.setText(_translate("GameWindow", ": Player 2 Score"))
        self.turnscorelbl.setText(_translate("GameWindow", "Turn Score:"))
        self.turnscorevalLbl.setText(_translate("GameWindow", "0"))
        if self.rollDiceBtn.isEnabled() == False:
            self.rollDiceBtn.setStyleSheet("background: #d2d2d2;\n"
                                           "color:#f1f1f1;\n"
                                           "border: 0px;\n"
                                           "border-radius: 10%;\n")

    def start(self):


        self.continueDialogBtn.clicked.connect(self.playgameDialog)



    def playgameDialog(self):
        mbox = QMessageBox()
        mbox.setWindowTitle("GipGame")
        mbox.setIcon(QMessageBox.Question)
        mbox.setText("Before we start.")
        mbox.setInformativeText(" Would you like to know how to play gip game?")
        yesButton = mbox.addButton("Yes",QMessageBox.YesRole)
        noBtn = mbox.addButton("No", QMessageBox.NoRole)

        mbox.exec()

        if mbox.clickedButton() == yesButton:
            self.introMessage()
        elif mbox.clickedButton() == noBtn:
            self.play()
            self.continueDialogBtn.clicked.disconnect(self.playgameDialog)


    def introMessage(self):
        """ This method is in charge of the introduction to the game"""
        messages = [
        "Each player gets a turn to roll a die, if the player rolls a number between 2 and 6.",
        "That number is added to the overall score for that turn.",
        "The player will have the option to keep re-rolling.",
        "But if they roll a 1, the amount of points built up in that turn is lost.",
        "And the other player gets a turn",
        "First Person to 100 wins.",
        "Good Luck."]

        self.gameDialogLbl.setText("The Rules of the game are simple")
        self.continueDialogBtn.clicked.disconnect(self.playgameDialog)
        self.continueDialogBtn.clicked.connect(lambda: self.updateIntro(messages))



    def updateIntro(self,messages):
        """ Updates dialog label"""
        if self.introCount == 0:
            self.gameDialogLbl.setText(messages[0])
            self.introCount += 1
        elif self.introCount == 1:
            self.gameDialogLbl.setText(messages[1])
            self.introCount += 1
        elif self.introCount == 2:
            self.gameDialogLbl.setText(messages[2])
            self.introCount += 1
        elif self.introCount == 3:
            self.gameDialogLbl.setText(messages[3])
            self.introCount += 1
        elif self.introCount == 4:
            self.gameDialogLbl.setText(messages[4])
            self.introCount += 1
        elif self.introCount == 5:
            self.gameDialogLbl.setText(messages[5])
            self.introCount += 1
        elif self.introCount == 6:
            self.gameDialogLbl.setText(messages[6])
            self.introCount += 1
        else:
            self.play()

    def play(self):
        self.currentlyPlaying = True

        self.p1 = Player(self.p1namelbl.text()[0:5], True)
        self.p2 = Player(self.p2namelbl.text()[1:5], False)

        self.gameDialogLbl.setText(f"{self.p1.name}, Please roll.")
        self.rollDiceBtn.setEnabled(True)
        self.rollDiceBtn.setStyleSheet(
        "background: #0F9D58; \n"
        "border: 0px solid black;\n"
        "color:white; \n"
        "border-radius: 10%;"
        )

        self.rollDiceBtn.clicked.connect(lambda: self.rollDice(self.p1,self.p2))




    def rollDice(self,p1,p2):

        self.dice = Dice()
        roll = self.dice.roll()

        if self.rollDiceBtn.isEnabled():
            if roll == 1:
                self.diceImg.setPixmap(QtGui.QPixmap("../resources/img/d1.png"))
                self.diceLbl.setText("Sorry, You Rolled a 1 :(")
                self.diceLbl.adjustSize()
                self.turnScore = 0
                self.turnscorevalLbl.setText(str(self.turnScore))

                if p1.turn:
                    p1.turn = False
                    p2.turn = True
                    self.gameDialogLbl.setText(f"Sorry {p1.name}, You rolled a 1, It's {p2.name}'s Turn")
                elif p2.turn:
                    p2.turn = False
                    p1.turn = True
                    self.gameDialogLbl.setText(f"Sorry {p2.name}, You rolled a 1, It's {p1.name}'s Turn")

            elif roll == 2:
                self.diceImg.setPixmap(QtGui.QPixmap("../resources/img/d2.png"))
                self.diceLbl.setText("You Rolled a 2")
                self.turnScore += 2
                self.turnscorevalLbl.setText(str(self.turnScore))
                rollAgain = self.rollQuestion(p1,p2)
                if rollAgain:
                    self.rollDice(p1,p2)

                elif not rollAgain and p1.turn:
                    p1.score += self.turnScore
                    self.p1scorelbl.setText(f"{p1.score}")
                    p1.turn = False
                    p2.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p1.name}, you earned {self.turnScore}pts. {p2.name}, Please Roll.")
                    self.turnScore = 0
                elif not rollAgain and p2.turn:
                    p2.score += self.turnScore
                    self.p2scorelbl.setText(f"{p2.score}")
                    p2.turn = False
                    p1.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p2.name}, you earned {self.turnScore}pts. {p1.name}, Please Roll.")
                    self.turnScore = 0
            elif roll == 3:
                self.diceImg.setPixmap(QtGui.QPixmap("../resources/img/d3.png"))
                self.diceLbl.setText("You Rolled a 3")
                self.turnScore += 3
                self.turnscorevalLbl.setText(str(self.turnScore))
                rollAgain = self.rollQuestion(p1,p2)

                if rollAgain:
                    self.rollDice(p1,p2)
                elif not rollAgain and p1.turn:
                    p1.score += self.turnScore
                    self.p1scorelbl.setText(f"{p1.score}")
                    p1.turn = False
                    p2.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p1.name}, you earned {self.turnScore}pts. {p2.name}, Please Roll.")
                elif not rollAgain  and p2.turn:
                    p2.score += self.turnScore
                    self.p2scorelbl.setText(f"{p2.score}")
                    p2.turn = False
                    p1.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p2.name}, you earned {self.turnScore}pts. {p1.name}, Please Roll.")
                    self.turnScore = 0

            elif roll == 4:
                self.diceImg.setPixmap(QtGui.QPixmap("../resources/img/d4.png"))
                self.diceLbl.setText("You Rolled a 4")
                self.turnScore += 4
                self.turnscorevalLbl.setText(str(self.turnScore))
                rollAgain = self.rollQuestion(p1,p2)
                if rollAgain:
                    self.rollDice(p1, p2)
                elif not rollAgain and p1.turn:
                    p1.score += self.turnScore
                    self.p1scorelbl.setText(f"{p1.score}")
                    p1.turn = False
                    p2.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p1.name}, you earned {self.turnScore}pts. {p2.name}, Please Roll.")
                    self.turnScore = 0
                elif not rollAgain and p2.turn:
                    p2.score += self.turnScore
                    self.p2scorelbl.setText(f"{p2.score}")
                    p2.turn = False
                    p1.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p2.name}, you earned {self.turnScore}pts. {p1.name}, Please Roll.")
                    self.turnScore = 0

        elif roll == 5:
                self.diceImg.setPixmap(QtGui.QPixmap("../resources/img/d5.png"))
                self.diceLbl.setText("You Rolled a 5")
                self.turnScore += 5
                self.turnscorevalLbl.setText(str(self.turnScore))
                rollAgain = self.rollQuestion(p1,p2)
                if rollAgain:
                    self.rollDice(p1,p2)
                elif not rollAgain and p1.turn:
                    p1.score += self.turnScore
                    p1.turn = False
                    p2.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p1.name}, you earned {self.turnScore}pts. {p2.name}, Please Roll.")
                    self.turnScore = 0
                elif not rollAgain and p2.turn:
                    p2.score += self.turnScore
                    self.p2scorelbl.setText(f"{p2.score}")
                    p2.turn = False
                    p1.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p2.name}, you earned {self.turnScore}pts. {p1.name}, Please Roll.")
                    self.turnScore = 0
        elif roll == 6:
                self.diceImg.setPixmap(QtGui.QPixmap("../resources/img/d6.png"))
                self.diceLbl.setText("You Rolled a 6!!")
                self.turnScore += 6
                self.turnscorevalLbl.setText(str(self.turnScore))
                rollAgain = self.rollQuestion(p1,p2)
                if rollAgain:
                    self.rollDice(p1,p2)
                elif not self.rollQuestion(p1,p2) and p1.turn:
                    p1.scrollAgainp1scorelbl.setText(f"{p1.score}")
                    p1.turn = False
                    p2.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p1.name}, you earned {self.turnScore}pts. {p2.name}, Please Roll.")
                    self.turnScore = 0
                elif not self.rollQuestion(p1,p2) and p2.turn:
                    p2.score += self.turnScore
                    self.p2scorelbl.setText(f"{p2.score}")
                    p2.turn = False
                    p1.turn = True
                    self.turnscorevalLbl.setText(f"{self.turnScore}")
                    self.gameDialogLbl.setText(f"Congrats {p2.name}, you earned {self.turnScore}pts. {p1.name}, Please Roll.")
                    self.turnScore = 0



    def rollQuestion(self,p1,p2):

        game = GipGame()
        if not GipGame.isWinner(game, p1) and not GipGame.isWinner(game, p2):
            mbox = QMessageBox()
            mbox.setWindowTitle("GipGame")
            mbox.setIcon(QMessageBox.Question)
            mbox.setText(f"Current Turn score: {self.turnScore}.")
            mbox.setInformativeText(" Would you like to roll again??")
            yesButton = mbox.addButton("Yes", QMessageBox.YesRole)
            noBtn = mbox.addButton("No", QMessageBox.NoRole)
            mbox.exec_()

            if mbox.clickedButton() == yesButton and p1.turn:
                p1.turn = True
                p2.turn = False
                return True
            elif mbox.clickedButton() == noBtn and p1.turn:
                return False
            elif mbox.clickedButton() == yesButton and p2.turn:
                p2.turn = True
                p1.turn = False
                return True
            elif mbox.clickedButton() == noBtn and p2.turn:

                return False
        elif GipGame.isWinner(game, p1):
            mbox = QMessageBox()
            mbox.setWindowTitle("GipGame")
            mbox.setIcon(QMessageBox.Question)
            mbox.setText(f"{p1.name} wins! with {p1.score}pts.")
            mbox.setStandardButtons(QMessageBox.Ok)
            mbox.exec_()
            self.centralwidget.close()


        elif GipGame.isWinner(game, p2):
            mbox = QMessageBox()
            mbox.setWindowTitle("GipGame")
            mbox.setIcon(QMessageBox.Question)
            mbox.setText(f"{p2.name} wins! with {p2.score}pts.")
            mbox.setStandardButtons(QMessageBox.Ok)

            mbox.exec_()

            self.centralwidget.close()












class Player:
    """ This class is to represent a real world player"""
    def __init__(self, name, turn):
        self.name = name  # Represents Player Name
        self.turn = turn  # Represents whether or not it is a player's turn
        self.score = 0  # Represents a player's overall score

    def updateScore(self, score):
        """ This method updates a player's score"""
        self.score += score



class GipGame:
    """ This Class is in charge of the logic of the GitGame"""
    def __init__(self):
        self.currentlyPlaying = False
        self.turnScore = 0


    def isWinner(self, player):
        """ This Method returns a boolean value based on whether or not a player has reached 100 points"""
        if player.score >= 100:
            return True
        else:
            return False


class Dice:
    """ This class is to represent a real world dice """
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]

    def roll(self):
        """ Rolls a number from the sides of the die"""
        from random import choice as roll
        return roll(self.sides)



def main():
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
