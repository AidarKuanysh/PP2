import importlib

q = int(input())
for _ in range(q):
    module_path, attr = input().split()
    try:
        mod = importlib.import_module(module_path)
    except Exception:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(mod, attr):
        print("ATTRIBUTE_NOT_FOUND")
        continue
    val = getattr(mod, attr)
    if callable(val):
        print("CALLABLE")
    else:
        print("VALUE")