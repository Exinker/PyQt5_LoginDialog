
import os

from PyQt5 import QtGui, QtWidgets, QtCore


class CentralWidget(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()

        # size
        self.setFixedSize(
            QtCore.QSize(600, 480)
        )

        #
        layout = QtWidgets.QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addStretch()

        homeLabel = QtWidgets.QLabel('HOME')
        homeLabel.setObjectName('homeLabel')
        homeLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        layout.addWidget(homeLabel)

        layout.addStretch()

        infoLabel = QtWidgets.QLabel(
            text='''<a href="https://">
                <span style="font-weight: bold; color: rgb(31, 111, 235); text-decoration: none;">
                    press me
                </span>
            </a> to exit
            ''',
            parent=self,
        )
        infoLabel.setObjectName('infoLabel')
        infoLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        infoLabel.linkActivated.connect(QtWidgets.QApplication.quit)
        layout.addWidget(infoLabel)


class MainWindow(QtWidgets.QMainWindow):  # FIXME: replace MainWindow
    '''Placeholder of the main window'''

    def __init__(self, user):
        super().__init__()

        self.username = user['username']

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # style
        filepath = os.path.join('.', 'styles', 'mainWindow.css')
        style = open(filepath, 'r').read()
        self.setStyleSheet(style)

        #
        self.setCentralWidget(CentralWidget())

        #
        self.show()

