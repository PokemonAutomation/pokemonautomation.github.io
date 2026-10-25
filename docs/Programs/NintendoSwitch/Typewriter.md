# Nintendo Switch: Typewriter

## Program Description

Typewriter types the text you enter into the option box, using the HID keyboard controller. It is useful for entering arbitrary text on the Switch (save file names, friend requests, messages, etc.) without having to mash each character by hand.

Only plain ASCII text is supported. Tab presses Tab and newlines press Enter. Windows (CRLF) line endings are accepted; a standalone carriage return is an error.

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

## Options

- **Text to Type**: The plain ASCII text to type. Tab presses Tab, newlines press Enter, and CRLF line endings are accepted.
- **Keyboard Layout**: The layout the Switch's physical keyboard is configured for (i.e. the Switch's language).
- **Delay**: The delay between key presses. Default: 24 ms.
- **Hold**: The duration each key press is held down. Default: 40 ms.
- **Cooldown**: How long after release a key cannot be reused. Default: 24 ms.

## Credits

- **Author:** Kuroneko
