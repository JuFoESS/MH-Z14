#!/usr/bin/python

## Read out CO2-sensor MH-Z14 digitally
## By Nicolas Goecke and Elias Messinesis
##

import time
import serial

class mhz14: 

	def __init__(self, userport):
		self.ser = serial.Serial(
			port=userport,
			baudrate=9600,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS
		)

		

	def readvalue(self):
		self.ser.isOpen()
		out =''
		command="\xFF\x01\x86\x00\x00\x00\x00\x00\x79"
		self.ser.write(command)

		# let's wait one second before reading output (let's give device time to answer)
		time.sleep(1)
		while self.ser.inWaiting() > 0:
			out += self.ser.read(1)

		err = (len(out) < 3)

		if not err:
		   if ord(out[0]) == 255 and ord(out[1]) == 134:
			  val = ord(out[2])*256 + ord(out[3])
			  return val
			  

		return "error reading CO2 value from MH-Z14"
		
		self.ser.close()
