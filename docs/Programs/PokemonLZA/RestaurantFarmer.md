# Restaurant Farmer

## Program Description

Repeatedly battle the restaurants to farm experience, items, and money.

There are currently 4 restaurants suitable for this:

- Restaurant Le Nah (1 Star)
- Restaurant Le Yeah (2 Star)
- Restaurant Le Wow (3 Star)
- Sushi High Roller (Multi-battles)

<img src="images/RestaurantFarmer.jpg">


## Settings

**Switch Settings:**

1. Screen size: Must be 100% within the Switch settings
2. [Switch 2: All HDR options must be disabled.](../NintendoSwitch/Switch2Notes.md#switch-2-hdr-may-be-problematic)

**Program Settings:**

1. Video Resolution: 1080p or higher

**Game Settings:**

1. Text Speed: Fast


## Instructions

1. Make sure you have all 3 Gold Canari Plushies. Otherwise you will lose money over time!
2. Stand facing the restaurant receptionist.
3. Start the program in the game.

This program has 2 modes: With and without a battle AI.

**With Battle AI (new to v0.59.5):**

In this mode, the program will choose the move with the best type effectiveness against the opponents. In the event of a tie, they will chosen in this priority order:

- Top
- Left
- Right
- Bottom


**Without Battle AI:**

In this mode, the program will the 4 moves in the following priority:

- Top
- Left
- Right
- Bottom


In both modes, if your Pokémon faints, it will automatically timeout and switch to the next Pokémon in your party. Keep that in mind if you expect your lead to faint. The move priority is the same for all members of your party.


### Tips

With battle AI enabled, have 4 strong moves of different types that maximize type coverage. The order does not matter.

When to pick each restaurant:

- **Restaurant Le Nah**: You want to farm battle wins for Mable's Research or you want to farm some money but dont have much money-in-hand and dont have Pokémon trained for harder restaurants
- **Restaurant Le Yeah**: You want to farm some exp but dont have Pokémon trained for harder restaurants
- **Restaurant Le Wow**: You want to farm lots of exp and good money. You have some money-in-hand and have leveled up and trained Pokémon
- **Sushi High Roller**: You want to maximize money farming and/or farm Seeds of Mastery. You have lots of money-in-hand and have relatively leveled and trained Pokémon

<Table>
  <tr>
    <th></th>
    <th>Restaurant Le Nah</th>
    <th>Restaurant Le Yeah</th>
    <th>Restaurant Le Wow</th>
    <th>Sushi High Roller</th>
  </tr>
  <tr>
    <th>Difficulty</th>
    <td>Easy</td>
    <td>Medium</td>
    <td>Hardest</td>
    <td>Hard</td>
  </tr>
  <tr>
    <th>Rounds</th>
    <td>3</td>
    <td>5</td>
    <td>10</td>
    <td>5</td>
  </tr>
  <tr>
    <th>Fee</th>
    <td>3,000</td>
    <td>15,000</td>
    <td>100,000</td>
    <td>30,000</td>
  </tr>
  <tr>
    <th>Battle Earnings*</th>
    <td>6,480</td>
    <td>16,200</td>
    <td>39,600</td>
    <td>0</td>
  </tr>
  <tr>
    <th>Item Reward Sale Value</th>
    <td>1,250</td>
    <td>7,500**</td>
    <td>100,000</td>
    <td>40,000</td>
  </tr>
  <tr>
    <th>Net Profit w/o Items*</th>
    <td>3,480</td>
    <td>1,200</td>
    <td>-60,400</td>
    <td>-30,000</td>
  </tr>
  <tr>
    <th>Net Profit w/ Items*</th>
    <td>4,730</td>
    <td>8,700</td>
    <td>39,600</td>
    <td>10,000</td>
  </tr>
  <tr>
    <th>Minutes per Round*</th>
    <td>2.67 minutes</td>
    <td>5 minutes</td>
    <td>10 minutes</td>
    <td>2.25 minutes</td>
  </tr>
  <tr>
    <th>Profit (w/o Items) per Hour*</th>
    <td>78,202 per hour</td>
    <td>14,400 per hour</td>
    <td>-362,400 per hour***</td>
    <td>-800,000 per hour***</td>
  </tr>
  <tr>
    <th>Profit (w/ Items) per Hour*</th>
    <td>106,292 per hour</td>
    <td>104,400 per hour</td>
    <td>237,600 per hour</td>
    <td>266,667 per hour</td>
  </tr>
  <tr>
    <th>Other Rewards</th>
    <td>3 Exp Candy S</td>
    <td>4 Exp Candy M</td>
    <td>10 Exp Candy L</td>
    <td>1 Seed of Mastery</td>
  </tr>
  <tr>
    <th>Exp Gain</th>
    <td>Low</td>
    <td>Medium</td>
    <td>Highest</td>
    <td>High</td>
  </tr>
</Table>

\* Values are estimates with 3 Gold Canari Plush. Time estimates are taken from optimized runs with quick KOs and a single Pokémon  
\*\* Le Yeah's 30x Tiny Mushroom reward can hit the 999 item limit which significantly cuts into profit. This maxes out in an estimated 3 hours  
\*\*\* Le Wow and Sushi High Roller give the most money but rely heavily on item rewards for that money. Your money-in-hand will actually decrease over time so you need initial seed money. You cannot run these indefinitely

### Recommended Pokémon

**Restaurant Le Nah**: No special considerations

**Restaurant Le Yeah**: To avoid being stalled by Talonflame/Altaria, choose Pokémon with these attributes:

  - Talonflame's Flame Wheel should not be the highest damaging option against your Pokémon. Talonflame's moves are Hurricane, Flame Wheel, U-Turn, and Steel Wing
  - The highest priority move should one-hit KO Talonflame. Talonflame is level 45 so the bar is fairly low.

**Restaurant Le Wow**: The hardest restaurant which encourages high leveled and EV trained Pokémon

- Dragalge can solo the entire round and is likely the only solo option for long term farming. This leaves 5 open slots for exp training:

    <table>
      <tr>
        <td>
          <b>Dragalge</b> @ Shell Bell<br>
          Level 100<br>
          EVs: 252 HP / 252 SpA<br>
          Modest Nature<br>
          - Sludge Bomb   (Top)<br>
          - Dragon Pulse  (Left)<br>
          - Thunderbolt   (Right)<br>
          - Hydro Pump    (Bottom)<br>
          <i>[Move Selection AI enabled, Plus Moves disabled]</i>
        </td>
        <td>
          <b>Dragalge</b> @ Shell Bell<br>
          Level 100<br>
          EVs: 252 HP / 252 SpA<br>
          Modest Nature<br>
          - Sludge Bomb   (Top)<br>
          - Dragon Pulse  (Left)<br>
          - Thunderbolt   (Right)<br>
          - Focus Blast   (Bottom)<br>
          <i>[Move Selection AI enabled, Plus Moves disabled]</i>
        </td>
      </tr>
    </table>
  
- Considerations when using your own Pokémon
  
    - Some form of healing is recommended. Shell Bell and/or draining moves are good options
    - The first opponent will attempt to poison you. The Pokémon that's sent out first will likely faint to this if it's not Poison or Steel type
    - The second opponent can potentially burn your Pokémon. It will cripple physical attackers and your Pokémon may not be able to outheal the burn
    - The second opponent also has moves that can angle the camera away and kill the run if the Pokémon are not immediately one-hit KO'd
    - The fourth opponent has Rocky Helmet and stall tactics. If you're using contact moves, you may take significant damage here
    - The best defense is a good offense, you'll take more damage if you're not able to quickly one-hit KO your opponents


**Sushi High Roller**: 3 Pokémon at once. You'll want something to KO everything quickly

- The player is not immune to damage here so you can lose if the player takes too much damage from stray attacks
- Choose Pokémon that have good ranged AOE moves that can knock out all 3 Pokémon quickly in one move to maximize your earnings and minimize player damage. Examples: Surf, Sludge Wave
- Examples of builds that can solo the entire round. Many other great options exist:
  
    <table>
      <tr>
        <td>
            <b>Clawitzer</b> @ Life Orb<br>
            Level 100<br>
            EVs: 252 HP / 252 SpA<br>
            Modest Nature<br>
            - Surf        (Top)<br>
            - Aqua Jet    (Left)<br>
            - Protect     (Right)<br>
            - Bubble Beam (Bottom)<br>
        </td>
        <td>
            <b>Dragalge</b> @ Life Orb<br>
            Level 100<br>
            EVs: 252 HP / 252 SpA<br>
            Modest Nature<br>
            - Sludge Wave (Top)<br>
            - Surf        (Left)<br>
            - Protect     (Right)<br>
            - Sludge Bomb (Bottom)<br>
        </td>
      <tr>
    </table>

## Credits

- **Author:** Kuroneko/Mysticial
- **Stats Table:** Gimikyu/Ericzklm


<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)











