[![hacs][hacs-shield]][hacs]
[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

[![Project Maintenance][maintenance-shield]][maintenance]
[![BuyMeCoffee][buymecoffee-shield]][buymecoffee]

# Fuel Tracker

This integration parse the information from [TankBillig](https://tankbillig.in), that covers fuel prices information from Austria, Spain, Germany, Switzerland and France.

You can use it to track the price of fuel (Diesel, Super95 or CNG) from the **closest** fuel station to the entered latitude and longitude.


# Configuration

Please before configuring the integration look for the coordinates in format 48.211459, 16.401445 closest to the fuel station you want to track.

The script will take the fuel station with the minimum distance to the enter location. 

To activate this extension you can put this in your configuration file "configuration.yml", with the following (required) parameters:

Parameter | Value
-- | --
latitude | `XX.XXXXXX`
longitude | `YY.YYYYYY`
fuel | `Diesel`, `Super95` or `CNG` 


## Example
On the configuration.yml :

```yaml
sensor:
  - platform: fuel_tracker
    name: Hofer
    latitude: !secret latitude_hofer
    longitude: !secret longitude_hofer
    fuel: "Diesel"

  - platform: fuel_tracker
    name: Jet
    latitude: !secret latitude_jet
    longitude: !secret longitude_jet
    fuel: "Diesel"
```

![Example](/images/example.PNG)

For visualizing such cool graph, use the [mini-graph-card](https://github.com/kalkih/mini-graph-card) custom integration!

```yaml
- type: custom:mini-graph-card
        name: Fuel
        icon: mdi:fuel
        entities:
          - entity: sensor.hofer
          - entity: sensor.jet
        decimals: 3
        show:
          labels: true
        hours_to_show: 168
        color_thresholds:
          - value: 1.5
            color: "#d35400"
          - value: 1.4
            color: "#f39c12"
          - value: 1.3
            color: "#2bc039"

```




[hacs-shield]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[hacs]: https://github.com/custom-components/hacs

[releases-shield]: https://img.shields.io/github/release/JGAguado/Fuel_Tracker.svg?style=for-the-badge
[releases]: https://github.com/JGAguado/Fuel_Tracker/releases

[license-shield]: https://img.shields.io/github/license/JGAguado/Fuel_Tracker.svg?style=for-the-badge

[maintenance-shield]: https://img.shields.io/badge/maintainer-J.%20G.%20Aguado-blue.svg?style=for-the-badge
[maintenance]: https://github.com/JGAguado

[buymecoffee-shield]: https://img.shields.io/badge/buy%20me%20a%20coffee-support-yellow.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/J.G.Aguado

