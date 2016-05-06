class Player:

    def __init__(self, song):
        self.song = song
        self.queue = set()

    def play(self):
        print("Now playing: '%s' by %s, official video at %s" % (self.song.get_title(), self.song.get_artist(), self.song.get_link()))

    def add(self, song):
        self.queue.add(song)
        print("Song '%s' added to playlist" % (song.get_title()))

    def remove(self, song):
        self.queue.remove(song)
        print("Song '%s' removed from playlist" % (song.get_title()))

    def queue_play(self):
        for song in self.queue:
            self.play()