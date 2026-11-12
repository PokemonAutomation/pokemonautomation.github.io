# Box Sorter Living Dex (Beta)

---
## Program Description

Arrange PC boxes into a living dex in Pokémon FireRed and LeafGreen on Nintendo Switch. The program places one matching Pokémon per template slot, leaves gaps for missing species, and places duplicates and other extras in the slots immediately after the template.

!!! note "Beta program"
    Look for **Box Sorter Living Dex** under **Untested/Beta/WIP** in the FireRed and LeafGreen program list in a beta build.

<!-- Replace this blank image with a screenshot of the living dex setup. -->
<img src="images/BoxSorterLivingDex.png" width="600" alt="Living dex box setup">

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
2. Go to the first box where you want the living dex to begin. Start with an empty selection hand and the cursor on the box grid.
3. Set **Number of Boxes to Organize** to cover the template and the Pokémon you want to scan, with space for extras after the template.
4. Use **Dry Run** to check the layout and missing Pokémon list. Return to the first box before starting the run that moves your Pokémon.

!!! warning "Allow room for extras"
    The Condensed template reserves 214 slots, leaving 26 slots for extras when you select eight boxes. If you have more extras than will fit, increase the box count or move some extras out of the selected range before running again.

---
## Options

### Box Settings

#### Game Language

Choose the language of your game so the program can read Pokémon species names. Supported languages are English (default), Japanese, Spanish, French, German, and Italian.

#### Number of Boxes to Organize

Choose 1 to 14 boxes, starting with the current box and continuing to the right. The Condensed template needs at least eight boxes, which is the default. The program scans the entire selected range, including any extra boxes.

#### Living Dex Template

**FRLG Living Dex (Condensed)** is the available template. It starts at the top-left slot of the current box and reserves one slot per species in National Dex order. It covers 214 species, including Kanto #001–#150 and selected later species through Deoxys. Mew and other species outside the template go with the extras. Any form or gender can fill the slot for its species.

#### Shiny Dex

Enable this to fill template slots with shiny Pokémon only. Non-shiny Pokémon go after the template with the extras. With the option off, both shiny and non-shiny Pokémon can fill template slots. A shiny run takes longer because the program checks each occupied slot's summary.

### Output and Notifications

#### Dry Run

Scan and plan the sort while leaving the Pokémon in place. Both dry runs and regular runs produce the following files.

| File | Contents |
| --- | --- |
| `frlg-living-dex-box-order.json` | The scanned layout. |
| `frlg-living-dex-box-order-sorted.json` | The planned layout. |
| `frlg-living-dex-missing-pokemon.txt` | The National Dex number and name of each missing species. |

#### Notifications

Configure notifications for program completion and fatal errors.

!!! tip "Sorting by rules"
    Use [Box Sorter](BoxSorter.md) to group all Pokémon by Dex Number, Level, Gender, or Shiny.

---
## Credits

- **Author** dolphincurry/Dalton-V

<hr>

**Discord Server**

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)
