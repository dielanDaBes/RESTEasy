# RESTEasy
![Alt text](RESTEasy_resize.jpg?raw=true "RESTEasy")

# Description
Open Source REST based easy button project for the Raspberry Pi Zero W.
Configure the parameters for an HTTP/HTTPS request through a browser based UI hosted on the Raspberry Pi Zero W and then send that request by hitting the button.

# Future Enhancements
- Ability to put button in host AP mode to configure wifi settings
- Optional Home Assistant mode that allows drop down selection for devices/automations
- Mobile app for configuration

# Instructions...Work In Progress - Full tutorial coming soon at link TBD

1. Wire Easy Button to Raspberry Pi Zero W 
2. 3D print and assemble housing https://www.tinkercad.com/things/0qxXQGSvE9Z?sharecode=hq_qgz9BtA8mJckSX1Y-pCkFWSxI0rSVLPcXG-DfLVY
3. Use Raspberry Pi imager to flash PI OS Lite to SD card configuring desired hostname, password, ssh, and network settings
4. ```wget https://raw.githubusercontent.com/dielanDaBes/RESTEasy/main/setup.sh && sudo chmod +x setup.sh && ./setup.sh```
5. Edit Docker Compose Settings
6. Docker Compose Up
