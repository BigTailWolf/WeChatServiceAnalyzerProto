#!/usr/bin/python

import sys
from PyQt4.QtGui import QApplication
from MainWindow  import MainWindow

def main():
    app = QApplication(sys.argv)
    ex  = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    main()

