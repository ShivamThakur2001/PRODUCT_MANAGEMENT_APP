# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\Internship 2\Product Management Application\Product.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 857)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 80, 1070, 611))
        self.tabWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.BACKGROUND = QtWidgets.QLabel(self.tab)
        self.BACKGROUND.setGeometry(QtCore.QRect(0, 0, 1065, 581))
        self.BACKGROUND.setText("")
        self.BACKGROUND.setPixmap(QtGui.QPixmap("login background.jpg"))
        self.BACKGROUND.setScaledContents(True)
        self.BACKGROUND.setObjectName("BACKGROUND")
        self.LOGIN_BACKGROUND = QtWidgets.QLabel(self.tab)
        self.LOGIN_BACKGROUND.setGeometry(QtCore.QRect(30, 20, 491, 541))
        self.LOGIN_BACKGROUND.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"border-radius:20;")
        self.LOGIN_BACKGROUND.setText("")
        self.LOGIN_BACKGROUND.setScaledContents(True)
        self.LOGIN_BACKGROUND.setObjectName("LOGIN_BACKGROUND")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(540, 20, 491, 541))
        self.label_4.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"border-radius:20;")
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 351, 61))
        self.label_2.setStyleSheet("color: rgb(251, 234, 235);\n"
"background-color: rgb(47, 60, 126);\n"
"text-decoration: underline;\n"
"font: 20pt \"Palatino Linotype\";\n"
"border: NONE;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 221, 41))
        self.label_3.setStyleSheet("color: rgb(251, 234, 235);\n"
"background-color: rgb(47, 60, 126);\n"
"border: NONE;\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(100, 310, 221, 41))
        self.label_5.setStyleSheet("color: rgb(251, 234, 235);\n"
"background-color: rgb(47, 60, 126);\n"
"border: NONE;\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.label_5.setObjectName("label_5")
        self.LOGIN = QtWidgets.QPushButton(self.tab)
        self.LOGIN.setGeometry(QtCore.QRect(100, 430, 81, 41))
        self.LOGIN.setStyleSheet("color: rgb(251, 234, 235);\n"
"background-color: rgb(47, 60, 126);\n"
"border: NONE;\n"
"font: 75 14pt \"Palatino Linotype\";")
        self.LOGIN.setObjectName("LOGIN")
        self.FORGET_PASSWORD = QtWidgets.QPushButton(self.tab)
        self.FORGET_PASSWORD.setGeometry(QtCore.QRect(90, 490, 251, 41))
        self.FORGET_PASSWORD.setStyleSheet("color: rgb(251, 234, 235);\n"
"background-color: rgb(47, 60, 126);\n"
"border: NONE;\n"
"font: 75 14pt \"Palatino Linotype\";")
        self.FORGET_PASSWORD.setObjectName("FORGET_PASSWORD")
        self.LOGIN_ALERT = QtWidgets.QLabel(self.tab)
        self.LOGIN_ALERT.setGeometry(QtCore.QRect(120, 100, 271, 41))
        self.LOGIN_ALERT.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(47, 60, 126);\n"
"border: NONE;\n"
"font: 75 12pt \"Palatino Linotype\";")
        self.LOGIN_ALERT.setText("")
        self.LOGIN_ALERT.setObjectName("LOGIN_ALERT")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(631, 30, 351, 71))
        self.label_6.setStyleSheet("color: rgb(47, 60, 126);\n"
"background-color: rgb(251, 234, 235);\n"
"text-decoration: underline;\n"
"font: 16pt \"Palatino Linotype\";\n"
"border: NONE;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(560, 170, 91, 41))
        self.label_7.setStyleSheet("color: rgb(47, 60, 126);\n"
"background-color: rgb(251, 234, 235);\n"
"font: 12pt \"Palatino Linotype\";\n"
"border: NONE;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(560, 350, 141, 41))
        self.label_8.setStyleSheet("color: rgb(47, 60, 126);\n"
"background-color: rgb(251, 234, 235);\n"
"font: 12pt \"Palatino Linotype\";\n"
"border: NONE;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(560, 290, 141, 41))
        self.label_9.setStyleSheet("color: rgb(47, 60, 126);\n"
"background-color: rgb(251, 234, 235);\n"
"font: 12pt \"Palatino Linotype\";\n"
"border: NONE;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(560, 230, 91, 41))
        self.label_10.setStyleSheet("color: rgb(47, 60, 126);\n"
"background-color: rgb(251, 234, 235);\n"
"font: 12pt \"Palatino Linotype\";\n"
"border: NONE;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(560, 410, 241, 41))
        self.label_11.setStyleSheet("color: rgb(47, 60, 126);\n"
"background-color: rgb(251, 234, 235);\n"
"font: 12pt \"Palatino Linotype\";\n"
"border: NONE;")
        self.label_11.setObjectName("label_11")
        self.REGISTER_BUTTON = QtWidgets.QPushButton(self.tab)
        self.REGISTER_BUTTON.setGeometry(QtCore.QRect(737, 510, 93, 28))
        self.REGISTER_BUTTON.setStyleSheet("color: rgb(47, 60, 126);\n"
"background-color: rgb(251, 234, 235);\n"
"font: 12pt \"Palatino Linotype\";\n"
"border: NONE;")
        self.REGISTER_BUTTON.setObjectName("REGISTER_BUTTON")
        self.REGISTER_INFO = QtWidgets.QLabel(self.tab)
        self.REGISTER_INFO.setGeometry(QtCore.QRect(645, 90, 281, 41))
        self.REGISTER_INFO.setStyleSheet("color: rgb(255, 0, 0);\n"
"border: NONE;\n"
"background-color: rgb(251, 234, 235);\n"
"font: 75 12pt \"Palatino Linotype\";")
        self.REGISTER_INFO.setText("")
        self.REGISTER_INFO.setObjectName("REGISTER_INFO")
        self.USERNAME = QtWidgets.QLineEdit(self.tab)
        self.USERNAME.setGeometry(QtCore.QRect(100, 230, 221, 41))
        self.USERNAME.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.USERNAME.setStyleSheet("color: rgb(47, 60, 126);\n"
"border: NONE;\n"
"background-color: rgb(251, 234, 235);\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.USERNAME.setText("")
        self.USERNAME.setObjectName("USERNAME")
        self.LOGIN_PASSWORD = QtWidgets.QLineEdit(self.tab)
        self.LOGIN_PASSWORD.setGeometry(QtCore.QRect(100, 360, 221, 41))
        self.LOGIN_PASSWORD.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.LOGIN_PASSWORD.setStyleSheet("color: rgb(47, 60, 126);\n"
"border: NONE;\n"
"background-color: rgb(251, 234, 235);\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.LOGIN_PASSWORD.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.LOGIN_PASSWORD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LOGIN_PASSWORD.setObjectName("LOGIN_PASSWORD")
        self.NAME = QtWidgets.QLineEdit(self.tab)
        self.NAME.setGeometry(QtCore.QRect(800, 170, 221, 41))
        self.NAME.setStyleSheet("color: rgb(251, 234, 235);\n"
"border: NONE;\n"
"background-color: rgb(47, 60, 126);\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.NAME.setObjectName("NAME")
        self.E_MAIL = QtWidgets.QLineEdit(self.tab)
        self.E_MAIL.setGeometry(QtCore.QRect(800, 230, 221, 41))
        self.E_MAIL.setStyleSheet("color: rgb(251, 234, 235);\n"
"border: NONE;\n"
"background-color: rgb(47, 60, 126);\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.E_MAIL.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.E_MAIL.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.E_MAIL.setObjectName("E_MAIL")
        self.MOBILE_NUMBER = QtWidgets.QLineEdit(self.tab)
        self.MOBILE_NUMBER.setGeometry(QtCore.QRect(800, 290, 221, 41))
        self.MOBILE_NUMBER.setStyleSheet("color: rgb(251, 234, 235);\n"
"border: NONE;\n"
"background-color: rgb(47, 60, 126);\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.MOBILE_NUMBER.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.MOBILE_NUMBER.setObjectName("MOBILE_NUMBER")
        self.REGISTER_PASSWORD = QtWidgets.QLineEdit(self.tab)
        self.REGISTER_PASSWORD.setGeometry(QtCore.QRect(800, 350, 221, 41))
        self.REGISTER_PASSWORD.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.REGISTER_PASSWORD.setStyleSheet("color: rgb(251, 234, 235);\n"
"border: NONE;\n"
"background-color: rgb(47, 60, 126);\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.REGISTER_PASSWORD.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.REGISTER_PASSWORD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.REGISTER_PASSWORD.setObjectName("REGISTER_PASSWORD")
        self.CONFIRM_PASSWORD = QtWidgets.QLineEdit(self.tab)
        self.CONFIRM_PASSWORD.setGeometry(QtCore.QRect(800, 410, 221, 41))
        self.CONFIRM_PASSWORD.setStyleSheet("color: rgb(251, 234, 235);\n"
"border: NONE;\n"
"background-color: rgb(47, 60, 126);\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.CONFIRM_PASSWORD.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.CONFIRM_PASSWORD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CONFIRM_PASSWORD.setObjectName("CONFIRM_PASSWORD")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.BACKGROUND_2 = QtWidgets.QLabel(self.tab_2)
        self.BACKGROUND_2.setGeometry(QtCore.QRect(0, 0, 1065, 581))
        self.BACKGROUND_2.setStyleSheet("background-color: rgb(47, 60, 126);")
        self.BACKGROUND_2.setText("")
        self.BACKGROUND_2.setScaledContents(True)
        self.BACKGROUND_2.setObjectName("BACKGROUND_2")
        self.ADD_PRODUCT = QtWidgets.QPushButton(self.tab_2)
        self.ADD_PRODUCT.setGeometry(QtCore.QRect(100, 270, 241, 91))
        self.ADD_PRODUCT.setStyleSheet("background-color: rgb(215, 216, 255);\n"
"font: 75 17pt \"Palatino Linotype\";\n"
"border-radius:30;")
        self.ADD_PRODUCT.setObjectName("ADD_PRODUCT")
        self.ORDER_PRODUCT = QtWidgets.QPushButton(self.tab_2)
        self.ORDER_PRODUCT.setGeometry(QtCore.QRect(740, 270, 241, 91))
        self.ORDER_PRODUCT.setStyleSheet("background-color: rgb(215, 216, 255);\n"
"font: 75 17pt \"Palatino Linotype\";\n"
"border-radius:30;")
        self.ORDER_PRODUCT.setObjectName("ORDER_PRODUCT")
        self.DELETE_PRODUCT = QtWidgets.QPushButton(self.tab_2)
        self.DELETE_PRODUCT.setGeometry(QtCore.QRect(420, 270, 241, 91))
        self.DELETE_PRODUCT.setStyleSheet("background-color: rgb(215, 216, 255);\n"
"font: 75 17pt \"Palatino Linotype\";\n"
"border-radius:30;")
        self.DELETE_PRODUCT.setObjectName("DELETE_PRODUCT")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(110, 390, 221, 51))
        self.label.setStyleSheet("background-color: rgb(215, 216, 255);\n"
"font: 75 8pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label.setObjectName("label")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(420, 390, 241, 51))
        self.label_12.setStyleSheet("background-color: rgb(215, 216, 255);\n"
"font: 75 8pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(790, 390, 141, 51))
        self.label_13.setStyleSheet("background-color: rgb(215, 216, 255);\n"
"font: 75 8pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_13.setObjectName("label_13")
        self.LOGOUT = QtWidgets.QPushButton(self.tab_2)
        self.LOGOUT.setGeometry(QtCore.QRect(970, 30, 81, 28))
        self.LOGOUT.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"")
        self.LOGOUT.setObjectName("LOGOUT")
        self.label_50 = QtWidgets.QLabel(self.tab_2)
        self.label_50.setGeometry(QtCore.QRect(350, 30, 351, 51))
        self.label_50.setStyleSheet("background-color: rgb(215, 216, 255);\n"
"font: 75 17pt \"Palatino Linotype\";\n"
"border-radius:30;")
        self.label_50.setObjectName("label_50")
        self.INFORMATION = QtWidgets.QLabel(self.tab_2)
        self.INFORMATION.setGeometry(QtCore.QRect(420, 140, 251, 16))
        self.INFORMATION.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10;")
        self.INFORMATION.setText("")
        self.INFORMATION.setObjectName("INFORMATION")
        self.tabWidget.addTab(self.tab_2, "")
        self.TAB_3 = QtWidgets.QWidget()
        self.TAB_3.setObjectName("TAB_3")
        self.BACKGROUND_3 = QtWidgets.QLabel(self.TAB_3)
        self.BACKGROUND_3.setGeometry(QtCore.QRect(0, 0, 1065, 581))
        self.BACKGROUND_3.setStyleSheet("background-color: rgb(47, 60, 126);")
        self.BACKGROUND_3.setText("")
        self.BACKGROUND_3.setScaledContents(True)
        self.BACKGROUND_3.setWordWrap(False)
        self.BACKGROUND_3.setObjectName("BACKGROUND_3")
        self.label_14 = QtWidgets.QLabel(self.TAB_3)
        self.label_14.setGeometry(QtCore.QRect(120, 20, 811, 40))
        self.label_14.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 14pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.TAB_3)
        self.label_15.setGeometry(QtCore.QRect(80, 160, 151, 41))
        self.label_15.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.TAB_3)
        self.label_17.setGeometry(QtCore.QRect(80, 240, 151, 41))
        self.label_17.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.TAB_3)
        self.label_19.setGeometry(QtCore.QRect(590, 160, 151, 41))
        self.label_19.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.TAB_3)
        self.label_20.setGeometry(QtCore.QRect(590, 240, 71, 41))
        self.label_20.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_20.setObjectName("label_20")
        self.label_23 = QtWidgets.QLabel(self.TAB_3)
        self.label_23.setGeometry(QtCore.QRect(830, 240, 61, 41))
        self.label_23.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.TAB_3)
        self.label_24.setGeometry(QtCore.QRect(80, 340, 151, 41))
        self.label_24.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.TAB_3)
        self.label_26.setGeometry(QtCore.QRect(80, 420, 151, 41))
        self.label_26.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_26.setObjectName("label_26")
        self.ADD = QtWidgets.QPushButton(self.TAB_3)
        self.ADD.setGeometry(QtCore.QRect(480, 510, 93, 28))
        self.ADD.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.ADD.setObjectName("ADD")
        self.ADD_INFO = QtWidgets.QLabel(self.TAB_3)
        self.ADD_INFO.setGeometry(QtCore.QRect(370, 80, 301, 41))
        self.ADD_INFO.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(255, 170, 0);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:15;")
        self.ADD_INFO.setText("")
        self.ADD_INFO.setObjectName("ADD_INFO")
        self.BACK_1 = QtWidgets.QPushButton(self.TAB_3)
        self.BACK_1.setGeometry(QtCore.QRect(990, 30, 61, 28))
        self.BACK_1.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"")
        self.BACK_1.setObjectName("BACK_1")
        self.PRODUCT_NAME = QtWidgets.QLineEdit(self.TAB_3)
        self.PRODUCT_NAME.setGeometry(QtCore.QRect(270, 160, 151, 41))
        self.PRODUCT_NAME.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PRODUCT_NAME.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.PRODUCT_NAME.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PRODUCT_NAME.setText("")
        self.PRODUCT_NAME.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PRODUCT_NAME.setObjectName("PRODUCT_NAME")
        self.BRAND_NAME = QtWidgets.QLineEdit(self.TAB_3)
        self.BRAND_NAME.setGeometry(QtCore.QRect(270, 240, 151, 41))
        self.BRAND_NAME.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.BRAND_NAME.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.BRAND_NAME.setInputMethodHints(QtCore.Qt.ImhNone)
        self.BRAND_NAME.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.BRAND_NAME.setObjectName("BRAND_NAME")
        self.PRODUCT_SKU = QtWidgets.QLineEdit(self.TAB_3)
        self.PRODUCT_SKU.setGeometry(QtCore.QRect(920, 240, 71, 41))
        self.PRODUCT_SKU.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PRODUCT_SKU.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.PRODUCT_SKU.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PRODUCT_SKU.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PRODUCT_SKU.setObjectName("PRODUCT_SKU")
        self.PRODUCT_PRICE = QtWidgets.QLineEdit(self.TAB_3)
        self.PRODUCT_PRICE.setGeometry(QtCore.QRect(700, 240, 81, 41))
        self.PRODUCT_PRICE.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PRODUCT_PRICE.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.PRODUCT_PRICE.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PRODUCT_PRICE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PRODUCT_PRICE.setObjectName("PRODUCT_PRICE")
        self.PRODUCT_USE = QtWidgets.QLineEdit(self.TAB_3)
        self.PRODUCT_USE.setGeometry(QtCore.QRect(270, 340, 731, 41))
        self.PRODUCT_USE.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PRODUCT_USE.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.PRODUCT_USE.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PRODUCT_USE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PRODUCT_USE.setObjectName("PRODUCT_USE")
        self.PRODUCT_DESCRIPTION = QtWidgets.QLineEdit(self.TAB_3)
        self.PRODUCT_DESCRIPTION.setGeometry(QtCore.QRect(270, 420, 731, 41))
        self.PRODUCT_DESCRIPTION.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PRODUCT_DESCRIPTION.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.PRODUCT_DESCRIPTION.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PRODUCT_DESCRIPTION.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PRODUCT_DESCRIPTION.setObjectName("PRODUCT_DESCRIPTION")
        self.PRODUCT_CATEGORY = QtWidgets.QLineEdit(self.TAB_3)
        self.PRODUCT_CATEGORY.setGeometry(QtCore.QRect(840, 160, 151, 41))
        self.PRODUCT_CATEGORY.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PRODUCT_CATEGORY.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.PRODUCT_CATEGORY.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PRODUCT_CATEGORY.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PRODUCT_CATEGORY.setObjectName("PRODUCT_CATEGORY")
        self.tabWidget.addTab(self.TAB_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.BACKGROUND_4 = QtWidgets.QLabel(self.tab_4)
        self.BACKGROUND_4.setGeometry(QtCore.QRect(0, 0, 1065, 581))
        self.BACKGROUND_4.setStyleSheet("background-color: rgb(47, 60, 126);")
        self.BACKGROUND_4.setText("")
        self.BACKGROUND_4.setScaledContents(True)
        self.BACKGROUND_4.setObjectName("BACKGROUND_4")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(200, 20, 671, 40))
        self.label_16.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 14pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(270, 150, 221, 41))
        self.label_18.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:20;")
        self.label_18.setObjectName("label_18")
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(580, 150, 221, 41))
        self.label_21.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:20;")
        self.label_21.setObjectName("label_21")
        self.label_27 = QtWidgets.QLabel(self.tab_4)
        self.label_27.setGeometry(QtCore.QRect(90, 340, 381, 41))
        self.label_27.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:20;")
        self.label_27.setObjectName("label_27")
        self.DELETE = QtWidgets.QPushButton(self.tab_4)
        self.DELETE.setGeometry(QtCore.QRect(460, 510, 91, 31))
        self.DELETE.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.DELETE.setObjectName("DELETE")
        self.DELETE_INFO = QtWidgets.QLabel(self.tab_4)
        self.DELETE_INFO.setGeometry(QtCore.QRect(360, 80, 301, 41))
        self.DELETE_INFO.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(255, 170, 0);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:15;")
        self.DELETE_INFO.setText("")
        self.DELETE_INFO.setObjectName("DELETE_INFO")
        self.BACK_2 = QtWidgets.QPushButton(self.tab_4)
        self.BACK_2.setGeometry(QtCore.QRect(990, 30, 61, 28))
        self.BACK_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"")
        self.BACK_2.setObjectName("BACK_2")
        self.DELETE_REASON = QtWidgets.QLineEdit(self.tab_4)
        self.DELETE_REASON.setGeometry(QtCore.QRect(90, 410, 821, 41))
        self.DELETE_REASON.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.DELETE_REASON.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.DELETE_REASON.setInputMethodHints(QtCore.Qt.ImhNone)
        self.DELETE_REASON.setText("")
        self.DELETE_REASON.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.DELETE_REASON.setObjectName("DELETE_REASON")
        self.DELETE_PRODUCT_NAME = QtWidgets.QLineEdit(self.tab_4)
        self.DELETE_PRODUCT_NAME.setGeometry(QtCore.QRect(270, 220, 221, 41))
        self.DELETE_PRODUCT_NAME.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:20;")
        self.DELETE_PRODUCT_NAME.setObjectName("DELETE_PRODUCT_NAME")
        self.DELETE_BRAND = QtWidgets.QLineEdit(self.tab_4)
        self.DELETE_BRAND.setGeometry(QtCore.QRect(580, 220, 221, 41))
        self.DELETE_BRAND.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:20;")
        self.DELETE_BRAND.setObjectName("DELETE_BRAND")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.BACKGROUND_5 = QtWidgets.QLabel(self.tab_5)
        self.BACKGROUND_5.setGeometry(QtCore.QRect(0, 0, 1065, 581))
        self.BACKGROUND_5.setStyleSheet("background-color: rgb(47, 60, 126);")
        self.BACKGROUND_5.setText("")
        self.BACKGROUND_5.setScaledContents(True)
        self.BACKGROUND_5.setObjectName("BACKGROUND_5")
        self.label_28 = QtWidgets.QLabel(self.tab_5)
        self.label_28.setGeometry(QtCore.QRect(290, 20, 481, 40))
        self.label_28.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 14pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_5)
        self.label_29.setGeometry(QtCore.QRect(10, 90, 161, 41))
        self.label_29.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_5)
        self.label_30.setGeometry(QtCore.QRect(380, 90, 151, 41))
        self.label_30.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setGeometry(QtCore.QRect(740, 90, 111, 41))
        self.label_31.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.label_31.setObjectName("label_31")
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 1041, 371))
        self.groupBox.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"border:none;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.PRODUCT_TABLE = QtWidgets.QTableWidget(self.groupBox)
        self.PRODUCT_TABLE.setGeometry(QtCore.QRect(0, 50, 1041, 321))
        self.PRODUCT_TABLE.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"color: rgb(47, 60, 126);\n"
