#!/usr/bin/python

# https://tesla-api.timdorr.com/api-basics/authentication
# https://www.teslaapi.io/authentication/oauth
# http://docs.python-requests.org/en/master/user/quickstart/

import requests
import json
import pprint

from os import environ

pp = pprint.PrettyPrinter(indent=4)


class TeslaAPI:
    def __init__(self):
        # Enter your Tesla.com credentials
        self.email = "your@email.com"
        self.password = "yourPassword123"
        # If you know your access_token, you can enter it here or set as ENV variable
        self.access_token = None

        # App keys
        self.client_id = "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384"
        self.client_secret = "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3"

        self.get = 'GET'
        self.post = 'POST'

        self.base_url = "https://owner-api.teslamotors.com/"
        self.base_api = "api/1/vehicles/"
        self.headers = None
        self.vehicle_id = ''

        self.remove = ['__init__', 'set_headers', 'get_access_token', 'api_call', 'set_vehicle_id']

        self.menu = """
    Statuses                        Commands                        Coming Soon
    --------                        --------                        -----------
    1 - get vehicle data            10 - wake up                    30 - remote start
    2 - get charge state            11 - honk horn                  31 - trigger homelink
    3 - get climate state           12 - flash lights               32 - speed limit (4)
    4 - get drive state             13 - door unlock                33 - valet mode (2)
    5 - get gui settings            14 - door lock                  34 - sentry mode
    6 - get vehicle state           15 - open charge port           35 - trunk control
    7 - get vehicle config          16 - close charge port          36 - window control
    8 - get mobile enabled          17 - start charging             37 - sun roof control
    9 - get nearby chargers         18 - stop charging              38 - charge limit set
                                    19 - set charge standard        39 - set temps (4)
                                    20 - set charge max             40 - media (7 endpoints)
                                    21 - conditioning start         41 - sharing
    99 - EXIT                       22 - conditioning stop          42 -software update (2)
            """

        self.menu_items = {1: ['get_vehicle_data', self.get, '/vehicle_data'],
                           2: ['get_charge_state', self.get, '/data_request/charge_state'],
                           3: ['get_climate_state', self.get, '/data_request/climate_state'],
                           4: ['get_drive_state', self.get, '/data_request/drive_state'],
                           5: ['get_gui_settings', self.get, '/data_request/gui_settings'],
                           6: ['get_vehicle_state', self.get, '/data_request/vehicle_state'],
                           7: ['get_vehicle_config', self.get, '/data_request/vehicle_config'],
                           8: ['get_mobile_enabled', self.get, '/mobile_enabled'],
                           9: ['get_nearby_chargers', self.get, '/nearby_charging_sites'],
                           10: ['wake_up', self.post, '/wake_up'], 11: ['honk_horn', self.post, '/command/honk_horn'],
                           12: ['flash_lights', self.post, '/command/flash_lights'],
                           13: ['door_unlock', self.post, '/command/door_unlock'],
                           14: ['door_lock', self.post, '/command/door_lock'],
                           15: ['open_charge_port', self.post, '/command/charge_port_door_open'],
                           16: ['close_charge_port', self.post, '/command/charge_port_door_close'],
                           17: ['start_charging', self.post, '/command/charge_start'],
                           18: ['stop_charging', self.post, '/command/charge_stop'],
                           19: ['set_charge_standard', self.post, '/command/charge_standard'],
                           20: ['set_charge_max', self.post, '/command/charge_max_range'],
                           21: ['conditioning_start', self.post, '/command/auto_conditioning_start'],
                           22: ['conditioning_stop', self.post, '/command/auto_conditioning_stop']}

    def set_headers(self, access_token):
        self.headers = {'Authorization': 'Bearer ' + access_token + ''}

    def get_access_token(self):
        """
        Obtain an access token using email / password from above
        """
        if self.access_token:
            self.set_headers(self.access_token)
            return self.access_token
        elif environ.get('TESLA_API_TOKEN') is not None:
            self.set_headers(environ.get('TESLA_API_TOKEN'))
            return environ.get('TESLA_API_TOKEN')
        else:
            payload = {'grant_type': 'password', 'client_id': self.client_id, 'client_secret': self.client_secret,
                       'email': self.email, 'password': self.password}
            api_response = requests.post(self.base_url + "oauth/token", data=payload)
            response_json = json.loads(api_response.text)
            self.set_headers(response_json["access_token"])

            pp.pprint(api_response)
            return response_json["access_token"]

    def api_call(self, method, endpoint=''):
        print('\nMaking Tesla API call to ' + endpoint)
        if method == self.get:
            api_response = requests.get(self.base_url + self.base_api + self.vehicle_id + endpoint,
                                        headers=self.headers)
        elif method == self.post:
            api_response = requests.post(self.base_url + self.base_api + self.vehicle_id + endpoint,
                                         headers=self.headers)
        else:
            return False

        response_json = json.loads(api_response.text)
        return response_json

    def set_vehicle_id(self):
        api_response = self.api_call(self.get)
        self.vehicle_id = str(api_response["response"][0]["id"])

        print(f'Your vehicle ID: {self.vehicle_id}\n')
        pp.pprint(api_response)

        return api_response['response'][0]['state']

    def get_vehicle_data(self):
        return self.api_call(self.get, '/vehicle_data')

    def print_menu(self):
        print(self.menu)

    def run_command(self):
        selection = input("Enter your command #:")
        selection = int(selection)

        if selection == 99:
            print('Goodbye')
            return True
        elif selection < len(self.menu_items):
            function_name, method, endpoint = self.menu_items[selection]
            result = self.api_call(method, endpoint)
            pp.pprint(result)
        else:
            print('Invalid option, pls try again, 99 to exit')

        return False


tesla = TeslaAPI()
api_token = tesla.get_access_token()
vehicle_state = tesla.set_vehicle_id()

if vehicle_state != 'online':
    print('Your vehicle state is ' + vehicle_state + '\nAttempting to wake it up')
    response = tesla.api_call(tesla.post, '/wake_up')
    vehicle_state = tesla.set_vehicle_id()
    if vehicle_state != 'online':
        print(
            'Unable to wake up vehicle. Please use the app or try opening the doors or putting it into drive then back into park.')

if vehicle_state == 'online':
    pp.pprint(tesla.get_vehicle_data())

done = False
while not done:
    tesla.print_menu()
    done = tesla.run_command()
