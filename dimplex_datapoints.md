# Dimplex WPM / NWPM – Home Assistant Integration  
## Datapoint specification list (device model driven)

This document is intended to be used as **implementation requirements** for a custom Home Assistant integration (`dimplex_wpm`) with a functional device model (sub-devices: HC1/HC2/HC3/DHW/Energy/Solar/Ventilation/Smart Grid).

Each datapoint below includes:
- `key` – stable logical identifier (basis for `unique_id`)
- `module` – target sub-device
- `platform` – `sensor` / `binary_sensor` / `select` / `number`
- `modbus` – `input` / `holding` / `coil` (Modbus register bank)
- `address`, `data_type`, `scale`, `unit`
- `rw` – `read` / `read_write`
- `entity_category` – `diagnostic` or null
- `enabled_by_default`

> Notes  
> 1) Some “settings” were previously implemented as read-only sensors in YAML; in an integration they are better represented as `number`/`select` **only if** the firmware allows write.  
> 2) There is a known conflict in the earlier YAML (Solar Collector Temperature vs HC3 Return Temperature at address 10). In this list Solar Collector Temperature is marked `TODO` until confirmed.  
> 3) Inverter frequency register is unknown in our current material and is marked `TODO`.

---

## Datapoints (YAML; YAML is a superset of JSON)

