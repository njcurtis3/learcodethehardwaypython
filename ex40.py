class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I dont want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally arounf tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

class Rules(object):

    def __init__(self, rules):
        self.rules = rules

    def read_rules(self):
        for line in self.rules:
            print line

rules_life = Rules (["1. never give up",
                    "2. always strive to be the best",
                    "3. do something that matters."])

rules_life.read_rules()
