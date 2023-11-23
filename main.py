import pyqrcode
import re
url = input("enter the url  : ")
from datetime import datetime


def is_valid_domain(domain):
    domain_pattern = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    match = domain_pattern.match(domain)
    return bool(match)


if is_valid_domain(url):
    print(f"{url} is a valid domain.")
    print("generating qr code ....")
    today_date = datetime.now().date()

    qr = pyqrcode.create(url)
    qr.png(f"{today_date}.png", scale=8)
else:
    print(f"{url} is not a valid domain.")
