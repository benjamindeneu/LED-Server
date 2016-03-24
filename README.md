#LED-Server

This Script can be used on a Raspberry Pi to Control a RGB-Led Strip connected to its GPIO-Pins.
The Script creates a Socket and waits for Commands to set the Color of your LED-Strip.

An Android App to Control the LED-Strip via Wifi can be found here: [Android LED-Controller App](https://github.com/simondankelmann/LED_Controller)

In Order to use it you will need the PIGPIOD Library installed on your Raspberry Pi, have a look at it here:
http://abyz.co.uk/rpi/pigpio/

Before you start the script (after installing PIGPIOD) you need to run:

`sudo pigpiod`

to start it as a daemon.
Set the IP-Address and Port in the Script to your local Settings.

Here's how to wire it, in my case i used **STP16NF06L Mosfets** (The RGB-Led in this Picture can be replaced by a RGB-Led Strip):

![](https://github.com/simondankelmann/LED-Server/blob/master/Server-Setup.png)