```yaml
datapoints:

  # =========================
  # D0: Controller / Status
  # =========================
  - key: controller.status_code
    module: controller
    platform: sensor
    modbus: input
    address: 103
    data_type: uint16
    scale: 1
    unit: null
    rw: read
    entity_category: diagnostic
    enabled_by_default: true

  - key: controller.lock_code
    module: controller
    platform: sensor
    modbus: input
    address: 104
    data_type: uint16
    scale: 1
    unit: null
    rw: read
    entity_category: diagnostic
    enabled_by_default: true

  - key: controller.fault_code
    module: controller
    platform: sensor
    modbus: input
    address: 105
    data_type: uint16
    scale: 1
    unit: null
    rw: read
    entity_category: diagnostic
    enabled_by_default: true

  - key: controller.sensor_error_code
    module: controller
    platform: sensor
    modbus: input
    address: 106
    data_type: uint16
    scale: 1
    unit: null
    rw: read
    entity_category: diagnostic
    enabled_by_default: true

  - key: controller.fault_active
    module: controller
    platform: binary_sensor
    derived_from: controller.fault_code
    rw: read
    device_class: problem
    entity_category: diagnostic
    enabled_by_default: true

  - key: controller.lock_active
    module: controller
    platform: binary_sensor
    derived_from: controller.lock_code
    rw: read
    device_class: problem
    entity_category: diagnostic
    enabled_by_default: true

  - key: controller.operating_mode_code
    module: controller
    platform: sensor
    modbus: input
    address: 5015
    data_type: uint16
    scale: 1
    unit: null
    rw: read
    entity_category: diagnostic
    enabled_by_default: true

  # =========================
  # D0: Core temperatures
  # =========================
  - key: temps.outdoor
    module: controller
    platform: sensor
    modbus: input
    address: 1
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  - key: temps.return
    module: hc1
    platform: sensor
    modbus: input
    address: 2
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  - key: temps.return_setpoint
    module: hc1
    platform: sensor
    modbus: input
    address: 53
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  - key: temps.flow
    module: hc1
    platform: sensor
    modbus: input
    address: 5
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  - key: dhw.temp
    module: dhw
    platform: sensor
    modbus: input
    address: 3
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  - key: dhw.temp_setpoint_live
    module: dhw
    platform: sensor
    modbus: input
    address: 58
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  # =========================
  # D2/D3: HC2 / HC3 return temps
  # =========================
  - key: hc2.return
    module: hc2
    platform: sensor
    modbus: input
    address: 9
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  - key: hc2.return_setpoint
    module: hc2
    platform: sensor
    modbus: input
    address: 54
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  - key: hc3.return
    module: hc3
    platform: sensor
    modbus: input
    address: 10
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  - key: hc3.return_setpoint
    module: hc3
    platform: sensor
    modbus: input
    address: 55
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: true

  # =========================
  # Room temps/humidity (optional)
  # =========================
  - key: rooms.temp_1
    module: controller
    platform: sensor
    modbus: input
    address: 11
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: false

  - key: rooms.temp_2
    module: controller
    platform: sensor
    modbus: input
    address: 12
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: false

  - key: rooms.humidity_1
    module: controller
    platform: sensor
    modbus: input
    address: 13
    data_type: int16
    scale: 0.1
    unit: "%"
    rw: read
    device_class: humidity
    enabled_by_default: false

  - key: rooms.humidity_2
    module: controller
    platform: sensor
    modbus: input
    address: 14
    data_type: int16
    scale: 0.1
    unit: "%"
    rw: read
    device_class: humidity
    enabled_by_default: false

  # =========================
  # Ventilation (optional)
  # =========================
  - key: vent.outdoor_air_temp
    module: ventilation
    platform: sensor
    modbus: input
    address: 120
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: false

  - key: vent.supply_air_temp
    module: ventilation
    platform: sensor
    modbus: input
    address: 121
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: false

  - key: vent.extract_air_temp
    module: ventilation
    platform: sensor
    modbus: input
    address: 122
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: false

  - key: vent.exhaust_air_temp
    module: ventilation
    platform: sensor
    modbus: input
    address: 123
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: false

  - key: vent.supply_fan_speed
    module: ventilation
    platform: sensor
    modbus: input
    address: 125
    data_type: int16
    scale: 1
    unit: "1/min"
    rw: read
    enabled_by_default: false

  - key: vent.extract_fan_speed
    module: ventilation
    platform: sensor
    modbus: input
    address: 126
    data_type: int16
    scale: 1
    unit: "1/min"
    rw: read
    enabled_by_default: false

  - key: vent.level
    module: ventilation
    platform: sensor
    modbus: input
    address: 5034
    data_type: uint16
    scale: 1
    unit: null
    rw: read
    entity_category: diagnostic
    enabled_by_default: false

  - key: vent.boost_time
    module: ventilation
    platform: sensor
    modbus: input
    address: 127
    data_type: uint16
    scale: 1
    unit: "min"
    rw: read
    entity_category: diagnostic
    enabled_by_default: false

  # =========================
  # HC1 settings (candidates for number/select)
  # =========================
  - key: hc1.curve_offset
    module: hc1
    platform: number
    modbus: holding
    address: 5036
    data_type: uint16
    scale: 1
    unit: null
    rw: read_write
    enabled_by_default: false

  - key: hc1.room_temp_setpoint
    module: hc1
    platform: number
    modbus: holding
    address: 46
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: hc1.fixed_flow_setpoint
    module: hc1
    platform: number
    modbus: holding
    address: 5037
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: hc1.heating_curve_end
    module: hc1
    platform: number
    modbus: holding
    address: 5038
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: hc1.hysteresis
    module: hc1
    platform: number
    modbus: holding
    address: 47
    data_type: uint16
    scale: 1
    unit: "K"
    rw: read_write
    enabled_by_default: false

  - key: hc1.cooling_room_setpoint
    module: hc1
    platform: number
    modbus: holding
    address: 5043
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: hc1.cooling_room_setpoint_35at
    module: hc1
    platform: number
    modbus: holding
    address: 5134
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  # =========================
  # HC2/3 settings (combined)
  # =========================
  - key: hc23.circuit_selection
    module: hc2_hc3
    platform: sensor
    modbus: input
    address: 5082
    data_type: uint16
    scale: 1
    unit: null
    rw: read
    entity_category: diagnostic
    enabled_by_default: false

  - key: hc23.heating_curve_end
    module: hc2_hc3
    platform: number
    modbus: holding
    address: 5084
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: hc23.fixed_temperature
    module: hc2_hc3
    platform: number
    modbus: holding
    address: 5085
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: hc23.curve_offset
    module: hc2_hc3
    platform: number
    modbus: holding
    address: 5086
    data_type: uint16
    scale: 1
    unit: null
    rw: read_write
    enabled_by_default: false

  - key: hc23.mixer_run_time
    module: hc2_hc3
    platform: number
    modbus: holding
    address: 5087
    data_type: uint16
    scale: 1
    unit: "min"
    rw: read_write
    enabled_by_default: false

  - key: hc23.mixer_hysteresis
    module: hc2_hc3
    platform: number
    modbus: holding
    address: 93
    data_type: uint16
    scale: 1
    unit: "K"
    rw: read_write
    enabled_by_default: false

  - key: hc23.maximum_temperature
    module: hc2_hc3
    platform: number
    modbus: holding
    address: 5088
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: hc23.cooling_room_setpoint
    module: hc2_hc3
    platform: number
    modbus: holding
    address: 5089
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  # =========================
  # DHW settings
  # =========================
  - key: dhw.hysteresis
    module: dhw
    platform: number
    modbus: holding
    address: 5045
    data_type: uint16
    scale: 1
    unit: "K"
    rw: read_write
    enabled_by_default: false

  - key: dhw.setpoint
    module: dhw
    platform: number
    modbus: holding
    address: 5047
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: dhw.setpoint_min
    module: dhw
    platform: number
    modbus: holding
    address: 5145
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: dhw.setpoint_max
    module: dhw
    platform: number
    modbus: holding
    address: 5048
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  # =========================
  # Pool settings
  # =========================
  - key: pool.hysteresis
    module: pool
    platform: number
    modbus: holding
    address: 5049
    data_type: uint16
    scale: 1
    unit: "K"
    rw: read_write
    enabled_by_default: false

  - key: pool.setpoint
    module: pool
    platform: number
    modbus: holding
    address: 5051
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  # =========================
  # 2nd heat generator settings
  # =========================
  - key: heatgen2.mixer_hysteresis
    module: controller
    platform: number
    modbus: holding
    address: 48
    data_type: uint16
    scale: 1
    unit: "K"
    rw: read_write
    enabled_by_default: false

  - key: heatgen2.parallel_limit_temp
    module: controller
    platform: number
    modbus: holding
    address: 5020
    data_type: uint16
    scale: 1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  - key: heatgen2.mixer_run_time
    module: controller
    platform: number
    modbus: holding
    address: 5021
    data_type: uint16
    scale: 1
    unit: "min"
    rw: read_write
    enabled_by_default: false

  # =========================
  # Energy counters (keep as-is until format verified)
  # =========================
  - key: energy.heating_1_4
    module: energy
    platform: sensor
    modbus: input
    address: 5096
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: energy.heating_5_8
    module: energy
    platform: sensor
    modbus: input
    address: 5097
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: energy.heating_9_12
    module: energy
    platform: sensor
    modbus: input
    address: 5098
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: energy.dhw_1_4
    module: energy
    platform: sensor
    modbus: input
    address: 5099
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: energy.dhw_5_8
    module: energy
    platform: sensor
    modbus: input
    address: 5100
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: energy.dhw_9_12
    module: energy
    platform: sensor
    modbus: input
    address: 5101
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: energy.pool_1_4
    module: energy
    platform: sensor
    modbus: input
    address: 5102
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: energy.pool_5_8
    module: energy
    platform: sensor
    modbus: input
    address: 5103
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: energy.pool_9_12
    module: energy
    platform: sensor
    modbus: input
    address: 5104
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: energy.environment_1_4
    module: energy
    platform: sensor
    modbus: input
    address: 5127
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: energy.environment_5_8
    module: energy
    platform: sensor
    modbus: input
    address: 5128
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: energy.environment_9_12
    module: energy
    platform: sensor
    modbus: input
    address: 5129
    data_type: uint16
    scale: 1
    unit: "kWh"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  # =========================
  # Runtimes (hours)
  # =========================
  - key: runtime.compressor_1
    module: energy
    platform: sensor
    modbus: input
    address: 72
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: runtime.compressor_2
    module: energy
    platform: sensor
    modbus: input
    address: 73
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: runtime.primary_pump_fan
    module: energy
    platform: sensor
    modbus: input
    address: 74
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: true

  - key: runtime.heatgen2
    module: energy
    platform: sensor
    modbus: input
    address: 75
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: runtime.heating_pump_m13
    module: energy
    platform: sensor
    modbus: input
    address: 76
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: runtime.dhw_pump
    module: dhw
    platform: sensor
    modbus: input
    address: 77
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: runtime.immersion_heater
    module: energy
    platform: sensor
    modbus: input
    address: 78
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: runtime.pool_pump
    module: pool
    platform: sensor
    modbus: input
    address: 79
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  - key: runtime.additional_circulation_pump
    module: energy
    platform: sensor
    modbus: input
    address: 71
    data_type: uint16
    scale: 1
    unit: "h"
    rw: read
    state_class: total_increasing
    enabled_by_default: false

  # =========================
  # Solar
  # =========================
  - key: solar.tank_temperature
    module: solar
    platform: sensor
    modbus: input
    address: 23
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: false

  - key: solar.collector_temperature
    module: solar
    platform: sensor
    modbus: input
    address: null
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read
    device_class: temperature
    enabled_by_default: false
    notes: "TODO: confirm correct Modbus address; do not create entity until confirmed."

  # =========================
  # Smart Grid / EMS
  # =========================
  - key: sg.ready_mode
    module: smart_grid
    platform: select
    modbus: holding
    address: 5167
    data_type: uint16
    rw: read_write
    options_map:
      Hardware: 0
      Yellow: 10
      Green: 11
      Red: 12
      Deep Green: 13
    enabled_by_default: true

  - key: sg.input_1
    module: smart_grid
    platform: binary_sensor
    modbus: coil
    address: 3
    rw: read
    enabled_by_default: true

  - key: sg.input_2
    module: smart_grid
    platform: binary_sensor
    modbus: coil
    address: 4
    rw: read
    enabled_by_default: true

  - key: sg.state_from_inputs
    module: smart_grid
    platform: sensor
    derived_from:
      - sg.input_1
      - sg.input_2
    mapping:
      "0,0": Yellow
      "0,1": Red
      "1,0": Green
      "1,1": Deep Green
    rw: read
    enabled_by_default: true

  # Optional (v0.2): EMS power / PV surplus
  - key: ems.heating_power
    module: energy
    platform: sensor
    modbus: input
    address: 5168
    data_type: uint16
    scale: 0.01
    unit: "kW"
    rw: read
    enabled_by_default: false

  - key: ems.electrical_power
    module: energy
    platform: sensor
    modbus: input
    address: 5170
    data_type: uint16
    scale: 0.01
    unit: "kW"
    rw: read
    enabled_by_default: false

  - key: ems.pv_surplus
    module: smart_grid
    platform: number
    modbus: holding
    address: 5182
    data_type: uint16
    scale: 0.01
    unit: "kW"
    rw: read_write
    enabled_by_default: false

  # Optional (v0.2): External lock mode
  - key: controller.external_lock_mode
    module: smart_grid
    platform: select
    modbus: holding
    address: 5130
    data_type: uint16
    rw: read_write
    options_map:
      Hardware: 0
      Not active: 10
      Active: 11
    enabled_by_default: false

  # Optional (v0.2): BMS outdoor temp override
  - key: controller.outdoor_temp_bms
    module: smart_grid
    platform: number
    modbus: holding
    address: 112
    data_type: int16
    scale: 0.1
    unit: "°C"
    rw: read_write
    enabled_by_default: false

  # =========================
  # Outputs (coils) – expose a useful subset by default
  # =========================
  - key: out.compressor_1
    module: controller
    platform: binary_sensor
    modbus: coil
    address: 41
    rw: read
    enabled_by_default: true

  - key: out.compressor_2
    module: controller
    platform: binary_sensor
    modbus: coil
    address: 42
    rw: read
    enabled_by_default: false

  - key: out.primary_pump_fan
    module: controller
    platform: binary_sensor
    modbus: coil
    address: 43
    rw: read
    enabled_by_default: true

  - key: out.dhw_pump
    module: dhw
    platform: binary_sensor
    modbus: coil
    address: 46
    rw: read
    enabled_by_default: false

  - key: out.immersion_heater
    module: controller
    platform: binary_sensor
    modbus: coil
    address: 50
    rw: read
    enabled_by_default: false

  - key: out.pool_pump
    module: pool
    platform: binary_sensor
    modbus: coil
    address: 56
    rw: read
    enabled_by_default: false

  - key: out.general_fault
    module: controller
    platform: binary_sensor
    modbus: coil
    address: 57
    rw: read
    device_class: problem
    enabled_by_default: true

  - key: out.heat_cool_changeover
    module: controller
    platform: binary_sensor
    modbus: coil
    address: 66
    rw: read
    enabled_by_default: false

  - key: out.solar_pump
    module: solar
    platform: binary_sensor
    modbus: coil
    address: 71
    rw: read
    enabled_by_default: false

  # =========================
  # TODO: Inverter frequency (needs confirmed register)
  # =========================
  - key: inverter.frequency
    module: energy
    platform: sensor
    modbus: input
    address: null
    data_type: uint16
    scale: 0.1
    unit: "Hz"
    rw: read
    enabled_by_default: false
    notes: "TODO: confirm Modbus register address for inverter frequency; create entity only after verification."
```

---

## Implementation notes (for Codex)
- Use `key` + `base_id` to derive stable `unique_id`.
- Map `module` → subdevice identifiers, using `via_device` to attach to the root controller device.
- For `derived_from` datapoints: implement as derived entities updated from coordinator data.
- For R/W datapoints: expose only when `enable_write_entities = true` (Options Flow), default OFF for safety.

