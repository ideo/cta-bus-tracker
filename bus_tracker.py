import os
import json

import requests
from dotenv import load_dotenv


load_dotenv()


class BusTracker():
    def __init__(self):
        self.base_url = "http://www.ctabustracker.com/bustime/api/v2/"


    def _make_request(self, url, payload):
        response = requests.get(url, params=payload)
        content = json.loads(response.content)
        return content
    

    def get_system_time(self):
        url = self.base_url + "gettime"
        payload = {
            "key":      os.environ["CTA_API_KEY"],
            "format":   "json",
            }
        content = self._make_request(url, payload)
        print(content)


    def get_vehicles(self, vehicle_ids=[], routes=[]):
        """
        Return the position of all vehicle specified by their ID or the position
        of all vehicles on the routes specified by their number. May request 
        either `vehicles_ids` or `routes`, but not both. A maximum of 10
        identifiers can be specified.
        --
        Example inputs:
            list(int):  vehicle_ids = [509, 392, 201, 4367]
            list(str):  routes = ["X3", "4", "20"]
        """
        url = self.base_url + "getvehicles"

        if len(vehicle_ids):
            payload = {
                "key":      os.environ["CTA_API_KEY"],
                "format":   "json",
                "vid":      vehicle_ids,
            }

        elif len(routes):
            payload = {
                "key":      os.environ["CTA_API_KEY"],
                "format":   "json",
                "rt":       routes,
                }

        content = self._make_request(url, payload)
        print(content)


if __name__ == "__main__":
    tracker = BusTracker()
    tracker.get_vehicles(routes=[66])