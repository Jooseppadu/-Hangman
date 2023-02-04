import glob
import sqlite3
from datetime import datetime

from leaderboard import Leaderboard


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

    def start_new_game(self):
        self.get_random_word()  # set new word
        self.user_word =[]
        self.all_user_chars = []
        self.counter = 0   # TODO is needed or not
        # kõik tähed asendatakse allkriipsuga
        for x in range(len(self.new_word)):
            self.user_word.append('_')

        print(self.new_word)   # Test autojuht
        print(self.user_word)   # TEST '_'

    def get_random_word(self):
        connection = sqlite3.connect(self.database_name)  # loob ühenduse andmebaasiga
        cursor = connection.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1')
        self.new_word = cursor.fetchone()[1]  # o = id ja 1 = word
        connection.close()  # close database connection

    def get_user_input(self, userinput):
        if userinput:
            user_char = userinput[:1].lower()
            if user_char in self.new_word.lower():
                # Kui täht on õige
                if user_char not in self.all_user_chars:
                    self.change_user_input(user_char)
                    # Siin oligi viga, üks rida koodi oli liiga palju :D

                else:

                    self.counter += 1
            else:
                # Kui täht on vale
                if user_char not in self.all_user_chars:

                    self.counter += 1
                    self.all_user_chars.append(user_char)
                else:
                    # Kui täht on juba valesti sisestatud, loeb selle uuesti veana
                    self.counter += 1

    def change_user_input(self, user_char):
        # replace all _ with found letter
        current_word = self.chars_to_list(self.new_word)
        x = 0
        for c in current_word:
            if user_char.lower() == c.lower():
                self.user_word[x] = user_char.upper()
            x += 1

    def chars_to_list(self, string):
        chars = []
        chars[:0] = string
        return chars
    def get_all_user_chars(self):
        return ','.join(self.all_user_chars)

    def set_player_name(self, name, seconds):
        line = []
        now = datetime.now().strftime('%Y-%m-%d %T')
        if name.strip():
            self.player_name = name.strip()

        line.append(now)
        line.append(self.player_name)
        line.append(self.new_word)
        line.append(self.get_all_user_chars())   # all wrong letters
        line.append(str(seconds))  # time in second example
        # loob faili.
        with open(self.leaderboard_file, 'a+', encoding='utf8') as f:
            f.write(';'.join(line) + '\n')

    def read_leaderboard_file_contents(self):
        self.score_data = []
        empty_list = []
        all_lines = open(self.leaderboard_file, 'r', encoding='utf-8').readlines()
        for line in all_lines:
            parts = line.strip().split(';')
            empty_list.append(Leaderboard(parts[0], parts[1], parts[2], parts[3], int(parts[4])))
        self.score_data = sorted(empty_list, key=lambda x: x.time, reverse=False)

        return self.score_data

