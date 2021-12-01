from config import MAX_BRIGHTNESS, SPI_PORT, SPI_DEVICE, PIXEL_COUNT
import RPi.GPIO as GPIO
# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)


def setLights(r, g, b):
		realBrightness_r = int(int(r) * (float(MAX_BRIGHTNESS) / 255.0))
		realBrightness_g = int(int(g) * (float(MAX_BRIGHTNESS) / 255.0))
		realBrightness_b = int(int(b) * (float(MAX_BRIGHTNESS) / 255.0))
		for i in range(pixels.count()):
			pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(realBrightness_r, realBrightness_g, realBrightness_b))
		pixels.show()


def setRGB(r, g, b):
	if r > 255:
		r = 255
	if g > 255:
		g = 255
	if b > 255:
		b = 255

	if r < 0:
		r = 0
	if g < 0:
		g = 0
	if b < 0:
		b = 0
	
	setLights(r, g, b)
