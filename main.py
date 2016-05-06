from song import Song
from player import Player

song = Song("Safe and Sound", "Capital Cites", "www.youtube.com/watch?v=47dtFZ8CFo8")
song2 = Song("In The End", "Linkin Park", "www.youtube.com/watch?v=eVTXPUF4Oz4")
song3 = Song("Beautiful Now", "Zedd", "www.youtube.com/watch?v=n1a7o44WxNo")

print(song.gettitle())
print(song.getartist())
print(song.getlink())

listen = Player(song)

listen.play()

listen.add(song)
listen.add(song2)
listen.add(song3)

listen.queueplay()

listen.remove(song2)

listen.queueplay()