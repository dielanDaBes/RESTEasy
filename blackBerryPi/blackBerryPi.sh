#! /bin/bash
echo 0  | tee /sys/class/leds/led0/brightness
echo 0 | tee /sys/class/leds/led[01]/brightness
sleep 1d
