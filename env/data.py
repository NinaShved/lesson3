from datetime import datetime, timedelta
dt_now = datetime.now()
print("сегодня", dt_now.strftime('%d.%m.%Y %H:%M'), "число")
#print(dt_now)
#from datetime import date, timedelta
delta = timedelta(days=1)
#print(timedelta)

dt = datetime.now()
print(dt)
dte = dt_now - delta
#print(dte.strftime('%d.%m.%Y'))
print("Вчера было", dte.strftime('%d.%m.%Y'), "число")
dtt = dt_now + delta
print("Завтра будет", dtt.strftime('%d.%m.%Y'), "число")

delta = timedelta(days=30)
dtm = dt_now + delta
print("Через 30 дней будет ", dtm.strftime('%d.%m.%Y'), "число")