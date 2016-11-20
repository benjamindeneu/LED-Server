from config import *

def setLights(pin, brightness):
        realBrightness = int(int(brightness) * (float(MAX_BRIGHTNESS) / 255.0))
        pi.set_PWM_dutycycle(pin, realBrightness)

def setRGB(r,g,b):
        setLights(RED_PIN, r)
        setLights(GREEN_PIN, g)
        setLights(BLUE_PIN,b)
