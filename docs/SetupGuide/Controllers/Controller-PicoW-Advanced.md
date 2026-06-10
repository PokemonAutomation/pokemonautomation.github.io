# Raspberry Pi: All Pico Models (Advanced Setup)

This is the advanced setup guide for the Pico and Pico 2 family. It is functionally the same as [UART mode](Controller-PicoW-UART.md), but it will not glitch or reset when docking/undocking the Nintendo Switch.

Further reading: [Power Glitching](../../PowerGlitching.md)

This is the most difficult to do serial setup that we've ever done and is reserved for readers with extensive experience in circuits. Incorrect connections can lead to damage to the hardware components involved.

| **Mode** | **Connections** | **Controller Support** | **Setup Difficulty** |
| --- | --- | --- | --- |
| [USB Mode](Controller-PicoW-USB.md) | 1. Pico W's USB port -> Computer | Wireless controllers only:<br>- NS1: Wireless Pro Controller<br>- NS1: Wireless Left Joycon<br>- NS1: Wireless Right Joycon | Very Easy |
| [UART Mode](Controller-PicoW-UART.md) | 1. Pico's USB port -> Switch<br>2. Pico's pins 6/7/8 -> External UART<br>3. External UART -> Computer | Both wired and wireless:<br>- HID: Keyboard<br>- NS1: Wired Controller<br>- NS2: Wired Controller<br>- NS1: Wired Pro Controller<br>- NS1: Wired Left Joycon<br>- NS1: Wired Right Joycon<br>- NS1: Wireless Pro Controller<br>- NS1: Wireless Left Joycon<br>- NS1: Wireless Right Joycon | More Difficult |
| **Advanced UART Mode<br>(this guide)** | 1. Pico W's USB port -> Switch<br>2. Pico W's pins 6/7/8/39 -> External UART<br>3. External UART -> Computer | Both wired and wireless:<br>- HID: Keyboard<br>- NS1: Wired Controller<br>- NS2: Wired Controller<br>- NS1: Wired Pro Controller<br>- NS1: Wired Left Joycon<br>- NS1: Wired Right Joycon<br>- NS1: Wireless Pro Controller<br>- NS1: Wireless Left Joycon<br>- NS1: Wireless Right Joycon | Most Difficult |

If you are here, we assume that you already have a working Pico (UART mode) setup. So this wiki will only cover the differences from the basic UART setup. Furthermore, the parts list that we will choose will be geared toward making the following (boxed) easy-to-use product with no exposed circuitry. You are free to do whatever you want.

<img src="../Images/PicoW/ControllerSetup-PicoW-Advanced.jpg" width="45%">

## Hardware Setup:

**Required Hardware:**

1. A Raspberry Pi Pico microcontroller (any model without pins).
2. [A micro-USB to USB-A cable or adapter.](https://www.amazon.com/gp/product/B09FXJD61Z)
3. [USB to Serial TTL (UART).](https://www.amazon.com/dp/B07T1XR9FT)
4. [1N5817 Schottky Diode.](https://www.amazon.com/dp/B07Q5H1SLY)
5. [Press-fit Headers.](https://www.adafruit.com/product/5938) (or soldering)
6. [Dupont connector kit.](https://www.amazon.com/dp/B096DC1J3X) (or soldering)
7. [Pico enclosure.](https://www.adafruit.com/product/6252) (only compatible with Picos without pins)

Building just one of these will be expensive since many of these parts can only be bought in volume. But the volume per-unit cost in parts comes down to about $12 USD.


### Hardware Assembly:

Make the following connections:

| **UART pin** | **Pico W pin** |
| --- | --- |
| RX | TX -> GP4 (pin 6) |
| TX | RX <- GP5 (pin 7) |
| GND | GND (pin 8, or any other GND pin) |
| VCC (+5V) | VSYS (pin 39) via diode |

The difference from the regular UART mode guide is that here we do connect the UART's +5V VCC line. This allows the Pico to be powered by both the USB or the UART - thus allowing it to stay powered and not glitch or reset when the USB power is momentarily lost when docking/undocking the Switch.

It is important that the VCC <-> VSYS connection be done through a diode which only allows current in the direction of VCC -> VSYS. This is needed to prevent backflow through the UART when both UART and USB are connected and the USB side has a higher voltage.

***Failing to use a diode (or putting it in the wrong direction) will short the computer with the dock and potentially damage all hardware involved!***

Further Reading:

- [Guide to powering the Raspberry Pi Pico](https://www.penguintutor.com/electronics/pico-power)
- [Which Shottky diode do I need for redundant power to a Raspberry Pi Pico?](https://electronics.stackexchange.com/questions/548990/which-shottky-diode-do-i-need-for-redundant-power-to-a-raspberry-pi-pico)
- [Pinout and Circuit Diagrams](https://deepbluembedded.com/raspberry-pi-pico-w-pinout-diagram-gpio-guide/)



Here are some various pictures of a working setup:

**Breadboard Prototype:**

<img src="../Images/PicoW/ControllerSetup-PicoW-Advanced-Breadboard0_small.jpg" width="39%"> <img src="../Images/PicoW/ControllerSetup-PicoW-Advanced-Breadboard1_small.jpg" width="51%">

**"Production-Level" Setup:**

<img src="../Images/PicoW/ControllerSetup-PicoW-Advanced-Raw0_small.jpg" width="45%"> <img src="../Images/PicoW/ControllerSetup-PicoW-Advanced-Raw1_small.jpg" width="45%">


## Software Setup

Everything is the same as the [Pico UART mode guide](Controller-PicoW-UART.md#software-setup).







<hr>

**Credits:**

- Kuroneko/Mysticial

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)



















