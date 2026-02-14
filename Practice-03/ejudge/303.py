stfu = input()

num1 = ""
num2 = ""
i = 0

# read first number
while stfu[i] != '+' and stfu[i] != '-' and stfu[i] != '*':
    c1 = stfu[i]
    c2 = stfu[i+1]
    c3 = stfu[i+2]

    if c1 == 'O' and c2 == 'N' and c3 == 'E':
        num1 += '1'
    if c1 == 'T' and c2 == 'W' and c3 == 'O':
        num1 += '2'
    if c1 == 'T' and c2 == 'H' and c3 == 'R':
        num1 += '3'
    if c1 == 'F' and c2 == 'O' and c3 == 'U':
        num1 += '4'
    if c1 == 'F' and c2 == 'I' and c3 == 'V':
        num1 += '5'
    if c1 == 'S' and c2 == 'I' and c3 == 'X':
        num1 += '6'
    if c1 == 'S' and c2 == 'E' and c3 == 'V':
        num1 += '7'
    if c1 == 'E' and c2 == 'I' and c3 == 'G':
        num1 += '8'
    if c1 == 'N' and c2 == 'I' and c3 == 'N':
        num1 += '9'
    if c1 == 'Z' and c2 == 'E' and c3 == 'R':
        num1 += '0'

    i += 3

op = stfu[i]
i += 1

# read second number
while i < len(stfu):
    c1 = stfu[i]
    c2 = stfu[i+1]
    c3 = stfu[i+2]

    if c1 == 'O' and c2 == 'N' and c3 == 'E':
        num2 += '1'
    if c1 == 'T' and c2 == 'W' and c3 == 'O':
        num2 += '2'
    if c1 == 'T' and c2 == 'H' and c3 == 'R':
        num2 += '3'
    if c1 == 'F' and c2 == 'O' and c3 == 'U':
        num2 += '4'
    if c1 == 'F' and c2 == 'I' and c3 == 'V':
        num2 += '5'
    if c1 == 'S' and c2 == 'I' and c3 == 'X':
        num2 += '6'
    if c1 == 'S' and c2 == 'E' and c3 == 'V':
        num2 += '7'
    if c1 == 'E' and c2 == 'I' and c3 == 'G':
        num2 += '8'
    if c1 == 'N' and c2 == 'I' and c3 == 'N':
        num2 += '9'
    if c1 == 'Z' and c2 == 'E' and c3 == 'R':
        num2 += '0'

    i += 3

a = int(num1)
b = int(num2)

if op == '+':
    res = a + b
if op == '-':
    res = a - b
if op == '*':
    res = a * b

res = str(res)
answer = ""

for d in res:
    if d == '0':
        answer += "ZER"
    if d == '1':
        answer += "ONE"
    if d == '2':
        answer += "TWO"
    if d == '3':
        answer += "THR"
    if d == '4':
        answer += "FOU"
    if d == '5':
        answer += "FIV"
    if d == '6':
        answer += "SIX"
    if d == '7':
        answer += "SEV"
    if d == '8':
        answer += "EIG"
    if d == '9':
        answer += "NIN"

print(answer)