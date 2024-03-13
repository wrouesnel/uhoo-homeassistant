import itertools
from datetime import timedelta
import logging

from homeassistant.const import (  # noqa:F401
    ATTR_DEVICE_CLASS,
    ATTR_ICON,
    ATTR_UNIT_OF_MEASUREMENT,
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    CONCENTRATION_PARTS_PER_BILLION,
    CONCENTRATION_PARTS_PER_MILLION,
    PERCENTAGE, EntityCategory,
)

from homeassistant.components.sensor.const import SensorDeviceClass, UnitOfPressure, UnitOfTemperature

# Base component constants
NAME = "uHoo Integration"
MODEL = "uHoo Indoor Air Monitor"
MANUFACTURER = "uHoo"
DOMAIN = "uhoo"
VERSION = "0.0.7"
ISSUE_URL = "https://github.com/wrouesnel/uhoo-homeassistant/issues"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

API_CO = "co"
API_CO2 = "co2"
API_DUST = "dust"
API_HUMIDITY = "humidity"
API_NO2 = "no2"
API_OZONE = "ozone"
API_PRESSURE = "pressure"
API_TEMP = "temp"
API_VOC = "voc"

API_SSID = "ssid"
API_MACADDRESS = "mac_address"

ATTR_LABEL = "label"
ATTR_UNIQUE_ID = "unique_id"
ATTR_ENTITY_CATEGORY = "entity_category"
ATTR_STATE_CLASS = "state_class"
ATTR_POSTPROCESS = "post_process"

LOGGER = logging.getLogger(__package__)

UPDATE_INTERVAL = timedelta(seconds=60)

SENSOR_TYPES = {
    API_SSID: {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:wifi",
        ATTR_UNIT_OF_MEASUREMENT: None,
        ATTR_LABEL: "SSID",
        ATTR_UNIQUE_ID: API_SSID,
        ATTR_ENTITY_CATEGORY: EntityCategory.DIAGNOSTIC,
        ATTR_STATE_CLASS: None,
    },
    API_MACADDRESS: {
        ATTR_DEVICE_CLASS: None,
        ATTR_ICON: "mdi:hexadecimal",
        ATTR_UNIT_OF_MEASUREMENT: None,
        ATTR_LABEL: "MAC Address",
        ATTR_UNIQUE_ID: API_MACADDRESS,
        ATTR_ENTITY_CATEGORY: EntityCategory.DIAGNOSTIC,
        ATTR_STATE_CLASS: None,
        ATTR_POSTPROCESS: lambda v: ":".join( "".join(t) for t in itertools.pairwise(v) )
    },
    API_CO: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.CO,
        ATTR_ICON: "mdi:molecule-co",
        ATTR_UNIT_OF_MEASUREMENT: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_LABEL: "Carbon monoxide",
        ATTR_UNIQUE_ID: API_CO,
    },
    API_CO2: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.CO2,
        ATTR_ICON: "mdi:molecule-co2",
        ATTR_UNIT_OF_MEASUREMENT: CONCENTRATION_PARTS_PER_MILLION,
        ATTR_LABEL: "Carbon dioxide",
        ATTR_UNIQUE_ID: API_CO2,
    },
    API_DUST: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.PM25,
        ATTR_ICON: "mdi:blur",
        ATTR_UNIT_OF_MEASUREMENT: CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        ATTR_LABEL: "PM2.5",
        ATTR_UNIQUE_ID: API_DUST,
    },
    API_HUMIDITY: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.HUMIDITY,
        ATTR_ICON: "mdi:water-percent",
        ATTR_UNIT_OF_MEASUREMENT: PERCENTAGE,
        ATTR_LABEL: "Humidity",
        ATTR_UNIQUE_ID: API_HUMIDITY,
    },
    API_NO2: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.NITROGEN_DIOXIDE,
        ATTR_ICON: "mdi:cloud",
        ATTR_UNIT_OF_MEASUREMENT: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_LABEL: "Nitrogen dioxide",
        ATTR_UNIQUE_ID: API_NO2,
    },
    API_OZONE: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.OZONE,
        ATTR_ICON: "mdi:cloud",
        ATTR_UNIT_OF_MEASUREMENT: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_LABEL: "Ozone",
        ATTR_UNIQUE_ID: API_OZONE,
    },
    API_PRESSURE: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.PRESSURE,
        ATTR_ICON: "mdi:gauge",
        ATTR_UNIT_OF_MEASUREMENT: UnitOfPressure.HPA,
        ATTR_LABEL: "Air pressure",
        ATTR_UNIQUE_ID: API_PRESSURE,
    },
    API_TEMP: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.TEMPERATURE,
        ATTR_ICON: "mdi:thermometer",
        ATTR_UNIT_OF_MEASUREMENT: UnitOfTemperature.CELSIUS,
        ATTR_LABEL: "Temperature",
        ATTR_UNIQUE_ID: API_TEMP,
    },
    API_VOC: {
        ATTR_DEVICE_CLASS: SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS,
        ATTR_ICON: "mdi:cloud",
        ATTR_UNIT_OF_MEASUREMENT: CONCENTRATION_PARTS_PER_BILLION,
        ATTR_LABEL: "Total volatile organic compounds",
        ATTR_UNIQUE_ID: API_VOC,
    },
}


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
