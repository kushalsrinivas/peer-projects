import pyqrcode
import re
url = input("enter the url  : ")
from datetime import datetime


print("generating qr code ....")
today_date = datetime.now().date()
qr = pyqrcode.create(url)
qr.png(f"{today_date}.png", scale=8)
print(f"{url} is not a valid domain.")
