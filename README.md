
To Link a URL using QRCode with Python
=============================

# What is a QR Code?

A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols)

# Usage:
At the moment, QR codes are being utilized for a wide range of applications such as making online payments, checking hotel menus, sharing Wi-Fi passwords, obtaining cost and other information of products, and a lot more.
QR codes have become so famous that now every new smartphone comes with a built-in QR code reader.

# Generating QR Code using Python

Python is a programming language that provides different modules and packages that allow us to generate a QR code. For this project, we will be working with the qrcode package in order to generate the code.

However, in order to start working with the package, we have to install it.

# Installing the Python qrcode package:

We can install the qrcode package with the help of the pip installer using the following command:
Syntax::

    $ pip install pyqrcode

The package will be installed in the system as the version of Python and ``pip``.

# Verifying the Installation:
In order to check whether the package has been installed in the system properly or not, we can try importing the package and execute the program.
Once the installation is complete, create a new Python file and type the following syntax in it.

# importing the required module:
    import pyqrcode 

# Generating a Simple QR Code
We can generate a simple QR code using the make function of qrcode and pass the data as its parameter.

Let us consider the following example that produces a QR code that reads "https://vigneshp2604.github.io/Portfolio/".

# importing pyqrcode library is used to create QR Code
    import pyqrcode

# Data to encode:
    QRstr="https://vigneshp2604.github.io/Portfolio/"

# generating a QR code using the create() function:
    url=pyqrcode.create(QRstr)

# Create and save the png file naming "myQR.png":
    url.png ('myQR.png', scale=10)


# Explanation:
In the above snippet of code, we have imported the pyqrcode library and defined a variable that uses the ``create()`` function of the qrcode library to generate a QR code. You can encode as ``SVG``, as well as use a new pure Python image processor to encode to ``PNG`` images.

We can use the smartphone in order to read the above QR code.

# Advanced Usage:
For more control, use the ``QRCode`` class. For example:

    import qrcode
	qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    qr.add_data('Some data')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
   
The version parameter is an integer from ``1 to 40`` that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). Set to None and use the fit parameter when making the code to determine this automatically. fill_color and back_color can change the background and the painting color of the QR, when using the default image factory. 
Both parameters accept RGB color tuples.

    img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
