# Power Glitching

## What is Power Glitching?

Power glitching a problem that affects all controllers that rely entirely on the dock to receive power. Thus it affects:

- All RP2040 and RP2350 family boards using external UART.
- Arduino Uno R3
- Arduino Leonardo
- Teensy 2.0 / Teensy++ 2.0
- Pro Micro

Each time the Nintendo Switch is docked or undocked, the dock will momentarily cut the power to all its USB ports. This causes problems for boards that rely on the dock for its power.

**Good Case: Clean Reboot**

In most cases, the microcontroller board will completely lose power and reboot properly. This is the good case and is usually not noticeable for wired controllers. For the RP2040/RP2350 family boards, it will lose its pairing with the Switch. If you are using a Pico W's wireless controllers, you will need to re-pair them.

**Bad Case: Glitch + Hang**

In the bad case, the microcontroller board will lose enough power to "glitch", but not enough to completely shutdown. This causes the board to become unresponsive. This is really annoying because the only way to fix it is to either press the reset button on it (if it has one), or power cycle it by unplugging every single cable attached to it and plugging it back in.

On the Switch 1, the bad case is quite rare. The controller would cleanly reset unnoticed. However, on the Switch 2 has made the bad (glitching) case much more common. This has been further exacerbated by recent changes in our stack that has drastically increased the complexity of the firmware.

In fact, the ***Switch 2 docks will almost always glitch the microcontrollers***. This is coming into attention now as Pokémon Legends ZA brings a lot of old-time users back to automation with their old setups, but now on the Switch 2.

## How do I clear a power glitch?

As mentioned in the previous section, you need to reset it:

- If the board has a reset button, try pressing that.
- If that doesn't work (or there is no reset button), you need to power cycle it. That means unplugging both the USB and the UART to ensure no power is reaching the board. Even though the UART does not supply power to the board, there is residual leakage through the TX and RX lines to prevent the board from fully shutting down.

Yes, this is incredibly annoying - especially now with the Switch 2 where it almost always glitches.

## How do I fix it permanently?

If you are still using the old controller setup (Uno, Leonardo, Teensy, Pro Micro), our advice is to upgrade to one of these newer setups:

- [Pico W (USB mode)](SetupGuide/Controllers/Controller-PicoW-USB.md)
- [ESP32](SetupGuide/Controllers/Controller-ESP32-WROOM.md)
- [ESP32-S3](SetupGuide/Controllers/Controller-ESP32-S3.md)

All 3 of these setups are immune to power glitching. The Pico and the ESP32 receive their power from the computer instead of the dock. Meanwhile, the ESP32-S3 receives power from both the computer and the dock and will stay powered if either side is powering it.

Unfortunately, the RP2040/RP2350 family boards (via external UART) is powered by the dock and is affected. But it tends to reset more often than it glitches. Nevertheless the situation is not ideal since a reset will disconnect and unpair the wireless as well.

## I am a circuits expert. How do I fix this for real?

The solution is to setup the power mechanism to be like the ESP32-S3 where the microcontroller board can be powered by either the computer or the dock.

To do this, you must connect the UART's +5V line to the board's power input line through a fast switching [Schottky diode](https://en.wikipedia.org/wiki/Schottky_diode). The connection allows the board to draw power from the computer via the UART. The purpose of the diode is to prevent backflow where power goes from the dock into the computer where it may damage one (or both) sides.

While both sides should be supplying a steady 5V, they will not be exactly the same. So power will flow from the higher side to the lower side. Most boards already have a diode that prevents backflow into its USB. So while backflow from computer -> dock is not possible, backflow from dock -> computer is possible without a diode. This is the reason why our guides leave the +5V VCC line disconnected.

We currently recommend the [1N5817 Schottky Diode](https://www.amazon.com/dp/B07Q5H1SLY). But anything with similar specs should work.

<img src="SetupGuide/Images/1N5817-Schottky-Diode.jpg">

### RP2040/RP2350 family boards:

Main Article: [Pico W (Advanced UART mode)](SetupGuide/Controllers/Controller-PicoW-Advanced.md)

For the RP2040/RP2350 boards, you should connect the UART's +5V to the VSYS (pin 39) via a diode. The diode must be in the direction that allows power to flow UART -> VSYS.

On the other side, most of these boards already has a diode between VSYS and its own USB +5V. So you don't need to add one there. Furthermore, there is usually a capacitor (47uF for the Pico) between VSYS and GND to keep the board powered long enough to survive the transition from one power source to the other. (Keeping in mind that the diode's switching latency is much longer than the clock period of the RP2040 or RP2350 chip.)

Note that the SeeedStudio Xiao boards do not expose VSYS. So this method will not work.

[Pinout and Circuit Diagrams](https://deepbluembedded.com/raspberry-pi-pico-w-pinout-diagram-gpio-guide/)

**Breadboard Prototype:**

<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced-Breadboard0-Small.jpg" width="39%"> <img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced-Breadboard1-Small.jpg" width="51%">

**"Production-Level" Setup:**

<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced-Raw0-Small.jpg" width="45%"> <img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced-Raw1-Small.jpg" width="45%">

### Pro Micro:

For the Pro Micro, you should connect the UART's +5V to the RAW pin via a diode. The diode must be in the direction that allows power to flow UART -> RAW.

On the other side, the Pro Micro already has a diode that sits between RAW and its own USB +5V. So you don't need to add one there. Furthermore, the Pro Micro has a 10uF capacitor between RAW and GND to keep the board powered long enough to survive the transition from one power source to the other. (Keeping in mind that the diode's switching latency is longer than the clock period of the ATmega32U4 chip.)

[Pinout and Circuit Diagrams](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide/hardware-overview-pro-micro)

<img src="SetupGuide/Images/ProMicro/ControllerSetup-ProMicro-Advanced-Breadboard0-Small.jpg" width="39%"> <img src="SetupGuide/Images/ProMicro/ControllerSetup-ProMicro-Advanced-Breadboard1-Small.jpg" width="51%">

### The other boards (Uno, Leonardo, Teensy):

We have not analyzed or tested these boards and we do not intend to given that they are all deprecated. But they are probably similar to the above two boards. Make sure you analyze their circuit diagrams.


## Credits

- **Author:** Kuroneko/Mysticial



<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)




