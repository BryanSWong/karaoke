# class used to indicate selected option
class Choice:

    def select(self):
        pass

# class used to track where one is in the interface
class Interface:

    def __init__(self, option):
        pass

    def start(self):
        pass

# the main display menu to make choices like play music or add songs and remove songs.
class Main(Choice):

    def display(self):
        pass

# the add menu to add songs to a queue to play or add songs to the db.
class Add(Choice):

    def display(self):
        pass

# the remove menu to remove songs from a queue or to remove songs form the db.
class Remove(Choice):

    def display(self):
        pass

# the queue menu to see which songs are lined up and then the option to play them.
class Queue(Choice):

    def display(self):
        pass

# the play menu to select songs to play .
class Play(Choice):

    def display(self):
        pass

