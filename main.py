import pyqrcode
url = input("enter the url  : ")
from datetime import datetime
print(f"{url} is a valid domain.")
print("generating qr code ....")
today_date = datetime.now().date()
qr = pyqrcode.create(url)
qr.png(f"{today_date}.png", scale=8)
print(f"{url} is not a valid domain.")
