from datetime import datetime, timedelta, timezone
import calendar
import math

def parse(s):
    d, t = s.split()
    dt = datetime.strptime(d, "%Y-%m-%d")
    sign = 1 if t[3] == "+" else -1
    h, m = map(int, t[4:].split(":"))
    return dt.replace(tzinfo=timezone(sign * timedelta(hours=h, minutes=m)))

def birthday(year, month, day, tz):
    if month == 2 and day == 29 and not calendar.isleap(year):
        day = 28
    return datetime(year, month, day, tzinfo=tz)

birth = parse(input().strip())
current = parse(input().strip())

current_utc = current.astimezone(timezone.utc)

year = current.year
cand = birthday(year, birth.month, birth.day, birth.tzinfo).astimezone(timezone.utc)

if cand < current_utc:
    year += 1
    cand = birthday(year, birth.month, birth.day, birth.tzinfo).astimezone(timezone.utc)

diff = (cand - current_utc).total_seconds()
print(max(0, math.ceil(diff / 86400)))