# Device Aliases

If you use several capture cards, their default names can be difficult to tell apart. Device aliases let you give each camera and audio input a name such as "Switch 1 - Video" or "Switch 1 - Audio" in the CC program's dropdowns.

Aliases only change the names displayed in the CC program. Device selection and saved settings still use the original device IDs.

## Find your settings folder

Aliases are configured in a file named `deviceAliases.json` inside `UserSettings/`.

## Find the device IDs

The keys in the alias file must be the original device IDs, which may differ from the names shown in the dropdowns. You can get them from a saved console profile:

1. Open **Virtual Console** and select the camera and audio input you want to name. Check the video and audio to confirm which Switch they belong to.
2. Click **Save Profile** and save the console settings to a JSON file.
3. Open that profile in a text editor. Copy the string value of `"Camera"` from the video settings and `"InputSource_Device"` from the audio settings. These are the camera and audio input IDs, respectively.
4. Repeat for each capture card you want to name.

Copy the complete quoted JSON strings, preserving any escaped characters such as `\\`.

## Alias file

1. Close the CC program.
2. Create `deviceAliases.json` in your settings folder using a plain text editor.
3. Add your aliases using the format below. Replace each placeholder key with the corresponding device ID copied from your profile.

```json
{
    "Cameras": {
        "CAMERA_ID_FROM_SWITCH_1_PROFILE": "Switch 1 - Video",
        "CAMERA_ID_FROM_SWITCH_2_PROFILE": "Switch 2 - Video"
    },
    "AudioInputs": {
        "AUDIO_ID_FROM_SWITCH_1_PROFILE": "Switch 1 - Audio",
        "AUDIO_ID_FROM_SWITCH_2_PROFILE": "Switch 2 - Audio"
    }
}
```

4. Start the CC program. The camera and audio input dropdowns will now show your aliases.

Aliases are loaded once per application run. **Restart the CC program after every change** to `deviceAliases.json`; refreshing the device list alone will not reload the file.
