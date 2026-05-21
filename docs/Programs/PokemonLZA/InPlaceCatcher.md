# In-Place Catcher

## Program Description

Stand in one place and catch everything that spawns within locking range.

The purpose of this program is to fill your boxes up.

- [Floette Stats Reset](StatsReset.md) requires that all your boxes are filled up.
- Mass transferring Pokémon from one save to another using [Self Box Trade](SelfBoxTrade.md).

Running out of box space is a huge problem in this game. So you will want to mass transfer all your shinies out of your main and into secondary save files. But to do that, you need a lot of trade fodder to facilitate that transfer. As of this writing, Pokémon Home connectivity has not been released for this game.

This program can also be used to (inefficiently) grind Mable's research for catching each type of Pokémon 50 times.

<img src="images/InPlaceCatcher.jpg">


## Settings

**Switch Settings:**

1. Screen size: Must be 100% within the Switch settings
2. [Switch 2: All HDR options must be disabled.](../NintendoSwitch/Switch2Notes.md#switch-2-hdr-may-be-problematic)
3. [Switch 2: The profile you are using must be the 1st (left-most) profile.](../NintendoSwitch/Switch2Notes.md#resetting-a-game-moves-the-cursor-to-the-1st-user-profile)

**Program Settings:**

1. Video Resolution: 1080p or higher

**Game Settings:**

1. Text Speed: Fast


## Instructions

1. Your active Pokémon has a enough move variety to easily kill everything in your area.
2. Your active Pokémon should be able to tank everything in the area. Give it Leftovers.
3. Have lots of Poké Balls.
4. Stand in a place with a lot of spawns. (such as the house in Wild Zone 4 with all the Spinarak)
5. Start the program in the game.

The program will rotate in place and throw Poké Balls at everything it can lock onto.

- If you get attacked for long enough, the program will begin killing everything around you until you are no longer under attack.
- If you die, the program will reset the game and resume at the last point that you auto-saved from a successful catch.
- If the program detects a shiny, it will (by default) stop the program so you can catch it using the ball of your choice.
- The program will start off using whatever ball you currently have selected. If you die and it resets, it will use whatever it defaults to (usually Poké Balls).
- When the program is done (reaches max balls used), it will go the Home menu to pause the game.

Note that this program isn't particularly skilled at throwing balls. Many balls will miss, and many catches will fail. So expect to pick up a lot of lost balls at the Pokémon center.


## Options

### Max Balls

Stop the program after this many balls are thrown.


### Shiny Sound Detected Action

When a shiny sound is heard, perform one of the following actions:

- Stop program and go Home. Send notification.
- Keep running. Notify on first shiny sound only. (default)

### Take a Video

Record a video of the encounter. This will happen each time a notification is sent. So be careful if you are notifying on all shiny sounds as this may lead a lot of recorded videos of the same shiny.

### Screenshot Delay

When a shiny is detected, wait this long before you take a screenshot and record a video. This will allow the screen to completely load before taking the screenshot.




## Credits

- **Author:** Kuroneko/Mysticial


<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)






