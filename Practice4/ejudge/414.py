from datetime import datetime, timedelta, timezone

def parse(line):
    date_part, tz_part = line.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if tz_part[3] == '+' else -1
    hours, minutes = map(int, tz_part[4:].split(':'))
    offset = timedelta(hours=hours, minutes=minutes) * sign
    tz = timezone(offset)
    return dt.replace(tzinfo=tz).astimezone(timezone.utc)

dt1 = parse(input().strip())
dt2 = parse(input().strip())

diff = abs((dt1 - dt2).total_seconds())
print(int(diff // 86400))