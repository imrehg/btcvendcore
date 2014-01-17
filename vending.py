import os
import serial
from escpos import *
import sys
import urllib
import datetime

## Hardware
# Bill acceptor
bill = serial.Serial('/dev/ttyUSB0', 9600, parity=serial.PARITY_EVEN, timeout=1)
# Thermal printer
Epson = printer.Serial('/dev/ttyACM1', baudrate=115200, xonxoff=True)

# Hardcoded, TWD/BTC, should be around the 2014/01/16 weighted avearge
exchange = 25400.0


# Have to start with bill acceptor off
# This part wait for it to start and enables it 
while True:
    try:
        r = bill.read()
        if len(r) > 0:
            print ord(r)
            rval = ord(r)

            if rval ==  0x8f: # "I'm on" code
                bill.write(chr(0x02))
                print "Power on; reply sent"
                bill.write(chr(0x5e))
                break
    except KeyboardInterrupt:
        sys.exit(0)

print "Welcome to BitcoinVending v0.0.1"
print "Scan your receiver code"

# Start zbar barcode reader on the laptop webcam, in the background
p=os.popen('LD_PRELOAD=/usr/lib/libv4l/v4l1compat.so /usr/bin/zbarcam --nodisplay --raw /dev/video0','r')

# Read a single code
code = p.readline()
address = code.split(':')[1]
print "Receiving address: " + address
print "Exchange rate: %d TWD/BTC" %exchange
print "Add bills... (press CTRL-C when finished)"

# Starting at nothing
value = 0

while True:
    try:
        r = bill.read()
        if len(r) > 0:
            # print ord(r)
            rval = ord(r)

            if rval ==  0x8f:  # "I'm on" code
                bill.write(chr(0x02))
                print "Power on; reply sent"
                bill.write(chr(0x5e))
            if rval == 0x40:  # "Bill type #1"
                bill.write(chr(0x02))
                value += 100
                print "Got 100NT"
            if rval == 0x41:  # "Bill type #2"
                bill.write(chr(0x02))
                value += 500
                print "Got 500NT"
            if rval == 0x42:  # "Bill type #3"
                bill.write(chr(0x02))
                value += 1000
                print "Got 1000NT"
        else:
            pass
            # print "."
    except KeyboardInterrupt: # Finished
        break

print "Total value: %d NTD" %value 

# Processing tranaction
if value > 0:
    btc = value / exchange
    print "Sending %.8f BTC" %btc 

    # Send by API call to server
    url = 'http://localhost:12000/send/%s/%.8f' %(address, btc)
    resp = urllib.urlopen(url)
    code = resp.read()

    # Print receipt
    now = datetime.datetime.now()

    Epson.text("Bitcoin Vending v0.0.1\n\n")
    Epson.text("%s\n" %now.date())
    Epson.text("%s\n\n" %now.time())

    Epson.text("Sending to:\n")
    Epson.text("%s\n" %address)
    Epson.text("TWD: %d\n" %value)
    Epson.text("BTC: %.8f\n" %btc)

    Epson.text("Transaction code:\n")
    Epson.text("%s\n" %code)

    Epson.text("Thank you!\n\n")
    Epson.image('bitcoin.gif')
    Epson.cut()

else:
    print "Nothing to send"

print "Thank you!"
