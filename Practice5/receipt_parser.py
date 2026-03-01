import re
import json

with open("C:/Users/Roar/Documents/GitHub/PP2/Practice5/raw.txt", encoding="utf-8") as f:
    text = f.read()

#convert numbers 1 200 to 1200
def normalize_number(s):
    return float(s.replace(" ", "").replace(",", "."))

#extract product details
item_pattern = re.compile(
    r"\d+\.\s*\n"
    r"(.+?)\n"
    r"([\d, ]+)\s*x\s*([\d, ]+)\n"
    r"([\d, ]+)\n",
    re.DOTALL
)

items = []
for m in item_pattern.finditer(text):
    items.append({
        "name": m.group(1).strip(),
        "quantity": normalize_number(m.group(2)),
        "unit_price": normalize_number(m.group(3)),
        "total_price": normalize_number(m.group(4)),
    })

#extract all prices
prices = [
    normalize_number(p)
    for p in re.findall(r"\b\d[\d ]*,\d{2}\b", text)
]

#extract total
total_match = re.search(r"ИТОГО:\s*\n([\d, ]+)", text)
total_amount = normalize_number(total_match.group(1)) if total_match else None

#extract date & time
dt_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
date, time = dt_match.groups() if dt_match else (None, None)

#extract payment method
payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment_method = payment_match.group(1) if payment_match else None

#structured output
result = {
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "total_amount": total_amount,
    "products": items,
    "prices_found": prices
}

print(json.dumps(result, ensure_ascii=False, indent=2))