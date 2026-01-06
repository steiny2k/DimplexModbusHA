"""Binary sensors for Dimplex WPM."""

from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DEVICE_MANUFACTURER, DEVICE_NAME, DOMAIN

FAULT_DESCRIPTION = BinarySensorEntityDescription(
    key="fault_active",
    translation_key="fault_active",
    device_class=BinarySensorDeviceClass.PROBLEM,
)

LOCK_DESCRIPTION = BinarySensorEntityDescription(
    key="lock_active",
    translation_key="lock_active",
    device_class=BinarySensorDeviceClass.PROBLEM,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up binary sensors from config entry."""
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]

    entities: list[BinarySensorEntity] = [
        DimplexBinarySensor(coordinator, entry, FAULT_DESCRIPTION),
        DimplexBinarySensor(coordinator, entry, LOCK_DESCRIPTION),
    ]
    async_add_entities(entities)


class DimplexBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Representation of a Dimplex binary sensor."""

    entity_description: BinarySensorEntityDescription

    def __init__(self, coordinator, entry: ConfigEntry, description) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_has_entity_name = True
        self._attr_translation_key = description.translation_key
        self._attr_unique_id = f"{entry.entry_id}_{description.key}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "manufacturer": DEVICE_MANUFACTURER,
            "name": DEVICE_NAME,
        }

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data
        if not data:
            return None
        return data["derived"].get(self.entity_description.key)