"gridline-color: rgb(47, 60, 126);")
        self.PRODUCT_TABLE.setObjectName("PRODUCT_TABLE")
        self.PRODUCT_TABLE.setColumnCount(0)
        self.PRODUCT_TABLE.setRowCount(0)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1041, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(910, 5, 111, 41))
        self.label_37.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_37.setObjectName("label_37")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(560, 5, 101, 41))
        self.label_35.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_35.setObjectName("label_35")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(395, 5, 101, 41))
        self.label_34.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_34.setObjectName("label_34")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(720, 5, 161, 41))
        self.label_36.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_36.setObjectName("label_36")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(210, 5, 121, 41))
        self.label_33.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_33.setObjectName("label_33")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(10, 5, 151, 41))
        self.label_32.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_32.setObjectName("label_32")
        self.ADD_TO_CART = QtWidgets.QPushButton(self.tab_5)
        self.ADD_TO_CART.setGeometry(QtCore.QRect(920, 90, 131, 41))
        self.ADD_TO_CART.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.ADD_TO_CART.setObjectName("ADD_TO_CART")
        self.PLACE_ORDER = QtWidgets.QPushButton(self.tab_5)
        self.PLACE_ORDER.setGeometry(QtCore.QRect(920, 530, 131, 41))
        self.PLACE_ORDER.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.PLACE_ORDER.setObjectName("PLACE_ORDER")
        self.label_38 = QtWidgets.QLabel(self.tab_5)
        self.label_38.setGeometry(QtCore.QRect(20, 540, 55, 31))
        self.label_38.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_38.setObjectName("label_38")
        self.TAX = QtWidgets.QLabel(self.tab_5)
        self.TAX.setGeometry(QtCore.QRect(90, 540, 91, 31))
        self.TAX.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:3;\n"
