import os.path

from Controller import Controller
from sys import argv    # käsurealt lugemiseks

class Hangman:

    def __init__(self):
        Controller(db_name).main()


if __name__ == '__main__':
    # TODO if letter inputed second time read as error
    # TODO Check leaderboard file exists
    db_name = None
    if len(argv) == 2:
        if os.path.exists(argv[1]):
            db_name = argv[1]   # new database name from commond line
    Hangman()