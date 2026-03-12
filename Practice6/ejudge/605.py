user = input()
vwl = "aeiouAEIOU"
bol = False
for uc in range(len(user)):
    for vc in range(len(vwl)):
        if user[uc] == vwl[vc]:
            bol = True
            break

if bol:
    print("Yes")
else:
    print("No")