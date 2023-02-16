import requests
from credentials import phillipshue


class Phillipshue_on:
    """
    Turn on Phillipshue Lights
    """

    def __init__(self):

        username = phillipshue.username
        ip = phillipshue.ip
        self.base_url = f'https://{ip}/api/{username}'

    def lights(self):

        def light1(self):

            url = f'{self.base_url}/lights/1/state'
            data = {"on": True, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        def light2(self):

            url = f'{self.base_url}/lights/2/state'
            data = {"on": True, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        def light3(self):

            url = f'{self.base_url}/lights/11/state'
            data = {"on": True, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        return light1(self), light2(self), light3(self)


class Phillipshue_off:
    """
    Turn off Phillipshue Lights
    """

    def __init__(self):

        username = phillipshue.username
        ip = phillipshue.ip
        self.base_url = f'https://{ip}/api/{username}'

    def lights(self):

        def light1(self):

            url = f'{self.base_url}/lights/1/state'
            data = {"on": False, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        def light2(self):

            url = f'{self.base_url}/lights/2/state'
            data = {"on": False, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        def light3(self):

            url = f'{self.base_url}/lights/11/state'
            data = {"on": False, "sat": 11, "bri": 254, "hue": 11013}

            response = requests.put(url, verify=False, json=data)

            return response

        return light1(self), light2(self), light3(self)


class bedroomLightsON:
    """
    Turn on Phillipshue Lights for bedroom
    """

    def __init__(self):

        username = phillipshue.username
        ip = phillipshue.ip
        self.base_url = f'https://{ip}/api/{username}'

    def lights(self):

        def light1(self):

            url = f'{self.base_url}/lights/8/state'
            data = {"on": True, "sat": 140, "bri": 254, "hue": 8417}

            response = requests.put(url, verify=False, json=data)

            return response

        def light2(self):

            url = f'{self.base_url}/lights/9/state'
            data = {"on": True, "sat": 140, "bri": 254, "hue": 8417}

            response = requests.put(url, verify=False, json=data)

            return response

        def light3(self):

            url = f'{self.base_url}/lights/10/state'
            data = {"on": True, "sat": 140, "bri": 254, "hue": 8417}

            response = requests.put(url, verify=False, json=data)

            return response

        return light1(self), light2(self), light3(self)

class bedroomLightsOff:
    """
    Turn off Phillipshue Lights for bedroom
    """

    def __init__(self):

        username = phillipshue.username
        ip = phillipshue.ip
        self.base_url = f'https://{ip}/api/{username}'

    def lights(self):

        def light1(self):

            url = f'{self.base_url}/lights/8/state'
            data = {"on": True, "sat": 140, "bri": 254, "hue": 8417}

            response = requests.put(url, verify=False, json=data)

            return response

        def light2(self):

            url = f'{self.base_url}/lights/9/state'
            data = {"on": True, "sat": 140, "bri": 254, "hue": 8417}

            response = requests.put(url, verify=False, json=data)

            return response

        def light3(self):

            url = f'{self.base_url}/lights/10/state'
            data = {"on": True, "sat": 140, "bri": 254, "hue": 8417}

            response = requests.put(url, verify=False, json=data)

            return response

        return light1(self), light2(self), light3(self)
