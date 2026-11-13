# Box Sorter (Beta)

---

## Program Description

Sort consecutive PC boxes in Pokémon FireRed and LeafGreen on Nintendo Switch. The program reads the Pokémon in the selected boxes, sorts them using your rules, and collects empty slots at the end.

!!! note "Beta program"
Look for **Box Sorter** under **Untested/Beta/WIP** in the FireRed and LeafGreen program list in a beta build.

<!-- Replace this blank image with a screenshot of the Move Pokémon screen. -->
<img src="images/BoxSorter.png" width="600" alt="Move Pokémon screen">

---

## Instructions

**Switch Settings**

1. Set the screen size to 100% in the Switch settings.
2. [Switch 2 users must disable HDR.](../NintendoSwitch/Switch2Notes.md#switch-2-hdr-may-be-problematic)

**Program Settings**

1. Use 16:9 video at 720p or higher. 1080p is recommended.
2. Set **Game Language** to match your copy of FireRed or LeafGreen.

### Before You Start

1. Open the Pokémon Storage System at a PC and select **Move Pokémon**.
2. Go to the first box you want to sort. Start with an empty selection hand and the cursor on the box grid.
3. Set **Number of Boxes to Sort** and **Sort Order Rules**.
4. Use **Dry Run** to check the planned order. Return to the first box before starting the run that moves your Pokémon.

!!! tip "Sorting a living dex"
Use [Box Sorter Living Dex](BoxSorterLivingDex.md) to reserve a slot for each species in a living dex template.

---

## Options

### Sorting

#### Game Language

Choose the language of your game so the program can read Pokémon species names. Supported languages are English (default), Japanese, Spanish, French, German, and Italian.

#### Number of Boxes to Sort

Choose 1 to 14 boxes, starting with the current box and continuing to the right. The default is 1.

#### Sort Order Rules

Add at least one rule. Rules apply from top to bottom, and later rows break ties. For example, with **Dex Number** above **Level**, the program orders Pokémon by species and puts lower-level Pokémon first within each species. Check **Reverse** on a row to reverse that rule's order. Any ties left after the last rule are sorted by National Dex number.

| Rule                              | Default order                       |
| --------------------------------- | ----------------------------------- |
| Dex Number                        | Lowest National Dex number first.   |
| Level                             | Lowest level first.                 |
| Gender (Male, Female, Genderless) | Male, then female, then genderless. |
| Shiny                             | Shiny Pokémon first.                |
| Ball Type                         | Alphabetical by Poké Ball name.     |

!!! info "Shiny and Ball Type add summary checks"
Either rule makes the program read both shininess and ball type from each Pokémon's summary. This adds a considerable amount of time to the program.

### Output and Notifications

#### Dry Run

Scan the boxes and write the current layout to `frlg-box_order.json` and the planned layout to `frlg-box_order-sorted.json` while leaving the Pokémon in place. A regular run writes the same files before moving Pokémon.

#### Notifications

Configure notifications for program completion and fatal errors.

---

## Credits

- **Author** dolphincurry/Dalton-V

<hr>

**Discord Server**

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)
