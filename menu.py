import readchar


class Menu:
    def __init__(self, tesla):
        self.tesla = tesla
        self.prev_menu = None
        self.menu = {
            # MAIN MENU
            "main": {
                "Vehicles": {
                    "select": "v",
                    "method": "get",
                    "endpoint": ""
                },
                "States": {
                    "select": "s",
                    "method": "menu",
                    "endpoint": "states"
                },
                "Commands": {
                    "select": "c",
                    "method": "menu",
                    "endpoint": "commands"
                }
            },

            # STATES MENU
            "states": {
                "Vehicle Data": {
                    "select": "d",
                    "method": "get",
                    "endpoint": "/vehicle_data"
                },
                "Charge State": {
                    "select": "c",
                    "method": "get",
                    "endpoint": "/data_request/charge_state"
                },
                "Climate State": {
                    "select": "l",
                    "method": "get",
                    "endpoint": "/data_request/climate_state"
                },
                "Drive State": {
                    "select": "r",
                    "method": "get",
                    "endpoint": "/data_request/drive_state"
                },
                "GUI Settings": {
                    "select": "g",
                    "method": "get",
                    "endpoint": "/data_request/gui_settings"
                },
                "Vehicle State": {
                    "select": "v",
                    "method": "get",
                    "endpoint": "/data_request/vehicle_state"
                },
                "Vehicle Config": {
                    "select": "o",
                    "method": "get",
                    "endpoint": "/data_request/vehicle_config"
                },
                "Mobile Enabled": {
                    "select": "m",
                    "method": "get",
                    "endpoint": "/mobile_enabled"
                },
                "Nearby Charging Sites": {
                    "select": "n",
                    "method": "get",
                    "endpoint": "/nearby_charging_sites"
                }
            },

            # COMMANDS MENU
            "commands": {
                "Wake Vehicle": {
                    "select": "w",
                    "method": "post",
                    "endpoint": "/wake_up"
                },
                "Honk Horn": {
                    "select": "h",
                    "method": "post",
                    "endpoint": "/command/honk_horn"
                },
                "Flash Lights": {
                    "select": "f",
                    "method": "post",
                    "endpoint": "/command/flash_lights"
                },
                "Remote Start - SOON": {
                    "select": "s",
                    "method": "post",
                    "endpoint": "/command/remote_start_drive",
                    "parameters": {
                        "password"
                    }
                },
                "Homelink - SOON": {
                    "select": "l",
                    "method": "post",
                    "endpoint": "/command/trigger_homelink",
                    "parameters": {
                        "lat", "lon"
                    }
                },
                "Speed Limit - SOON": {
                    "select": "p",
                    "method": "menu",
                    "endpoint": "speed limit"
                },
                "Valet Mode - SOON": {
                    "select": "v",
                    "method": "menu",
                    "endpoint": "valet mode"
                },
                "Sentry Mode": {
                    "select": "y",
                    "method": "post",
                    "endpoint": "/command/set_sentry_mode",
                    "parameters": {
                        "on"
                    },
                    "help": "True to turn on, false to turn off."
                },
                "Doors": {
                    "select": "d",
                    "method": "menu",
                    "endpoint": "doors"
                },
                "Trunk": {
                    "select": "t",
                    "method": "post",
                    "endpoint": "/command/actuate_trunk",
                    "parameters": {
                        "which_trunk"
                    },
                    "help": "Which trunk to open/close. rear and front are the only options."
                },
                "Windows": {
                    "select": "i",
                    "method": "post",
                    "endpoint": "/command/window_control",
                    "parameters": {
                        "command", "lat", "lon"
                    },
                    "help": "Controls the windows. Will vent or close all windows simultaneously.\n"
                            "lat and lon values must be near the current location of the car for close operation to succeed.\n"
                            "For vent, the lat and lon values are ignored, and may both be 0 (which has been observed from the app itself).\n"
                            "Command: What action to take with the windows. Allows the values vent and close"
                },
                "Sunroof": {
                    "select": "r",
                    "method": "post",
                    "endpoint": "/command/sun_roof_control",
                    "parameters": {
                        "state"
                    },
                    "help": "The amount to open the sunroof. Currently this only allows the values vent and close."
                },
                "Charging": {
                    "select": "c",
                    "method": "menu",
                    "endpoint": "charging"
                },
                "Climate": {
                    "select": "e",
                    "method": "menu",
                    "endpoint": "climate",
                },
                "Media - SOON": {
                    "select": "m",
                    "method": "menu",
                    "endpoint": "media"
                },
                "Sharing - SOON": {
                    "select": "a",
                    "method": "post",
                    "endpoint": "/command/share",
                    "parameters": {
                        "type", "locale", "timestamp_ms", "value"
                    }
                },
                "Software Updates - SOON": {
                    "select": "u",
                    "method": "menu",
                    "endpoint": "software updates"
                }
            },

            # DOORS MENU
            "doors": {
                "Lock": {
                    "select": "l",
                    "method": "post",
                    "endpoint": "/command/door_lock"
                },
                "Unlock": {
                    "select": "u",
                    "method": "post",
                    "endpoint": "/command/door_unlock"
                },
            },

            # CHARGING MENU
            "charging": {
                "Open Charge Door": {
                    "select": "o",
                    "method": "post",
                    "endpoint": "/command/charge_port_door_open"
                },
                "Close Charge Door": {
                    "select": "c",
                    "method": "post",
                    "endpoint": "/command/charge_port_door_close"
                },
                "Start Charging": {
                    "select": "s",
                    "method": "post",
                    "endpoint": "/command/charge_start"
                },
                "Stop Charging": {
                    "select": "x",
                    "method": "post",
                    "endpoint": "/command/charge_stop"
                },
                "Charge Standard": {
                    "select": "d",
                    "method": "post",
                    "endpoint": "/command/charge_standard"
                },
                "Charge Max": {
                    "select": "m",
                    "method": "post",
                    "endpoint": "/command/charge_max_range"
                },
                "Set Charge Limit": {
                    "select": "l",
                    "method": "post",
                    "endpoint": "/command/set_charge_limit",
                    "parameters": {
                        "percent"
                    },
                    "help": "The percentage the battery will charge until."
                },
            },

            # CLIMATE MENU
            "climate": {
                "Auto Conditioning Start": {
                    "select": "o",
                    "method": "post",
                    "endpoint": "/command/auto_conditioning_start"
                },
                "Auto Conditioning Stop": {
                    "select": "c",
                    "method": "post",
                    "endpoint": "/command/auto_conditioning_stop"
                },
                "Set Temps": {
                    "select": "s",
                    "method": "post",
                    "endpoint": "/command/set_temps",
                    "parameters": {
                        "driver_temp", "passenger_temp"
                    },
                    "help": "The desired temperatures on the celsius."
                },
                "Set Preconditioning Max": {
                    "select": "x",
                    "method": "post",
                    "endpoint": "/command/set_preconditioning_max",
                    "parameters": {
                        "on"
                    },
                    "help": "True to turnb on, false to turn off."
                },
                "Seat Heaters": {
                    "select": "d",
                    "method": "post",
                    "endpoint": "/command/remote_seat_heater_request",
                    "parameters": {
                        "heater", "level"
                    },
                    "help": "Seat (0-5) and level (0-3). Seats: 0-driver, 1-passenger, 2-rear left, 4-rear center, 5-rear right"
                },
                "Steering Wheel": {
                    "select": "m",
                    "method": "post",
                    "endpoint": "/command/remote_steering_wheel_heater_request",
                    "parameters": {
                        "on"
                    },
                    "help": "True to turn on, false to turn off."
                }
            }

        }

    def get(self, level):
        return self.menu[level]

    def show_menu(self, level):
        menu = self.get(level)

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
            if not self.prev_menu:
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
