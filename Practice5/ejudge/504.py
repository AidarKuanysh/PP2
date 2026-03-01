import re
a = input()
nums = re.findall("[0-9]", a)
if len(nums) > 0:
    for i in nums:
        print(i, end=' ')
else:
    print()