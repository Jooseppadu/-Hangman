from datetime import datetime


class GameTime:

    def __init__(self, label:time):
        self.label_time = label_time  # Label kus on aeg
        self.counter = 0 # second
        self.running = False


    def update(self):
        if self.running:
            if self.counter == 0:
                display = ' 0:00:00'
            else:
                tt = datetime.utcfromtimestamp(self.counter)
                string = tt.strftime('%T')  #%H:%M:%S  see om sama
                display = string

            self.label_time['text'] = display
            self.label_time.after(1000, self.update)   # self.update on ilma sulgudeta
            self.counter += 1

    def start(self):
        self.running = True
        self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.counter = 0
        self.label_time['text'] = '0:00:00'

