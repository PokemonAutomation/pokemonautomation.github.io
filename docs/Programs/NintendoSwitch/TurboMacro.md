# Nintendo Switch: Turbo Macro

## Program Description

Turbo Macro lets you loop any combination of button presses and joystick movements. Thus it is primary for blind macro automation. If you create a macro and think it would be useful for others, feel free to share it on discord and other people will be able to load your macro (or we can even create a new program from it).

Macros can be saved/loaded to a JSON file. It is compatible with the [Record Keyboard Controller](RecordKeyboardController.md) program. So you can record macros using Record Keyboard Controller], load them with Turbo Macro, edit, and run.


### Instructions

None needed as it is pretty self explanatory. Once you've made your table, click Start Program to run it.


## Options

### Number of times to loop

Loop the table this many times before stopping the program.

### Controller Type

Select the controller type that the table is meant for.
- NS1: Pro Controller
- NS1: Left Joycon
- NS1: Right Joycon

Be aware that changing the controller type will clear the table. So make sure you save your table before changing controller types!


### Milliseconds

This is how many milliseconds that row should be run for.

Please be aware that small values that are smaller than the controller's "tick size" will be rounded up accordingly.

- For wired controllers, the minimum duration is 8 milliseconds.
- For wireless controllers, the minimum duration is 15 milliseconds.

The controller may further increase these durations if needed. So if you want consistency, avoid short durations.

Other useful numbers:

- The minimum duration you must press and hold down a button for the Switch to reliably see it is 40 milliseconds.
- The minimum duration that a held button must be released for the Switch to reliably see the release is 24 milliseconds.
- When game lag is taken into account, 80 milliseconds is recommended duration for a button press hold duration. Don't go below this unless you are trying to optimize timings.


### Buttons

This is a checklist of which buttons should be pressed for this row. You can select any combination you want.

Note that the GL, GR, and C buttons only exist on Switch 2 controllers. If your select controller does not ahve these buttons, these buttons will be ignored.

### Joysticks

X axis:

- Negative is left.
- Positive is right.

Y axis:

- Negative is down.
- Positive is up.

Min/max values are -1.0 and +1.0 respectively. Zero is neutral.


## Credits

- **Author:** pifopi



<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)


