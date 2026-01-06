"""Constants for the Dimplex WPM integration."""

from __future__ import annotations

from typing import Final

DOMAIN: Final = "dimplex_wpm"

DEFAULT_PORT: Final = 502
DEFAULT_UNIT_ID: Final = 1
DEFAULT_SCAN_INTERVAL: Final = 30
DEFAULT_TIMEOUT: Final = 5

CONF_HOST: Final = "host"
CONF_PORT: Final = "port"
CONF_UNIT_ID: Final = "unit_id"
CONF_SCAN_INTERVAL: Final = "scan_interval"
CONF_TIMEOUT: Final = "timeout"
CONF_REGISTER_STRATEGY: Final = "register_strategy"
CONF_ENABLE_WRITE_ENTITIES: Final = "enable_write_entities"
CONF_ENABLE_EMS: Final = "enable_ems_entities"
CONF_ENABLE_BMS_TEMP: Final = "enable_bms_temp"
CONF_ENABLE_EXTERNAL_LOCK: Final = "enable_external_lock"

REGISTER_STRATEGY_AUTO: Final = "auto"
REGISTER_STRATEGY_HOLDING: Final = "holding"
REGISTER_STRATEGY_INPUT: Final = "input"

REGISTER_STRATEGY_MAP: Final = {
    REGISTER_STRATEGY_AUTO: REGISTER_STRATEGY_AUTO,
    REGISTER_STRATEGY_HOLDING: REGISTER_STRATEGY_HOLDING,
    REGISTER_STRATEGY_INPUT: REGISTER_STRATEGY_INPUT,
}

REG_OUTDOOR_TEMPERATURE: Final = 1
REG_RETURN_TEMPERATURE: Final = 2
REG_DHW_TEMPERATURE: Final = 3
REG_FLOW_TEMPERATURE: Final = 5
REG_RETURN_SETPOINT_TEMPERATURE: Final = 53

REG_STATUS_CODE: Final = 103
REG_LOCK_CODE: Final = 104
REG_FAULT_CODE: Final = 105
REG_SENSOR_ERROR_CODE: Final = 106

REG_SG_READY_MODE: Final = 5167

# Initial, extensible mappings for status, lock, and fault codes. These can be
# expanded iteratively as users report additional codes.
STATUS_MAP: Final = {
    0: "Idle",
    1: "Heating",
    2: "Domestic hot water",
    3: "Cooling",
    4: "Defrost",
}

LOCK_MAP: Final = {
    0: "No lock",
    1: "Volume flow lock",
    2: "Safety temperature limiter",
    3: "High pressure",
    4: "Low pressure",
    5: "Flow switch",
    6: "Compressor protection",
    7: "Antifreeze protection",
    8: "Heating curve lock",
    9: "Legionella cycle",
    10: "Fault",
}

FAULT_MAP: Final = {
    0: "No fault",
    1: "High pressure fault",
    2: "Low pressure fault",
    3: "Flow switch fault",
    4: "Sensor fault",
    5: "Compressor fault",
}

SG_READY_MAP: Final = {
    0: "Hardware",
    10: "Yellow",
    11: "Green",
    12: "Red",
    13: "Deep Green",
}

SG_READY_REVERSE: Final = {value: key for key, value in SG_READY_MAP.items()}

DEVICE_MANUFACTURER: Final = "Dimplex"
DEVICE_NAME: Final = "Dimplex WPM"
