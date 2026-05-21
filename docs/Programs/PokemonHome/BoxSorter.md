# Pokemon Home Box Sorter

***Warning: This is a high-demand program that gets many requests for improvements yet is no longer maintained by anyone. The original author has abandoned it and nobody on the current dev team is interested in taking it up. So this program is dead until someone revives it.***

***Do not expect any feature requests or bug reports to be addressed.***

## Program Description

This program goes through each Pokémon summary page in HOME. It will check for the National Dex number to sort Pokémon starting at the current box and ending after a set number of boxes chosen by the user.
It will skip empty slots and empty boxes. Please note that the program may sometimes incorrectly read the National Dex number. In such cases, the user will need to sort incorrectly placed Pokémon manually.

<img src="images/BoxSorter.png">

## Stats

This program is able to read one box in 20 seconds and able to sort one box in less than 1 minutes.

I successfuly sorted 18 boxes in 54 minutes with default settings.

## Settings

**Switch Settings:**

1. Screen size: Must be 100% within the Switch settings
2. [Switch 2: All HDR options must be disabled.](../NintendoSwitch/Switch2Notes.md#switch-2-hdr-may-be-problematic)

**Program Settings:**

1. Video Resolution: 720p or higher

## Instructions

1. Go to the first box you want to sort
2. Try the program with one box to figure out camera and game delay
3. Select the number of boxes you want to order

## Options

### Number of Boxes to Sort:

The program will sort this many boxes, starting at the current box where you start the program.

### Capture Card Delay:

Every capture card has some delay. Cheap ones tend to have more. You will have to test the program on a small number of boxes first to see what delay works best for you.

### Pokémon Home App Delay:

Maximum delay from when you press a button to Pokémon Home App finishes the action on that action.
In most cases the program blindly presses buttons to operate Home. You will have to test the program on a small number of boxes first to ensure you have enough delay.
For robustness, increase this delay further if you plan on doing a lot of box sorting. Do note the more delay you put the slower the sorter will be. 

### Sort Order Rules:

Set up your sorting rules. Each table row is a rule on the Pokémon order. Available rules are:

- Dex Number: Pokémon with smaller national dex numbers will be placed at front.
- Shiny: shiny Pokémon will be placed at front.
- Gigantamax: Gigantamax Pokémon will be placed at front.
- Alpha: Alpha Pokémon will be placed at front.
- Ball Type: will place Pokémon based on their Pokéball names' alphabetical order
- Gender (Male, Female, Genderless): male Pokémon will be placed first, then comes female and at last genderless.

The higher a rule is in the table, the "outer" or "earlier" the rule applies. e.g. for a table of rule "National Dex Number" followed by "Alpha".
It will have the order: Alpha Bulbasaur, Bulbasaur, Alpha Ivysaur, Ivysaur, ... Basically, the program first sorts Pokémon based on national dex numbers. Then
for each subgroup of Pokémon with the same dex number, sort them by their alphaness.

Each rule also has a "reverse" checkerbox to reverse its ordering. e.g. reversed "Alpha" rule will place Alpha Pokémon at end.

### Output File

The program saves the catalogued Pokémon summary information into `<output_file>.json` and its planned sorted Pokémon order into `<output_file>-sorted.json`.

### Dry Run

If checked, the program will only catalogue Pokémon summary information into `<output_file>.json` and `<output_file>-sorted.json` without sorting the Pokémon in Home.
This is useful for exporting your Pokémon Home data.

## Credits

- **Author:** Prismillon

<hr>

**Discord Server:** 

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)
