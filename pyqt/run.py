#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Santiago Bruno
# License: GPL v3
# Web pages: http://www.santiagobruno.com.ar/programas.html
#            http://code.google.com/p/deflog/

#python imports
import re, sys

#PyQt imports
from PyQt4 import QtCore, QtGui

#UI imports
from ui.deflog import Ui_MainWindow

from pylibdeflog.libdeflog import *


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

    def translate(self):
        text = unicode(self.originalTextEdit.toPlainText())
        text = dessimbolizar(text)
        words_re = re.compile(u"([\\w\\d+]+)", re.UNICODE)
        words = words_re.split(text)
        translated = u""

        if words:
            if self.deleet.isChecked():
                words = map(deleet, words)
            if self.desalternar.isChecked():
                words = map(desalternar, words)
            if self.desmultiplicar.isChecked():
                words = map(desmultiplicar, words)
            if self.dessmsar.isChecked():
                words = map(lambda x: desms(x, format='plain'), words)
            if self.desestupidizar.isChecked():
                words = map(lambda x: desestupidizar(x, format='plain'), words)
            if self.deszezear.isChecked():
                words = map(deszezear, words)
            if self.deskar.isChecked():
                words = map(desk, words)
            if self.desporteniar.isChecked():
                words = map(desporteniar, words)
            if self.fixmissingvowels.isChecked():
                words = map(fixmissingvowels, words)
            translated += "".join( [ w for w in words] )


        self.translatedTextEdit.setPlainText(translated)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
