# Device Aliases

If you use several capture cards, their default names can be difficult to tell apart. Device aliases let you give cameras, audio inputs, and audio outputs recognizable names in the CC program's dropdowns, such as "Switch 1 - Video", "Switch 1 - Audio", or "Headphones".

Aliases only change the displayed names. Device selection and saved console profiles still use the original device IDs.

## Set device aliases

1. Connect the cameras and audio devices you want to name.
2. Click **Settings** to open **Global Settings**.
3. Double-click the collapsed **Device Aliases** section to expand it. Connected devices are added to the table automatically when Global Settings opens.
4. Find each device using its **Type** and **Original Name**, then enter the name you want in its **Alias** column. Click outside the field to finish editing.
5. Return to your program panel to see the aliases in the video and audio dropdowns.

## Table columns

| Column | Meaning |
| --- | --- |
| **Type** | **Video** for cameras; **Audio** for both audio inputs and outputs. |
| **Device ID** | The original identifier used to select the device. Leave this unchanged for automatically discovered devices. |
| **Original Name** | The name reported by the device. |
| **Alias** | The name to show in the dropdowns. Leave it empty to use the original name. |

## Refresh or remove aliases

If you connect another device, leave Global Settings and open it again to update the table.

Existing aliases are preserved when the device list is updated. Disconnected devices stay in the table so their aliases are available when they reconnect.

To restore a device's original name, clear its **Alias** field. You can also delete its row; a connected device will be added again without an alias the next time you open Global Settings.
