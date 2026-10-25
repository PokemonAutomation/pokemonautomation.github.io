# Nintendo Switch: Typewriter

## Program Description

Typewriter types the text you enter into the option box, using the HID keyboard controller. It is useful for entering arbitrary text on the Switch (save file names, friend requests, messages, etc.) without having to mash each character by hand.

Only plain ASCII text is supported. Newline characters press Enter.

### Keyboard Layout

The program sends raw HID key presses, so it has to know how the Switch interprets the physical keyboard. The "Keyboard Layout" option should match the language/keyboard layout the Switch is configured for:

- **QWERTY**: English (and other QWERTY-based) languages. Every printable ASCII character can be typed with a single key press plus at most Shift.
- **AZERTY**: French. Note that a few characters (`# < > @ [ ] ^ ` { }`) can only be typed with the AltGr key on a French keyboard and are **not supported** by this program yet.

## Instructions

1. Make sure the keyboard controller is connected and is the active controller.
2. Enter the text to type in the "Text to Type" box.
3. Set "Keyboard Layout" to match the Switch's language.
4. Put the cursor in the text field on the Switch you want to type into.
5. Start the program. It types the whole text and then stops.

The timing of each key press comes from the global "Keyboard Controller" settings in the Nintendo Switch settings panel.

## Options

- **Text to Type**: The plain ASCII text to type. Newlines press Enter.
- **Keyboard Layout**: The layout the Switch's physical keyboard is configured for (i.e. the Switch's language).

## Credits

- **Author:** Kuroneko
