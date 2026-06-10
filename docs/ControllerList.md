# Controller List

This is a full list of devices and controllers that we currently support.
For the full setup guide, see [Getting Started](SetupGuide/index.md).

For a list of deprecated and discontinued setups, see: [Deprecated and Discontinued Controller List](ControllerListOld.md)

**Terminology:**

- **Device** - A microcontroller such as an ESP32, Arduino, Teensy, etc...
- **Controller** - A game controller such as the Nintendo Pro Controller or Joycon.
- **Setup** or **Controller Setup** - A setup where a "device" is emulating a "controller" for automation.


## Controller Setups

This table lists all the device and controller combinations that we support in this project.

### Recommended Setups:

| | **Device Type** | **Supported Controllers** | **Setup Difficulty<br>(Scale 1-10)** | **Guides** |
| --- | --- | --- | --- | --- |
| [<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-USB_small.jpg" width="200">](SetupGuide/Images/PicoW/ControllerSetup-PicoW-USB.jpg) | Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(USB Mode) {.nowrap} | NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | 1 | [Guide](SetupGuide/Controllers/Controller-PicoW-USB.md) {.nowrap} |
| [<img src="SetupGuide/Images/ESP32/ControllerSetup-ESP32_small.jpg" width="200">](SetupGuide/Images/ESP32/ControllerSetup-ESP32-WROOM.jpg) | ESP32 {.nowrap} | NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | 3 | [Windows](SetupGuide/Controllers/Controller-ESP32-WROOM.md)<br>[Mac](SetupGuide/Controllers/Controller-ESP32-WROOM-MacOS.md)<br>[Video Tutorial](https://youtu.be/YzGyQQOGjl8) {.nowrap} |
| [<img src="SetupGuide/Images/ESP32-S3/ControllerSetup-ESP32-S3_small.jpg" width="200">](SetupGuide/Images/ESP32-S3/ControllerSetup-ESP32-S3.jpg) | ESP32-S3 {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | 3 | [Windows](SetupGuide/Controllers/Controller-ESP32-S3.md)<br>[Video Tutorial](https://youtu.be/ezBuwk48z8w) {.nowrap} |
| [<img src="SetupGuide/Images/sys-botbase/ControllerSetup-sbb_small.jpg" width="200">](SetupGuide/Images/sys-botbase/ControllerSetup-sbb.jpg) | CFW: sys-botbase 3 {.nowrap} | NS1: Wired Controller {.nowrap} | 2 | [Guide](SetupGuide/Controllers/Controller-sys-botbase.md) {.nowrap} |

### Other Supported Setups:

| | **Device Type** | **Supported Controllers** | **Setup Difficulty<br>(Scale 1-10)** | **Guides** |
| --- | --- | --- | --- | --- |
| [<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-UART_small.jpg" width="200">](SetupGuide/Images/PicoW/ControllerSetup-PicoW-UART.jpg) | RP2040 Family<br>RP2350 Family {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | 5 | [Guide](SetupGuide/Controllers/Controller-RP2040-Family.md) {.nowrap} |
| [<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-UART_small.jpg" width="200">](SetupGuide/Images/PicoW/ControllerSetup-PicoW-UART.jpg) | Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(UART Mode) {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon<br>NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | 5 | [Guide](SetupGuide/Controllers/Controller-PicoW-UART.md) {.nowrap} |
| [<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced_small.jpg" width="200">](SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced.jpg) | RP2040 Family<br>RP2350 Family<br>(Advanced UART Mode) {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | 10 | [Guide](SetupGuide/Controllers/Controller-PicoW-Advanced.md) {.nowrap} |
| [<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced_small.jpg" width="200">](SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced.jpg) | Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(Advanced UART Mode) {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon<br>NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | 10 | [Guide](SetupGuide/Controllers/Controller-PicoW-Advanced.md) {.nowrap} |

### Setup Comparison Table:

| Setup | **Supported Controllers** | **Price (per Unit)** | **Setup Difficulty<br>(Scale 1-10)** | **Notes:** |
| --- | --- | --- | --- | --- |
| Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(USB Mode) {.nowrap} | NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | Single: $8<br>Volume: $7 {.nowrap} | 1 | Upgradable to UART mode. {.nowrap} |
| ESP32 {.nowrap} | NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | Single: $10<br>Volume: $4 {.nowrap} | 3 | Unresolved Bugs:<br>- [Issue 800](https://github.com/PokemonAutomation/Arduino-Source/issues/800)<br>- [Issue 694](https://github.com/PokemonAutomation/Arduino-Source/issues/694) {.nowrap} |
| ESP32-S3 {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | Single: $15<br>Volume: $8 {.nowrap} | 3 | Best wired setup by far.<br>Workhorse for most seasoned users. {.nowrap} |
| RP2040 Family<br>RP2350 Family {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | Single: $17<br>Volume: $8 {.nowrap} | 5 | [Vulnerable to power glitching.](PowerGlitching.md)<br>Exposed pins can be annoying. {.nowrap} |
| Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(UART Mode) {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon<br>NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | Single: $19<br>Volume: $10 {.nowrap} | 5 | [Vulnerable to power glitching.](PowerGlitching.md)<br>Exposed pins can be annoying. {.nowrap} |
| RP2040 Family<br>RP2350 Family<br>(Advanced UART Mode) {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} | Single: $28+<br>Volume: $10 {.nowrap} | 10 | <br>Hardest to build. {.nowrap} |
| Raspberry Pi Pico W<br>Raspberry Pi Pico 2 W<br>(Advanced UART Mode) {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon<br>NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} | Single: $30+<br>Volume: $12 {.nowrap} | 10 | Best final product.<br>Hardest to build. {.nowrap} |


## Device Types

A "device" is a microcontroller or development board that we will use to implement a game controller.

| Image | Description |
| :---: | --- |
| <img src="SetupGuide/Images/ESP32/ControllerSetup-ESP32-WROOM-Board-2.jpg" width="200"> | **ESP32**<br><br>Supported Controllers:<br>- NS1: Wireless Pro Controller<br>- NS1: Wireless Left Joycon<br>- NS1: Wireless Right Joycon<br><br>The ESP32 is a microcontroller that supports Bluetooth. It is one of the few microcontrollers that supports Bluetooth Classic (BTC) since the world has moved onto Bluetooth LE (BLE). Thus it is (almost) uniquely suited to implement the Switch 1 wireless controllers which are also BTC.<br><br>The USB port on it is a built-in UART intended for debugging, but we hijack it as the main line of communication with CC to eliminate the need for an external UART. This makes it super convenient since a single USB adapter turns it into fully wireless dongle that allows your computer full control of your Switch without the hassle of any cables at all.<br><br>It's worth noting that the ESP32 also supports BLE. However it only supports BLE 4.2 while the Switch 2 wireless controllers are BLE 5.2. So it's unlikely the ESP32 can do the Switch 2 wireless controllers. |
| <img src="Images/Devices/ESP32-S3.jpg" width="200"> | **ESP32-S3**<br><br>Supported Controllers:<br>- HID: Keyboard<br>- NS1: Wired controller<br>- NS2: Wired controller<br>- NS1: Wired Pro Controller<br>- NS1: Wired Left Joycon<br>- NS1: Wired Right Joycon<br><br>The ESP32-S3 is the by far the best wired controller setup. It has both USB OTG and USB UART as separate ports. The USB OTG can be programmed as a game controller while the USB UART elminates the need for the external UART that was needed by the AVR8 setups (Arduino/Teensy). Thus ESP32-S3 is the perfect replacement for those older setups. Ease of setup is very important as it lowers the technical bar of entry for new users.<br><br>The ESP32-S3 also supports Bluetooth, but only Bluetooth LE (BLE). So while it cannot implement the Switch 1 wireless controllers, it does give us future ambitions of supporting the Switch 2 wireless controllers. |
| **Pico W**<br><img src="Images/Devices/PicoW.jpg" width="200"><br><br><br>**Pico 2 W**<br><img src="Images/Devices/Pico2W.jpg" width="200"> | **Raspberry Pi: Pico W and Pico 2 W**<br><br>Supported Controllers:<br>- HID: Keyboard<br>- NS1: Wired Controller<br>- NS2: Wired Controller<br>- NS1: Wired Pro Controller<br>- NS1: Wired Left Joycon<br>- NS1: Wired Right Joycon<br>- NS1: Wireless Pro Controller<br>- NS1: Wireless Left Joycon<br>- NS1: Wireless Right Joycon<br><br>The Raspberry Pi Pico W is unique in that it can support every single controller. However, accessing the wired controllers is more difficult as it requires more setup.<br><br>The large (silver) chip is a Bluetooth module that supports both BTC and BLE. This allows it to implement wireless controllers. Meanwhile, the USB port on it is USB OTG which allows it to implement the wired controllers. But unlike the ESP32-S3, it does not have a 2nd USB port to use as a UART connection to the computer. <br><br>Therefore we have programmed two operating modes for the Pico W:<br>- USB Mode<br>- UART Mode<br><br>In USB mode, the USB port acts as a serial port that can be plugged directly into the computer. This makes it functionally the same as the ESP32 with only wireless controller support.<br><br>In UART mode, the USB port becomes a wired controller plugged into the console. This unlocks all the remaining (wired) controllers. However, you need to wire up an external UART to UART1 in order for it to communicate with the computer. Thus this setup is similar to that of the Teensy 2 and Pro Micro with the added bonus of the wireless controller support.<br><br>Both operating modes use the same firmware binary. On boot, it starts in USB mode. It automatically switches to UART mode when it sees valid traffic on UART1.<br><br>**Raspberry Pi: Pico and Pico 2**<br><br>Supported Controllers:<br>- HID: Keyboard<br>- NS1: Wired Controller<br>- NS2: Wired Controller<br>- NS1: Wired Pro Controller<br>- NS1: Wired Left Joycon<br>- NS1: Wired Right Joycon<br><br>Same as the Pico W and Pico 2 W, but without the wireless. So UART mode with an external UART is required. Given the price difference of only $2 between wireless and non-wireless, there is no point in using the non-wireless Picos unless you already have one lying around.<br><br>The same firmware is used as the wireless versions. The firmware will detect the existence of the wireless chip and present only the usable controllers. |



## Controller Types

A "controller" (not to be confused with the microcontrollers above) refers to a game controller that will be emulated for the purpose of controlling the game console.

| Image | Description |
| --- | --- |
| <img src="Images/Controllers/HID-PhysicalKeyboard.jpg" width="300"> | **HID: Keyboard** ([Controller Guide](SetupGuide/ControllerGuide.md#hid-keyboard))<br><br>This is a standard HID keyboard over USB. While it can't be used to play a Nintendo Switch, it is useful for typing in text fields. Thus it provides the fastest method for Fast Code Entry.<br><br>This uses the standard 8-byte HID keyboard report that allows for up to 6 keys to be held at once. |
| <img src="Images/Controllers/Switch1-Horipad-Wired.jpg" width="300"> | **Switch 1: Wired Controller** ([Controller Guide](SetupGuide/ControllerGuide.md#ns1-wired-controller))<br><br>This is the standard 3rd party "officially licensed" wired controller. Most wired controllers from Horipad and PowerA fall into this category.<br><br>This controller type only supports the standard buttons/joystick and do not support rumble or gyro. It also does not support custom colors in its icon when connected to the Switch.<br><br>These use the standard 8-byte HID report type with 14 buttons, a dpad, and two joysticks with 8-bit precision. |
| <img src="Images/Controllers/Switch2-PowerA-Wired.jpg" width="300"> | **Switch 2: Wired Controller** ([Controller Guide](SetupGuide/ControllerGuide.md#ns2-wired-controller))<br><br>This is the same as the Switch 1 wired controller, except that they add the GL, GR, and C (gamechat) buttons for the Switch 2. This controller type is backwards compatible with the Switch 1 such that pressing the new buttons simply do nothing on the Switch 1.<br><br>These also use the standard 8-byte HID report type with 17 buttons, a dpad, and two joysticks with 8-bit precision. Due to the button field having only 16 bits, the 17'th button (the C button) instead uses an unused bit in the dpad byte. |
| <img src="Images/Controllers/Switch1-ProController.jpg" width="300"> | **Switch 1: Wired/Wireless Pro Controller** (Controller Guide: [Wired](SetupGuide/ControllerGuide.md#ns1-wired-pro-controller)/[Wireless](SetupGuide/ControllerGuide.md#ns1-wireless-pro-controller))<br><br>This is the official pro controller from Nintendo. In addition to all the features of the 3rd party wired controllers above, it also supports gyro, rumble, NFC, console wake up, and custom icon colors. (Though we currently only support rumble and console colors.)<br><br>This controller exists in two variants, wired and wireless. Wireless is supported by the ESP32 and the Pico W. Wired is supported by the ESP32-S3, Pico (UART mode only), and sys-botbase.<br><br>This controller uses Nintendo's proprietary 48-byte HID report 0x30. |
| <img src="Images/Controllers/Switch1-Joycons.jpg" width="300"> | **Switch 1: Wired/Wireless Joycons** (Controller Guide: [Wired](SetupGuide/ControllerGuide.md#ns1-wired-leftright-joycon)/[Wireless](SetupGuide/ControllerGuide.md#ns1-wireless-leftright-joycon))<br><br>These are the official joycons from Nintendo and supports the same set of features as the Pro Controller (minus fewer buttons/joysticks). Joycons are important to this project because they are required for some games such as Pokémon Let's Go Pikachu and Eevee (LGPE).<br><br>While wired joycons do not (officially) exist, the protocol for it does. Thus joycons can also be either wired or wireless. Wireless is supported by the ESP32 and Pico W controllers. Wired is supported by the ESP32-S3 and Pico (UART mode only).<br><br>These use Nintendo's proprietary 48-byte HID report 0x30. |









## Controller Performance Classes

For the purposes of program compatibility, each setup/device + controller combination is placed into one of 2 performance categories:

- Wired
- Wireless

Programs that are speed-critical will have separate execution paths optimized for each performance category. (i.e. date spam, Fast Code Entry...)

### Wired:

Wired controllers are by far the most stable with a button timing accuracy of < 1ms (typically ~100us). They are not prone to random disconnects and can connect to the Switch from almost anywhere. This makes them the best suited for automation.

| **Device** | **Controller** |
| --- | --- |
| ESP32-S3<br>Pico 1 W (UART mode)<br>Pico 2 W (UART mode)<br>RP2040 Family<br>RP2350 Family {.nowrap} | HID: Keyboard<br>NS1: Wired Controller<br>NS2: Wired Controller<br>NS1: Wired Pro Controller<br>NS1: Wired Left Joycon<br>NS1: Wired Right Joycon {.nowrap} |
| Arduino Uno R3<br>Arduino Leonardo<br>Pro Micro<br>Teensy 2.0<br>Teensy++ 2.0 {.nowrap} | NS2: Wired Controller {.nowrap} |
| sys-botbase 3 (sbb3) {.nowrap} | NS1: Wired Controller {.nowrap} |


### Wireless:

Wireless controllers are less stable and usually have timing variation on the order of 2-10ms. While they are clean and easy to setup with no additional cabling, wireless controllers are generally less reliable since they are prone to random disconnects and high latencies from wireless interference. Nintendo's complicated (and proprietary) wireless protocol means that 3rd party implementations (including this project) are typically less than perfect and prone to compatibility issues.

The main issue with wireless is that it can only reliably connect to the Switch inside the grip menu. So if you get disconnected outside of the grip menu and are unable to reconnect, you will need another controller or physical access to navigate back to the grip menu to re-pair the controller. For this reason, wireless controllers are less suited for remotely controlled automation.

| **Device** | **Controller** |
| --- | --- |
| ESP32<br>Pico 1 W (both modes)<br>Pico 2 W (both modes) {.nowrap} | NS1: Wireless Pro Controller<br>NS1: Wireless Left Joycon<br>NS1: Wireless Right Joycon {.nowrap} |

<hr>

**Discord Server:** 


[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)












