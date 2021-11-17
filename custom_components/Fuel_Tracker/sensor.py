"""
Fuel Tracker for Home Assistant
------------------------------------------------------------
%   Description: Sensor script for tracking fuel
%   Author: J.G.Aguado
%   Date of creation: 16/11/2021
------------------------------------------------------------
"""

import logging

import csv
import json
from datetime import datetime, date
from urllib.request import urlopen
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_API_KEY, CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

DOMAIN = "sensor"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required("latitude"): cv.string,
        vol.Required("longitude"): cv.string,
        vol.Required("fuel"): cv.string,
        vol.Required(CONF_NAME): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the fuel tracker sensor."""

    _LOGGER.info("init sensor")
    name = config.get(CONF_NAME)
    latitude = config.get("latitude")
    longitude = config.get("longitude")
    fuel = config.get("fuel")

    fn = FuelData(name, latitude, longitude, fuel)

    if not fn:
        _LOGGER.error("Unable to create the Fuel tracker sensor")
        return

    add_entities([FuelSensor(hass, fn)], True)


class FuelSensor(Entity):
    def __init__(self, hass, fn):
        self._hass = hass
        self.data = fn

    @property
    def name(self):
        """Return the name of the sensor."""
        return "{}".format(self.data.name)

    @property
    def state(self):
        """Return the state of the device."""
        return self.data.attr['sortPrice']

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.data.attr

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "€"
        
    @property
    def icon(self):
        return "mdi:fuel"

    def update(self):
        self.data.get_price()


class FuelData:
    def __init__(self, name, latitude, longitude, fuel):
        self.name = name
        self.attr = {}
        self.latitude = latitude
        self.longitude = longitude
        self.fuel = fuel
        
        try:
            # create the fuel tracking object
            self.get_price()
        except:
            pass

    def get_price(self):
        url = "https://en.tankbillig.in/index.php?long=" + str(self.longitude) + "&lat=" + str(self.latitude) + "&show=1&treibstoff=" + self.fuel + "&switch#0"

        page = urlopen(url)
        html = page.read().decode("utf-8")
        start_results = html.find("results = [{")
        end_results = html[start_results:].find("}],")
        results = html[start_results + 10:start_results + end_results + 2]
        results = json.loads(results)
        min_dist = 100
        for station in results:
            dist = station['distance']
            if dist < min_dist:
                closest_station = station
                min_dist = dist

        self.attr = closest_station
        
