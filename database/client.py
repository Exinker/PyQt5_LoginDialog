import datetime
import hashlib

from pymongo import MongoClient

from settings import *


class Client():

    def __init__(self):
        
        client = MongoClient(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
        )
        
        self.users = client.PyQt5_LoginDialog.users
        self.users.create_index('email')

    def get_user(self, email:str) -> dict:
        return self.users.find_one({
            'email': email,
        })

    def sign_in(self, email:str, password:str) -> bool:
        status = False

        try:
            user = self.get_user(email)
            if user:
                if self.hash_password(password, user['creationtime']) == user['password']:
                    status = True
        except Exception as error:
            print(error)

        return status

    def sign_up(self, email:str, username:str, password:str) -> bool:
        status = False

        try:
            if self.users.find_one({'email': email}) is None:
                creationtime = datetime.datetime.now().ctime()

                self.users.insert_one({
                    'email': email,
                    'username': username,
                    'password': self.hash_password(password, creationtime),
                    'creationtime': creationtime,
                })
                status = True
        except Exception as error:
            print(error)

        return status

    def restore(self, email:str) -> bool:  # FIXME restore a password by email
        pass

    @staticmethod
    def hash_password(password, creationtime):
        return hashlib.sha256((
            PASSWORD_PAPER + hashlib.sha256((password + creationtime).encode()).hexdigest()
        ).encode()).hexdigest()
