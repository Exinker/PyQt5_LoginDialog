
import os
import sys

from PyQt5 import QtWidgets, QtCore

from wigets.loginDialog import LoginDialog
from wigets.mainWindow import MainWindow
from database.client import Client


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
