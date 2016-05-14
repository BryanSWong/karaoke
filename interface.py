from sys import exit


class Choice:

    def display(self):
        print "This menu is not yet configured."
        exit(1)


class Interface:

    def __init__(self, menu):
        self.menu = menu

    def start(self):
        current_menu = self.menu.current_menu()
        power_off = self.menu.next_menu('off')

        while current_menu != power_off:
            next_menu_name = current_menu.display()
            current_menu = self.menu.next_menu(next_menu_name)

        current_menu.display()


class Main(Choice):

    def display(self):
        pass


class Off(Choice):

    def display(self):
        pass


class Power:

    menu = {
        'main': Main(),
        'off': Off(),
    }

    def __init__(self, start_menu):
        self.start_menu = start_menu

    def next_menu(self, scene_name):
        val = Power.menu.get(scene_name)
        return val

    def current_menu(self):
        return self.next_menu(self.start_menu)
