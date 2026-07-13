import qrcode
 
url = input("Enter URL")
file_path = "C:\\Users\\Testing\\Desktop\\Projects\\QR Generator\\my_qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Generated")