from sys import exit
from player import Player
from songDB import songDB

starter = Player()  # a var that sets up the player class for later use.
queue_builder = []


def options(songlist):
    count = 1
    for song in songlist:
        print(
            "{0}.Title: {1}, Artist: {2}, Link:{3}".format(count, song.get_title(), song.get_artist(), song.get_link()))
        count += 1


def queue_list(thequeue):
    count = 1
    for item in thequeue:
        print(
            "{0}.Title: {1}, Artist: {2}, Link:{3}".format(count, item.get_title(), item.get_artist(), item.get_link()))
        count += 1


def removal_list(queue):
    count = 1

    for song in queue:
        queue_builder.append(song)

    for item in queue_builder:
        print(
            "{0}.Title: {1}, Artist: {2}, Link:{3}".format(count, item.get_title(), item.get_artist(), item.get_link()))
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
        print("")
        print("Welcome to the main menu please select a option:")
        print("1. Play a song.")
        print("2. Create and play a playlist.")
        print("3. Power off.")
        print("")

        action = input("> ")

        if action == '1':
            return 'play'

        elif action == '2':
            return 'queue'

        elif action == '3':
            print("Powering off, have a nice day.")
            return 'off'

        else:
            not_valid()
            return 'main'


class Off:
    @property
    def display(self):
        return exit(1)


class Play:
    @property
    def display(self):
        print("")
        print("Which song do you want to play:")
        options(songDB)
        print("")
        print("type main to go back to main menu")
        print("")

        action = input("> ")

        if action.isdigit():
            num = int(action)
            length = len(songDB)
            if num <= length:
                num -= 1
                starter.play(songDB[num])
                print("")
                return 'again'
            else:
                not_valid()
                return 'play'

        elif action == "main":
            return 'main'

        else:
            not_valid()
            return 'play'


class Again:
    @property
    def display(self):
        print("")
        print("Play another song? (Y/N)")
        print("note selecting no(N) will power off the system.")
        print("")

        action = input("> ")
        action.lower()

        if action == 'y':
            return 'play'

        elif action == 'n':
            print("Powering off, have a nice day.")
            return 'off'

        else:
            not_valid()
            return 'again'


class Queue:
    @property
    def display(self):
        print("")
        print("The playlist is currently empty.")
        print("Which song do you want to add to the playlist?")
        options(songDB)
        print("")
        print("type main to go back to main menu")
        print("")

        action = input("> ")
        action.lower()

        if action.isdigit():
            num = int(action)
            length = len(songDB)
            if num <= length:
                num -= 1
                starter.add(songDB[num])
                print("")
                return 'playlist'
            else:
                not_valid()
                return 'queue'

        elif action == 'main':
            return 'main'

        else:
            not_valid()
            return 'queue'


class Playlist:
    @property
    def display(self):
        print("")
        print("Current song(s) in playlist:")
        queue_list(starter.queue)
        print("")
        print("Would you like to 'play' the list now? type in 'play'.")
        print("if you want to add more songs type in 'add'.")
        print("fi you want to remove a song type in 'remove'.")
        print("if you want to return to the main menu type in 'main'.")
        print("note if you return to main your playlist will be deleted.")
        print("")

        action = input("> ")
        action.lower()

        if action == 'main':
            starter.queue.clear()
            return 'main'

        elif action == 'play':
            return 'play_queue'

        elif action == 'add':
            return 'add'

        elif action == 'remove':
            return 'remove'

        else:
            not_valid()
            return 'playlist'


class Add:
    @property
    def display(self):
        print("")
        print("Which other song do you want to add?")
        options(songDB)
        print("")
        print("type in main to return to main menu, also discards your playlist.")
        print("note: repeated songs will not be played or added, only add one of each.")
        print("")

        action = input("> ")
        action.lower()

        if action.isdigit():
            num = int(action)
            length = len(songDB)
            if num <= length:
                num -= 1
                starter.add(songDB[num])
                print("")
                return 'playlist'
            else:
                not_valid()
                return 'add'

        elif action == 'main':
            starter.queue.clear()
            del queue_builder[:]
            return 'main'

        else:
            not_valid()
            return 'add'


class Remove:
    @property
    def display(self):
        print("")
        print("Which song do you want to remove?")
        if len(starter.queue) == 0:
            print("The playlist is empty returning to main.")
            print("")
            return 'main'
        else:
            removal_list(starter.queue)
        print("")
        print("Type 'play' to play the current playlist.")
        print("Type 'add' to add songs to the playlist.")
        print("Type 'main' to return to the main menu.")
        print("note: returning to the main menu will discard your playlist.")
        print("")

        action = input("> ")
        action.lower()

        if action.isdigit():
            num = int(action)
            length = len(starter.queue)
            if num <= length:
                num -= 1
                starter.remove(queue_builder[num])
                del queue_builder[:]
                return 'remove'
            else:
                not_valid()
                del queue_builder[:]
                return 'remove'

        elif action == 'main':
            starter.queue.clear()
            del queue_builder[:]
            return 'main'

        elif action == 'play':
            del queue_builder[:]
            return 'play_queue'

        elif action == 'add':
            del queue_builder[:]
            return 'add'

        else:
            not_valid()
            del queue_builder[:]
            return 'remove'


class QueuePlay:
    @property
    def display(self):
        starter.queue_play()
        print("")
        print("If you want to play the songlist again type in 'play'")
        print("If you want to return to the main menu type in 'main'")
        print("Note: returning to the main menu will erase your playlist.")
        print("")

        action = input("> ")
        action.lower()

        if action == 'play':
            return 'play_queue'

        elif action == 'main':
            del queue_builder[:]
            starter.queue.clear()
            return 'main'

        else:
            not_valid()
            del queue_builder[:]
            return 'play_queue_options'


class QueuePlayOptions:
    @property
    def display(self):
        print("")
        print("If you want to play the songlist again type in 'play'")
        print("If you want to return to the main menu type in 'main'")
        print("Note: returning to the main menu will erase your playlist.")
        action = input("> ")
        action.lower()

        if action == 'play':
            return 'play_queue'

        elif action == 'main':
            del queue_builder[:]
            starter.queue.clear()
            return 'main'

        else:
            not_valid()
            del queue_builder[:]
            return 'play_queue_options'


class Power:
    menu = {
        'main': Main(),
        'off': Off(),
        'play': Play(),
        'again': Again(),
        'queue': Queue(),
        'playlist': Playlist(),
        'add': Add(),
        'remove': Remove(),
        'play_queue': QueuePlay(),
        'play_queue_options': QueuePlayOptions(),
    }

    def __init__(self, start_menu):
        self.start_menu = start_menu

    def next_menu(self, menu_name):
        val = Power.menu.get(menu_name)
        return val

    def opening_menu(self):
        return self.next_menu(self.start_menu)
