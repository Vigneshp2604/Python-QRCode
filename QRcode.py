#importing pyqrcode library is used to create QR Code
import pyqrcode

# Data to encode
QRstr="https://vigneshp2604.github.io/Portfolio/"

# generating a QR code using the create() function  
url=pyqrcode.create(QRstr)

# Create and save the png file naming "myQR.png"
url.png ('myQR.png', scale=10)