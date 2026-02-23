from datetime import datetime, timedelta, timezone

def parse(s):
    d, t, tz = s.split()
    dt = datetime.strptime(f"{d} {t}", "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz[3] == "+" else -1
    h, m = map(int, tz[4:].split(":"))
    return dt.replace(tzinfo=timezone(sign * timedelta(hours=h, minutes=m)))

start = parse(input().strip()).astimezone(timezone.utc)
end = parse(input().strip()).astimezone(timezone.utc)

print(int((end - start).total_seconds()))