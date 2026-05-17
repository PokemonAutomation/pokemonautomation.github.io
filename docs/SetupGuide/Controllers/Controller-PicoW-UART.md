# Raspberry Pi: All Pico Models (UART Mode)

**Note: This setup works on all the Pico models including the non-W ones. However, non-W Pico models will lack the wireless controllers.**

The Raspberry Pi Pico W (and Pico 2 W) is the easiest setup to get up and running (even easier than the ESP32). Thus, it is ideal for new users who just want to try out this project without getting too deep.

There are two operating modes of the Pico W family:

| **Mode** | **Connections** | **Controller Support** | **Setup Difficulty** |
| --- | --- | --- | --- |
| [USB Mode](Controller-PicoW-USB.md) | 1. Pico W's USB port -> Computer | Wireless controllers only:<br>- NS1: Wireless Pro Controller<br>- NS1: Wireless Left Joycon<br>- NS1: Wireless Right Joycon | Very Easy |
| **UART Mode (this guide)** | 1. Pico's USB port -> Switch<br>2. Pico's pins 6/7/8 -> External UART<br>3. External UART -> Computer | Both wired and wireless:<br>- HID: Keyboard<br>- NS1: Wired Controller<br>- NS2: Wired Controller<br>- NS1: Wired Pro Controller<br>- NS1: Wired Left Joycon<br>- NS1: Wired Right Joycon<br>- NS1: Wireless Pro Controller<br>- NS1: Wireless Left Joycon<br>- NS1: Wireless Right Joycon | More Difficult |
| [Advanced UART Mode](Controller-PicoW-Advanced.md) | 1. Pico's USB port -> Switch<br>2. Pico's pins 6/7/8/39 -> External UART<br>3. External UART -> Computer | Both wired and wireless:<br>- HID: Keyboard<br>- NS1: Wired Controller<br>- NS2: Wired Controller<br>- NS1: Wired Pro Controller<br>- NS1: Wired Left Joycon<br>- NS1: Wired Right Joycon<br>- NS1: Wireless Pro Controller<br>- NS1: Wireless Left Joycon<br>- NS1: Wireless Right Joycon | Most Difficult |

This is the harder version of the Pico setup. If you haven't already, we recommend following the guide for [USB mode](Controller-PicoW-USB.md) first (though USB mode requires a wireless Pico model).

In UART mode, the line of communication between the Pico and the computer is moved to an external UART instead of using the USB port. This frees up the USB port to be plugged into the Switch as a wired controller.

This is the most versatile setup as it supports every single controller in this project - both wired and wireless. 

<img src="../Images/PicoW/ControllerSetup-PicoW-UART.jpg" width="45%"> <img src="../Images/PicoW/ControllerSetup-PicoW-UART-Setup-Small.jpg" width="45%">

## Hardware Setup:

**Required Hardware (Full List):**

