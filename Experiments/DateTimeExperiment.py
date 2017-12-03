import locale
import time
from datetime import datetime

locale.setlocale(locale.LC_TIME, "el")


def crm(): return int(round(time.time()) / 24 / 60 / 60)


# print(datetime.now().time())
# print(datetime.now())
# print(datetime.now().timestamp())
# print(round(time.time()))

date1 = datetime.now()
date2 = date1.replace(month=12, day=25)

i = date2.timestamp() - date1.timestamp()
print(i / 24 / 60 / 60)

date3 = date1.strftime("%d/%m/%Y")
print(date3)
