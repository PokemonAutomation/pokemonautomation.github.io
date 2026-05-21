# RNG Helper (in development)

## Program Description

Semi-automate button presses for performing RNG manipulation in FireRed and LeafGreen. This program requires some knowledge of how RNG manipulation is performed as well as external tools to select your target frame and advance.

This program includes options for several RNG targets:

#### Gifts
- Bulbasaur / Squirtle / Charmander (Starters)
- Magikarp (Route 4 Gift)
- Hitmonchan / Hitmonlee (Saffron City Gift)
- Eevee (Celadon City Gift)
- Lapras (Silph Co. Gift)
- Omanyte / Kabuto / Aerodactyl (Fossils)
- Game Corner Prizes
   - Abra
   - Clefairy
   - Scyther / Pinsir
   - Dratini
   - Porygon
- Togepi (Water Labyrinth Gift Egg)

<img src="images//RngHelper-0.jpg" width="600">

#### Static Encounters
- Electrode (Power Plant)
- Snorlax (Routes 12 and 16)
- Articuno / Zapdos / Moltres
- Mewtwo
- Hypno (Berry Forest)
- Ho-oh (Navel Rock)
- Lugia (Navel Rock)
- Deoxys (Birth Island)

<img src="images//RngHelper-1.jpg" width="600">

#### Random Encounters
- Sweet Scent (for any location where wild Pokémon spawn when walking or surfing)
- Fishing
- Safari Zone

<img src="images//RngHelper-2.jpg" width="600">


## Instructions

**Switch Settings:**

