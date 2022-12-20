from datetime import date, datetime
import locale

locale.setlocale(locale.LC_ALL)

tuday = date.today()
print(tuday)

now=datetime.now()
print(now)

print(now.strftime('%A'))