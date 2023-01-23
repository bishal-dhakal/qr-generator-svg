import pyqrcode
from pyqrcode import QRCode

#input
s= 'Welcome to the python world'

#Generate QR code
url = pyqrcode.create(s)

#final qr
url.svg('info.svg', scale=8)