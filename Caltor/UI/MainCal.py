# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainCal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1124, 835)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout = QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.pb_draw = QPushButton(self.tab_1)
        self.pb_draw.setObjectName(u"pb_draw")

        self.gridLayout_2.addWidget(self.pb_draw, 0, 4, 1, 1)

        self.pb_clear = QPushButton(self.tab_1)
        self.pb_clear.setObjectName(u"pb_clear")

        self.gridLayout_2.addWidget(self.pb_clear, 0, 5, 1, 1)

        self.label_2 = QLabel(self.tab_1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.cb_ctyp = QComboBox(self.tab_1)
        self.cb_ctyp.addItem("")
        self.cb_ctyp.addItem("")
        self.cb_ctyp.addItem("")
        self.cb_ctyp.setObjectName(u"cb_ctyp")

        self.gridLayout_2.addWidget(self.cb_ctyp, 0, 0, 1, 1)

        self.stWidget_type = QStackedWidget(self.tab_1)
        self.stWidget_type.setObjectName(u"stWidget_type")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stWidget_type.sizePolicy().hasHeightForWidth())
        self.stWidget_type.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_nb = QLineEdit(self.page)
        self.le_nb.setObjectName(u"le_nb")

        self.horizontalLayout.addWidget(self.le_nb)

        self.stWidget_type.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_b = QLineEdit(self.page_2)
        self.le_b.setObjectName(u"le_b")

        self.gridLayout.addWidget(self.le_b, 1, 4, 1, 1)

        self.lb_sin = QLabel(self.page_2)
        self.lb_sin.setObjectName(u"lb_sin")

        self.gridLayout.addWidget(self.lb_sin, 1, 1, 1, 1)

        self.le_c = QLineEdit(self.page_2)
        self.le_c.setObjectName(u"le_c")

        self.gridLayout.addWidget(self.le_c, 1, 6, 1, 1)

        self.lb_tan = QLabel(self.page_2)
        self.lb_tan.setObjectName(u"lb_tan")

        self.gridLayout.addWidget(self.lb_tan, 1, 5, 1, 1)

        self.lb_cos = QLabel(self.page_2)
        self.lb_cos.setObjectName(u"lb_cos")

        self.gridLayout.addWidget(self.lb_cos, 1, 3, 1, 1)

        self.le_a = QLineEdit(self.page_2)
        self.le_a.setObjectName(u"le_a")

        self.gridLayout.addWidget(self.le_a, 1, 2, 1, 1)

        self.cb_choose = QComboBox(self.page_2)
        self.cb_choose.addItem("")
        self.cb_choose.addItem("")
        self.cb_choose.setObjectName(u"cb_choose")

        self.gridLayout.addWidget(self.cb_choose, 1, 0, 1, 1)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)

        self.stWidget_type.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.layoutWidget_2 = QWidget(self.page_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 30, 279, 26))
        self.gridLayout_3 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.le_fun3a = QLineEdit(self.layoutWidget_2)
        self.le_fun3a.setObjectName(u"le_fun3a")

        self.gridLayout_3.addWidget(self.le_fun3a, 0, 3, 1, 1)

        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)

        self.stWidget_type.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stWidget_type, 0, 2, 1, 1)

        self.le_maximum = QLineEdit(self.tab_1)
        self.le_maximum.setObjectName(u"le_maximum")

        self.gridLayout_2.addWidget(self.le_maximum, 1, 2, 1, 1)

        self.label_3 = QLabel(self.tab_1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 3, 1, 1)

        self.le_minimum = QLineEdit(self.tab_1)
        self.le_minimum.setObjectName(u"le_minimum")

        self.gridLayout_2.addWidget(self.le_minimum, 1, 4, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.widget_plot = QWidget(self.tab_1)
        self.widget_plot.setObjectName(u"widget_plot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_plot.sizePolicy().hasHeightForWidth())
        self.widget_plot.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.widget_plot)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1124, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.stWidget_type.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pb_draw.setText(QCoreApplication.translate("MainWindow", u"\u753b\u56fe", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u503c", None))
        self.cb_ctyp.setItemText(0, QCoreApplication.translate("MainWindow", u"\u591a\u6b21\u51fd\u6570", None))
        self.cb_ctyp.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e09\u89d2\u51fd\u6570", None))
        self.cb_ctyp.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5e42\u51fd\u6570", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u6570", None))
        self.lb_sin.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.lb_tan.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.lb_cos.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.cb_choose.setItemText(0, QCoreApplication.translate("MainWindow", u"sin", None))
        self.cb_choose.setItemText(1, QCoreApplication.translate("MainWindow", u"cos", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"y=a*sin/cos(bx+c)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5e42\u51fd\u6570", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ax^2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u503c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u4ee3\u6570", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u51e0\u4f55", None))
    # retranslateUi

