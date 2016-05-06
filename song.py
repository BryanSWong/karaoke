class Song:

    def __init__(self, title, artist, youtube):
        self.title = title
        self.artist = artist
        self.youtube = youtube
        self.song = {}
        self.song["title"] = self.title
        self.song["artist"] = self.artist
        self.song["youtube"] = self.youtube

    def gettitle(self):
        return self.title

    def getartist(self):
        return self.artist

    def getlink(self):
        return self.youtube