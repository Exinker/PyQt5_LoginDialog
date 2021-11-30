import os

with open('.env', 'r') as file:
    for line in file.readlines():
        try:
            key, value = line.strip().split('=')
            os.environ[key] = value

        except ValueError:
            pass

# database
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_PORT = int(os.environ['DATABASE_PORT'])

PASSWORD_PAPER = os.environ['PASSWORD_PAPER']