"")
        self.TAX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TAX.setObjectName("TAX")
        self.label_40 = QtWidgets.QLabel(self.tab_5)
        self.label_40.setGeometry(QtCore.QRect(260, 540, 141, 31))
        self.label_40.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_40.setObjectName("label_40")
        self.GRAND_TOTAL = QtWidgets.QLabel(self.tab_5)
        self.GRAND_TOTAL.setGeometry(QtCore.QRect(430, 540, 141, 31))
        self.GRAND_TOTAL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GRAND_TOTAL.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 14pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:3;\n"
"")
        self.GRAND_TOTAL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GRAND_TOTAL.setObjectName("GRAND_TOTAL")
        self.BACK_3 = QtWidgets.QPushButton(self.tab_5)
        self.BACK_3.setGeometry(QtCore.QRect(990, 30, 61, 28))
        self.BACK_3.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"")
        self.BACK_3.setObjectName("BACK_3")
        self.ORDER_PRODUCT_NAME = QtWidgets.QLineEdit(self.tab_5)
        self.ORDER_PRODUCT_NAME.setGeometry(QtCore.QRect(180, 90, 191, 41))
        self.ORDER_PRODUCT_NAME.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ORDER_PRODUCT_NAME.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.ORDER_PRODUCT_NAME.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ORDER_PRODUCT_NAME.setText("")
        self.ORDER_PRODUCT_NAME.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ORDER_PRODUCT_NAME.setObjectName("ORDER_PRODUCT_NAME")
        self.ORDER_BRAND = QtWidgets.QLineEdit(self.tab_5)
        self.ORDER_BRAND.setGeometry(QtCore.QRect(540, 90, 191, 41))
        self.ORDER_BRAND.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ORDER_BRAND.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.ORDER_BRAND.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ORDER_BRAND.setText("")
        self.ORDER_BRAND.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ORDER_BRAND.setObjectName("ORDER_BRAND")
        self.QUANTITY = QtWidgets.QLineEdit(self.tab_5)
        self.QUANTITY.setGeometry(QtCore.QRect(860, 90, 51, 41))
        self.QUANTITY.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.QUANTITY.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 12pt \"Palatino Linotype\";\n"
