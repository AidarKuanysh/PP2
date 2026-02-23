from datetime import datetime, timedelta

#ex 1
now = datetime.now()
print(now - timedelta(days=5))

#ex 2
today = datetime.now().date()
print(today - timedelta(days=1))
print(today)
print(today + timedelta(days=1))

#ex 3
dt = datetime.now()
print(dt.replace(microsecond=0))

#ex 4
d1 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
d2 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
print(int((d2 - d1).total_seconds()))