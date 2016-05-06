class Player:

    def __init__(self, song):
        self.song = song
        self.queue = set()

    def play(self):
        title = self.song.gettitle()
        artist = self.song.getartist()
        youtube = self.song.getlink()
        print "Now playing: '%s' by %s, official video at %s" % (title, artist, youtube)
        # return is used instead of print to avoid a none in the console

    def add(self, song):
        self.queue.add(song)
        title = song.gettitle()
        print "Song '%s' added to playlist" % (title)

    def remove(self, song):
        self.queue.remove(song)
        title = song.gettitle()
        print "Song '%s' removed from playlist" % (title)

    def queueplay(self):
        for song in self.queue:
            title = song.gettitle()
            artist = song.getartist()
            youtube = song.getlink()
            print "Now playing: '%s' by %s, official video at %s" % (title, artist, youtube)