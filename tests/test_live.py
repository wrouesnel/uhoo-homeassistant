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
    await async_setup_entry(hass, config_entry=config_entry)