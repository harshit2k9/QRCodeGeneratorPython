import pyqrcode
import png
from pyqrcode import QRCode

url = input("Enter the text/url you want to generate a QR for: ")

link = pyqrcode.create(url)

link.svg("quickres.svg", scale=8)

link.png("quickresponse.png", scale=29)
