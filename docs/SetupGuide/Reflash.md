# Re-flashing the microcontroller.

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)

When trying to connect your microcontroller to the Computer Control program, you may get an error with red text: 
```
Incompatible protocol. Device: ...
Please flash your microcontroller (e.g. ESP32, Pico W, Arduino) with the .bin/.uf2/.hex that came with this version of the program.
```

This likely means that the firmware flashed to your microcontroller is out of date, and that you need to re-flash your microcontroller with updated firmware. You may remember flashing the microcontroller when you first set-up Pokemon Automation. With ongoing software updates, we do require users to re-flash the microcontroller with updated firmware from time to time.

The steps for flashing your microcontroller are outlined in one of the guides below. Please see the guide that matches your microcontroller.

## Recommended Setups:

| | **Device Type** | **Guides** |
| --- | --- | --- |
| <img src="Images/PicoW/ControllerSetup-PicoW-USB.jpg" width="200"> | Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(USB Mode) {.nowrap} | [Guide](Controllers/Controller-PicoW-USB#step-1-flash-the-firmware-to-the-pico-w.md) {.nowrap} |
| <img src="Images/ESP32/ControllerSetup-ESP32-WROOM.jpg" width="200"> | ESP32 {.nowrap} | [Windows](Controllers/Controller-ESP32-WROOM#step-2-flash-the-firmware-to-the-esp32.md)<br>[Mac](Controllers/Controller-ESP32-WROOM-MacOS#step-3-flash-the-firmware-to-the-esp32.md) {.nowrap} |
| <img src="Images/ESP32-S3/ControllerSetup-ESP32-S3.jpg" width="200"> | ESP32-S3 {.nowrap} |[Windows](Controllers/Controller-ESP32-S3#step-2-flash-the-firmware-to-the-esp32.md) {.nowrap} |
| <img src="Images/PicoW/ControllerSetup-PicoW-UART.jpg" width="200"> | Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(UART Mode) {.nowrap} | [Guide](Controllers/Controller-PicoW-UART#step-1-flash-the-firmware-to-the-pico-w.md) {.nowrap} |
| <img src="Images/PicoW/ControllerSetup-PicoW-Advanced.jpg" width="200"> | Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(Advanced UART Mode) {.nowrap} | [Guide](Controllers/Controller-PicoW-Advanced#software-setup.md) {.nowrap} |
<!-- | <img src="Images/sys-botbase/ControllerSetup-sbb.jpg" width="200"> | CFW: sys-botbase 3 {.nowrap} | [Guide](Controllers/Controller-sys-botbase.md) {.nowrap} | -->

## Deprecated Setups:

These are older setups that are still supported, but no longer recommended for new users.

| | **Device Type** | **Guides** |
| --- | --- | --- |
| <img src="Images/ArduinoUnoR3/ControllerSetup-UnoR3.jpg" width="200"> | Arduino Uno R3 {.nowrap} |  [Guide](Controllers/Controller-ArduinoUnoR3#hardware-assembly.md) {.nowrap} |
| <img src="Images/ArduinoLeonardo/ControllerSetup-Leonardo.jpg" width="200"> | Arduino Leonardo {.nowrap} | [Guide](Controllers/Controller-ArduinoLeonardo#hardware-assembly.md) {.nowrap} |
| <img src="Images/ProMicro/ControllerSetup-ProMicro-HammerHeaders.jpg" width="200"> | Pro Micro {.nowrap} | [Mini-Grabbers](Controllers/Controller-ProMicro-MiniGrabbers#hardware-assembly.md)<br>[Hammer Headers](Controllers/Controller-ProMicro-HammerHeaders#hardware-assembly.md) {.nowrap} |
| <img src="Images/Teensy2/ControllerSetup-Teensy2-HammerHeaders.jpg" width="200"> | Teensy 2.0<br>Teensy++ 2.0 {.nowrap} | [Mini-Grabbers](Controllers/Controller-Teensy2-MiniGrabbers#hardware-assembly.md)<br>[Hammer Headers](Controllers/Controller-Teensy2-HammerHeaders#hardware-assembly.md) {.nowrap} |



<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)
























