class song():

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = song(["happy birthday to you",
                   "i don't want to get sued",
                   "so i'll stop right there"])

bull_on_parade = song(["they rally around the family",
                       "with pocksts full of shells"])

happy_bday.sing_me_a_song()

bull_on_parade.sing_me_a_song()
