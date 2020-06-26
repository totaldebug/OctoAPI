from urllib.parse import urlencode

import requests


class RequestAPI:
    def __init__(
        self, host_url: str, api_key: str,
    ):
        """Constructor requires Host-URL and API-KEY

            Args:
                host_url (str): Host url to sonarr.
                api_key: API key from Sonarr. You can find this
        """
        self.host_url = "https://api.octopus.energy/v1"
        self.api_key = api_key
        self.session = requests.Session()
        self.auth = None

def request_get(self, path, params=None):
        """
        Make a GET HTTP request
        """
        if params is None:
            params = {}
        request_url = self.host_url + path
        try:
            response = self.session.get(request_url, auth=self.api_key, params=params)
        except requests.RequestException as e:
            raise self.DataUnavailable("Network exception") from e

        if response.status_code != 200:
            raise self.DataUnavailable("Unexpected response status (%s)" % response.status_code)

        return response.json()
