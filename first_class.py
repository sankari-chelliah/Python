class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        #print(self.lyrics)
        for line in self.lyrics:
            print(line)

rhymes = Song (["If you are happy and you know it clap your Hands",
            "Clap! Clap!"])

happy_bday = Song(["Happy Birthday to you",
                    "Happy Birthday to you",
                    "Happy Birthday, Happy Birthday",
                    "Happy Birthday to you!"])




happy_bday.sing_me_a_song()

print("-" *15)

rhymes.sing_me_a_song()
