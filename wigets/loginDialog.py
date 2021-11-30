
import os

from PyQt5 import QtWidgets, QtCore, QtGui


class BaseWidget(QtWidgets.QWidget):

    def __init__(self, parent, objectName):
        super().__init__(parent=parent)

        #
        self.setObjectName(objectName)

        #
        self.layout = QtWidgets.QVBoxLayout(self)

        # spacing
        self.layout.addSpacing(20)

        # logo label
        logoLabel = QtWidgets.QLabel(parent=self)

        pixmap = QtGui.QPixmap(os.path.join('.', 'img', 'logo.png'))
        # pixmap = pixmap.scaledToWidth(250)
        logoLabel.setPixmap(pixmap)

        logoLabel.setFixedSize(pixmap.size())
        self.layout.addWidget(logoLabel)

        self.layout.addSpacing(20)

    def setCurrectWidget(self, kind):
        parent = self.parent()

        if kind == 'signInWidget':
            widget = parent.signInWidget
            parent.layout.setCurrentWidget(widget)

        if kind == 'signUpWidget':
            widget = parent.signUpWidget
            parent.layout.setCurrentWidget(widget)

        if kind == 'restoreWidget':
            widget = parent.restoreWidget
            parent.layout.setCurrentWidget(widget)


class SignInWidget(BaseWidget):

    def __init__(self, parent, objectName):
        super().__init__(parent=parent, objectName=objectName)

        # signIn frame
        frame = QtWidgets.QFrame(parent=self)

        layout = QtWidgets.QVBoxLayout(frame)

        self.emailLineEdit = QtWidgets.QLineEdit('', parent=self)
        self.emailLineEdit.setObjectName('emailLineEdit')
        self.emailLineEdit.setPlaceholderText('Email address')
        layout.addWidget(self.emailLineEdit)

        self.passwordLineEdit = QtWidgets.QLineEdit('', parent=self)
        self.passwordLineEdit.setObjectName('passwordLineEdit')
        self.passwordLineEdit.setPlaceholderText('Password')
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.returnPressed.connect(self.onSignInButtonClicked)
        layout.addWidget(self.passwordLineEdit)

        restoreLabel = QtWidgets.QLabel(
            text='''<a href="https://www.google.com/">
                <span style="color: darkblue; text-decoration: none;">
                    Forgotten your password?
                </span>
            </a>
            ''',
            parent=self,
        )
        restoreLabel.linkActivated.connect(lambda: self.setCurrectWidget(kind='restoreWidget'))
        layout.addWidget(restoreLabel)

        layout.addStretch()

        signInPushButton = QtWidgets.QPushButton(text='Sign In', parent=self)
        signInPushButton.setObjectName('signInPushButton')
        signInPushButton.clicked.connect(self.onSignInButtonClicked)
        layout.addWidget(signInPushButton)

        self.layout.addWidget(frame)
        self.layout.addSpacing(0)

        # signUp frame
        frame = QtWidgets.QFrame(parent=self)

        layout = QtWidgets.QVBoxLayout(frame)

        signUpLabel = QtWidgets.QLabel(
            text='''Don\'t have an account? <a href="https://www.google.com/">
                <span style="font-weight: bold; color: rgba(31, 111, 235, 255); text-decoration: none;">
                    Sign up
                </span>
            </a>
            ''',
            parent=self,
        )
        signUpLabel.linkActivated.connect(lambda: self.setCurrectWidget(kind='signUpWidget'))
        layout.addWidget(signUpLabel)

        self.layout.addWidget(frame)

    def onSignInButtonClicked(self):
        email = self.emailLineEdit.text()
        password = self.passwordLineEdit.text()
        
        #
        parent = self.parent()

        status = parent.client.sign_in(
            email=email,
            password=password,
        )

        if status:
            parent.set_status(
                status
            )
            parent.set_user(
                user=parent.client.get_user(email)
            )

            parent.accept()


