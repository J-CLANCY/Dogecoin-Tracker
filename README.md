# Dogecoin Tracker


This simple script was accompanied by a Raspberry Pi 3B+, an SSD1306 (128x32) OLED screen and a single WS2812B addressable-RGB LED. Every ~10s the script polled the [CoinGecko API]() for the current value of dogecoin. The current value in Euro and US Dollar was then printed to the screen over I2C. Finally, the RGB LED was switched to either green or red depending on whether or not the current value was higher or lower than the previous value, green if the same.

This little system brought about great amusement in my old shared accommodation. Many feigned celebrations and woes were uttered when the LED turned green or red. Typically, when green, it was seen as an excuse to treat oneself: "Oh, I see dogecoin is in the green, I can treat myself to a chocolate bar for dessert", for it only to change moments after to red: "Well, no chocolate for me I guess, I'll have to go sell my kidney". One would intuit that this would become tiresome after a while, it did not.

## Project Structure

```
├── ""dogeCounter.py"" => The simple Python script for the dogecoin tracker.
├── ""dogeTracker.mp4"" => A short video of the system (only one I could find). 
```
