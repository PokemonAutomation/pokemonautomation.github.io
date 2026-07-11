# Date Spam - Watt Farmer

## Program Description

WattFarmer will farm watts from a wishing piece beam. It requires activating the Y-Comm glitch for best efficiency.

**Switch 1:**

- **Wired Controller:** 9.0 seconds/fetch (~800k watts per hour at 2000/fetch)
- **ESP32 Wireless:** 9.5 seconds/fetch (~760k watts per hour at 2000/fetch)
- **sys-botbase 2.x:** 16.3 seconds/fetch (~440k watts per hour at 2000/fetch)
- **sys-botbase 3.0:** TBD

**Switch 2:**

- **Wired Controller:** 9.6 seconds/fetch (~750k watts per hour at 2000/fetch)

<img src="images/DateSpam-WattFarmer-0.jpg">

## Settings

**Switch Settings:**

1. Screen size: Must be 100% within the Switch settings
2. [Switch 2: All HDR options must be disabled.](../NintendoSwitch/Switch2Notes.md#switch-2-hdr-may-be-problematic)
3. [Switch 2: The profile you are using must be the 1st (left-most) profile.](../NintendoSwitch/Switch2Notes.md#resetting-a-game-moves-the-cursor-to-the-1st-user-profile)
4. System Time: Unsynced

**Program Settings:**

1. Video Resolution: 720p or higher

**Game Settings:**

1. Text Speed: Fast
2. Casual mode: Off
3. Y-Comm glitch must be active
    1. Verify the glitch is active by checking for a "flash" when re-entering the game from the Home menu.
    2. NOTE: Activating the Y-Comm glitch requires Nintendo Switch Online (NSO). If you don't have NSO, uncheck "I have Nintendo Switch Online" in the Computer Control program and the program will not require the Y-Comm glitch. However, farming Watts is much slower without using the Y-Comm glitch.
4. You must be offline.
5. Airplane mode must be off.

   > **Stability Recommendation:** Stand ***behind*** the den so that the beam is directly in front of your character. Sometimes, the program will miss a button press which causes the date-spamming to happen in the game instead of the Switch settings. This will cause the character to move downwards and away from the den if you're not standing behind it.

### Activating the Y-Comm glitch

Video tutorial: https://www.youtube.com/watch?v=cZTB1ZGZu18

As mentioned above, you need to have Nintendo Switch Online in order to activate this glitch.

1. Go to a secure indoor location in game like a Pokécenter and save your game. This isn't strictly necessary, but it's safer so you don't get attacked by wild Pokemon, while you try to activate this glitch.
3. Undock the Switch so that it's in hand-held mode. This allows you to easily toggle Airplane Mode from within the game.
4. Click the 'Y' button to open Y-Comm. Then click the '+' button to connect to Internet.
5. Select 'Link Battle'. Then click 'Single Battle'. Do not set a Link Code.
6. Press A to clear the text boxes. The game then backs you out of Y-Comm.
7. While the game searches for an opponent, hold the Home Button to access quick settings. Then hover over Airplane Mode.
8. Once you see text announcing that "an opposing Trainer has been found", toggle airplane mode on and off again to disconnect from the internet. When you do this, you will see an error message.
    - NOTE: Depending on when you try to activate this glitch, there may not be very many users online to battle. So, it can take several minutes to find an opponent. You just need to be patient.
9. Hide the Quick Settings and close the error message.
10. The Y-Comm glitch is now active. To confirm, click the home button to return to the Switch Home menu, then re-enter the game. If the screen "blinks", the glitch was done correctly.

## Instructions

1. You must be standing in front of a wishing piece den with watts collected.
2. Your location should be safe from getting attacked by wild Pokémon.
3. Start the program in game or the [Change Grip/Order Menu](https://github.com/PokemonAutomation/Microcontroller/blob/master/Wiki/Programs/NintendoSwitch/ChangeGripOrderMenu.md) depending on which option you choose.


## Options

This program does not have the ability to avoid the system update window. Should the window appear while the program is running, the program will enter a safe do-nothing loop within the Switch settings.

Most of the options here are self-explanatory.

<img src="images/DateSpam-WattFarmer-Settings.jpg">


## Credits

- **Author:** Kuroneko/Mysticial
- **Optimized:** SakuraKim
- **Ported to CC:** Kuroneko/Mysticial


<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)


