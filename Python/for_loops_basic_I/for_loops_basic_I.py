print("Basic")
for x in range(151):
    print(x)

print("Multiples of Five")
for y in range(5,1001,5):
    print(y)

print("Counting,the Dojo Way")
for z in range(151):
    if z%10 == 0:
        print("Coding Dojo")
    elif z%5 == 0:
        print("Coding")
    else:
        print(z)

print("Whoa, That Suckers Huge")
sumArr = []
for i in range(1, 500001, 2):
    sumArr.append(i)

total = sum(sumArr)
print(total)

print("Countdown by Fours")
for a in range(2018, 0, -4):
    print(a)

print("Flexible Counter")
lowNum = 2
highNum = 9
mult = 3
for b in range(lowNum,highNum+1):
    if b%mult == 0:
        print(b)