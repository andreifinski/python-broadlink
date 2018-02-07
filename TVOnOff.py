#!/usr/bin/python
import broadlink
import time
import sys

device = broadlink.rm(host=("ip_of_broadlink_rm",80), mac=bytearray.fromhex("mac_address_of_broadlink_rm"))
device.auth()
device.host


myhex="get_your_hex_code"

device.send_data(myhex.decode('hex'))
