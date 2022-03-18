# -*- encoding: utf-8 -*-
# Ivan Perehiniak , 2022-03-18

"""
Main file for github pypeline test. Execute this file to run an application.

"""

import os
import sys
import traceback

from contextlib import suppress

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

if __name__ == "__main__":
    with suppress(Exception):
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setCentralWidget(QLabel("Hello World !!! :)"))
        window.setWindowTitle(f"Github Pypes Test, v.0.0.1")
        window.show()
        app.exec_()
