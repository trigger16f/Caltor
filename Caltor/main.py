from PySide2 import QtWidgets
import Caltor
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Caltor.Caltor()

    window.show()
    sys.exit(app.exec_())
