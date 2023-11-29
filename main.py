import pyqrcode
from datetime import datetime

url = input("enter the url  : ")
print(f"generating qr code for {url} .... ")

today_date = datetime.now().date()
qr = pyqrcode.create(url)
qr.png(f"{today_date}.png", scale=8)

