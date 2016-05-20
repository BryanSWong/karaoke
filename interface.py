from sys import exit
from player import Player
from songDB import songDB


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
            print("programing needed")
            return 'main'

        elif action == '3':
            print("Powering off, have a nice day.")
            return 'off'

        else:
            print("That is not a valid option.")
            print("")
            return 'main'


class Off:
    def display(self):
        exit(1)


class Play:
    @property
    def display(self):
        count = 1
        print("Which song do you want to play:")
        for song in songDB:
            print("%d.Title: %s, Artist: %s: Link:%s") % (count, song.get_title(), song.get_artist(), song.get_link())
            count += 1
        print("type main to go back to main menu")

        action = raw_input("> ")

        if action == '1':
            play_it = Player(songDB[0])
            play_it.play()
            print("")

            return 'again'

        elif action == '2':
            play_it = Player(songDB[1])
            play_it.play()
            print("")

            return 'again'

        elif action == '3':
            play_it = Player(songDB[2])
            play_it.play()
            print("")

            return 'again'

        elif action == '4':
            play_it = Player(songDB[3])
            play_it.play()
            print("")

            return 'again'

        elif action == '5':
            play_it = Player(songDB[4])
            play_it.play()
            print("")

            return 'again'

        elif action == "main":
            return 'main'

        else:
            print("that is not a valid choice.")
            print("")
            return 'play'


class Queue:
    def display(self):
        pass


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
            print("that is not a valid choice")
            print("")
            return 'again'


class Power:
    menu = {
        'main': Main(),
        'off': Off(),
        'play': Play(),
        'queue': Queue(),
        'again': Again(),
    }

    def __init__(self, start_menu):
        self.start_menu = start_menu

    def next_menu(self, menu_name):
        val = Power.menu.get(menu_name)
        return val

    def opening_menu(self):
        return self.next_menu(self.start_menu)
