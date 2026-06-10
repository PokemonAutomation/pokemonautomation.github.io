---
social:
  cards: false
---

# 欠压故障

## 什么是欠压故障？

每次从底座插拔Switch时，底座的所有USB端口会短暂断电，影响到所有完全依赖Switch底座供电的单片机：

- Pico W（UART模式）
- Arduino Uno R3
- Arduino Leonardo
- Teensy 2.0 / Teensy++ 2.0
- Pro Micro

在大多数情况下，单片机会完全断电并正常重启。用户通常不会注意到有线连接的单片机重启了。而无线连接的Pico W则会丢失与Switch的配对，需要用户重新配对。

但有时候，电压没有低到让单片机彻底关机，而是让单片机板进入"故障"模式，导致单片机无响应。这就有点麻烦了。修复方法是按下板子上的重置按钮（如果有的话），或者断掉连接它的所有电源再通电。

在Switch 1的底座上欠压故障很少出现。**但Switch 2上这问题很常见**。
因为最近《宝可梦传说 Z-A》发行，许多老用户拿着以前的单片机控制Switch 2，就遇到了这个问题。雪上加霜的是我们的单片机固件最近更新后变得更复杂了，更容易受低电压影响。

## 如何暂时解决欠压故障？

重置单片机：

- 按板子上的重置按钮（如果有的话）
- 如果按了没效果（或没有重置按钮），就需要给单片机断电：拔掉USB和UART以确保没有电源到达单片机板。即使UART不为板子供电，TX和RX线路也会有电源从UART泄漏到单片机。

Switch 2用户需要经常做这番操作，很影响用户体验。

## 如何永久解决欠压故障？

对于旧的单片机设置（Uno、Leonardo、Teensy、Pro Micro），我们建议升级到以下新的单片机：

- [Pico W（USB模式）](SetupGuide/Controllers/Controller-PicoW-USB.md)
- [ESP32](SetupGuide/Controllers/Controller-ESP32-WROOM.md)
- [ESP32-S3](SetupGuide/Controllers/Controller-ESP32-S3.md)

这3种设置都不受欠压故障影响。Pico和ESP32由电脑供电，不依赖Switch底座。ESP32-S3由电脑和底座同时供电，只要任一侧在供电它就会保持通电状态。

Pico（UART模式）则由底座供电，不幸受影响。尽管它往往更常重启而不是故障，重启也会解除与Switch的配对。

## 我对硬件很熟，如何真正解决这个问题？

思路是把单片机板的供电设置成像ESP32-S3那样可以由电脑或底座任一供电。

具体的方案是买一根允许高速切换的[肖特基二极管](https://en.wikipedia.org/wiki/Schottky_diode)。用它连接UART的+5V线和单片机板的电源输入，使得板子能通过UART从电脑供电的同时防止电流从底座流向电脑烧坏器件。

虽然电脑和Switch底座都能提供稳定的5V，但它们不会有完全相同的电压。因此电流会从较高侧流向较低侧。大多数板子已经有一个二极管来防止电流回流到其USB。所以虽然从电脑->底座的回流是不可能的，但如果没有二极管，从底座->电脑的回流是可能的。这就是为什么我们的单片机安装指南里提到让+5V VCC线断开连接。

我们目前推荐[1N5817肖特基二极管](https://www.amazon.com/dp/B07Q5H1SLY)。但任何规格类似的二极管应该都可以。

<img src="SetupGuide/Images/1N5817-Schottky-Diode.jpg">

### Pico W：

主文章：[Pico W（高级UART模式）](SetupGuide/Controllers/Controller-PicoW-Advanced.md)

通过二极管将UART的+5V连接到Pico的VSYS（引脚39）。二极管必须允许电流从UART到VSYS。

Pico在VSYS和其自己的USB +5V之间已经有一个二极管。所以你不需要在那里再添加一个。此外，Pico在VSYS和GND之间包含一个47uF电容器，以保证板子有足够电从一个电源过渡到另一个电源。（二极管的切换延迟远长于RP2040或RP2350芯片的时钟周期。）

[引脚图和电路图](https://deepbluembedded.com/raspberry-pi-pico-w-pinout-diagram-gpio-guide/)

**面包板样机：**

<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced-Breadboard0_small.jpg" width="39%"> <img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced-Breadboard1_small.jpg" width="51%">

**"成品"配置：**

<img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced-Raw0_small.jpg" width="45%"> <img src="SetupGuide/Images/PicoW/ControllerSetup-PicoW-Advanced-Raw1_small.jpg" width="45%">

### Pro Micro：

通过二极管将UART的+5V连接到RAW引脚。二极管必须允许电流从UART到RAW。

Pro Micro在RAW和其自己的USB +5V之间已经有一个二极管。所以你不需要在那里在添加一个。此外，Pro Micro在RAW和GND之间有一个10uF电容器，以保证板子有足够电从一个电源过渡到另一个电源。（二极管的切换延迟长于ATmega32U4芯片的时钟周期。）

[引脚图和电路图](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide/hardware-overview-pro-micro)

<img src="SetupGuide/Images/ProMicro/ControllerSetup-ProMicro-Advanced-Breadboard0-Small.jpg" width="39%"> <img src="SetupGuide/Images/ProMicro/ControllerSetup-ProMicro-Advanced-Breadboard1-Small.jpg" width="51%">

### 其他单片机（Uno、Leonardo、Teensy）：

我们没有分析或测试这些单片机，鉴于它们已经是过时的硬件，我们也不打算解决它们上面的低电源故障。但它们的解决方案可能与上述两个单片机类似。如果你想自己动手的话，确保你先了解它们的电路图。


## 致谢

- **作者：** Kuroneko/Mysticial



<hr>

**Discord服务器：**

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)
