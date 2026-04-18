# Device Research

While we currently support a handful of microcontrollers, in reality, we have looked at many more boards.

In order for a board to be usable, it must support at least one following:

- Bluetooth Classic
- USB OTG

For wireless controllers, Bluetooth Classic (BTC) is the protocol for the Switch 1 controllers, yet it is also a dying protocol since the world has moved to Bluetooth Low Energy (BLE). While many boards support wireless and Bluetooth, very few of them support BTC. If they support Bluetooth, they only support BLE. The (original) ESP32 and the Raspberry Pi Pico W are the only boards that still retain built-in support for BTC. Later ESP32 models only support BLE.

For wired controllers, you need USB OTG. While many boards support USB OTG, almost all of them lack an easy 2nd way to connect to the computer. Thus almost everything requires an external UART to do so. The ESP32-S3 remains the only board that has both USB OTG and a built-in USB-UART TTL. While there are board with multiple USB ports, all the ones we have found have power circuitry that is incompatible with the setup that we need.

It may be possible to use WiFi or Ethernet to connect a wired controller to the computer. But we haven't explored these options much due to the complications of dealing with IP addresses, discovery, and security.

## Currently Supported Boards

|**Name** | **Specs** | **Capabilities** | **Target Controllers** | **Verdict** |
| --- | --- | --- | --- | --- |
| ESP32 {.nowrap} | - CPU: Xtensa LX6 <br>- RAM: 520 KB<br>- Flash: 4 MB {.nowrap} | BT Classic<br>BT LE<br>Built-in UART-USB port {.nowrap} | NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | Supports Bluetooth Classic! No external UART required!<br><br>Setup Difficulty: 2<br>Immune to [power glitching](PowerGlitching.md).<br><br>Powerful CPU. Good modern toolchain. Can run PABotBase2. Bluetooth stack is very buggy though.<br><br>Currently supported by PA. |
| ESP32-S3 {.nowrap} | - CPU: Xtensa LX7 <br>- RAM: 512 KB<br>- Flash: 8 MB {.nowrap} | USB OTG<br>BT LE<br>Built-in UART-USB port {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | No external UART required!<br><br>Setup Difficulty: 2<br>Immune to [power glitching](PowerGlitching.md).<br><br>Powerful CPU. Good modern toolchain. Can run PABotBase2. Unfortunately lacks BT Classic and cannot do wireless NS1 controllers.<br><br>Currently supported by PA. |
| Raspberry Pi Pico W {.nowrap} | Pico 1:<br>- CPU: RP2040 <br>- RAM: 264 KB<br>- Flash: 2 MB<br><br>Pico 2:<br>- CPU: RP2350 <br>- RAM: 520 KB<br>- Flash: 4 MB {.nowrap} | USB OTG<br>BT Classic<br>BT LE {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon<br>NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | Easiest wireless setup! Supports wired as well with external UART.<br><br>Setup Difficulty: 1 (USB)<br>Setup Difficulty: 5 (UART)<br>USB mode is immune to [power glitching](PowerGlitching.md).<br>UART mode is vulnerable to [power glitching](PowerGlitching.md).<br><br>Powerful CPU. Good modern toolchain. Can run PABotBase2. Unfortunately requires external UART for wired capability.<br><br>Currently supported by PA. |
| Raspberry Pi Pico {.nowrap} | Pico 1:<br>- CPU: RP2040 <br>- RAM: 264 KB<br>- Flash: 2 MB<br><br>Pico 2:<br>- CPU: RP2350 <br>- RAM: 520 KB<br>- Flash: 4 MB {.nowrap} | USB OTG {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | Same as Raspberry Pi Pico W, but without wireless support. Requires external UART.<br><br>Setup Difficulty: 5<br>Vulnerable to [power glitching](PowerGlitching.md).<br><br>Unofficially works for PABotBase2. Officially supported for PABotBase2. |

## Deprecated Boards

|**Name** | **Specs** | **Capabilities** | **Target Controllers** | **Verdict** |
| --- | --- | --- | --- | --- |
| Arduino Uno R3 {.nowrap} | - CPU: ATMega16u2<br>- RAM: 512 bytes<br>- Flash: 12 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | [Original Fightstick PoC](https://github.com/shinyquagsire23/Switch-Fightstick)<br><br>Setup Difficulty: 6<br>Vulnerable to [power glitching](PowerGlitching.md).<br><br>Too little flash and memory. RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |
| Teensy 2.0 {.nowrap} | - CPU: ATMega32u4<br>- RAM: 2.5 KB<br>- Flash: 31.5 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | [Original Fightstick PoC](https://github.com/shinyquagsire23/Switch-Fightstick)<br><br>Setup Difficulty: 8<br>Vulnerable to [power glitching](PowerGlitching.md).<br><br>RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |
| Teensy++ 2.0 {.nowrap} | - CPU: AT90USB1286<br>- RAM: 8 KB<br>- Flash: 128 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | [Original Fightstick PoC](https://github.com/shinyquagsire23/Switch-Fightstick)<br><br>Setup Difficulty: 8<br>Vulnerable to [power glitching](PowerGlitching.md).<br><br>RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |
| Arduino Leonardo {.nowrap} | - CPU: ATMega32u4<br>- RAM: 2.5 KB<br>- Flash: 31.5 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | Same chip as the Teensy 2.0. Added as stronger alternative to Uno R3.<br><br>Setup Difficulty: 6<br>Vulnerable to [power glitching](PowerGlitching.md).<br><br>RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |
| Pro Micro {.nowrap} | - CPU: ATMega32u4<br>- RAM: 2.5 KB<br>- Flash: 31.5 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | Same chip as the Teensy 2.0. Added as low-cost option for expert users.<br><br>Setup Difficulty: 8<br>Vulnerable to [power glitching](PowerGlitching.md).<br><br>RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |

## Boards that Didn't Make the Cut

|**Name** | **Specs** | **Capabilities** | **Target Controllers** | **Verdict** |
| --- | --- | --- | --- | --- |
| [CH552G](https://www.amazon.com/USpB-CH552-Development-Microcontroller-Frequency-Performance/dp/B0GX8CP37F) {.nowrap} | - CPU: E8051<br>- RAM: 1.25 KB<br>- Flash: 16 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | Has 2 USB ports for the perfect wired controller. We thought we could use both of them, but it turns out they are shorted to each other (i.e. they are the same port). Therefore it's useless.<br><br>Setup Difficulty: 1 (if it worked the way we thought)<br><br>Not supported by PA. |
| [waveshare RP2350 USB Mini](https://www.amazon.com/dp/B0DXF4WPRV) {.nowrap} | - CPU: RP2350 <br>- RAM: 520 KB<br>- Flash: 4 MB {.nowrap} | USB OTG x 2 {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | Has 2 USB ports for the perfect wired controller. But the VCC lines are shorted across them - which will fry either the Switch or the computer.<br><br>Setup Difficulty: 1 (if it worked the way we thought)<br><br>Not supported by PA. |
| STM32 Blue Pill {.nowrap} | - CPU: ARM Cortex-M3 <br>- RAM: 20 KB<br>- Flash: 64/128 MB {.nowrap} | USB OTG {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | Presoldered debug pins can be reprogrammed as UART to allow for easy no-solder setup. Designed to be powered over the debug pins with USB attached. So immune to [power glitching](PowerGlitching.md).<br><br>However, flashing it is extremely user unfriendly and requires external hardware.<br><br>Currently not supported by PA. Still experimenting. |

<hr>

**Discord Server:** 


[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)