class SignUpWidget(BaseWidget):

    def __init__(self, parent, objectName):
        super().__init__(parent=parent, objectName=objectName)

        # signUp frame
        frame = QtWidgets.QFrame(parent=self)
        layout = QtWidgets.QVBoxLayout(frame)

        self.emailLineEdit = QtWidgets.QLineEdit('', parent=self)
        self.emailLineEdit.setPlaceholderText('Email address')
        layout.addWidget(self.emailLineEdit)

        self.usernameLineEdit = QtWidgets.QLineEdit('', parent=self)
        self.usernameLineEdit.setPlaceholderText('Username')
        layout.addWidget(self.usernameLineEdit)

        self.passwordLineEdit = QtWidgets.QLineEdit('', parent=self)
        self.passwordLineEdit.setPlaceholderText('Password')
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.returnPressed.connect(self.onSignUpButtonClicked)
        layout.addWidget(self.passwordLineEdit)

        layout.addStretch()

        signUpPushButton = QtWidgets.QPushButton(text='Sign Up', parent=self)
        signUpPushButton.setObjectName('signUpPushButton')
        signUpPushButton.clicked.connect(self.onSignUpButtonClicked)
        layout.addWidget(signUpPushButton)

        self.layout.addWidget(frame)

        # signIn frame
        frame = QtWidgets.QFrame(parent=self)
        layout = QtWidgets.QVBoxLayout(frame)

        signInLabel = QtWidgets.QLabel(
            text='''Back to <a href="https://www.google.com/">
                <span style="font-weight: bold; color: rgba(31, 111, 235, 255); text-decoration: none;">
                    sign in
                </span>
            </a>
            ''',
            parent=self,
        )
        signInLabel.linkActivated.connect(lambda: self.setCurrectWidget(kind='signInWidget'))
        layout.addWidget(signInLabel)

        self.layout.addWidget(frame)

    def onSignUpButtonClicked(self):
        print('On SignUp button clicked!')

        client: Client = self.parent().client
        status = client.sign_up(
            email=self.emailLineEdit.text(),
            username=self.usernameLineEdit.text(),
            password=self.passwordLineEdit.text(),
        )

        if status:
            self.setCurrectWidget(kind='signInWidget')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Email is already registered')


class RestoreWidget(BaseWidget):

    def __init__(self, parent, objectName):
        super().__init__(parent=parent, objectName=objectName)

        # frame
        frame = QtWidgets.QFrame(parent=self)
        layout = QtWidgets.QVBoxLayout(frame)

        emailLineEdit = QtWidgets.QLineEdit('', parent=self)
        emailLineEdit.setPlaceholderText('Email address')
        layout.addWidget(emailLineEdit)

        layout.addStretch()

        restorePushButton = QtWidgets.QPushButton(text='Restore password', parent=self)
        restorePushButton.clicked.connect(self.onRestoreButtonClicked)
        layout.addWidget(restorePushButton)

        self.layout.addWidget(frame)

        # signIn frame
        frame = QtWidgets.QFrame(parent=self)

        layout = QtWidgets.QVBoxLayout(frame)

        signInLabel = QtWidgets.QLabel(
            text='''Back to <a href="https://www.google.com/">
                <span style="font-weight: bold; color: rgba(31, 111, 235, 255); text-decoration: none;">
                    sign in
                </span>
            </a>
            ''',
            parent=self,
        )
        signInLabel.linkActivated.connect(lambda: self.setCurrectWidget(kind='signInWidget'))
        layout.addWidget(signInLabel)

        self.layout.addWidget(frame)

    def onRestoreButtonClicked(self):
        print('On restore password clicked')

        self.setCurrectWidget(kind='signInWidget')


class LoginDialog(QtWidgets.QDialog):

    def __init__(self, client):
        super().__init__()

        self.client = client
        self.status = False
        self.user = None

        # style
        filepath = os.path.join('.', 'styles', 'loginDialog.css')
        style = open(filepath, 'r').read()
        self.setStyleSheet(style)

        # size
        self.setFixedSize(
            QtCore.QSize(420, 520)
        )

        # layout
        self.layout = QtWidgets.QStackedLayout(self)

        self.signInWidget = SignInWidget(parent=self, objectName='signInWidget')
        self.layout.addWidget(self.signInWidget)

        self.signUpWidget = SignUpWidget(parent=self, objectName='signInWidget')
        self.layout.addWidget(self.signUpWidget)

        self.restoreWidget = RestoreWidget(parent=self, objectName='restoreWidget')
        self.layout.addWidget(self.restoreWidget)


    def set_status(self, status:bool):
        self.status = status

    def set_user(self, user:dict):
        self.user = user
