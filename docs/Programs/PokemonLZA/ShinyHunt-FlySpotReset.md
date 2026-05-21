# Shiny Hunt - Fly Spot Reset

See also: [Shiny Hunting Recommendations](ShinyHuntRecommendations.md)

## Program Description

Shiny hunt by repeatedly fast traveling to the same spot outside Lumiose Wild Zones after following certain pre-determined route. This will shiny hunt all spawns within 50m of the fly spot and the route. Unlike blind macros, this program will tolerate the day/night cycle and will detect audible shinies that are nearby.

By choosing to fast travel without character movement, this program can shiny hunt:
- An alpha Swirlix near Nouveau Cafe (Truck No. 3).
- A non-alpha Swirlix near the same cafe
- A Dedenne/Emolga spawner on the street near Magenta Pokémon Center.
- Two Mareep and a Pichu in Wild Zone 1 near Pokémon Research Lab. (The Mareep are about 50m from the lab. They can be hunt on Switch 2. Unclear on Switch 1.)
- Pokemon near the entrance of a Hyperspace Wild Zones.

By picking a route, this program can shiny hunt:
- More Pokémon in Wild Zone 19.
- Alpha Pidgey in Wild Zone 1.

This program only works for fly spots outside Wild Zones in Lumiose City. To shiny hunt more Pokémon in Wild Zone 1 - 20, use our [Shiny Hunt - Wild Zone Entrance](ShinyHunt-WildZoneEntrance.md) program.
To shiny hunt Pokémon near the two Cafes located inside a Wild Zone (Café Bataille in Wild Zone 6 or Café Ultimo in Wild Zone 15), use our [Shiny Hunt - Wild Zone Cafe](ShinyHunt-WildZoneCafe.md) program.

With the Shiny Charm you will get a shiny Pokémon quite fast if there are many Pokémon spawned around you. Don't let the program run for too long or have old shinies overwritten by new ones.

Shiny sound detection will happen at most once to avoid detecting the same shiny Pokémon over and over.


## Settings

**Switch Settings:**

1. Screen size: Must be 100% within the Switch settings
2. [Switch 2: All HDR options must be disabled.](../NintendoSwitch/Switch2Notes.md#switch-2-hdr-may-be-problematic)

**Program Settings:**

1. Video Resolution: 1080p or higher

## Instructions

1. If you wish to hunt in Hyperspace, use a donut with AT LEAST ONE flavor power for the program to read Calorie number correctly.
2. Fast travel to a fly spot in Hyperspace or in Lumiose City but outside any Wild Zones.
3. Start the program in the game.


## Options

### Hunt Route

The route to follow.

- No Movement in Lumiose
- Hyperspace Wild Zone
- Wild Zone 19
- Alpha Pidgey (Wild Zone 1)


#### No Movement in Lumiose

Fast travel to a fly spot in Lumiose City, e.g. Nouveau Cafe No. 3, Pokémon Research Lab, etc.

[<img src="images/ShinyHunt-FlySpotReset1.png" width="800">](images/ShinyHunt-FlySpotReset1.png)
[<img src="images/ShinyHunt-FlySpotReset3.png" width="800">](images/ShinyHunt-FlySpotReset3.png)

#### Hyperspace Wild Zone

You are in Hyperspace and not regular Lumiose. Be sure to set the Hyperspace Resets option below:

**Max Hyperspace Resets**: Number of resets when running the Hyperspace Wild Zone route. The program will fly reset the specified number of times, then go to home to pause the Cal. timer. This setting does not apply when any other route is selected. Make sure to leave enough time to catch found shinies.

**Minimum Cal. allowed While Resetting in Hyperspace**: The program will stop when the detected calorie number is small or equal to this number.

When hunting in Hyperspace, be mindful of how fast calorie burns. Cal. per sec: 1 Star: 1 Cal./s, 2 Star: 1.6 Cal./s, 3 Star: 3.5 Cal./s, 4 Star: 7.5 Cal./s, 5 Star: 10 Cal./s. Each reset takes between 0.6-1.0 sec of the timer. Calculate how long you wish to let the program run accordingly.

#### Wild Zone 19

Fast travel to Wild Zone 19, standing in front of the entrance. This route covers right half of the wild zone, including Furfrou, Audino, Eevee, Kangaskhan, Cleffa/Clefairy (night only), Drampa (daytime only), and a Patrat outside of the wild zone.

[<img src="images/ShinyHunt-ShuttleRun-WildZone19.jpg" width="800">](images/ShinyHunt-ShuttleRun-WildZone19.jpg)

#### Alpha Pidgey (Wild Zone 1)

Fast travel to Pokémon Research Lab. This route will makes the character run repeatedly from the lab to the building near Wild Zone 1 and get to the roof by the elevator. While the target is the Alpha Pidgey in Wild Zone 1, it also reaches other regular Pidgey (can't be alpha) on the roof or lamppost, Kakuna tree, Mareep and Pichu in Wild Zone 1, a Buneary in a fenced yard, and a Hawlucha on the roof.

[<img src="images/ShinyHuntLocations/FlySpotReset-AlphaPidgey-Start.jpg" width="800">](images/ShinyHuntLocations/FlySpotReset-AlphaPidgey-Start.jpg)
[<img src="images/ShinyHuntLocations/FlySpotReset-AlphaPidgey.jpg" width="800">](images/ShinyHuntLocations/FlySpotReset-AlphaPidgey.jpg)


### Shiny Sound Detected Action

When a shiny sound is heard, perform one of the following actions:

- Stop program and go Home. Send notification.
- Keep running. Notify on first shiny sound only. (default)
    - When running at Nouveau Cafe (Truck No. 3), the program will detect shiny sound if the alpha Swirlix becomes shiny.


## Credits

- **Author:** Gin


<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)













