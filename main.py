from song import Song
from player import Player

song = Song("Safe and Sound", "Capital Cites", "youtube214232.com")

print(song.getTitle())
print(song.getArtist())
print(song.getLink())

listen = Player(song)

print listen.play()