"border-radius:10;")
        self.QUANTITY.setInputMethodHints(QtCore.Qt.ImhNone)
        self.QUANTITY.setText("")
        self.QUANTITY.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.QUANTITY.setObjectName("QUANTITY")
        self.DATE_3 = QtWidgets.QLabel(self.tab_5)
        self.DATE_3.setGeometry(QtCore.QRect(620, 540, 111, 31))
        self.DATE_3.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:3;\n"
"")
        self.DATE_3.setObjectName("DATE_3")
        self.ORDER_ID_2 = QtWidgets.QLabel(self.tab_5)
        self.ORDER_ID_2.setGeometry(QtCore.QRect(750, 540, 71, 31))
        self.ORDER_ID_2.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:3;\n"
"")
        self.ORDER_ID_2.setObjectName("ORDER_ID_2")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.BACKGROUND_6 = QtWidgets.QLabel(self.tab_3)
        self.BACKGROUND_6.setGeometry(QtCore.QRect(0, 0, 1065, 581))
        self.BACKGROUND_6.setStyleSheet("background-color: rgb(47, 60, 126);")
        self.BACKGROUND_6.setText("")
        self.BACKGROUND_6.setScaledContents(True)
        self.BACKGROUND_6.setObjectName("BACKGROUND_6")
        self.PRINTAREA = QtWidgets.QGroupBox(self.tab_3)
        self.PRINTAREA.setGeometry(QtCore.QRect(10, 10, 361, 561))
        self.PRINTAREA.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"border:none;")
        self.PRINTAREA.setTitle("")
        self.PRINTAREA.setObjectName("PRINTAREA")
        self.frame_2 = QtWidgets.QFrame(self.PRINTAREA)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 341, 51))
        self.frame_2.setStyleSheet("background-color: rgb(46, 59, 125);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_39 = QtWidgets.QLabel(self.frame_2)
        self.label_39.setGeometry(QtCore.QRect(19, 5, 71, 41))
        self.label_39.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.frame_2)
        self.label_41.setGeometry(QtCore.QRect(130, 5, 101, 41))
        self.label_41.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_2)
        self.label_42.setGeometry(QtCore.QRect(250, 5, 71, 41))
        self.label_42.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_2)
        self.label_43.setGeometry(QtCore.QRect(70, 40, 151, 41))
        self.label_43.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_43.setObjectName("label_43")
        self.INVOICE = QtWidgets.QTableWidget(self.PRINTAREA)
        self.INVOICE.setGeometry(QtCore.QRect(10, 70, 331, 391))
        self.INVOICE.setStyleSheet("background-color: rgb(251, 234, 235);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"")
        self.INVOICE.setObjectName("INVOICE")
        self.INVOICE.setColumnCount(0)
        self.INVOICE.setRowCount(0)
        self.label_44 = QtWidgets.QLabel(self.PRINTAREA)
        self.label_44.setGeometry(QtCore.QRect(4, 527, 131, 31))
        self.label_44.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"")
        self.label_44.setObjectName("label_44")
        self.GRAND_TOTAL_2 = QtWidgets.QLabel(self.PRINTAREA)
        self.GRAND_TOTAL_2.setGeometry(QtCore.QRect(150, 527, 101, 31))
        self.GRAND_TOTAL_2.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 75 14pt \"Palatino Linotype\";\n"
