import serial
import sys
import time
import RPi.GPIO as GPIO
import threading
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime, time

#set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#global variables
TriggerCounter = 0
TimerCounter = 0

#Handeler method for when the sensor is triggered
def triggerFunction(channel):
	#get global variable
	global TriggerCounter
	global TimerCounter
	#increase counter
	TriggerCounter = TriggerCounter + 1
	#reser timer counter
	TimerCounter = 0
	print('Sensor Triggered: ' + str(TriggerCounter))

#method for special commands in the display 
def matrixwritecommand(commandlist):
	commandlist.insert(0, 0xFE)
	for i in range(0, len(commandlist)):
		ser.write(chr(commandlist[i]))

def clearDisplay():
	matrixwritecommand([0x58])

def turnDisplayOn():
	matrixwritecommand([0x42])

def turnDisplayOff():
	matrixwritecommand([0x46])

def timerTrigger():
	#get global variables
	global TriggerCounter
	global TimerCounter
	#increase timer
	TimerCounter = TimerCounter + 1
	threading.Timer(5.0, timerTrigger).start()
	#check if it has been 15 seconds with no activity
	if TimerCounter > 3:
		#15 seconds has passed with no trigger
		if TriggerCounter > 6:
			#coffee has been made
			TriggerCounter = 0
			TimerCounter = 0
			print('coffee is made')
			#clearTheDisplay
			clearDisplay()
			#print the new time to the display
			ser.write("Last Coffee Brewed At ")
			ser.write(time.strftime("%I:%M %p"))
			sendEmail()
		else:
			#false trigger reset
			TriggerCounter = 0
			TimerCounter = 0
			print('no Coffee')

def sendEmail():
	password = " Add Password Here "
	fromaddr = "coffee@yourdomain.org"
	toaddr = "coffeealert@yourdomain.org"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Hot Coffee Has Been Brewed"

	body = 'Hot Coffee Has Been Brewed <br> <img src="http://i.imgur.com/VQEsGHz.jpg"></img>'
	msg.attach(MIMEText(body, 'html'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, password)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

#set the serial port for the LDC Display 
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#GPIO Event regrestration
GPIO.add_event_detect(23, GPIO.RISING, callback=triggerFunction, bouncetime=300)

#start timer
timerTrigger()

#display status variable
displayStatus = true
#check display status
nowDate = datetime.now()
nowTime = now.time()
if nowTime >= time(08,00) and nowTime <= time(17,00):
	displayStatus = true
	turnDisplayOn()
else:
	displayStatus = false
	turnDisplayOff()

#turn display on/off loop
while True:
	print(time.strftime("%I:%M:%S:%p"))
	time.sleep(1)
	#turn the diplay on between 8:00am - 5:00pm
	nowDate = datetime.now()
	nowTime = now.time()
	if nowTime >= time(08,00) and nowTime <= time(17,00) and displayStatus != true:
			displayStatus = true
			turnDisplayOn()
	elif displayStatus != false:
			displayStatus = false
			turnDisplayOff()
#cleanup	
GPIO.cleanup()