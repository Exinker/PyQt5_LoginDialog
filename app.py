
import sys

from PyQt5 import QtWidgets

from wigets.loginDialog import LoginDialog
from database.client import Client

class MainWindow(QtWidgets.QMainWindow):
    '''Placeholder of the main window'''

    def __init__(self, user):
        super().__init__()

        #
        username = user['username']
        self.setWindowTitle(f'Welcome, {username}')

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

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
