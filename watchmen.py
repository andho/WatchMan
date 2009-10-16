# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication
from UserInterface import mainwindow

app = QApplication(sys.argv)

main = mainwindow.MainWindow()
main.show()

sys.exit(app.exec_())