import httpx
import json
from typing import Literal
from cliqet_api.models.base import BaseModel


DISTANCE_UNIT_TYPES = Literal['Kilometers', 'Miles']

class Locate(BaseModel):
    def locate_device(self, longitude: float, latitude: float) -> dict:
        """
            Get the text location of a device based on coordinates.
            @param longitude - The longitude coordinate of the device
            @param latitude - The latitude coordinate of the device
        """
        data = json.dumps({
            'service': 'locate-device',
            'payload': {
                'longitude': longitude,
                'latitude': latitude
            }
        })

        response = httpx.post(self.locate_url, headers=self.headers, data=data)
        return response.json()


    def autocomplete_suggestions(
            self, 
            search_term: str, 
            limit: int = 5, 
            country_filter: list[str] = []) -> dict:
        """
            Get list of places as text as suggestions for autocompletion of search.
            For country_filter, use 3-letter country codes using ISO 3166.
            @param search_term - The text of the place to search for
            @param limit - The maximum number of results to suggest. Defaults to 5
            @country_filter - The list of countries where suggestions will be based.
        """
        payload = {
            'search_term': search_term,
            'limit': limit
        }

        if country_filter:
            payload['country_filter'] = country_filter
        
        data = json.dumps({
            'service': 'locate-suggestions',
            'payload': payload
        })

        response = httpx.post(self.locate_url, headers=self.headers, data=data)
        return response.json()

    def geocode(self, search_term: str) -> dict:
        """
            Get longitude and latitude coordinates of a location.
            @param search_term - The text of the place being searched
        """
        data = json.dumps({
            'service': 'locate-geocode',
            'payload': {
                'search_term': search_term
            }
        })

        response = httpx.post(self.locate_url, headers=self.headers, data=data)
        return response.json()

    def calculate_routes(
            self, 
            origin: dict, 
            destinations: list[dict], 
            distance_unit: DISTANCE_UNIT_TYPES) -> dict:
        """
            Get distance and time calculations for origin to destination.
            @param origin - The place of origin to based the calculation. It must be a 
                dictionary of the form {'longitude': x, 'latitude': y}
            @param destinations - The list of locations to be calculated with the origin. 
                Each item in the list must be a dictionary of the form 
                {'longitude': x, 'latitude': y, 'id': <unique_identifier>}
            @param distance_unit - The distance unit used for the calculation. Options are 
                'Kilometers' or 'Miles'
        """
        data = json.dumps({
            'service': 'locate-geocode',
            'payload': {
                'origin': origin,
                'destinations': destinations,
                'distance_unit': distance_unit
            }
        })

        response = httpx.post(self.locate_url, headers=self.headers, data=data)
        return response.json()
