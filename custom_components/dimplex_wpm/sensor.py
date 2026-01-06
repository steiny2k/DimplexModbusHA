"""Sensor entities for Dimplex WPM."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DEVICE_MANUFACTURER,
    DEVICE_NAME,
    DOMAIN,
    REG_DHW_TEMPERATURE,
    REG_FLOW_TEMPERATURE,
    REG_OUTDOOR_TEMPERATURE,
    REG_LOCK_CODE,
    REG_FAULT_CODE,
    REG_RETURN_SETPOINT_TEMPERATURE,
    REG_RETURN_TEMPERATURE,
    REG_SENSOR_ERROR_CODE,
    REG_STATUS_CODE,
)


@dataclass
class DimplexSensorEntityDescription(SensorEntityDescription):
    """Describes Dimplex sensor entity."""

    value_fn: Callable[[dict[str, Any]], Any] | None = None
    data_key: str | None = None
    register: int | None = None


SENSOR_DESCRIPTIONS: tuple[DimplexSensorEntityDescription, ...] = (
    DimplexSensorEntityDescription(
        key="outdoor_temperature",
        translation_key="outdoor_temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data["derived"].get("outdoor_temperature"),
    ),
    DimplexSensorEntityDescription(
        key="return_temperature",
        translation_key="return_temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data["derived"].get("return_temperature"),
    ),
    DimplexSensorEntityDescription(
        key="return_setpoint_temperature",
        translation_key="return_setpoint_temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data["derived"].get("return_setpoint_temperature"),
    ),
    DimplexSensorEntityDescription(
        key="flow_temperature",
        translation_key="flow_temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data["derived"].get("flow_temperature"),
    ),
    DimplexSensorEntityDescription(
        key="dhw_temperature",
        translation_key="dhw_temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data["derived"].get("dhw_temperature"),
    ),
    DimplexSensorEntityDescription(
        key="status_code",
        translation_key="status_code",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["raw"].get(REG_STATUS_CODE),
        register=REG_STATUS_CODE,
    ),
    DimplexSensorEntityDescription(
        key="status_text",
        translation_key="status_text",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["derived"].get("status_text"),
    ),
    DimplexSensorEntityDescription(
        key="lock_code",
        translation_key="lock_code",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["raw"].get(REG_LOCK_CODE),
    ),
    DimplexSensorEntityDescription(
        key="lock_text",
        translation_key="lock_text",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["derived"].get("lock_text"),
    ),
    DimplexSensorEntityDescription(
        key="fault_code",
        translation_key="fault_code",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["raw"].get(REG_FAULT_CODE),
    ),
    DimplexSensorEntityDescription(
        key="fault_text",
        translation_key="fault_text",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["derived"].get("fault_text"),
    ),
    DimplexSensorEntityDescription(
        key="sensor_error_code",
        translation_key="sensor_error_code",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["raw"].get(REG_SENSOR_ERROR_CODE),
    ),
    DimplexSensorEntityDescription(
        key="sensor_error_text",
        translation_key="sensor_error_text",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["derived"].get("sensor_error_text"),
    ),
    DimplexSensorEntityDescription(
        key="sg_ready_text",
        translation_key="sg_ready_text",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data["derived"].get("sg_ready_text"),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up sensors from config entry."""
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]

    entities: list[SensorEntity] = []
    for description in SENSOR_DESCRIPTIONS:
        entities.append(DimplexSensor(coordinator, entry, description))

    async_add_entities(entities)


class DimplexSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Dimplex sensor."""

    entity_description: DimplexSensorEntityDescription

    def __init__(
        self,
        coordinator,
        entry: ConfigEntry,
        description: DimplexSensorEntityDescription,
    ) -> None:
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
    def native_value(self):
        data = self.coordinator.data
        if not data or not self.entity_description.value_fn:
            return None
        return self.entity_description.value_fn(data)
