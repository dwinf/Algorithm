def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if(ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

for _ in range(len(before)):
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])

print(before)
print(after)