1. A regular [Nintendo Switch](../index.md#the-nintendo-switch) and its accessories (dock, power cable, HDMI cable). (You cannot use a Switch Lite.)
2. A [computer](../index.md#the-computer-the-player) running x64 Windows. (or another OS if you are able to set it up.)
3. A [video capture card](../index.md#video-capture-card-the-computers-eyes).
4. A Raspberry Pi Pico microcontroller. (any model will work)
5. A micro-USB to USB-A cable or adapter.
6. USB to Serial TTL (UART)

\#1-5 is the same as the Pico W USB mode. \#6 is the additional hardware that you will need.

**Estimated Total Cost (USD):** (not including computer and Nintendo Switch)

- **Single Setup:** $29 - $40
    - Capture Card: $10 - $20
    - Pico (with pins): $7 - $8
    - USB Cable/Adapter: $2
    - UART: $10
- **Bulk Purchase:** ~$20 per setup
    - Capture Card: $10
    - Pico (with pins): $7 each from Micro Center
    - USB Cable/Adapter: < $1 each from AliExpress
    - UART: $2 each from Amazon

<img src="../Images/PicoW/ControllerSetup-PicoW-UART-SetupCloseup-Annotated-Small.jpg" width="45%">


### Recommended Purchase Links:

**Capture Card:** [See previous section.](../index.md#video-capture-card-the-computers-eyes)

**Pico W Microcontroller:**

| **Model** | **Quantity** | **Price / Unit** | **Shopping Link** |
| --- | --- | --- | --- |
| Pico WH | 1 (with pins) | $7 / unit | [Micro Center](https://www.microcenter.com/product/650109/raspberry-pi-pico-wh-pico-wireless-with-headers-soldered) |
| Pico WH | 1 (with pins) | $7 / unit | [Adafruit](https://www.adafruit.com/product/5544) |
| Pico 2 WH | 1 (with pins) | $8 / unit | [Micro Center](https://www.microcenter.com/product/692334/raspberry-pi-pico-2w-with-header) |
| Pico 2 WH | 1 (with pins) | $8 / unit | [Adafruit](https://www.adafruit.com/product/6315) |
| Pico WH | 1 (with pins) | $12 / unit | [https://www.amazon.com/gp/product/B0BHM95WCM](https://www.amazon.com/gp/product/B0BHM95WCM) |
| Pico WH | 2 (with pins) | $11 / unit | [https://www.amazon.com/gp/product/B0BHM7TH1C](https://www.amazon.com/gp/product/B0BHM7TH1C) |
| Pico 2 WH | 1 (with pins + cable) | $15 / unit | [https://www.amazon.com/gp/product/B0F4W9J5CC](https://www.amazon.com/gp/product/B0F4W9J5CC) |
| Pico 2 WH | 1 (with pins) | $14 / unit | [https://www.amazon.com/gp/product/B0FGVQPZP6](https://www.amazon.com/gp/product/B0FGVQPZP6) |
| Pico W | 1 (no pins) | $6 / unit | [Micro Center](https://www.microcenter.com/product/650108/raspberry-pi-pico-w) |
| Pico W | 1 (no pins) | $6 / unit | [Adafruit](https://www.adafruit.com/product/5526) |
| Pico 2 W | 1 (no pins) | $7 / unit | [Micro Center](https://www.microcenter.com/product/687384/raspberry-pi-pico-2-w) |
| Pico 2 W | 1 (no pins) | $7 / unit | [Adafruit](https://www.adafruit.com/product/6087) |
| Pico W | 1 (no pins) | $12 / unit | [https://www.amazon.com/gp/product/B0FJFLM9DW](https://www.amazon.com/gp/product/B0FJFLM9DW) |
| Pico W | 2 (no pins) | $10 / unit | [https://www.amazon.com/gp/product/B0B72GV3K3/](https://www.amazon.com/gp/product/B0B72GV3K3/) |
| Pico 2 W | 1 (no pins) | $13 / unit | [https://www.amazon.com/gp/product/B0DPF9N1MN](https://www.amazon.com/gp/product/B0DPF9N1MN) |

Notes:

- All Pico models will work here including the non-W (no wireless) ones. The non-W Picos will simply lack the wireless controllers.
- There is no difference between the Pico W and the Pico 2 W. Both work identically for this project. The Pico 2 is newer and $1 more expensive. This project is unaffected by Pico 2 errata RP2350-E9.

Here you will need the versions with pre-soldered pins in order to connect the UART. If you have other methods of connecting such as soldering or [press-fit/hammer headers](https://www.adafruit.com/product/5938), feel free to get the pinless ones and do your own thing.

<sup>*While the wired controllers have been reported to work on a regular (non-W) Pico, it is not officially supported nor do we recommend it.</sup>

**A micro-USB  cable:**

- Micro-USB -> USB-A Adapter: [https://www.amazon.com/gp/product/B09FXJD61Z](https://www.amazon.com/gp/product/B09FXJD61Z)
- Micro-USB -> USB-A Cable: [https://www.amazon.com/Android-Compatible-Smartphones-Charging-Stations/dp/B095JZSHXQ](https://www.amazon.com/Android-Compatible-Smartphones-Charging-Stations/dp/B095JZSHXQ)

**USB to Serial TTL (UART):**

There are many options here. The one we recommend (for ease of use) is the Adafruit model:

  - [https://www.adafruit.com/product/954](https://www.adafruit.com/product/954)
  - [https://www.digikey.com/en/products/detail/adafruit-industries-llc/954/7064488](https://www.digikey.com/en/products/detail/adafruit-industries-llc/954/7064488)
  - [https://www.amazon.com/dp/B00DJUHGHI/](https://www.amazon.com/dp/B00DJUHGHI/)

<img src="../Images/UART/ControllerSetup-UART-Adafruit.jpg" width="30%">

Or you can search for "CP2102" and you'll get tons of hits from various brands/sellers that look like these:

<img src="../Images/UART/ControllerSetup-UART-CP210x-Blue.jpg" width="22%"> <img src="../Images/UART/ControllerSetup-UART-CP210x-Red.jpg" width="34.5%">

**Important:**

**DO NOT get cables with the Prolific controllers. e.g. PL2303 or any other model number.** They are cheap, do not work, and they are explicitly blocked in the program. **They often look deceptively similar to the Adafruit UART, but they are not the same.** If you buy outside of this link, verify it does not use PL controllers. If you buy it anyway, you will be wasting your time and money. **YOU HAVE BEEN WARNED!**

<img src="../Images/UART/ControllerSetup-UART-NoProlific.jpg" width="40%">

### Hardware Assembly:

Make the following connections:

| **UART pin** | **Adafruit UART Wire Color** | **Pico pin** |
| --- | --- | --- |
| RX | White | TX -> GP4 (pin 6) |
| TX | Green | RX <- GP5 (pin 7) |
| GND | Black | GND (pin 8, or any other GND pin) |
| VCC | Red | Leave unconnected |

Notes:

- **If you did *NOT* buy the Adafruit UART, your wire colors will be different!** Refer to your UART's manual or board for the correct pins. Often, with CP210x modules, the pin type is written on the board itself. Also, note that the color of the jumper wires do not matter.
- It is important to leave VCC disconnected. VCC allows the UART to power the board, but the board is already being powered by the USB. Attempting to power the board from multiple sources without the appropriate backflow protection can damage your hardware!

<img src="../Images/PicoW/ControllerSetup-PicoW-UART-Wiring-0.jpg">


## Software Setup

### Step 0: Getting Ready

Make sure you have everything else setup so that it looks like this:

<img src="../Images/GeneralSetup-CC.jpg">

If not, you should go back to the [general setup guide](../index.md) and start over.


### Step 1: Enable "Pro Controller Wired Communication".

Go into your Switch settings and enable the following option. This step is required for wired Pro Controllers and Joycons.

<img src="../../Images/Controllers/NS-ProControllerEnable.jpg">

For those of you revisiting this page, you will notice that this step is new. This is because we have begun pushing everyone to use the Pro Controller since it has more features.


### Step 2: Flash the firmware to the Pico W.

1. Unplug the Pico from everything. (both computer and dock)
2. Press and hold the white `Bootsel` button.
3. Plug the Pico's USB back into your computer while holding the `Bootsel` button. You can now release the button.
4. Go to "This PC" and look for a storage device:

     - On the Pico and Pico W, it will be named `RPI-RP2`.
     - On the Pico 2 and Pico 2 W, it will be named `RP2350`.

5. Drag and drop one of the following files into that storage device. Once the copy is done, the device will disappear.

     - Pico and Pico W: `PABotBase2-Pico1-<version>.uf2`
     - Pico 2 and Pico 2 W: `PABotBase2-Pico2-<version>.uf2`

    <img src="../Images/PicoW/ControllerSetup-PicoW-Flash1.jpg">

6. Unplug the Pico's USB from your computer. Then plug it into your Switch.
7. Plug the UART into your computer.

Note that the same firmware is used for both wireless and non-wireless Picos.


### Step 3: Install UART drivers

If your computer doesn't recognize the UART as a COM port (serial device), you may need to install the UART drivers. If you brought the Adafruit UART in this guide, the driver you will need is this:

- CP210x: [https://www.silabs.com/documents/public/software/CP210x_Windows_Drivers.zip](https://www.silabs.com/documents/public/software/CP210x_Windows_Drivers.zip)

Open up Device Manager and look for it under "Serial Ports". If you don't see it, then maybe these above drivers are not correct. Or try a different USB port.


### Step 4: Navigate to the Grip Menu

The grip menu is the only place where a wireless controller can pair with the Switch. Wired controllers have more flexibility. But for simplicity, we'll go to the grip menu regardless.

To get there from the Switch Home screen: `Controllers` (button next to the Settings gear) -> `Change Grip/Order`

<img src="../Images/GripMenu3.png">


### Step 5: Connect the Pico to the Computer Control program

1. At the top for the "Controller" option, click the dropdown and select `Serial: PABotBase2` (Make sure you choose `Serial: PABotBase2` and not `Serial: PABotBase`!)
2. In the next dropdown, select your serial device. On Windows it will be something like `COM3`.

If you don't see the device in the dropdown, you probably need to refresh it (especially if you kept the program open since Step 0). You can refresh the list by clicking "Reset Ctrl".

If everything worked correctly, it will look like this:

<img src="../Images/PicoW/ControllerSetup-PicoW-UART-Connected-Cropped.png">

If you see it stuck on `Connecting...`, try swapping the TX and RX lines between the Pico W and the UART. These are very commonly wrong!


### Step 6: Connect the Pico W to the Switch as a Wireless Controller

**(If your Pico is a non-W model that lacks the wireless capability, skip this step.)**

In the 3rd dropdown, choose "NS1: Wireless Pro Controller".

After a few seconds, you should see a controller pop-up in the Grip menu on the Switch. If not, try rebooting the Pico W by pressing the `Bootsel` button or be unplugging and replugging it. Lastly, try rebooting the Switch since sometimes it can get into a state where it refuses to accept controllers.

<img src="../Images/PicoW/ControllerSetup-PicoW-UART-Wireless-Ready.jpg">

**Status Indicator:**

- The 3 colored dots should match the colors of the controller as shown in the Switch. This helps to distinguish controllers if you have multiple of them. You can change the colors in the `Nintendo Switch -> Framework Settings` menu.
- The four alpha-numeric characters after `Paired:` are the last 2 bytes of the MAC address of the Switch that the controller is paired with.
- The 4 vertical lines after `Connected:` are the player lights that are normally found on a real controller.


### Step 7: Connect the Pico to the Switch as a Wired Controller

Now lets try a wired connection:

In the controller drop, choose "NS1: Wired Pro Controller". After a few seconds, you should see "USB" appear above the battery indicator. This means your controller has now switched to a wired connection!

If you skipped the previous step because your Pico does not support wireless, click on the video feed and press ENTER on your keyboard. This will connect your controller.

<img src="../Images/PicoW/ControllerSetup-PicoW-UART-Wired-Ready.jpg">

Even though we used the grip menu here, wired controllers will connect from almost anywhere.


### Step 8: Test the connection

You can control your Switch from the keyboard. Click on the video display to activate the keyboard controls. Then try pressing some buttons. You can view the keyboard -> controller mapping by clicking on the "keyboard layout" at the bottom left corner of the program.

The default keyboard layout is the English QWERTY layout. If you have a different layout, you can change the mappings in `Nintendo Switch -> Framework Settings` and scroll down to the controller mapping tables.

We recommend familiarizing yourself with the keyboard controls as this is the preferred way to control your Switch while setting up to run a program. Each controller type has a different keyboard mapping. By default, the joystick (left joystick for Pro Controller) is mapped to the usual WASD setup that's used in FPS games. For joycons, there are two sets of mappings (using different keys) that will serve both vertical and sideways orientations.

Overall, the idea here is that you can play your Switch from your computer. While it's not as nice as using a native controller, it is good enough to easily setup programs - especially if you're doing this remotely where you do not have physical access to the Switch.

<img src="../Images/PicoW/ControllerSetup-PicoW-UART-Controls.jpg">

**Controller Types:**

You will notice that there are 10 controller options:

- None
- [HID: Keyboard](../ControllerGuide.md#hid-keyboard)
- [NS1: Wired Controller](../ControllerGuide.md#ns1-wired-controller)
- [NS2: Wired Controller](../ControllerGuide.md#ns2-wired-controller)
- [NS1: Wired Pro Controller](../ControllerGuide.md#ns1-wired-pro-controller)
- [NS1: Wired Left Joycon](../ControllerGuide.md#ns1-wired-leftright-joycon)
- [NS1: Wired Right Joycon](../ControllerGuide.md#ns1-wired-leftright-joycon)
- [NS1: Wireless Pro Controller](../ControllerGuide.md#ns1-wireless-pro-controller)
- [NS1: Wireless Left Joycon](../ControllerGuide.md#ns1-wireless-leftright-joycon)
- [NS1: Wireless Right Joycon](../ControllerGuide.md#ns1-wireless-leftright-joycon)

Click on the link for detailed documentation for the controller type. "None" simply idles the Pico and turns off its antenna so it isn't trying to connect to a Switch. The others tell the Pico to act as that controller respectively. Setting to "None" is a convenient way to disconnect the Pico so you can connect your physical controller.

Every time you press "Reset Ctrl" or change the controller type, it will disconnect from your Switch and try to reconnect using the new controller type. If the new controller is a wireless controller that has not been previously paired with the Switch, you will need to be in the Grip menu for the new controller to pair. See [Pairing Behavior](#pairing-behavior).

Changing programs (or even closing the application entirely) will not disconnect the Pico from the Switch. When you load a program and connect to the Pico, it will automatically continue its previous connection to the Switch (and change the controller dropdown accordingly).

**Connecting as a Joycon:**

When you connect as a joycon, it will behave like a normal joycon. It doesn't immediately connect and wants you to either pair with a 2nd joycon or press SL+SR to put it into horizontal mode.

For the right joycon, you can press the Home button to immediately leave the grip menu. This will let you easily start LGPE programs which use the right joycon. The left joycon doesn't have this option and will require you to either pair with a right joycon or to enter horizontal mode. There are currently no programs that use the left joycon.

To enter horizontal mode, you can press SL+SR on the keyboard controls by pressing F1 and F3 at the same time. This will let you exit the grip menu and enter a game like LGPE that requires a joycon. But keep in mind that this will also rotate the controls by 90 degrees (IOW, confusing). Check the keyboard mapping for both vertical and horizontal joycon orientations.

*You cannot easily pair two Pico joycons anyway since you need to press L+R on them simultaneously and the keyboard controls don't allow you simultaneously press buttons on different controllers. However, you can easily pair a Pico joycon with a real joycon.


### Step 7: You are done!

If keyboard commands are working (along with video and audio), you are done!

Try clicking on other programs on the sidebar. You will find that all of them are "virtual consoles" that will accept keyboard commands. At the top of every program is a link to the wiki that explains how to setup and use that program.

Continue on to [Finishing Up](../index.md#step-4-finishing-up)!


## Pairing Behavior:

When you connect a Pro Controller or a Joycon to the Switch, it will remember its pairing state with that Switch. Wired and wireless version of the same controller share the same pairing state. So pairing one will automatically pair the other. However each different controller type has a separate pairing state. So pairing the left joycon will not automatically pair the right joycon.

Keep in mind the following behaviors:

- When you switch from a different controller to a controller that was previous paired, it will reconnect to the same console it is paired with.
- When you click "Reset Ctrl", it will disconnect and try to reconnect to the console that it was paired with.
- When you SHIFT + click "Reset Ctrl", not only does it reset, it will clear the pairing state and try to pair with a new console.
- The Pico will forget its pairing state when it loses power. So unlike a real controller, it is not stored in non-volatile memory.

Once a Pico controller is paired with a console, it will be able to reconnect wirelessly outside of the grip menu.


## Troubleshooting:

### Docking and undocking the Switch resets or hangs the Pico.

Main Article: [Power Glitching](../../PowerGlitching.md)

If you are experienced with circuits and would like to attempt a hardware fix, see [Pico W (Advanced)](Controller-PicoW-Advanced.md).



<hr>

**Credits:**

- Kuroneko/Mysticial

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)
























