from tkinter import simpledialog, messagebox

from GameTime import GameTime
from Model import Model
from View import View
from os import path


class Controller:

    def __init__(self, db_name=None):
        self.model = Model()
        if db_name is not None:
            self.model.database_name = db_name  # database file changed
        self.view = View(self, self.model)
        self.gametime = GameTime(self.view.lbl_time)  # Create gametime object

    def main(self):
        self.view.main()
    def click_button_new(self):
        self.view.btn_new['state'] = 'disabled'
        self.view.btn_cancel['state'] = 'normal'
        self.view.btn_send['state'] = 'normal'
        self.view.char_input['state'] = 'normal'
        self.view.change_image(0)  #  esimene pilt tuleb tühi
        self.model.start_new_game()  # startind new game
        self.view.lbl_result.configure(text=self.model.user_word)
        self.view.lbl_error.configure(text='Wrong o letter(s)', fg='black')
        self.view.char_input.focus()
        self.gametime.reset()
        self.gametime.start()

    def click_btn_cancel(self):
        self.gametime.stop()  # seiskab aja
        self.view.btn_new['state'] = 'normal'
        self.view.btn_cancel['state'] = 'disabled'
        self.view.btn_send['state'] = 'disabled'
        self.view.char_input['state'] = 'disabled'
        self.view.char_input.delete(0, 'end')  # teeb kasti tühjaks
        self.view.change_image(len(self.model.image_files) - 1)  # teeb pildi kasti tühjaks ja võtab esimese pildi

    def click_btn_send(self):
        self.model.get_user_input(self.view.userinput.get().strip())
        self.view.lbl_result.configure(text=self.model.user_word)
        self.view.lbl_error.configure(text=f'Wrong {self.model.counter} letter(s). {self.model.get_all_user_chars()}')
        self.view.char_input.delete(0, 'end')
        if self.model.counter > 0:
            self.view.lbl_error.configure(fg='red')  # font color
            self.view.change_image(self.model.counter)  # error image change
        self.is_game_over()

    def is_game_over(self):
        if self.model.counter >= 11 or '_' not in self.model.user_word \
                or self.model.counter >= (len(self.model.image_files) - 1):
            self.gametime.stop()
            self.view.btn_new['state'] = 'normal'
            self.view.btn_cancel['state'] = 'disabled'
            self.view.btn_send['state'] = 'disabled'
            self.view.char_input['state'] = 'disabled'
            # Küsime mängijalt nime ja näitab kuhu see aken tuleb.
            player_name = simpledialog.askstring('Game Over!', 'What is the player name?', parent=self.view)
            self.model.set_player_name(player_name, self.gametime.counter)
            self.view.change_image(len(self.model.image_files) - 1)

        #ltoob esile skoori tabeli
    def click_btn_leaderboard(self):
        if path.exists(self.model.leaderboard_file) and path.isfile(self.model.leaderboard_file):
            popup_window = self.view.create_popup_window()
            data = self.model.read_leaderboard_file_contents()
            self.view.generate_leaderboard(popup_window, data)
        else:
            messagebox.showwarning('Message', 'Leaderboard file is missing. Play first!')






