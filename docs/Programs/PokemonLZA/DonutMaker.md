# Donut Maker

## Program Description

Make, reset, and keep donuts with the desired flavor powers.

<img src="images/DonutMaker.png">


## Settings

**Switch Settings:**

1. Screen size: Must be 100% within the Switch settings
2. [Switch 2: All HDR options must be disabled.](../NintendoSwitch/Switch2Notes.md#switch-2-hdr-may-be-problematic)
3. [Switch 2: The profile you are using must be the 1st (left-most) profile.](../NintendoSwitch/Switch2Notes.md#resetting-a-game-moves-the-cursor-to-the-1st-user-profile)

**Program Settings:**

1. Video Resolution: 1080p or higher
2. The language in the option must match your in-game language.

**Game Settings:**

1. Text Speed: Fast
2. Your have more than 8 types of regular berries and 8 types of hyperspace berries. The program assumes each line of the berry menu always has a valid berry when making a donut.
3. You have more berries than the quantities required to make the donut, as using up a berry makes the icon appear faded and interferes with proper berry reading.

## Instructions

1. Start the program in the overworld.

### Notes and Examples
When filling in the Donuts table, make sure your donut is possible by using a [donut calculator](https://rotomlabs.net/legends-z-a/donut-maker) first.

#### Basic Example:

For this target donut:

| Donut 1 |
| - |
| - Alpha Power (Lv. 3)<br>- Sparkling Power: All Types (Lv. 3)<br>- \[Final power does not matter\] |

Insert the following entry into the donut table:

| Keep Limit | Flavor Power 1 | Level 1 | Flavor Power 2 | Level 2 | Flavor Power 3 | Level 3 |
| - | - | - | - | - | - | - |
| 1 | Sparkling: All Types | Lv . 3 | Alpha Power | Lv. 3 | Any Power | Any |

Note: the order of Flavor Power 1, 2, and 3 does not matter.

#### Advanced Example

To match _any_ of the following donuts:

| Donut 1 | Donut 2 | Donut 3 |
| - | - | - |
| - Item Power: Berries (Lv. 3)<br>- Big Haul Power (Lv. 2)<br>- \[Final Power does not matter\] | - Item Power: Berries (Lv. 2)<br>- Big Haul Power (Lv. 3)<br>- \[Final Power does not matter\] | - Big Haul Power (Lv. 3)<br>- Item Power: Berries (Lv. 3)<br>- \[Final Power does not matter\] |

Insert the following entries into the donut table:

| Keep Limit | Flavor Power 1 | Level 1 | Flavor Power 2 | Level 2 | Flavor Power 3 | Level 3 |
| - | - | - | - | - | - | - |
| 3 | Item: Berries | Lv . 3 | Big Haul | Lv. 2 or 3 | Any Power | Any |
| 3 | Item: Berries | Lv . 2 or 3 | Big Haul | Lv. 2 | Any Power | Any |

**Important note**: A single donut can count towards the limit of multiple entries in the table. If you're using the inclusive "Lv. 2 or 3" setting, be aware that either Lv. 2 or Lv. 3 will count towards the limit.

In the advanced example, if you immediately find 3 donuts with "Item Power: Berries (Lv. 3)" and "Big Haul (Lv. 3)", all limits will be fulfilled and the program will stop. If you need finer control over the limits, specify the exact level and list each combination individually in the table.

| Keep Limit | Flavor Power 1 | Level 1 | Flavor Power 2 | Level 2 | Flavor Power 3 | Level 3 |
| - | - | - | - | - | - | - |
| 2 | Item: Berries | Lv . 3 | Big Haul | Lv. 2 | Any Power | Any |
| 2 | Item: Berries | Lv . 2 | Big Haul | Lv. 3 | Any Power | Any |
| 10 | Item: Berries | Lv . 3 | Big Haul | Lv. 3 | Any Power | Any |

#### Basic Item Power Donut Recipes

These recipes can yield Item Power (Lv. 3) and Big Haul Power (Lv. 3)

| Recipe | Stats | Use Case |
| - | - | - |
| 8x Hyper Kasib Berry | 3240 Donut Energy<br>+108 Level Boost<br>No 3rd Power | The donut with the highest chance of two Lv. 3 powers but the most expensive.<br><br>Best used when you want a good donut for immediate use |
| 4x Hyper Kasib Berry<br>4x Hyper Roseli Berry | 3660 Donut Power<br>+114 Level Boost<br>Lv. 1 or Lv. 2 Spicy Power | A lower chance of two Lv. 3 powers but a more balanced price.<br><br>Best used when you want to build up a stockpile of good donuts for later use<br>More efficient in terms of berry usage, better suited for longer sessions |
| 2x Hyper Roseli Berry<br>4x Hyper Colbur Berry<br>1x Hyper Payapa Berry<br>1x Hyper Coba Berry<br><br>2x Hyper Roseli Berry<br>4x Hyper Colbur Berry<br>1x Hyper Payapa Berry<br>1x Hyper Charti Berry<br><br>2x Hyper Roseli Berry<br>4x Hyper Babiri Berry<br>1x Hyper Payapa Berry<br>1x Hyper Coba Berry | 4050 Donut Energy<br>+111 Level Boost<br>Sour and Fresh Powers<br><br><br>4185 Donut Energy<br>+108 Level Boost<br>Sour and Fresh Powers<br><br><br>4365 Donut Power<br>+108 Level Boost<br>Sour and Bitter Powers<br><br> | Papa Jefé's Kasib-less Rainbow Donuts:<br><br>Best used when trying to use up leftover berries<br>Rainbow donuts have a boost to the level of the resulting flavor powers<br> Less efficient at getting higher powers than the previous recipes but uses up less desirable berries |

#### Basic Sparkling Power Donut Recipes

These recipes can yield Sparkling Power: ??? (Lv. 3) and Alpha/Humungo/Teensy (Lv. 3)

| Recipe | Stats | Use Case |
| - | - | - |
| 8x Hyper Tanga Berry | 3600 Donut Energy<br>+84 Level Boost<br>No 3rd Power | The donut with the highest chance of two Lv. 3 powers but the most expensive.<br><br>Best used when you're searching for a specific donut for immediate use |
| 4x Hyper Tanga Berry<br>4x Hyper Haban Berry | 4020 Donut Power<br>+90 Level Boost<br>Lv. 1 or Lv. 2 Fresh Power | A lower chance of two Lv. 3 powers but a more balanced price.<br><br>Best used when you want to build up a stockpile of good donuts for later use<br>More efficient in terms of berry usage, better suited for longer sessions |
| 5x Hyper Haban Berry<br>1x Hyper Payapa Berry<br>1x Hyper Charti Berry<br>1x Hyper Chilan Berry<br><br>5x Hyper Haban Berry<br>1x Hyper Payapa Berry<br>1x Hyper Charti Berry<br>1x Hyper Babiri Berry<br><br>5x Hyper Haban Berry<br>1x Hyper Payapa Berry<br>1x Hyper Charti Berry<br>1x Hyper Roseli Berry | 4275 Donut Power<br>+97 Level Boost<br>Sweet and Fresh Powers<br><br><br>4320 Donut Power<br>+97 Level Boost<br>Sweet and Fresh Powers<br><br><br>4230 Donut Power<br>+99 Level Boost<br>Sweet and Fresh Powers<br><br> | Papa Jefé's Tanga-less Rainbow Donuts:<br><br>Best used when trying to use up leftover berries<br>Rainbow donuts have a boost to the level of the resulting flavor powers<br> Less efficient at getting higher powers than the previous recipes but uses up less desirable berries |


## Options

### Game Language:

Select the language that matches what you are using in-game. This setting is required to read berries and donut powers.

### Berries Table:

The berries that will be used to make the donut. Must enter a minimum of three berries and a maximum of eight.

One berry per line. To use a berry more than once, select it in multiple rows.

### Number of Donuts to Keep:

The program continues resetting and making donuts until this many donuts matching the specified powers are kept.

The program will stop when this many donuts are kept or all limits in the table are reached, whichever happens first.

Make sure you have enough berries to make this many donuts. The program will fail when not given enough berries.

### Donuts Table:

The program will check the powers of a made donut and compare the powers to each row in the table.

A keep limit can be set for each donut. Make sure you have enough berries to make this many donuts!

A single donut can match and count towards the limit of multiple entries in the table.

The order in which you list Flavor Powers 1, 2, and 3 does not matter.

Note: "All Types" means the All Types power in-game. "*" means match any type for the specified power.

### Go Home when Done:

Go to the Switch Home to idle when finished.

## Credits

- **Authors:** Gin, kichithewolf, Gimikyu


<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)

