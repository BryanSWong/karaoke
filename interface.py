from sys import exit


class Interface(object):

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
            print("programing needed")
            return 'main'

        elif action == '2':
            print("programing needed")
            return 'main'

        elif action == '3':
            print("Powering off, have a nice day.")
            return 'off'

        else:
            print("That is not a valid option.")
            return 'main'


class Off:

    def display(self):
        exit(1)


class Play:

    def display(self):
        pass


class Queue:

    def display(self):
        pass


class Power(object):

    menu = {
        'main': Main(),
        'off': Off(),
        'play': Play(),
        'queue': Queue(),
    }

    def __init__(self, start_menu):
        self.start_menu = start_menu

    def next_menu(self, menu_name):
        val = Power.menu.get(menu_name)
        return val

    def opening_menu(self):
        return self.next_menu(self.start_menu)
