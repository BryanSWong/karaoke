from sys import exit
from player import Player
from songDB import songDB

starter = Player()  # a var that sets up the player class for later use.
queue_builder = []


def options(songlist):
    count = 1
    for song in songlist:
        print("%d.Title: %s, Artist: %s: Link:%s") % (count, song.get_title(), song.get_artist(), song.get_link())
        count += 1


def queue_list(thequeue):
    count = 1
    for item in thequeue:
        print("%d.Title: %s, Artist: %s: Link:%s") % (count, item.get_title(), item.get_artist(), item.get_link())
        count += 1


def removal_list(queue):
    count = 1

    for song in queue:
        queue_builder.append(song)

    for item in queue_builder:
        print("%d.Title: %s, Artist: %s: Link:%s") % (count, item.get_title(), item.get_artist(), item.get_link())
        count += 1


def not_valid():
    print("That is not a valid choice.")
    print("")


class Interface:
    def __init__(self, the_menu):
        self.the_menu = the_menu

    def start(self):
        current_menu = self.the_menu.opening_menu()
        last_menu = self.the_menu.next_menu('off')

        while current_menu != last_menu:
            next_menu_choice = current_menu.display
            current_menu = self.the_menu.next_menu(next_menu_choice)


class Main:
    @property
    def display(self):
        print("Welcome to the main menu please select a option:")
        print("1. Play a song.")
        print("2. Create and play a playlist.")
        print("3. Power off.")

        action = raw_input("> ")

        if action == '1':
            return 'play'

        elif action == '2':
            return 'playlist'

        elif action == '3':
            print("Powering off, have a nice day.")
            return 'off'

        else:
            not_valid()
            return 'main'


class Off:
    def display(self):
        exit(1)


class Play:
    @property
    def display(self):
        count = 1
        print("Which song do you want to play:")
        options(songDB)
        print("type main to go back to main menu")

        action = raw_input("> ")

        if action == '1':
            starter.play(songDB[0])
            print("")

            return 'again'

        elif action == '2':
            starter.play(songDB[1])
            print("")

            return 'again'

        elif action == '3':
            starter.play(songDB[2])
            print("")

            return 'again'

        elif action == '4':
            starter.play(songDB[3])
            print("")

            return 'again'

        elif action == '5':
            starter.play(songDB[4])
            print("")

            return 'again'

        elif action == "main":
            return 'main'

        else:
            not_valid()
            return 'play'


class Queue:
    @property
    def display(self):
        print("The playlist is currently empty.")
        print("Which song do you want to add to the playlist?")
        options(songDB)
        print("type main to go back to main menu")

        action = raw_input("> ")
        action.lower()

        if action == 'main':
            return 'main'

        elif action == '1':
            starter.add(songDB[0])
            return 'queue'

        elif action == '2':
            starter.add(songDB[1])
            return 'queue'

        elif action == '3':
            starter.add(songDB[2])
            return 'queue'

        elif action == '4':
            starter.add(songDB[3])
            return 'queue'

        elif action == '5':
            starter.add(songDB[4])
            return 'queue'

        else:
            not_valid()
            return 'playlist'


class Again:
    @property
    def display(self):
        print("Play another song? (Y/N)")
        print("note selecting no will power off the system.")

        action = raw_input("> ")
        action.lower()

        if action == 'y':
            return 'play'

        elif action == 'n':
            print("Powering off, have a nice day.")
            return 'off'

        else:
            not_valid()
            return 'again'


class Playlist:
    @property
    def display(self):
        print("Current song(s) in playlist:")
        queue_list(starter.queue)
        print("Would you like to 'play' the list now?")
        print("type in 'play'.")
        print("if you want to add more songs type in 'add'.")
        print("fi you want to remove a song type in 'remove'.")
        print("if you want to return to the main menu type in 'main'.")
        print("note if you return to main your playlist will be deleted.")

        action = raw_input("> ")
        action.lower()

        if action == 'main':
            starter.queue.clear()
            return 'main'

        elif action == 'add':
            return 'add'

        elif action == 'remove':
            return 'remove'

        else:
            not_valid()
            return 'queue'


class Add:
    @property
    def display(self):
        print("Which other song do you want to add?")
        options(songDB)
        print("type in main to return to main menu, also discards your playlist.")
        print("note: repeated songs will not be played so only add one of each.")

        action = raw_input("> ")
        action.lower()

        if action == 'main':
            starter.queue.clear()
            return 'main'

        elif action == '1':
            starter.add(songDB[0])
            return 'queue'

        elif action == '2':
            starter.add(songDB[1])
            return 'queue'

        elif action == '3':
            starter.add(songDB[2])
            return 'queue'

        elif action == '4':
            starter.add(songDB[3])
            return 'queue'

        elif action == '5':
            starter.add(songDB[4])
            return 'queue'

        else:
            not_valid()
            return 'playlist'


class Remove:
    @property
    def display(self):
        print("Which song do you want to remove?")
        if len(starter.queue) == 0:
            print("The playlist is empty returning to main.")
            print("")
            return 'main'
        else:
            removal_list(starter.queue)
        print("type main to return to the main menu.")
        print("note: returning to the main menu will discard your playlist.")

        action = raw_input("> ")
        action.lower()

        if action == 'main':
            starter.queue.clear()
            del queue_builder[:]
            return 'main'

        elif action == '1':
            if len(queue_builder) < 1:
                not_valid()
                del queue_builder[:]
                return 'remove'
            else:
                starter.remove(queue_builder[0])
                del queue_builder[:]
                return 'remove'

        elif action == '2':
            if len(queue_builder) < 2:
                not_valid()
                del queue_builder[:]
                return 'remove'

            else:
                starter.remove(queue_builder[1])
                del queue_builder[:]
                return 'remove'

        elif action == '3':
            if len(queue_builder) < 3:
                not_valid()
                del queue_builder[:]
                return 'remove'

            else:
                starter.remove(queue_builder[2])
                del queue_builder[:]
                return 'remove'

        elif action == '4':
            if len(queue_builder) < 3:
                not_valid()
                del queue_builder[:]
                return 'remove'

            else:
                starter.remove(queue_builder[3])
                del queue_builder[:]
                return 'remove'

        elif action == '5':
            if len(queue_builder) < 4:
                not_valid()
                del queue_builder[:]
                return 'remove'

            else:
                starter.remove(queue_builder[4])
                del queue_builder[:]
                return 'remove'

        else:
            not_valid()
            del queue_builder[:]
            return 'remove'


class QueuePlay:

    def display(self):
        starter.queue_play()
        print("")
        print("If you want to play the songlist again type in 'play'")
        print("If you want to return to the main menu type in 'main'")
        print("Note: returning to the main menu will erase your playlist.")
        action = raw_input("> ")
        action.lower()

        if action == 'play':
            return 'play_more'

        elif action == 'main':
            del queue_builder[:]
            return 'main'

        else:
            not_valid()
            del queue_builder[:]
            return 'play_more'


class Power:
    menu = {
        'main': Main(),
        'off': Off(),
        'play': Play(),
        'queue': Playlist(),
        'again': Again(),
        'playlist': Queue(),
        'add': Add(),
        'remove': Remove(),
        'play_more': QueuePlay(),
    }

    def __init__(self, start_menu):
        self.start_menu = start_menu

    def next_menu(self, menu_name):
        val = Power.menu.get(menu_name)
        return val

    def opening_menu(self):
        return self.next_menu(self.start_menu)
