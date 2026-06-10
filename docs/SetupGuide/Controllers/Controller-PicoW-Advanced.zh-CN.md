---
social:
  cards: false
---

# 树莓派: Pico W 和 Pico 2 W（高级配置）

这高级配置在功能上与[UART模式](Controller-PicoW-UART.md)相同，但在从底座插拔Switch时单片机既不会故障也不会重置。

延伸阅读：[欠压故障](../../PowerGlitching.md)

这是我们做过的最困难的串口配置，适合硬件老手。注意要是配置错误有烧坏器件的风险。

| **模式** | **连接方式** | **模拟游戏手柄支持** | **配置难度** |
| --- | --- | --- | --- |
| [USB模式](Controller-PicoW-USB.md) | 1. Pico W的USB端口 -> 电脑 | 仅能无线连接Switch：<br>- Switch 1: 无线Pro手柄<br>- Switch 1: 左Joy-Con<br>- Switch 1: 右Joy-Con | 非常简单 |
| [UART模式](Controller-PicoW-UART.md) | 1. Pico W的USB端口 -> Switch<br>2. Pico W的引脚6/7/8 -> UART<br>3. UART -> 电脑 | 无线和有线连接：<br>- 键盘<br>- Switch 1: 有线手柄<br>- Switch 2: 有线手柄<br>- Switch 1: 无线Pro手柄<br>- Switch 1: 左Joy-Con<br>- Switch 1: 右Joy-Con | 较困难 |
| **高级UART模式<br>（本指南）** | 1. Pico W的USB端口 -> Switch<br>2. Pico W的引脚6/7/8/39 -> UART<br>3. UART -> 电脑 | 无线和有线：<br>- 键盘<br>- Switch 1: 有线手柄<br>- Switch 2: 有线手柄<br>- Switch 1: 无线Pro手柄<br>- Switch 1: 左Joy-Con<br>- Switch 1: 右Joy-Con | 最困难 |

如果你读到这里，说明你已正确配好了Pico W（UART模式）。本指南只会涵盖与基本UART模式的不同点。

<img src="../Images/PicoW/ControllerSetup-PicoW-Advanced.jpg" width="45%">

## 硬件配置：

我们给的硬件清单是用来制作一个没有外露电路且易于使用的盒装成品。但你也可以自由发挥。

**所需硬件：**

1. 一个树莓派Pico W或Pico 2 W单片机板（不带引脚）
2. [一根micro-USB转USB-A线或转接头](https://www.amazon.com/gp/product/B09FXJD61Z)
3. [USB转串口TTL（UART）](https://www.amazon.com/dp/B07T1XR9FT)
4. [1N5817肖特基二极管](https://www.amazon.com/dp/B07Q5H1SLY)
5. [压入式排针](https://www.adafruit.com/product/5938)（或焊接）
6. [杜邦连接器套件](https://www.amazon.com/dp/B096DC1J3X)（或焊接）
7. [Pico外壳](https://www.adafruit.com/product/6252)（仅兼容不带引脚的Pico）

因为不少零件只能批量购买，单制作一台成品的价格很贵。但批量制作的话，单件成本仅为12美元。


### 硬件组装：

进行以下连接：

| **UART引脚** | **Pico W引脚** |
| --- | --- |
| RX | TX -> GP4（引脚6） |
| TX | RX <- GP5（引脚7） |
| GND | GND（引脚8，或任何其他GND引脚） |
| VCC (+5V) | 通过二极管连接VSYS（引脚39）|

与基本UART模式的不同之处在于，这里我们连接了UART的+5V VCC线。这让Pico可以由USB或UART任一方供电，从而让它在插拔Switch时保持供电而不会故障或重置。

重要的是VCC到VSYS连接必须通过这肖特基二极管，该二极管只允许电流从VCC流到VSYS。**不然Switch底座USB侧电压更高时电流会通过UART回流到电脑，烧坏器件!!**


延伸阅读：

- [树莓派Pico供电指南](https://www.penguintutor.com/electronics/pico-power)
- [我需要什么肖特基二极管为树莓派Pico提供冗余电源？](https://electronics.stackexchange.com/questions/548990/which-shottky-diode-do-i-need-for-redundant-power-to-a-raspberry-pi-pico)
- [引脚图和电路图](https://deepbluembedded.com/raspberry-pi-pico-w-pinout-diagram-gpio-guide/)



以下是各种正确配置的图片：

**面包板样机：**

<img src="../Images/PicoW/ControllerSetup-PicoW-Advanced-Breadboard0_small.jpg" width="39%"> <img src="../Images/PicoW/ControllerSetup-PicoW-Advanced-Breadboard1_small.jpg" width="51%">

**“成品”配置：**

<img src="../Images/PicoW/ControllerSetup-PicoW-Advanced-Raw0_small.jpg" width="45%"> <img src="../Images/PicoW/ControllerSetup-PicoW-Advanced-Raw1_small.jpg" width="45%">


## 软件设置

一切都与[Pico W UART模式指南](Controller-PicoW-UART.md#software-setup)相同。







<hr>

**致谢：**

- Kuroneko/Mysticial

**Discord服务器：**

[<img src="https://canary.discordapp.com/api/guilds/695809740428673034/widget.png?style=banner2">](https://discord.gg/cQ4gWxN)