1. Screen size: Must be 100% within the Switch settings
2. System memory: If the game data for FireRed/LeafGreen is on an SD card, move it to the Switch's system memory to reduce variability of reset times.
3. Single-Profile Users: If you only have one user profile, make sure you disable 'Skip Selection Screen' in System Settings -> User settings.
4. Disable Auto Sleep: Make sure to disable the 'Auto-Sleep' feature in System Settings -> Sleep Mode -> Auto-Sleep
5. [Switch 2: All HDR options must be disabled.](../NintendoSwitch/Switch2Notes.md#switch-2-hdr-may-be-problematic)
6. [Switch 2: The profile you are using must be the 1st (left-most) profile.](../NintendoSwitch/Switch2Notes.md#resetting-a-game-moves-the-cursor-to-the-1st-user-profile)


**Program Settings:**

1. Video Resolution: 1080p or higher

**Game Settings:**

1. Text Speed: Fast
2. Button Mode: **NOT L=A**
3. Frame: Type 1
4. Mono / Stereo depending on your target Seed

### Before You Start

- Know your Secret ID and use it to determine your target Seed and Advance. See the [SID Helper](SidHelper.md) program for a way to obtain your Secret ID.

- Be ready to manually adjust your timings. This program does not perform automatic calibration!

- Come prepared. Ensure you have any necessary Pokémon (e.g. a Sweet Scent user) and items (e.g. a Super Rod, Pokéballs, Max Repel) required by your target

- If fishing, register the rod of your choice to the SELECT button

- If using the Teachy TV, place it at the top of your KEY ITEMS pocket.

<img src="images//RngHelper-3.jpg" width="600">

### Instructions

Refer to the following tables for setup instructions for each target:

#### Gifts

For all gifts/prizes, make sure you have a free spot in your party to allow the program to check the Pokémon you obtain.

| Target | Image |
| --- | --- |
| **Starters**<br>- Save facing the Pokéball with your desired starter | [<img src="images//RngHelper-starters.jpg" width="600">](images//RngHelper-starters.jpg) |
| **Magikarp**<br>- Have at least 500 Pokédollars <br>- Save facing the Magikarp salesman | [<img src="images//RngHelper-magikarp.jpg" width="600">](images//RngHelper-magikarp.jpg) |
| **Hitmonchan / Hitmonlee**<br>- Save facing the Pokéball with your desired choice | --- |
| **Eevee**<br>- Save facing Eevee's Pokéball | [<img src="images//RngHelper-eevee.jpg" width="600">](images//RngHelper-eevee.jpg) |
| **Lapras**<br>- Save facing the Silph Co. employee | [<img src="images//RngHelper-lapras.jpg" width="600">](images//RngHelper-lapras.jpg) |
| **Fossils**<br>- Give a fossil to the scientist at the Cinnabar Lab <br>- Exit and reenter the building <br>- Save next to the scientist | [<img src="images//GiftReset-1.png" width="600">](images//GiftReset1.png) |
| **Game Corner Prizes**<br>- Have enough coins to purchase your desired prize <br>- Save facing the prize counter | [<img src="images//RngHelper-gamecorner.jpg" width="600">](images//RngHelper-gamecorner.jpg) |
| **Togepi**<br>- Set your lead Pokémon to something with maximum Friendship <br>- Use your bicycle <br>- Save facing the old man | [<img src="images//RngHelper-togepi.jpg" width="600">](images//RngHelper-togepi.jpg) |


#### Static Encounters

For all static encounters, make sure you have all Pokémon and items you need to succeed in catching your target.

| Target | Image |
| --- | --- |
| **Static Overworld Encounters**<br>- Valid for anything not otherwise listed in this table <br>- (Optional) Pick up any overworld items and break any smashable rocks to prevent them from adding RNG advances <br>- Save facing the Pokémon <br>- For Deoxys, solve the puzzle on Birth Island and save in front of the red triangle | [<img src="images//RngHelper-deoxys.jpg" width="600">](images//RngHelper-deoxys.jpg) |
| **Snorlax**<br>- Obtain the Pokéflute <br>- Save facing Snorlax | [<img src="images//RngHelper-snorlax.jpg" width="600">](images//RngHelper-snorlax.jpg) |
| **Mewtwo**<br>- Save facing the Mewtwo | --- |
| **Ho-oh**<br>- Save at the top of the steps at the very top of Navel Rock <br>- The encounter with Ho-oh is triggered after taking another step northward | [<img src="images//RngHelper-hooh.jpg" width="600">](images//RngHelper-hooh.jpg) |
| **Berry Forest Hypno**<br>- Save facing Lostelle in Berry Forest | --- |


#### Random Encounters

For all random encounters, make sure you have all Pokémon and items you need to succeed in catching your target.

| Target | Image |
| --- | --- |
| **Sweet Scent**<br>- Travel to a location where your target spawns (in tall grass, a cave, etc.) <br>- Move a Pokémon with Sweet Scent to the last occupied slot in your party <br>- Save the game | --- |
| **Fishing**<br>- Register the fishing rod you'd like to use to the SELECT button <br>- Travel to the water's edge where your target spawns <br>- Save the game | --- |
| **Safari Zone**<br>- If fishing, register the rod you'd like to use to the SELECT button <br>- Have at least 500 Pokédollars <br>- Stand atop the Pokéball logo on the floor of the Safari Zone entrance <br>- Use a Max Repel <br>- Save the game | [<img src="images//RngHelper-safarizone.jpg" width="600">](images//RngHelper-safarizone.jpg) |


**For all targets, start the program after saving.**

#### Calibration

After performing the in-game setup for your target, run the program for 1 reset and obtain whatever Pokémon you encounter. Determine how much you missed your seed and advance and adjust their calibration offsets as needed.
Repeat until you hit your target.

There can be a small amount of inconsistency in the program, particularly when it comes to hitting seeds. If you are consistently within ±1 of your seed and advance, it might be a good idea to set Max Resets higher than 1 and let the program loop through several attempts until it hits a shiny.

## Options

### Max Resets:

Set this to the maximum number of resets to attempt. Only use this after you've dialed in your calibrations.

### Seed Button:

The button to be pressed when setting the seed. Set this with the help of an external RNG tool.

### Extra Button:

Additional button presses during reset necessary to hit the target seed. Set this with the help of an external RNG tool.

### Seed Delay Time (ms):

Sets the target amount of time to wait between starting the game and pressing A on the title screen. Set this with the help of an external RNG tool. 
Because the program needs to wait for the entire title screen sequence to finish, 30473ms is the lowest supported seed delay.

### Seed Calibration (ms):

Modifies the seed delay time. This should be changed in the opposite of the direction that you missed your seed.
*Example: if you missed your target seed by +16ms (meaning the button press was too late), **decrease** your seed calibration by -16 (shortening the delay)*.

### Continue Screen Frames:

The number of RNG advances before loading the game. Set this with the help of an external RNG tool.
These pass at the "normal" rate compared to other consoles, with 1 RNG advance every frame.
Note that the Advances of your target should be equal to the sum of your Continue Screen Frames and In-Game Advances.

### Continue Screen Frames Calibration:

A "fine adjustment" that modifies the RNG advances passed on the Continue Screen. Set this to offset the program's timing by amount you missed your target advance.
If you've missed your advance frame, you can calibrate your timing using either the Load Screen or In-Game advances.
*Example: if your target advance was 10000 and you hit 10025, you can **decrease** your calibration value by 25.*

### In-Game Advances:

The number of in-game RNG advances before triggering the gift/encounter. Set this with the help of an external RNG tool.
These pass at double the rate compared to other consoles, where every frame results in 2 RNG advances.
If using the Teachy TV, which advances frames at x313 speed, most of your target advances should be passed in-game. 
*Warning: this value needs to be long enough to accomodate all in-game button presses prior to the gift/encounter*

### In-Game Calibration (frames):

A "coarse adjustment" that modifies the RNG advances passed after loading the game.
If you've missed your advance frame, you can calibrate your timing using either the Load Screen or In-Game advances.
Note that In-Game advances can only result in 2 by 2 changes in hit advances.
*Example: if your target advance was 10000 and you hit 8500, you can **increase** your calibration value by 1500.*

### Use Teachy TV:
If checked, the program will open the Teachy TV to quickly advance in-game frames at 313x speed.
*Warning: can result in larger misses before calibration*

### User Profile Position:

The position, from left to right, of the Switch profile with the FRLG save you'd like to use.
If this is set to 0, Switch 1 defaults to the last-used profile, while Switch 2 defaults to the first profile (position 1).
Only useful if using a Switch 2 and playing on a profile other than the primary one.

### Take Video:

Record a video when a shiny is found.

### Go Home when Done:

Go to the Switch Home to idle when finished.

## Credits

- **Author:** Astro (Tom)


<hr>

**Discord Server:** 


[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)

