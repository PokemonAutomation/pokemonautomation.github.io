# Deprecated and Discontinued Controller List

This is a list of controllers which have been deprecated or discontinued. If you are setting up for the first time, please see the [supported controller list](ControllerList.md).

## Controller Setups

### Deprecated Setups:

These are older setups that are still supported, but will be removed in the future. Please do not use these setups.

| | **Device Type** | **Supported Controllers** | **Setup Difficulty<br>(Scale 1-10)** | **Guides** |
| --- | --- | --- | --- | --- |
| <img src="SetupGuide/Images/ArduinoUnoR3/ControllerSetup-UnoR3.jpg" width="200"> | Arduino Uno R3 {.nowrap} | NS2: Wired Controller<br>(compatible with Switch 1) {.nowrap} | 6 | [Guide](SetupGuide/Controllers/Controller-ArduinoUnoR3.md) {.nowrap} |
| <img src="SetupGuide/Images/ArduinoLeonardo/ControllerSetup-Leonardo.jpg" width="200"> | Arduino Leonardo {.nowrap} | NS2: Wired Controller<br>(compatible with Switch 1) {.nowrap} | 6 | [Guide](SetupGuide/Controllers/Controller-ArduinoLeonardo.md) {.nowrap} |
| <img src="SetupGuide/Images/ProMicro/ControllerSetup-ProMicro-HammerHeaders.jpg" width="200"> | Pro Micro {.nowrap} | NS2: Wired Controller<br>(compatible with Switch 1) {.nowrap} | 7 - (Mini Grabber)<br>9 - (Hammer Header) {.nowrap} | [Mini-Grabbers](SetupGuide/Controllers/Controller-ProMicro-MiniGrabbers.md)<br>[Hammer Headers](SetupGuide/Controllers/Controller-ProMicro-HammerHeaders.md) {.nowrap} |
| <img src="SetupGuide/Images/Teensy2/ControllerSetup-Teensy2-HammerHeaders.jpg" width="200"> | Teensy 2.0<br>Teensy++ 2.0 {.nowrap} | NS2: Wired Controller<br>(compatible with Switch 1) {.nowrap} | 7 - (Mini Grabber)<br>9 - (Hammer Header) {.nowrap} | [Mini-Grabbers](SetupGuide/Controllers/Controller-Teensy2-MiniGrabbers.md)<br>[Hammer Headers](SetupGuide/Controllers/Controller-Teensy2-HammerHeaders.md) {.nowrap} |


### Discontinued Setups:

| | **Device Type** | **Supported Controllers** | **Recommended Replacement** |
| --- | --- | --- | --- |
| <img src="SetupGuide/Images/sys-botbase/ControllerSetup-sbb.jpg" width="200"> | CFW: sys-botbase 2 {.nowrap} | NS1: Wired Controller {.nowrap} | CFW: sys-botbase 3 {.nowrap} |


### Setup Comparison Table:

| Setup | **Supported Controllers** | **Price (per Unit)** | **Setup Difficulty<br>(Scale 1-10)** | **Notes:** |
| --- | --- | --- | --- | --- |
| Arduino Uno R3 {.nowrap} | NS2: Wired Controller {.nowrap} | Single: $20 {.nowrap} | 6 | [Vulnerable to power glitching.](PowerGlitching.md) {.nowrap} |
| Arduino Leonardo {.nowrap} | NS2: Wired Controller {.nowrap} | Single: $25 {.nowrap} | 6 | [Vulnerable to power glitching.](PowerGlitching.md) {.nowrap} |
| Teensy 2/Teensy++ 2<br>(Mini Grabbers) {.nowrap} | NS2: Wired Controller {.nowrap} | (discontinued) | 7 | [Vulnerable to power glitching.](PowerGlitching.md)<br>Final product is bulky and fragile. {.nowrap} |
| Teensy 2/Teensy++ 2<br>(Hammer Headers) {.nowrap} | NS2: Wired Controller {.nowrap} | (discontinued) | 9 | [Vulnerable to power glitching.](PowerGlitching.md) {.nowrap} |
| Pro Micro<br>(Mini Grabbers) {.nowrap} | NS2: Wired Controller {.nowrap} | Single: $25<br>Volume: $10 {.nowrap} | 7 | [Vulnerable to power glitching.](PowerGlitching.md)<br>Final product is bulky and fragile. {.nowrap} |
| Pro Micro<br>(Hammer Headers) {.nowrap} | NS2: Wired Controller {.nowrap} | Single: $25<br>Volume: $8 {.nowrap} | 9 | [Vulnerable to power glitching.](PowerGlitching.md) {.nowrap} |


## Device Types

| Image | Description |
| :---: | --- |
| <img src="Images/Devices/ArduinoUnoR3.jpg" width="200"> | **Arduino Uno R3**<br><br>Supported Controllers:<br>- NS2: Wired controller<br><br>The Arduino Uno R3 is one of the original boards that spearheaded the Nintendo Switch automation community. However, its ATmega16U2 AVR8 CPU is very weak with only 512 bytes of ram and 12KB of usable program memory.<br><br>This controller is only suitable for emulating the basic wired controllers. It doesn't even have enough memory to hold multiple controller implementations the way that some of the newer controllers can. |
| <img src="Images/Devices/ArduinoLeonardo.jpg" width="200"> | **Arduino Leonardo**<br><br>Supported Controllers:<br>- NS2: Wired controller<br><br>The Arduino Leonardo uses an ATmega32U4 AVR8 CPU. It has significantly more ram and program memory at 2.5KB and 32KB respectively. This was the last addition to the AVR8 microcontroller line up and was chosen because it was easier to setup a serial connection than the Teensy or Pro Micro boards.<br><br>Being an AVR8 processor, it shares codebase with the Arduino Uno R3 and thus we only support a single wired controller type on it. |
| <img src="Images/Devices/ProMicro.jpg" width="200"> | **Pro Micro**<br><br>Supported Controllers:<br>- NS2: Wired controller<br><br>The Pro Micro uses an ATmega32U4 AVR8 CPU and is functionally the same as the Arduino Leonardo and Teensy 2.0. This was added to our lineup because it was the cheapest microcontroller of this type in volume. Thus it became the work horse for many people with multiple Switches. |
| <img src="Images/Devices/Teensy2.jpg" width="200"> | **Teensy 2.0**<br><br>Supported Controllers:<br>- NS2: Wired controller<br><br>The Arduino Uno R3 is one of the original boards that spearheaded the Nintendo Switch automation community.<br><br>The Teensy 2.0 uses an ATmega32U4 AVR8 CPU and is functionally the same as the Arduino Leonardo and Pro Micro. This (along with the Teensy++ 2.0) was by far the best board during the microcontroller-only automation era due to the easy-to-use button to put the board into flash mode. It began to fall out of use in the computer-control era due to the difficulty of setting up a serial connection on it. |
| <img src="Images/Devices/TeensyPP2.jpg" width="200"> | **Teensy++ 2.0**<br><br>Supported Controllers:<br>- NS2: Wired controller<br><br>The Teensy++ 2.0 is the same as the Teensy 2.0, but with an upgraded AT90USB1286 CPU which has much more ram and program memory.<br><br>This extra ram and program memory was never put to use in this project. So it is functionally the same as the Teensy 2.0 along with all its advantages and drawbacks. |




<hr>

**Discord Server:** 


[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)












