class Player:

    def __init__(self, song):
        self.song = song
        self.queue = set()

    def play(self):
        print ("Now playing: '%s' by %s, official video at %s" % (self.song.gettitle(), self.song.getartist(), self.song.getlink()))

    def add(self, song):
        self.queue.add(song)
        print ("Song '%s' added to playlist" % (song.gettitle()))

    def remove(self, song):
        self.queue.remove(song)
        print ("Song '%s' removed from playlist" % (song.gettitle()))

    def queue_play(self):
        for song in self.queue:
            self.play()