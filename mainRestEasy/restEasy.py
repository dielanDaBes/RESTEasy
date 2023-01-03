#!/usr/bin/python
from datetime import datetime
import time
import RPi.GPIO as GPIO
import json
import sys
import requests
import ast
import traceback
import os

SleepyTime = int(os.getenv('DEBOUNCE' , 3))# default deboune time for button
EasyButtonGPIO = int(os.getenv('BUTTONINPUT',13))
EnableLogging = eval(os.getenv('ENABLELOGS', 'False'))
StandardLogic = eval(os.getenv('STANDARDLOGIC', 'True'))
if StandardLogic:
  pullDirection = GPIO.PUD_DOWN
else:
  pullDirection = GPIO.PUD_UP
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(EasyButtonGPIO, GPIO.IN, pull_up_down=pullDirection)  

def timePrint(string):
  timeString = str(datetime.now()) + "UTC0" + " | " + str(string) + "\n"
  if EnableLogging:
    log = open('easyButton.log', 'a') 
    log.write(timeString)
    log.close()
  print(timeString)
    

def buttonPressed(channel):
  jsonFile = open('./static/restEasy.conf', 'r')
  configFile = json.load(jsonFile)
  url = configFile["url"]
  method = configFile["method"]
  body = ast.literal_eval(configFile["body"])
  headers = ast.literal_eval(str(configFile["headers"]))
  timePrint("Button was pushed!\nSending Request to: " + url + "\nHeaders: " + str(headers) + "\nBody: " + str(body) + "\nMethod: " + method)
  requests.post(url,headers=headers,data=body)
  httpMethod = getattr(requests, method.lower())
  timePrint(httpMethod(url, headers=headers, data=json.dumps(body)))
  jsonFile.close()
    

try:
  timePrint('Started')
  while True:
    if GPIO.input(EasyButtonGPIO) == StandardLogic:
      try:
        buttonPressed(EasyButtonGPIO) 
      except Exception as e:
         traceback.print_exc()
      time.sleep(SleepyTime)
finally:
  GPIO.cleanup()
