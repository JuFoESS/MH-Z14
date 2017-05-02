from mhz14 import mhz14

# Important: UART enable in /boot/config.txt !!
# configure the serial connections (the parameters differs on the device you are connecting to)
# /dev/ttyUSB0 is used, if USB Console Cable is connected
# Raspberry Pi3: /dev/ttyS0, else /dev/ttyAMA0

sensor=mhz14.mhz14("/dev/ttyS0")
print sensor.readvalue()
