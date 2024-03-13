"""
This file contains a live data test for the pyUHoo plugin. It is useful for finding bugs
where the implementation of the cloud has changed.
"""
import os

import pytest
import pytest_socket

from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from custom_components.uhoo import async_setup_entry, DOMAIN
from custom_components.uhoo.const import SENSOR_TYPES

if os.getenv("UHOO_USERNAME") is None:
    pytest.skip(
        "UHOO_USERNAME not defined, live tests will fail. Skipping.",
        allow_module_level=True,
    )

if os.getenv("UHOO_PASSWORD") is None:
    pytest.skip(
        "UHOO_PASSWORD not defined, live tests will fail. Skipping.",
        allow_module_level=True,
    )

@pytest.mark.enable_socket
async def test_live_availability(hass: HomeAssistant):
    pytest_socket._remove_restrictions()
    config_entry = ConfigEntry(version=1, minor_version=0, domain=DOMAIN, title="uhoo", source="user",
                               data={
                                   CONF_USERNAME: os.getenv("UHOO_USERNAME"),
                                   CONF_PASSWORD: os.getenv("UHOO_PASSWORD"),
                               })

    hass.config_entries._entries[config_entry.entry_id] = config_entry
    await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    states = hass.states.async_all()

    suffixes = {
        "ssid",
        "mac_address",
        "carbon_monoxide",
        "carbon_dioxide",
        "pm2_5",
        "humidity",
        "nitrogen_dioxide",
        "ozone",
        "air_pressure",
        "temperature",
        "total_volatile_organic_compounds",
    }

    # Check that we get states back for at least one device
    sensors = []
    for sensor_suffix in suffixes:
        for state in states:
            if state.entity_id.endswith(sensor_suffix):
                sensors.append(state)

    assert len(sensors) == len(SENSOR_TYPES)
    pass