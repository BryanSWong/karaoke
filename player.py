class Player:

    def __init__(self):
        self.queue = set()

    def play(self, song_to_play):
        print("Now playing: '%s' by %s, official video at %s" %
              (song_to_play.get_title(), song_to_play.get_artist(), song_to_play.get_link()))

    def add(self, song):
        self.queue.add(song)
        print("Song '%s' added to playlist" % (song.get_title()))

    def remove(self, song):
        self.queue.remove(song)
        print("Song '%s' removed from playlist" % (song.get_title()))

    def queue_play(self):
        for song in self.queue:
            self.play(song)
