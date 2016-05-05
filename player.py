class Player:

    def __init__(self, song):
        self.song = song

    def play(self):
        title = self.song.getTitle()
        artist = self.song.getArtist()
        youtube = self.song.getLink()
        return "Now playing: %s by %s, official video at %s" % (title, artist, youtube)