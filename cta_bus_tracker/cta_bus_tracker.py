import os
import json
from copy import copy

import requests
from dotenv import load_dotenv


import pprint
pp = pprint.PrettyPrinter(indent=4)


load_dotenv()


class BusTracker():
    def __init__(self):
        self.base_url = "http://www.ctabustracker.com/bustime/api/v2/"
        self.default_payload = {
            "key":      os.environ["CTA_API_KEY"],
            "format":   "json",
            }


    def _make_request(self, endpoint, payload):
        url = self.base_url + endpoint
        response = requests.get(url, params=payload)
        content = json.loads(response.content)
        assert(len(content.keys()) == 1)
        content = content["bustime-response"]
        return content
    

    def get_system_time(self):
        content = self._make_request("gettime", self.default_payload)
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
            list(str, int):  routes = ["X3", 4, 20]

            BUG: While the documentation states you can request up to ten  
            routes, it seems to only return busses for the last route in the
            list
        """
        payload = copy(self.default_payload)

        if len(vehicle_ids):
            payload["vid"] = vehicle_ids            

        elif len(routes):
            payload["rt"] = routes

        content = self._make_request("getvehicles", payload)
        content = content["vehicle"]
        return content


    def get_directions(self, route_designator):
        """
        """
        payload = copy(self.default_payload)
        payload["rt"] = route_designator
        content = self._make_request("getdirections", payload)
        print(content)


if __name__ == "__main__":
    tracker = BusTracker()
    busses = tracker.get_vehicles(routes=["X9", 4, 66])
    print(busses)