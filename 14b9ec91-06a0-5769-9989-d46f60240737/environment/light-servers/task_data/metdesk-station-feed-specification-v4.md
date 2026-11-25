# MetDesk Fellside - Northfell station forecast feed, specification v4

Applies from 1 March 2025 (contract schedule B rev 4). Supersedes v3.

## Delivery
- Service: MetDesk station forecast service (OpenWeather-compatible API surface: `get_forecast` by station name or coordinates, `get_current_weather`).
- Stations on the Northfell contract: Skelwith Edge, Coldfell Moor, Harrowgate Pike, Lunsdale, Brackmoor, Tarnholme, Oxenrigg.
  Valley towns that share a name with a station (for example Harrowgate) are public town forecasts, not contract stations.
- Steps: 3-hourly, stamped in UTC in `dt_txt`, at least 36 hours ahead.
- The service holds one current forecast per station. When a station is reissued (new model run, observation-driven
  correction, duty forecaster amendment) the reissued forecast replaces the previous one in the service.

## Fields and units (Northfell contract)
| field | meaning | unit |
|---|---|---|
| main.temp | air temperature at 1.5 m for the step | degrees Celsius |
| main.temp_min / main.temp_max | spread of temperature within the step | degrees Celsius |
| wind.speed | 10 m mean wind speed for the step | **knots (kn)** |
| wind.deg | wind direction | degrees true |
| pop | probability of precipitation | 0-1 |

v3 delivered wind.speed in metres per second; v4 changed the unit to knots at Northfell's request (marine-style
wind products for the coastal stations). Field names did not change.

## Reissues and amendments
- Routine model runs: 00Z (in service ~05:00), 06Z (~06:45), 12Z (~13:00).
- Station reissue: when a station's observations correct the forecast (e.g. after a sensor fault).
- Amendment: a duty forecaster change to one or more stations, numbered AMD-<mmdd>-<nn>, mailed to the rating desk
  mailbox; the station forecasts are reissued in the service at the same time.
