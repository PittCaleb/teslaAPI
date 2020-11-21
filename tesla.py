import time
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

        self.get = 'get'
        self.post = 'post'

        self.base_url = "https://owner-api.teslamotors.com/"
        self.base_api = "api/1/vehicles/"
        self.headers = None
        self.vehicle_id = ''

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
            if 'your' in self.email or 'your' in self.password:
                print(
                    'You must set email & password or provide token in order for this to work.  Please see the Readme file for more information.')
                return False
            else:
                payload = {'grant_type': 'password', 'client_id': self.client_id, 'client_secret': self.client_secret,
                           'email': self.email, 'password': self.password}
                api_response = requests.post(self.base_url + "oauth/token", data=payload)
                response_json = json.loads(api_response.text)
                self.set_headers(response_json["access_token"])
                return response_json["access_token"]

    def api_call(self, method, endpoint='', payload=''):
        url = self.base_url + self.base_api + self.vehicle_id + endpoint
        print(f'\nMaking Tesla API call. Method: {method} URL: {url}\n')
        if method == self.get:
            api_response = requests.get(url, headers=self.headers)
        elif method == self.post:
            api_response = requests.post(url, headers=self.headers, data=payload)
        else:
            return False

        if api_response.text:
            return json.loads(api_response.text)

        return False

    def set_vehicle_id(self):
        api_response = self.api_call(self.get)
        if api_response:
            self.vehicle_id = str(api_response["response"][0]["id"])
            return api_response['response'][0]['state']
        return False

    def run_command(self, method, endpoint, payload=''):
        result = self.api_call(method, endpoint, payload)
        pp.pprint(result)

    def initiate_communications(self):
        if not self.get_access_token():
            exit()

        vehicle_state = self.set_vehicle_id()

        if vehicle_state != 'online':
            print(f'Your vehicle state is {vehicle_state}\nAttempting to wake it up')
            response = self.api_call(self.post, '/wake_up')
            time.sleep(7)
            vehicle_state = self.set_vehicle_id()
            if not vehicle_state and vehicle_state != 'online':
                print(
                    'Unable to wake up vehicle. Please use the app or try opening the doors or putting it into drive then back into park.')
                return False

        if vehicle_state == 'online':
            return True

        return False
