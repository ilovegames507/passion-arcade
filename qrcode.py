 import qrcode



data ="https://passionmccaleb.exprealty.com"


qr = qrcode.QRCode(
    version=5,  # controls size; 1 is smallest, 40 is largest
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (default is 4)
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("groomers_qr_custom_size.png")
img.show()
