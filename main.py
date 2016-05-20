from interface import Power, Interface

# print(song.get_title())
# print(song.get_artist())
# print(song.get_link())

# ten.add(song)
# listen.add(song2)
# listen.add(song3)
# listen.add(song4)
# listen.add(song5)

# listen.play()
# listen.queue_play()

# listen.remove(song2)

# listen.queue_play()

power_on = Power('main')
start = Interface(power_on)
start.start()
