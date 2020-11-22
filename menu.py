import readchar

from data import define_menu, set_disclaimer


class Menu:
    def __init__(self, tesla):
        self.tesla = tesla
        self.display_disclaimer = True
        self.menu = define_menu()
        self.disclaimer = set_disclaimer()

    def get(self, level):
        return self.menu[level]

    def show_disclaimer(self):
        if self.display_disclaimer:
            print(self.disclaimer)
            self.display_disclaimer = False

    def show_menu(self, level):
        menu = self.get(level)

        if 'main' in level.lower():
            self.show_disclaimer()

        print(f'\n\n{level.title()} Menu')
        commands = {}
        for item in menu:
            print(f"{menu[item]['select'].upper()} - {item}")
            commands[menu[item]['select']] = (menu[item]['method'], menu[item]['endpoint'])
            if 'parameters' in menu[item]:
                commands[menu[item]['select']] += (menu[item]['parameters'],)
            if 'help' in menu[item]:
                commands[menu[item]['select']] += (menu[item]['help'],)

        print(f"B - Back")
        print(f"E - Exit")

        return commands

    def get_keypress(self):
        key_press_key = repr(readchar.readkey())
        return key_press_key.replace("'", "").lower()

    def process_keypress(self, key_press, commands):
        if key_press in commands:
            if commands[key_press][0] == 'menu':
                self.display(self.tesla, commands[key_press][1])
            else:
                payload = {}
                if len(commands[key_press]) > 2:
                    if len(commands[key_press]) == 4:
                        print(commands[key_press][3])

                    for param in commands[key_press][2]:
                        value = input(f'Value for {param}:')
                        payload[param] = value

                self.tesla.run_command(commands[key_press][0], commands[key_press][1], payload)
        elif key_press == 'e':
            exit()
        elif key_press == 'b':
            return True
        else:
            print(f'  {key_press.upper()} not found.')

        return False

    def display(self, tesla, level):
        done = False
        while not done:
            commands = self.show_menu(level)
            key_press = self.get_keypress()
            done = self.process_keypress(key_press, commands)
