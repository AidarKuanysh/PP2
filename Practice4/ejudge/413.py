import json
import re

data = json.loads(input())
q = int(input())

pattern = re.compile(r'([^[.\]]+)|\[(\d+)\]')

def resolve(obj, query):
    current = obj
    for match in pattern.finditer(query):
        key, index = match.groups()
        if key is not None:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None, False
        else:
            idx = int(index)
            if isinstance(current, list) and 0 <= idx < len(current):
                current = current[idx]
            else:
                return None, False
    return current, True

for _ in range(q):
    query = input().strip()
    result, ok = resolve(data, query)
    if ok:
        print(json.dumps(result, separators=(',', ':')))
    else:
        print("NOT_FOUND")