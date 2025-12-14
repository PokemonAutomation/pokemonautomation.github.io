# Program List (Computer Control)

This is a list of all the computer-control programs. To run these programs, you need the [computer-control setup](../SetupGuide/index.md).

**Jump To Program Section:**

- [General Nintendo Switch Programs](#general-nintendo-switch-programs)
- [Pokémon Home](#pokemon-home)
- [Pokémon Let's Go Pikachu/Eevee](#pokemon-lets-go-pikachueevee-lgpe)
- [Pokémon Sword/Shield](#pokemon-swordshield)
- [Pokémon Brilliant Diamond/Shining Pearl](#pokemon-brilliant-diamondshining-pearl)
- [Pokémon Legends Arceus](#pokemon-legends-arceus)
- [Pokémon Scarlet/Violet](#pokemon-scarlet-and-violet)
- [Pokémon Legends ZA](#pokemon-legends-za)
- [Zelda: Tears of the Kingdom](#zelda-tears-of-the-kingdom)

**Notes:**

- Programs that require video feedback cannot run on the Switch Lite because it does not have HDMI output.
- Not every program can run on every controller. Please check the table for compatibility.
- Controllers marked as "Degraded" mean that the program will run, but performance and reliability may be severely degraded.

**Controller Categories:**

| **Wired Controller** | **Wireless Controller** | **Other** |
| --- | --- | --- |
| - ESP32-S3<br>- Pico W (wired controller)<br>- Pico 2 W (wired controller)<br>- sys-botbase 3 (sbb3)<br>- Arduino Uno R3<br>- Arduino Leonardo<br>- Teensy 2.0<br>- Teensy++ 2.0<br>- Pro Micro {.nowrap} | - ESP32<br>- Pico W (wireless controller)<br>- Pico 2 W (wireless controller)<br><br><br><br><br><br><br> {.nowrap} | - sys-botbase 2.4 (sbb2)<br><br><br><br><br><br><br><br><br> {.nowrap} |

Read more about [Controller Performance Categories](../ControllerList.md#controller-performance-classes).


## General Nintendo Switch Programs

| **Program** | **Feedback** | **Controllers** |
| --- | --- | --- |
| [Framework Settings](NintendoSwitch/FrameworkSettings.md) {.nowrap}       | --- | --- |
| [Virtual Console](NintendoSwitch/VirtualConsole.md) {.nowrap}             | --- | All |
| [Switch Viewer](NintendoSwitch/SwitchViewer.md) {.nowrap}                 | --- | All |
| [TurboA](NintendoSwitch/TurboA.md) {.nowrap}                              |     | All |
| [Turbo Button](NintendoSwitch/TurboButton.md) {.nowrap}                   |     | All |
| [Turbo Macro](NintendoSwitch/TurboMacro.md) {.nowrap}                     |     | All |
| [Prevent Sleep](NintendoSwitch/PreventSleep.md) {.nowrap}                 |     | All |
| [Friend Code Adder](NintendoSwitch/FriendCodeAdder.md) {.nowrap}          |     | All (Degraded: sbb2) |
| [Friend Delete](NintendoSwitch/FriendDelete.md) {.nowrap}                 |     | All |
| [Record Keyboard Controller](NintendoSwitch/RecordKeyboardController.md) {.nowrap} |     | All |

## Pokémon Home

| **Program** | **Feedback** | **Controllers** |
| --- | --- | --- |
| [Page Swap](PokemonHome/PageSwap.md) {.nowrap}             |       | All |
| [Box Sorter](PokemonHome/BoxSorter.md) {.nowrap}           | Video | Wired, Wireless |

## Pokémon Let's Go Pikachu/Eevee (LGPE)

This game cannot be played with a Pro Controller and instead requires the use of joycons. In the past, this restricted this game only be playable with the ESP32 and the Pico W. But now that wired joycons are supported, it can now be played on the ESP32-S3 as well.

| **Program** | **Feedback** | **Controllers** |
| --- | --- | --- |
| Game Settings | --- | --- |
||
| **General:** |
| [Daily Item Farmer](PokemonLGPE/DailyItemFarmer.md) {.nowrap} | Video         | Wired, Wireless |
||
| **Shiny Hunting:** |
| [Alolan Trade](PokemonLGPE/AlolanTrade.md) {.nowrap}          | Video         | Wired, Wireless |
| [Fossil Revival](PokemonLGPE/FossilRevival.md) {.nowrap}      | Video         | Wired, Wireless |
| [Gift Reset](PokemonLGPE/GiftReset.md) {.nowrap}              | Video         | Wired, Wireless |
| [Legendary Reset](PokemonLGPE/LegendaryReset.md) {.nowrap}    | Video + Audio | Wired, Wireless |



## Pokémon Sword/Shield

| **Program** |  **Description** | **Feedback** | **Controllers** |
| --- | --- | --- | --- |
| [Game Settings](PokemonSwSh/PokemonSettings.md)        | --- | --- | --- |
||
| **QoL Macros:** |
| [Fast Code Entry (FCE)](PokemonSwSh/FastCodeEntry.md) {.nowrap} |              |                  | All (Degraded: Wireless, sbb2) |
| [Friend Search Disconnect](PokemonSwSh/FriendSearchDisconnect.md) {.nowrap} |  |                  | All |
||
| **General Programs:** |
| [Mass Release](PokemonSwSh/MassRelease.md) {.nowrap} |                       |                  | All (Degraded: sbb2) |
| [Surprise Trade](PokemonSwSh/SurpriseTrade.md) {.nowrap} |                   |                  | Wired, Wireless |
| [Trade Bot](PokemonSwSh/TradeBot.md) {.nowrap} |                             |                  | Wired, Wireless |
| [Clothing Buyer](PokemonSwSh/ClothingBuyer.md) {.nowrap} |                   |                  | All |
| [Autonomous Ball Thrower](PokemonSwSh/AutonomousBallThrower.md) {.nowrap} |  | Video            | All |
| [Dex Rec Finder](PokemonSwSh/DexRecFinder.md) {.nowrap} |                    | Video (Optional) | All (Degraded: sbb2) |
| [Box Reorder National Dex](PokemonSwSh/BoxReorderNationalDex.md) {.nowrap} | | Video            | Wired, Wireless |
||
| **Date-Spam Farmers:** |
| [Date Spam: Watt Farmer](PokemonSwSh/DateSpam-WattFarmer.md) {.nowrap} | Farm watts. To farm money, use watts to buy Luxury balls, then sell them. || All (Degraded: Wireless, sbb2) |
| [Date Spam: Berry Farmer](PokemonSwSh/DateSpam-BerryFarmer.md) {.nowrap} | Farm berries.                                                           || All (Degraded: Wireless, sbb2) |
| [Date Spam: Berry Farmer 2](PokemonSwSh/DateSpam-BerryFarmer2.md) {.nowrap} | Farm berries using audio/video feedback                              | Video + Audio | All (Degraded: sbb2) |
| [Date Spam: Loto Farmer](PokemonSwSh/DateSpam-LotoFarmer.md) {.nowrap} |                          || All (Degraded: sbb2) |
| [Date Spam: Stow-On-Side Farmer](PokemonSwSh/DateSpam-StowOnSideFarmer.md) {.nowrap} |            || All (Degraded: sbb2) |
| [Date Spam: Daily Highlight Farmer](PokemonSwSh/DateSpam-DailyHighlightFarmer.md) {.nowrap} |     || All (Degraded: sbb2) |
| [Date Spam: Poké Jobs Farmer](PokemonSwSh/DateSpam-PokeJobsFarmer.md) {.nowrap} |                 || All (Degraded: sbb2) |
||
| **Den Hunting:** |
| [Purple Beam Finder](PokemonSwSh/PurpleBeamFinder.md) {.nowrap} |         | Video            | All |
| [Event Beam Finder](PokemonSwSh/EventBeamFinder.md) {.nowrap} |           |                  | All |
| [Day Skipper (JPN)](PokemonSwSh/DaySkipperJPN.md) {.nowrap} |             |                  | Switch 1: Wired, Wireless (Degraded: Wireless)<br>Switch 2: Wired Only |
| [Day Skipper (EU)](PokemonSwSh/DaySkipperEU.md) {.nowrap} |               |                  | Switch 1: Wired, Wireless (Degraded: Wireless)<br>Switch 2: Wired Only |
| [Day Skipper (US)](PokemonSwSh/DaySkipperUS.md) {.nowrap} |               |                  | Switch 1: Wired, Wireless (Degraded: Wireless)<br>Switch 2: Wired Only |
| [Day Skipper (JPN) - 7.8k](PokemonSwSh/DaySkipperJPN-7.8k.md) {.nowrap} | |                  | Switch 1: Wired Only<br>Switch 2: None |
||
| **Hosting:** |
| [Den Roller](PokemonSwSh/DenRoller.md) {.nowrap} |                    | Video (Optional) | All (Degraded: sbb2) |
| [Auto-Host Rolling](PokemonSwSh/AutoHost-Rolling.md) {.nowrap} |      | Video (Optional) | All (Degraded: sbb2) |
| [Auto-Host Multi-Game](PokemonSwSh/AutoHost-MultiGame.md) {.nowrap} | | Video (Optional) | All (Degraded: sbb2) |
||
| **Eggs:** |
| [Egg Fetcher 2](PokemonSwSh/EggFetcher2.md) {.nowrap} |                              |       | All |
| [Egg Fetcher Multiple](PokemonSwSh/EggFetcherMultiple.md) {.nowrap} |                |       | All |
| [Egg Hatcher](PokemonSwSh/EggHatcher.md) {.nowrap} |                                 |       | All |
| [Egg Autonomous](PokemonSwSh/EggAutonomous.md) {.nowrap} |                           | Video | All |
| [God Egg Item Duplication](PokemonSwSh/GodEggItemDuplication.md) {.nowrap} |         |       | All (Degraded: sbb2) |
| [God Egg Duplication (developer only)](PokemonSwSh/GodEggDuplication.md) {.nowrap} | |       | All (Degraded: sbb2) |
||
| **Non-Shiny Hunting:** |
| [Stats Reset](PokemonSwSh/StatsReset.md) {.nowrap} |                   | Video | All |
| [Stats Reset - Calyrex](PokemonSwSh/StatsReset-Calyrex.md) {.nowrap} | | Video | All |
| [Stats Reset - Moltres](PokemonSwSh/StatsReset-Moltres.md) {.nowrap} | | Video | All |
| [Stats Reset - Regi](PokemonSwSh/StatsReset-Regi.md) {.nowrap} |       | Video | All |
||
| **Shiny Hunting:** |
| [Multi-Game Fossil Revive](PokemonSwSh/MultiGameFossil.md) {.nowrap} |                                      |                  | All (Degraded: sbb2) |
| [Curry Hunter](PokemonSwSh/CurryHunter.md) {.nowrap} |                                                      | Video (Optional) | Wired, Wireless |
| [Shiny Hunt Autonomous - Regi](PokemonSwSh/ShinyHuntAutonomous-Regi.md) {.nowrap} |                         | Video | All (Degraded: sbb2) |
| [Shiny Hunt Autonomous - Swords Of Justice](PokemonSwSh/ShinyHuntAutonomous-SwordsOfJustice.md) {.nowrap} | | Video | All |
| [Shiny Hunt Autonomous - Strong Spawn](PokemonSwSh/ShinyHuntAutonomous-StrongSpawn.md) {.nowrap} |          | Video | All |
| [Shiny Hunt Autonomous - Regigigas2](PokemonSwSh/ShinyHuntAutonomous-Regigigas2.md) {.nowrap} |             | Video | All |
| [Shiny Hunt Autonomous - IoA Trade](PokemonSwSh/ShinyHuntAutonomous-IoATrade.md) {.nowrap} |                | Video | All |
| [Shiny Hunt Autonomous - Berry Tree](PokemonSwSh/ShinyHuntAutonomous-BerryTree.md) {.nowrap} |              | Video | All (Degraded: sbb2) |
| [Shiny Hunt Autonomous - Whistling](PokemonSwSh/ShinyHuntAutonomous-Whistling.md) {.nowrap} |               | Video | All |
| [Shiny Hunt Autonomous - Fishing](PokemonSwSh/ShinyHuntAutonomous-Fishing.md) {.nowrap} |                   | Video | All |
| [Shiny Hunt Autonomous - Overworld](PokemonSwSh/ShinyHuntAutonomous-Overworld.md) {.nowrap} |               | Video | All |
||
| **RNG:** |
| [RNG Seed Finder](PokemonSwSh/SeedFinder.md) {.nowrap} | Finds the current state to be used for manual RNG manipulation      | Video | All |
| [Cram-o-matic RNG](PokemonSwSh/CramomaticRNG.md) {.nowrap} | Farm apriballs using RNG manip of Cram-o-matic                  | Video | All (Degraded: sbb2) |
||
| **Multi-Switch Programs:** |
| Synchronized Spinning {.nowrap} |                                                    || All (Degraded: sbb2) |
| [Raid Item Farmer (OHKO)](PokemonSwSh/RaidItemFarmerOHKO.md) {.nowrap}  |            || Wired, Wireless |
||
| [**Auto Max Lair 2.0:**](PokemonSwSh/MaxLair.md) {.nowrap} |
| [Max Lair: Standard](PokemonSwSh/MaxLair-Standard.md) {.nowrap} | Run Dynamax Adventures until a shiny Legendary is found.               | Video | All |
| [Max Lair: Strong Boss](PokemonSwSh/MaxLair-StrongBoss.md) {.nowrap} | Run Dynamax Adventures and intelligently reset to keep paths with high win rates (for Legendaries that are hard to beat) | Video | All |
| [Max Lair: Boss Finder](PokemonSwSh/MaxLair-BossFinder.md) {.nowrap} | Run Dynamax Adventures until you find the boss you want.          | Video | All |
||
| **Deprecated Programs:** |
||
| [Ball Thrower](PokemonSwSh/BallThrower.md) {.nowrap} |                               |       | All |
| [Beam Reset](PokemonSwSh/BeamReset.md) {.nowrap} |                                   |       | Wired, Wireless |
| [Egg Combined 2](PokemonSwSh/EggCombined2.md) {.nowrap} |                            |       | Wired, Wireless |
| [Egg Super-Combined 2](PokemonSwSh/EggSuperCombined2.md) {.nowrap} |                 |       | Wired, Wireless |
| [Shiny Hunt Unattended - Regi](PokemonSwSh/ShinyHuntUnattended-Regi.md) {.nowrap} |                         |                  | Wired, Wireless |
| [Shiny Hunt Unattended - Swords Of Justice](PokemonSwSh/ShinyHuntUnattended-SwordsOfJustice.md) {.nowrap} | |                  | Wired, Wireless |
| [Shiny Hunt Unattended - Strong Spawn](PokemonSwSh/ShinyHuntUnattended-StrongSpawn.md) {.nowrap} |          |                  | Wired, Wireless |
| [Shiny Hunt Unattended - Regigigas2](PokemonSwSh/ShinyHuntUnattended-Regigigas2.md) {.nowrap} |             |                  | Wired, Wireless |
| [Shiny Hunt Unattended - IoA Trade](PokemonSwSh/ShinyHuntUnattended-IoATrade.md) {.nowrap} |                |                  | Wired, Wireless |


## Pokémon Brilliant Diamond/Shining Pearl

| **Program** | **Feedback** | **Controllers** |
| --- | --- | --- |
| Game Settings | --- | --- |
||
| **General:** |
| [Mass Release](PokemonBDSP/MassRelease.md) {.nowrap}                           |       | All |
| [Autonomous Ball Thrower](PokemonBDSP/AutonomousBallThrower.md) {.nowrap}      | Video | All |
||
| **Trading:** |
| [Self Box Trade](PokemonBDSP/SelfBoxTrade.md) {.nowrap}                        | Video | All |
| [Self Touch Trade](PokemonBDSP/SelfTouchTrade.md) {.nowrap}                    | Video | All |
||
| **Farming:** |
| [Money Farmer (Route 212)](PokemonBDSP/MoneyFarmerRoute212.md) {.nowrap}        | Video | Wired, Wireless |
| [Money Farmer (Route 210)](PokemonBDSP/MoneyFarmerRoute210.md) {.nowrap}       | Video | Wired, Wireless |
| [Double Battle Leveling](PokemonBDSP/DoublesLeveling.md) {.nowrap}             | Video | All |
| [Amity Square Pick Up Farmer](PokemonBDSP/AmitySquarePickUpFarmer.md) {.nowrap} |       | All |
| [Gift Berry Reset](PokemonBDSP/GiftBerryReset.md) {.nowrap}                    | Video | All |
| [Poffin Cooker](PokemonBDSP/PoffinCooker.md) {.nowrap}                          | Video | All (Degraded: sbb2) |
||
| **Shiny Hunting:** |
| [Starter Reset](PokemonBDSP/StarterReset.md) {.nowrap}                         | Video | All |
| [Legendary Reset](PokemonBDSP/LegendaryReset.md) {.nowrap}                     | Video | All |
| [Shiny Hunt - Overworld](PokemonBDSP/ShinyHunt-Overworld.md) {.nowrap}         | Video | All |
| [Shiny Hunt - Fishing](PokemonBDSP/ShinyHunt-Fishing.md) {.nowrap}             | Video | All |
| [Shiny Hunt - Shaymin](PokemonBDSP/ShinyHunt-Shaymin.md) {.nowrap}             | Video | All |
||
| **Eggs:** |
| [Egg Fetcher](PokemonBDSP/EggFetcher.md) {.nowrap}                             |       | All |
| [Egg Hatcher](PokemonBDSP/EggHatcher.md) {.nowrap}                             |       | All |
| [Egg Autonomous](PokemonBDSP/EggAutonomous.md) {.nowrap}                       | Video | All |
||
| **Glitches (v1.1.3):** |
| [Activate Menu Glitch (1.1.3)](PokemonBDSP/ActivateMenuGlitch-113.md) {.nowrap}    | Video | Wired, Wireless |
| [Clone Items (Box Copy Method 2)](PokemonBDSP/CloneItemsBoxCopy2.md) {.nowrap}     | Video | Wired, Wireless |
||
| **Glitches (v1.1.2):** |
| [Activate Menu Glitch (1.1.2)](PokemonBDSP/ActivateMenuGlitch-Poketch.md) {.nowrap} | Video | Wired, Wireless |


## Pokémon Legends Arceus

| **Program** | **Feedback** | **Controllers** |
| --- | --- | --- |
| Game Settings | --- | --- |
||
| **General:** |
| [Braviary Height Glitch](PokemonLA/BraviaryHeightGlitch.md) {.nowrap}          |               | All |
| [Distortion Waiter](PokemonLA/DistortionWaiter.md) {.nowrap}                   | Video         | All |
| [Outbreak Finder](PokemonLA/OutbreakFinder.md) {.nowrap}                       | Video         | All |
| [Clothing Buyer](PokemonLA/ClothingBuyer.md) {.nowrap}                         |               | All |
| [Skip To Full Moon](PokemonLA/SkipToFullMoon.md) {.nowrap}                     | Video         | All |
| [Apply Grits](PokemonLA/ApplyGrits.md) {.nowrap}                               |               | All |
| [Pokédex Task Reader](PokemonLA/PokedexTasksReader.md) {.nowrap}               | Video         | All |
||
| **Trading:** |
| [Self Box Trade](PokemonLA/SelfBoxTrade.md) {.nowrap}                          | Video         | All |
| [Self Touch Trade](PokemonLA/SelfTouchTrade.md) {.nowrap}                      | Video         | All |
||
| **Farming:** |
| [Nugget Farmer (Highlands)](PokemonLA/NuggetFarmerHighlands.md) {.nowrap}      | Video + Audio | All |
| [Ingo Battle Grinder](PokemonLA/IngoBattleGrinder.md) {.nowrap}                | Video         | All |
| [Ingo Move Grinder](PokemonLA/IngoMoveGrinder.md) {.nowrap}                    | Video         | All |
| [Magikarp Move Grinder](PokemonLA/MagikarpMoveGrinder.md) {.nowrap}            | Video         | All |
| [Tenacity Candy Farmer](PokemonLA/TenacityCandyFarmer.md) {.nowrap}            | Video         | All |
| [Leap Grinder](PokemonLA/LeapGrinder.md) {.nowrap}                             | Video + Audio | All |
||
| **Shiny Hunting:** |
| [Alpha Crobat Hunter](PokemonLA/AlphaCrobatHunter.md) {.nowrap}                | Video + Audio | All |
| [Alpha Gallade Hunter](PokemonLA/AlphaGalladeHunter.md) {.nowrap}              | Video + Audio | All |
| [Alpha Froslass Hunter](PokemonLA/AlphaFroslassHunter.md) {.nowrap}            | Video + Audio | All |
| [Burmy Hunter](PokemonLA/BurmyHunter.md) {.nowrap}                             | Video + Audio | All (Degraded: sbb2) |
| [Unown Hunter](PokemonLA/UnownHunter.md) {.nowrap}                             | Video + Audio | All |
| [Shiny Hunt - Flag Pin](PokemonLA/ShinyHunt-FlagPin.md) {.nowrap}              | Video + Audio | All |
| [Post-MMO Spawn Reset](PokemonLA/PostMMOSpawnReset.md) {.nowrap}               | Video + Audio | All |
| [Shiny Hunt - Custom Path](PokemonLA/ShinyHunt-CustomPath.md) {.nowrap}        | Video + Audio | All (Degraded: sbb2) |


## Pokémon Scarlet and Violet

| **Program** | **Description** | **Feedback** | **Controllers** |
| --- | --- | --- | --- |
| Game Settings | --- | --- | --- |
||
| **General:** |
| [Mass Purchase](PokemonSV/MassPurchase.md) {.nowrap} | Purchase items from the shop.                                           | Video         | All |
| [Clothing Buyer](PokemonSV/ClothingBuyer.md) {.nowrap} | Purchase clothing from shops.                                         | Video         | All |
| [Autonomous Ball Thrower](PokemonSV/AutonomousBallThrower.md) {.nowrap} | Repeatedly throw a ball until you catch the pokemon. | Video         | All |
| [Size Checker](PokemonSV/SizeChecker.md) {.nowrap} | Check boxes of Pokemon for size marks.                                    | Video         | All |
| [Self Box Trade](PokemonSV/SelfBoxTrade.md) {.nowrap} | Trade boxes of Pokemon between two local Switches.                      | Video         | All |
| [Sandwich Maker](PokemonSV/SandwichMaker.md) {.nowrap} | Make a sandwich  of your choice.                                      | Video         | All |
|| 
| **Boxes:** |
| [Mass Release](PokemonSV/MassRelease.md) {.nowrap} | Mass release boxes of Pokemon.          | Video         | All |
| [Mass Attach Items](PokemonSV/MassAttachItems.md) {.nowrap} | Mass attach items to Pokemon.  | Video         | All |
||
| **Farming:** |
| [LP Farmer](PokemonSV/LPFarmer.md) {.nowrap} | Farm LP by day skipping Tera raids.                                                            | Video         | All (Degraded: sbb2) |
| [Gimmighoul Roaming Farmer](PokemonSV/GimmighoulRoamingFarmer.md) {.nowrap} | Farm roaming Gimmighoul for coins.                              | Video         | All (Degraded: sbb2) |
| [Gimmighoul Chest Farmer](PokemonSV/GimmighoulChestFarmer.md) {.nowrap} | Farm chest Gimmighoul for coins.                                    | Video         | Wired, Wireless |
| [Auction Farmer](PokemonSV/AuctionFarmer.md) {.nowrap} | Farm special Pokeballs (now superceded by Item Printer RNG), EV reset berries, feathers | Video      | All (Degraded: sbb2) |
| [ESP Training](PokemonSV/ESPTraining.md) {.nowrap} | Farm EV reset berries          	                                                        | Video         | All |
| [Tournament Farmer](PokemonSV/TournamentFarmer.md) {.nowrap} | Farm money (now superceded by Item Printer RNG)                                | Video         | All |
| [Tournament Farmer 2](PokemonSV/TournamentFarmer2.md) {.nowrap} | Farm money (now superceded by Item Printer RNG)                             | Video         | All |
| [Flying Trial Farmer](PokemonSV/FlyingTrialFarmer.md) {.nowrap} | Farm Blueberry points (BP) with the Flying trial                            | Video         | Wired, Wireless |
| [BBQ Farmer](PokemonSV/BBQSoloFarmer.md) {.nowrap} | Farm Blueberry points (BP) with Blueberry quests                                        | Video + Audio | Wired, Wireless |
| [Material Farmer](PokemonSV/MaterialFarmer.md) {.nowrap} | Farm Happiny dust                                                                  | Video + Audio | All |
| [Item Printer RNG](PokemonSV/ItemPrinterRNG.md) {.nowrap} | Farm rare items (e.g. Ability Patch, PP Max, EXP Candy, rare Pokeballs, Tera shards). To farm money, farm and sell Ability Patches. | Video + Audio | All (Degraded: sbb2) |
||
| **Eggs:** |
| [Egg Fetcher](PokemonSV/EggFetcher.md) {.nowrap} | Fetch eggs from a picnic.                         | Video         | All |
| [Egg Hatcher](PokemonSV/EggHatcher.md) {.nowrap} | Hatch eggs from boxes.                            | Video         | All |
| [Egg Autonomous](PokemonSV/EggAutonomous.md) {.nowrap} | Get meal power, fetch eggs, and hatch them. | Video         | All |
||
| **Tera Raids:** |
| [Auto-Host](PokemonSV/AutoHost.md) {.nowrap} | Auto-host a Tera raid.                                                                     | Video         | All |
| [Tera Roller](PokemonSV/TeraRoller.md) {.nowrap} | Roll Tera raids to find shiny Pokemon.                                                 | Video         | All (Degraded: sbb2) |
| [Tera Self Farmer](PokemonSV/TeraSelfFarmer.md) {.nowrap} | Farm items and Pokemon from Tera raids. Hunt for shiny and high reward raids. | Video         | All (Degraded: sbb2) |
| [Tera Multi-Farmer](PokemonSV/TeraMultiFarmer.md) {.nowrap} | Farm items and Pokemon from your own Tera raid using multiple Switches.     | Video         | All |
||
| **Fast Code Entry:** |
| [Fast Code Entry (FCE)](PokemonSV/FastCodeEntry.md) {.nowrap} | Quickly enter a 4, 6, 8 digit link code.                                                      |               | All (Degraded, Wireless, sbb2) |
| [Clipboard Fast Code Entry (C-FCE)](PokemonSV/ClipboardFastCodeEntry.md) {.nowrap} | Quickly enter a 4, 6, 8 digit link code from clipboard.                  |               | All (Degraded, Wireless, sbb2) |
| [Video Fast Code Entry (V-FCE)](PokemonSV/VideoFastCodeEntry.md) {.nowrap} | Read a 4, 6, 8 digit link code from someone on your screen and enter it quickly. |               | All (Degraded, Wireless, sbb2) |
||
| **Stats Hunting:** |
| [Stats Reset](PokemonSV/StatsReset.md) {.nowrap} | Repeatedly catch static encounters (e.g. Legendaries) until you get the stats you wish.         | Video         | All |
| [Stats Reset - Event Battle](PokemonSV/StatsResetEventBattle.md) {.nowrap} | Repeatedly catch Ursaluna/Pecharunt until you get the stats you wish. | Video         | All |
||
| **Shiny Hunting:** |
| [Shiny Hunt - Area Zero Platform](PokemonSV/ShinyHunt-AreaZeroPlatform.md) {.nowrap} | Shiny hunt Pokemon on the isolated platform at the bottom of Area Zero. | Video + Audio | All |
| [Shiny Hunt - Scatterbug](PokemonSV/ShinyHunt-Scatterbug.md) {.nowrap} | Shiny hunt Scatterbug.                                                                | Video + Audio | All |
||
| **Glitches (v3.0.0):** |
| [Wild Item Farmer (cloning glitch)](PokemonSV/WildItemFarmer.md) {.nowrap} | Farm an item held by a cloned wild Pokemon. (glitch patched) | Video         | All |
||
| **Glitches (v1.0.1):** |
| [Ride Cloner (1.0.1)](PokemonSV/RideCloner-101.md) {.nowrap} | Clone your ride legendary and its item using the add-to-party glitch. (glitch patched) | Video         | Wired, Wireless |
| [Clone Items (1.0.1)](PokemonSV/CloneItems-101.md) {.nowrap} | Clone items using the add-to-party glitch. (glitch patched)                            | Video         | Wired, Wireless |
||
| **Beta/WIP Programs:** |
| [AutoStory](PokemonSV/AutoStory.md) {.nowrap} | Progress through the tutorial and mainstory of Scarlet/Violet | Video         | Wired (Wireless untested) |
| [Claim Mystery Gift](PokemonSV/ClaimMysteryGift.md) {.nowrap} | Claim the Mystery Gift in Scarlet/Violet | Video              | Wired (Wireless untested) |
||
| **Deprecated Programs:** |
| [Autonomous Item Printer](PokemonSV/AutoItemPrinter.md) {.nowrap}              || Video         | All |


## Pokémon Legends ZA

See also: [Shiny Hunting Recommendations](PokemonLZA/ShinyHuntRecommendations.md)

| **Program** | **Description** | **Feedback** | **Controllers** |
| --- | --- | --- | --- |
| Game Settings | --- | --- | --- |
||
| **General:** |
| [Clothing Buyer](PokemonLZA/ClothingBuyer.md) {.nowrap}                         | Purchase clothing from shops.                          | Video         | All |
| [Stall Buyer](PokemonLZA/StallBuyer.md) {.nowrap}                               | Purchase items from stalls.                            | Video         | All |
| [Self Box Trade](PokemonLZA/SelfBoxTrade.md) {.nowrap}                          | Trade boxes of Pokémon between two Switches locally.   | Video         | All |
| [Post-Kill Catcher](PokemonLZA/PostKillCatcher.md) {.nowrap}                    | Reset and throw balls at something until it catches.   | Video         | All |
||
| **Farming:** |
| [Restaurant Farmer](PokemonLZA/RestaurantFarmer.md) {.nowrap}                   | Farm the restaurant battles for exp, items, and money. | Video         | All |
| [Mega Shard Farmer](PokemonLZA/MegaShardFarmer.md) {.nowrap}                    | Farm Mega Shards.                                      | Video         | All |
| [Jacinthe Infinite Farmer](PokemonLZA/JacintheInfiniteFarmer.md) {.nowrap}      | Repeatedly battle Jacinthe for exp and money.          | Video         | All |
| [Friendship Farmer](PokemonLZA/FriendshipFarmer.md) {.nowrap}                   | Farm friendship via cafes or benches.                  | Video         | All |
| [In-Place Catcher](PokemonLZA/InPlaceCatcher.md) {.nowrap}                      | Catch everything in one place to fill your boxes.      | Video + Audio | All |
| [Hyperspace Reward Reset](PokemonLZA/HyperspaceRewardReset.md) {.nowrap}        | Reset in front of a Hyperspace Battle Zone trainer to receive a specific reward. | Video | All |
||
| **Shiny Hunting:** |
| [Shiny Hunt - Bench Sit](PokemonLZA/ShinyHunt-BenchSit.md) {.nowrap}            | Shiny hunt using the bench reset method.               | Video + Audio | All |
| [Shiny Hunt - Overworld Reset](PokemonLZA/ShinyHunt-OverworldReset.md) {.nowrap} | Shiny hunt using the overworld reset method.           | Video + Audio | All |
| [Shiny Hunt - Wild Zone Entrance](PokemonLZA/ShinyHunt-WildZoneEntrance.md) {.nowrap} | Shiny hunt at wild zone entrance using fast travel method. | Video + Audio | All |
| [Auto Fossil](PokemonLZA/AutoFossil.md) {.nowrap}                               | Find shiny or alpha fossil Pokémon, by repeatedly reviving fossils. | Video         | All |
||
| **Non-Shiny Hunting:** |
| [Stats Reset](PokemonLZA/StatsReset.md) {.nowrap}                               | Reset for stats on gift Pokémon like Eternal Flower Floette. | Video         | All |


## Zelda: Tears of the Kingdom

| **Program** | **Feedback** | **Controllers** |
| --- | --- | --- |
| **Glitches (v1.1.1):** |
| [Bow Item Duper](ZeldaTotK/BowItemDuper.md) {.nowrap}             |                  | Wired, Wireless |
| [Paraglide Item Duper](ZeldaTotK/ParaglideItemDuper.md) {.nowrap} |                  | Wired, Wireless |
| [Shield Surf Item Duper](ZeldaTotK/SurfItemDuper.md) {.nowrap}    |                  | Wired, Wireless |
| [Mineru Item Duper](ZeldaTotK/MineruItemDuper.md) {.nowrap}       |                  | Wired, Wireless |

<hr>

**Discord Server:** 


[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)

