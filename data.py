def define_menu():
    return {
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
            "Remote Start": {
                "select": "s",
                "method": "post",
                "endpoint": "/command/remote_start_drive",
                "parameters": {
                    "password"
                },
                "help": "The password for the authenticated tesla.com account.\n"
                        "Endpoint does not appear to work properly\n"
                        "Note: Your password will show on this screen in clear-text."
            },
            "Homelink": {
                "select": "l",
                "method": "post",
                "endpoint": "/command/trigger_homelink",
                "parameters": {
                    "lat", "lon"
                },
                "help": "Current latitude & longitude in decimal degrees, i.e. 40.123456, -82.123456"
            },
            "Speed Limit": {
                "select": "p",
                "method": "menu",
                "endpoint": "speed limit"
            },
            "Valet Mode": {
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
                "help": "True to turn on, False to turn off."
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
            "Media": {
                "select": "m",
                "method": "menu",
                "endpoint": "media"
            },
            "Sharing": {
                "select": "a",
                "method": "post",
                "endpoint": "/command/share",
                "parameters": {
                    "type", "locale", "timestamp_ms", "value"
                },
                "help": "Does not yet work, but you can try\n"
                        "type: Must be share_ext_content_raw.\n"
                        "locale: en-US\n"
                        "timestamp_ms: The current UNIX timestamp.\n"
                        "value: JSON in format like:\n"
                        '{"android.intent.extra.TEXT": "123 Main St, City, ST 12345\n\nhttps://goo.gl/maps/X"}\n'
            },
            "Software Updates": {
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
                "help": "True to turnb on, False to turn off."
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
                "help": "True to turn on, False to turn off."
            }
        },

        # UPDATES MENU
        "software updates": {
            "Schedule Software Update": {
                "select": "u",
                "method": "post",
                "endpoint": "/command/schedule_software_update",
                "parameters": {
                    "offset_sec"
                },
                "help": "How many seconds in the future to schedule the update. Set to 0 for immediate install."
            },
            "Cancel Software Update": {
                "select": "c",
                "method": "post",
                "endpoint": "/command/cancel_software_update"
            },
        },

        # SPEED LIMITS MENU
        "speed limit": {
            "Set maximum speed limit": {
                "select": "m",
                "method": "post",
                "endpoint": "/command/speed_limit_set_limit",
                "parameters": {
                    "limit_mph"
                },
                "help": "The speed limit in MPH. Must be between 50-90."
            },
            "Activate speed limit mode": {
                "select": "a",
                "method": "post",
                "endpoint": "/command/speed_limit_activate",
                "parameters": {
                    "pin"
                },
                "help": "The existing PIN, if previously set, or a new 4 digit PIN."
            },
            "Deactivate speed limit mode": {
                "select": "d",
                "method": "post",
                "endpoint": "/command/speed_limit_deactivate",
                "parameters": {
                    "pin"
                },
                "help": "The existing PIN used to activate speed limit mode."
            },
            "Clear Speed Limit PIN": {
                "select": "c",
                "method": "post",
                "endpoint": "/command/speed_limit_clear_pin",
                "parameters": {
                    "pin"
                },
                "help": "The existing PIN used to activate speed limit mode."
            },

        },

        # VALET MENU
        "valet mode": {
            "Set Valet Mode": {
                "select": "v",
                "method": "post",
                "endpoint": "/command/set_valet_mode",
                "parameters": {
                    "on", "password"
                },
                "help": "on: true to activate, false to deactivate\n"
                        "A PIN to deactivate Valet Mode. Please see note about the password parameter."
            },
            "Reset Valet PIN": {
                "select": "r",
                "method": "post",
                "endpoint": "/command/reset_valet_pin"
            },
        },

        # MEDIA MENU
        "media": {
            "Toggle Playback": {
                "select": "p",
                "method": "post",
                "endpoint": "/command/media_toggle_playback",
            },
            "Next Track": {
                "select": "n",
                "method": "post",
                "endpoint": "/command/media_next_track"
            },
            "Prev Track": {
                "select": "m",
                "method": "post",
                "endpoint": "/command/media_prev_track"
            },
            "Next Fav": {
                "select": "f",
                "method": "post",
                "endpoint": "/command/media_next_fav"
            },
            "Prev Fav": {
                "select": "g",
                "method": "post",
                "endpoint": "/command/media_prev_fav"
            },
            "Volume Up": {
                "select": "u",
                "method": "post",
                "endpoint": "/command/media_volume_up"
            },
            "Volume Down": {
                "select": "d",
                "method": "post",
                "endpoint": "/command/media_volume_down"
            }
        },
    }


def set_disclaimer():
    return """
        This application allows you to retrieve data and perform actions on a Tesla automobile.
        The software is provided as-is, without claim of correctness or with warranty.
        Anything you choose to do with this software is at your own risk.
        
        All source code is freely examinable and it is suggested you do so prior to using it.
        
        Please be very careful when using your tesla.com username/password and/or api token.
        Be sure never to share them with others and never upload files containing them to public locations.
        
        If you are unsure about anything, please do not use this software!        
        """
