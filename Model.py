import glob


class Model:

    def __init__(self):
        self.database_name = 'databases/hangman_words_ee.db'
        self.image_files = glob.glob('images/*.png')  # kõik failid mille laiendiks on png. (pildid)
        # Uus mäng
        self.new_word = None  # random word
        self.user_word = []    # User find letter tähed mida kasutaja on leidnud
        self.all_user_chars = []  # kõik tähed mis on lisatud suvaliselt
        self.counter = 0  # Error counter ( valed tähed)
        # Leaderboard / edetabel
        self.player_name = 'UNKNOWN'
        self.leaderboard_file = 'leaderboard.txt'
        self.score_data = []  # sisaldab eelnevat faili sisu

