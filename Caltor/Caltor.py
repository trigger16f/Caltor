# import matplotlib.pyplot
from PySide2 import QtWidgets, QtCore
import Matplot
from UI import MainCal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import numpy as np
import math


# from matplotlib import pyplot

class Caltor(QtWidgets.QMainWindow, MainCal.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        MainCal.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Caltor")
        self.sc = Matplot.MplCanvas(self, width=6, height=8, dpi=100)
        toolbar = NavigationToolbar2QT(self.sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.sc)
        layout.addWidget(toolbar)
        self.widget_plot.setLayout(layout)
        # self.setCentralWidget(self.sc)
        self.connect()

    def connect(self):
        self.cb_ctyp.currentIndexChanged.connect(self.choose)
        self.pb_draw.clicked.connect(self.choice_type)
        self.pb_clear.clicked.connect(self.sc.clear)

    def choose(self, index):
        self.stWidget_type.setCurrentIndex(index)
        # int(self.cb_ctyp.currentIndex())=

    def choice_type(self):
        if self.stWidget_type.currentIndex() == 0:
            return self.cal_fun1()
        elif self.stWidget_type.currentIndex() == 1:
            return self.cal_fun2()
        elif self.stWidget_type.currentIndex() == 2:
            return self.cal_fun3()

    def cal_fun1(self):  # 普通函数
        if self.le_minimum.text() != '' and self.le_maximum.text() != '':
            xs = np.arange(float(self.le_minimum.text()), float(self.le_maximum.text()), 0.1)
        else:
            xs = np.arange(1, 30, 0.1)
        ys = []
        nb = []
        ls = self.le_nb.text().split(",")
        # size = len(nb)
        for d in ls:
            nb.append(float(d))
        size = len(nb)
        for x in xs:
            y = 0
            for i in range(0, size):
                y += nb[i] * math.pow(x, size - i - 1)
            ys.append(y)
        self.sc.axes.plot(xs, ys)
        self.sc.draw()

    def cal_fun2(self):  # 三角函数
        if self.le_minimum.text() != '' and self.le_maximum.text() != '':
            xm = np.arange(float(self.le_minimum.text()), float(self.le_maximum.text()), 0.1)
        else:
            xm = np.arange(1, 30, 0.1)
        ym = []
        if self.cb_choose.currentIndex() == 0:
            for p in xm:
                x = math.sin(math.radians(p * float(self.le_b.text()) + float(self.le_c.text())))
                y = float(self.le_a.text()) * x
                ym.append(y)
            self.sc.axes.plot(xm, ym)
            self.sc.draw()
        if self.cb_choose.currentIndex() == 1:
            for l in xm:
                x = math.cos(math.radians(l * float(self.le_b.text()) + float(self.le_c.text())))
                y = float(self.le_a.text()) * x
                ym.append(y)
            self.sc.axes.plot(xm, ym)
            self.sc.draw()

    def cal_fun3(self):
        if self.le_minimum.text() != '' and self.le_maximum.text() != '':
            xm = np.arange(float(self.le_minimum.text()), float(self.le_maximum.text()), 0.1)
        else:
            xm = np.arange(1, 30, 0.1)
        ym = []
        for i in xm:
            y=math.pow(float(self.le_fun3a.text()),i)
            ym.append(y)
        self.sc.axes.plot(xm,ym)
        self.sc.draw()
