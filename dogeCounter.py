import time
from board import SCL, SDA
import board
import neopixel
import busio
import os
from oled_text import OledText, Layout32
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
i2c = busio.I2C(SCL,SDA)

pixels = neopixel.NeoPixel(board.D18, 1)

oled = OledText(i2c, 128, 32)
oled.layout = Layout32.layout_2medium()

while True:
	oled.text("Getting good",1)
	oled.text("boi prices...", 2)
	time.sleep(1)
	previous = 0

	doge = cg.get_price(ids="dogecoin", vs_currencies="eur, usd")
	oled.text("EUR: " + str(doge['dogecoin']['eur']),1)
	oled.text("USD: " + str(doge['dogecoin']['usd']),2)
	current = doge['dogecoinn']['eur']
	if current >= previous:
		pixels[0] = (0,255,0)
	else:
		pixels[0] = (255,0,0)
	previous = current
	
	time.sleep(10)
