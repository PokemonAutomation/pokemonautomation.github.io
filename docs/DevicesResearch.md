# Device Research

While we currently support a handful of microcontrollers, in reality, we have looked at many more boards.

## Currently Supported Boards

|**Name** | **Specs** | **Capabilities** | **Target Controllers** | **Verdict** |
| --- | --- | --- | --- | --- |
| ESP32 {.nowrap} | - CPU: Xtensa LX6 <br>- RAM: 520 KB<br>- Flash: 4 MB {.nowrap} | BT Classic<br>BT LE<br>Built-in UART-USB port. {.nowrap} | NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | Supports Bluetooth Classic! No external UART required!<br><br>Setup Difficulty: 2<br><br>Powerful CPU. Good modern toolchain. Can run PABotBase2. Bluetooth stack is very buggy though.<br><br>Currently supported by PA. |
| ESP32-S3 {.nowrap} | - CPU: Xtensa LX7 <br>- RAM: 512 KB<br>- Flash: 8 MB {.nowrap} | USB OTG<br>BT LE<br>Built-in UART-USB port. {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | No external UART required!<br><br>Setup Difficulty: 2<br><br>Powerful CPU. Good modern toolchain. Can run PABotBase2. Unfortunately lacks BT Classic and cannot do wireless NS1 controllers.<br><br>Currently supported by PA. |
| Raspberry Pi Pico W {.nowrap} | Pico 1:<br>- CPU: RP2040 <br>- RAM: 264 KB<br>- Flash: 2 MB<br><br>Pico 2:<br>- CPU: RP2350 <br>- RAM: 520 KB<br>- Flash: 4 MB {.nowrap} | USB OTG<br>BT Classic<br>BT LE {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon<br>NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | Easiest wireless setup! Supports wired as well with external UART.<br><br>Setup Difficulty: 1 (USB)<br>Setup Difficulty: 5 (UART)<br><br>Powerful CPU. Good modern toolchain. Can run PABotBase2. Unfortunately requires external UART for wired capability.<br><br>Currently supported by PA. |
| Raspberry Pi Pico {.nowrap} | Pico 1:<br>- CPU: RP2040 <br>- RAM: 264 KB<br>- Flash: 2 MB<br><br>Pico 2:<br>- CPU: RP2350 <br>- RAM: 520 KB<br>- Flash: 4 MB {.nowrap} | USB OTG {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | Same as Raspberry Pi Pico, but without wireless support.<br><br>Setup Difficulty: 5 (UART) |

## Deprecated Boards

|**Name** | **Specs** | **Capabilities** | **Target Controllers** | **Verdict** |
| --- | --- | --- | --- | --- |
| Arduino Uno R3 {.nowrap} | - CPU: ATMega16u2<br>- RAM: 512 bytes<br>- Flash: 12 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | [Original Fightstick PoC](https://github.com/shinyquagsire23/Switch-Fightstick)<br><br>Setup Difficulty: 6<br><br>Too little flash and memory. RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |
| Teensy 2.0 {.nowrap} | - CPU: ATMega32u4<br>- RAM: 2.5 KB<br>- Flash: 31.5 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | [Original Fightstick PoC](https://github.com/shinyquagsire23/Switch-Fightstick)<br><br>Setup Difficulty: 8<br><br>RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |
| Teensy++ 2.0 {.nowrap} | - CPU: AT90USB1286<br>- RAM: 8 KB<br>- Flash: 128 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | [Original Fightstick PoC](https://github.com/shinyquagsire23/Switch-Fightstick)<br><br>Setup Difficulty: 8<br><br>RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |
| Arduino Leonardo {.nowrap} | - CPU: ATMega32u4<br>- RAM: 2.5 KB<br>- Flash: 31.5 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | Same chip as the Teensy 2.0. Added as stronger alternative to Uno R3.<br><br>Setup Difficulty: 6<br><br>RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |
| Pro Micro {.nowrap} | - CPU: ATMega32u4<br>- RAM: 2.5 KB<br>- Flash: 31.5 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | Same chip as the Teensy 2.0. Added as low-cost option for expert users.<br><br>Setup Difficulty: 8<br><br>RAM/progmem separation is annoying. Toolchain C++ support is very poor. Can run PABotBase1, but not PABotbase2.<br><br>Currently supported by PA. Soon to be deprecated and removed with migration to PABotBase2. |

## Boards that Never Made the Cut

|**Name** | **Specs** | **Capabilities** | **Target Controllers** | **Verdict** |
| --- | --- | --- | --- | --- |
| CH552 {.nowrap} | - CPU: E8051<br>- RAM: 1.25 KB<br>- Flash: 16 KB {.nowrap} | USB OTG {.nowrap} | NS1: Wired Controller<br>NS2: Wired Controller {.nowrap} | Has 2 USB ports. We thought we could use both of them, but it turns out they are shorted to each other (i.e. they are the same port). Therefore it's useless.<br><br>Setup Difficulty: 1 (if it worked the way we thought)<br><br>Not supported by PA. |

<hr>

**Discord Server:** 


[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)







