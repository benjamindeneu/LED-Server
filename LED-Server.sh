#STOP POSSIBLE RUNNING PIGPIOD
sudo killall pigpiod
#START PIGPIOD
sudo pigpiod
#START LED-SERVER
sudo python ./server.py
