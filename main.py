import os
from datetime import datetime
import qrcode

def generate_qr():
    url = input("Enter the URL to encode: ").strip()
    if not url:
        print("Error: URL cannot be empty.")
        return

    # 1. Create a unique filename using the current date and time
    # Format results in something like: qr_20260714_120530.png
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"qr_{timestamp}.png"
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    try:
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"🎉 QR Code saved as: {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    generate_qr()