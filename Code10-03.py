def addNum(num):
    if num <= 1:
        return 1
    return num + addNum(num-1)

print(addNum(10))

sumValue = 0
for n in range(10, 0, -1):
    sumValue += n

print(sumValue)