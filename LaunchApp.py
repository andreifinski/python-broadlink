#!/usr/bin/python
import broadlink
import time
import sys

device = broadlink.rm(host=("broadlink_rm_ip",80), mac=bytearray.fromhex("broadlink_rm_mac"))
device.auth()
device.host

myapphex="application_signal_hex"

device.send_data(myappshex.decode('hex'))

time.sleep(1)

okhex="ok_signal_hex"

device.send_data(okhex.decode('hex'))

time.sleep(1)

device.send_data(okhex.decode('hex'))
