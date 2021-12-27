
import os
import sys

from PyQt5 import QtWidgets, QtCore

from wigets.loginDialog import LoginDialog
from wigets.centralWidget import CentralWidget
from database.client import Client


class MainWindow(QtWidgets.QMainWindow):  # FIXME: replace MainWindow
    '''Placeholder of the main window'''

    def __init__(self, user):
        super().__init__()

        self.username = user['username']

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        # style
        filepath = os.path.join('.', 'styles', 'mainWindow.css')
        style = open(filepath, 'r').read()
        self.setStyleSheet(style)

        #
        self.setCentralWidget(CentralWidget())

        #
        self.show()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    loginDialog = LoginDialog(
        client=Client(),
    )
    if loginDialog.exec() == QtWidgets.QDialog.Accepted:
        window = MainWindow(
            user=loginDialog.user,
        )
    else:
        sys.exit()

    sys.exit(app.exec())
