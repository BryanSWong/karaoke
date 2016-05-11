from sys import exit

# class used to indicate selected option
class Choice:

    def __init__(self):
        pass

    def display(self):
        print("This choice has not been set up yet")
        exit(1)

# class used to track where one is in the interface
class Interface:

    def __init__(self, option):
        self.option = option

    def start(self):
        current_choice = self.option.start_choice()

        while True:
            next_choice_option = current_choice.display()
            current_choice = self.option.next_choice(next_choice_option)


# the main display menu to make choices like play music or add songs and remove songs.
class Main(Choice):

    def display(self):
        print("Karaoke machine is powered on")
        print("What would you like to do?")
        print("Please select a number:")
        print("1. Song selection.")
        print("2. Create a list.")
        print("3. Turn off karaoke machine..")

        action = raw_input("> ")

        if action == "1":
            return 'play'

        if action == "2":
            return "queue"

        if action == "3":
            return 'off'

# the add menu to add songs to a queue to play.
class Add(Choice):

    def display(self):
        print("Which song do you want to add to queue?")
        # add code to display all songs available in a list order.
        # have input be matched and used to id the song to be added.
        # note to warn user only one song should be added and no multiples
        # player will only play the song once anyway.

# the remove menu to remove songs from a queue.
class Remove(Choice):

    def display(self):
        print("Which song do you want to remove?")
        # note to look up all added songs in queue
        # if there are no songs return message stating queue is empty and go back to queue menu

# the queue menu to see which songs are lined up and then the option to play them.
class Queue(Choice):

    def display(self):
        print("Which songs do you want to add to playlist?")
        # note make code for displaying a song db with numbers to choose songs

# the play menu to select songs to play .
class Play(Choice):

    def display(self):
        print("which song do you want to play?")
        # show a list of the songs available
        # select the song number then used to play song
        # ask to play another song after or exit

class Off(Choice):

    def display(self):
        print("Power off, have a nice day")
        exit(1)


class Power:

    choice = {
        'play': Play(),
        'queue': Queue(),
        'off': Off(),
        'add': Add(),
        'remove': Remove(),
        'main': Main(),
    }

    def __init__(self, start_choice):
        self.start_choice = start_choice

    def next_choice(self, choice):
        return Power.choice.get(choice)

    def start_choice(self):
        return self.next_choice(self.start_choice)


power = Power('main')
start = Interface(power)
start.start()
