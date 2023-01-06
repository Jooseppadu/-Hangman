from Controller import Controller


class Hangman:

    def __init__(self):
        Controller().main()


if __name__ == '__main__':
    # TODO käsurea pealt andmebaasi faili lugemine
    Hangman()

# If __name__ == '__main__':
    # TODO if letter inputed second time read as error