"border-radius:10;\n"
"padding-right:3;\n"
"\n"
"")
        self.GRAND_TOTAL_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GRAND_TOTAL_2.setObjectName("GRAND_TOTAL_2")
        self.label_48 = QtWidgets.QLabel(self.PRINTAREA)
        self.label_48.setGeometry(QtCore.QRect(10, 470, 41, 16))
        self.label_48.setStyleSheet("color: rgb(47, 60, 126);\n"
"font: 8pt \"Palatino Linotype\";")
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.PRINTAREA)
        self.label_49.setGeometry(QtCore.QRect(10, 490, 41, 16))
        self.label_49.setStyleSheet("color: rgb(47, 60, 126);\n"
"font: 8pt \"Palatino Linotype\";")
        self.label_49.setObjectName("label_49")
        self.TIME = QtWidgets.QLabel(self.PRINTAREA)
        self.TIME.setGeometry(QtCore.QRect(60, 490, 101, 16))
        self.TIME.setStyleSheet("color: rgb(47, 60, 126);\n"
"font: 8pt \"Palatino Linotype\";")
        self.TIME.setObjectName("TIME")
        self.DATE = QtWidgets.QLabel(self.PRINTAREA)
        self.DATE.setGeometry(QtCore.QRect(60, 470, 81, 16))
        self.DATE.setStyleSheet("color: rgb(47, 60, 126);\n"
"font: 8pt \"Palatino Linotype\";")
        self.DATE.setObjectName("DATE")
        self.DATE_2 = QtWidgets.QLabel(self.PRINTAREA)
        self.DATE_2.setGeometry(QtCore.QRect(170, 470, 61, 16))
        self.DATE_2.setStyleSheet("color: rgb(47, 60, 126);\n"
"font: 8pt \"Palatino Linotype\";")
        self.DATE_2.setObjectName("DATE_2")
        self.ORDER_ID = QtWidgets.QLabel(self.PRINTAREA)
        self.ORDER_ID.setGeometry(QtCore.QRect(180, 490, 61, 16))
        self.ORDER_ID.setStyleSheet("color: rgb(47, 60, 126);\n"
"font: 8pt \"Palatino Linotype\";")
        self.ORDER_ID.setObjectName("ORDER_ID")
        self.label_46 = QtWidgets.QLabel(self.tab_3)
        self.label_46.setGeometry(QtCore.QRect(550, 220, 351, 51))
        self.label_46.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 75 22pt \"Palatino Linotype\";")
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.tab_3)
        self.label_47.setGeometry(QtCore.QRect(480, 160, 471, 51))
        self.label_47.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 75 22pt \"Palatino Linotype\";")
        self.label_47.setObjectName("label_47")
        self.GET_INVOICE = QtWidgets.QPushButton(self.tab_3)
        self.GET_INVOICE.setGeometry(QtCore.QRect(570, 340, 271, 28))
        self.GET_INVOICE.setStyleSheet("background-color: rgb(47, 60, 126);\n"
"color: rgb(251, 234, 235);\n"
"font: 10pt \"Palatino Linotype\";\n"
"text-decoration: underline;")
        self.GET_INVOICE.setObjectName("GET_INVOICE")
        self.BACK_4 = QtWidgets.QPushButton(self.tab_3)
        self.BACK_4.setGeometry(QtCore.QRect(970, 30, 81, 28))
        self.BACK_4.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(47, 60, 126);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"")
        self.BACK_4.setObjectName("BACK_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 65, 1068, 41))
        self.frame_3.setStyleSheet("background-color: rgb(47, 60, 126);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(251, 8, 521, 24))
        self.label_22.setStyleSheet("color: rgb(251, 234, 235);\n"
"background-color: rgb(47, 60, 126);\n"
"border: NONE;\n"
"font: 75 18pt \"Palatino Linotype\";")
        self.label_22.setObjectName("label_22")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "LOGIN TO ACCOUNT"))
        self.label_3.setText(_translate("MainWindow", "USERNAME"))
        self.label_5.setText(_translate("MainWindow", "PASSWORD"))
        self.LOGIN.setText(_translate("MainWindow", "LOGIN"))
        self.FORGET_PASSWORD.setText(_translate("MainWindow", "FORGET PASSWORD"))
        self.label_6.setText(_translate("MainWindow", "NEW USER. REGISTER !!"))
        self.label_7.setText(_translate("MainWindow", "NAME :- "))
        self.label_8.setText(_translate("MainWindow", "PASSWORD :- "))
        self.label_9.setText(_translate("MainWindow", "MOBILE NO. :- "))
        self.label_10.setText(_translate("MainWindow", "E-MAIL :- "))
        self.label_11.setText(_translate("MainWindow", "CONFIRM PASSWORD :- "))
        self.REGISTER_BUTTON.setText(_translate("MainWindow", "SUBMIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.ADD_PRODUCT.setText(_translate("MainWindow", "ADD"))
        self.ORDER_PRODUCT.setText(_translate("MainWindow", "ORDER"))
        self.DELETE_PRODUCT.setText(_translate("MainWindow", "DELETE"))
        self.label.setText(_translate("MainWindow", " TO ADD A NEW PRODUCT DETAIL"))
        self.label_12.setText(_translate("MainWindow", " TO REMOVE THE EXISTING PRODUCT"))
        self.label_13.setText(_translate("MainWindow", " TO PLACE AN ORDER "))
        self.LOGOUT.setText(_translate("MainWindow", "LOGOUT"))
        self.label_50.setText(_translate("MainWindow", " SELECT THE OPERATION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_14.setText(_translate("MainWindow", "   TO ADD THE NEW PRODUCT IN THE LIST, PLEASE PROVIDE DETAILS"))
        self.label_15.setText(_translate("MainWindow", " PRODUCT NAME"))
        self.label_17.setText(_translate("MainWindow", "   BRAND NAME"))
        self.label_19.setText(_translate("MainWindow", "      CATEGORY"))
        self.label_20.setText(_translate("MainWindow", "   PRICE"))
        self.label_23.setText(_translate("MainWindow", "   SKU"))
        self.label_24.setText(_translate("MainWindow", "              USE"))
        self.label_26.setText(_translate("MainWindow", "    DISCRIPTION"))
        self.ADD.setText(_translate("MainWindow", "ADD "))
        self.BACK_1.setText(_translate("MainWindow", "BACK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_3), _translate("MainWindow", "Page"))
        self.label_16.setText(_translate("MainWindow", "  SELECT PRODUCT TO REMOVE/DELETE FOR THE SYSTEM"))
        self.label_18.setText(_translate("MainWindow", "      PRODUCT NAME"))
        self.label_21.setText(_translate("MainWindow", "        SELECT BRAND"))
        self.label_27.setText(_translate("MainWindow", "  WHY YOU ARE DELETING THIS PRODUCT ?"))
        self.DELETE.setText(_translate("MainWindow", " DELETE "))
        self.BACK_2.setText(_translate("MainWindow", "BACK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.label_28.setText(_translate("MainWindow", "  SELECT PRODUCT TO PLACE AN ORDER"))
        self.label_29.setText(_translate("MainWindow", " SELECT PRODUCT"))
        self.label_30.setText(_translate("MainWindow", "   SELECT BRAND"))
        self.label_31.setText(_translate("MainWindow", " QUANTITY"))
        self.label_37.setText(_translate("MainWindow", "TOTAL PRICE"))
        self.label_35.setText(_translate("MainWindow", "QUANTITY"))
        self.label_34.setText(_translate("MainWindow", "CATEGORY"))
        self.label_36.setText(_translate("MainWindow", "PRODUCT PRICE"))
        self.label_33.setText(_translate("MainWindow", "BRAND NAME"))
        self.label_32.setText(_translate("MainWindow", "PRODUCT NAME"))
        self.ADD_TO_CART.setText(_translate("MainWindow", "ADD TO CART"))
        self.PLACE_ORDER.setText(_translate("MainWindow", "PLACE ORDER"))
        self.label_38.setText(_translate("MainWindow", "  TAX"))
        self.TAX.setText(_translate("MainWindow", "0"))
        self.label_40.setText(_translate("MainWindow", " GRAND TOTAL"))
        self.GRAND_TOTAL.setText(_translate("MainWindow", "0"))
        self.BACK_3.setText(_translate("MainWindow", "BACK"))
        self.DATE_3.setText(_translate("MainWindow", "ORDER ID"))
        self.ORDER_ID_2.setText(_translate("MainWindow", "1234"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.label_39.setText(_translate("MainWindow", "NAME"))
        self.label_41.setText(_translate("MainWindow", "QUANTITY"))
        self.label_42.setText(_translate("MainWindow", "   PRICE"))
        self.label_43.setText(_translate("MainWindow", "PRODUCT NAME"))
        self.label_44.setText(_translate("MainWindow", "  NET PAYABLE"))
        self.GRAND_TOTAL_2.setText(_translate("MainWindow", "0"))
        self.label_48.setText(_translate("MainWindow", "DATE :"))
        self.label_49.setText(_translate("MainWindow", "TIME :"))
        self.TIME.setText(_translate("MainWindow", "4:48 PM"))
        self.DATE.setText(_translate("MainWindow", "24/7/2023"))
        self.DATE_2.setText(_translate("MainWindow", "ORDER ID"))
        self.ORDER_ID.setText(_translate("MainWindow", "1234"))
        self.label_46.setText(_translate("MainWindow", "THANK YOU 🎉🎉"))
        self.label_47.setText(_translate("MainWindow", "PLEASE DO COME AGAIN"))
        self.GET_INVOICE.setText(_translate("MainWindow", "CLICK HERE TO GET INVOICE"))
        self.BACK_4.setText(_translate("MainWindow", "LOGOUT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.label_22.setText(_translate("MainWindow", "PRODUCT MANAGEMENT SYSTEM"))

