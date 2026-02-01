#the break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#examples:
#count to 10
ctt = 1
while ctt < 11:
    print(ctt, end=' ')
    ctt += 1

#square numbers from 1 to 6
snn = 1
while snn < 7:
    print(snn**2, end=' ')
    snn += 1
print()
#sum of all numbers from 20 to 25
sum = 0
san = 20
while san < 26:
    sum += san
    san += 1
print(sum)
#endless loop until user types 'stop'
els = ''
while els != 'stop':
    els = input()