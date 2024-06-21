import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

ab = []
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])

cd = []
for i in range(n):
    for j in range(n):
        cd.append(arr[i][2] + arr[j][3])

result = 0
ab.sort()
cd.sort(reverse=True)
idx1, idx2 = 0, 0

while idx1 < len(ab) and idx2 < len(cd):
    if ab[idx1] + cd[idx2] > 0:
        idx2 += 1
    elif ab[idx1] + cd[idx2] < 0:
        idx1 += 1
    else:
        tmp1, tmp2 = ab[idx1], cd[idx2]
        cnt1, cnt2 = 0, 0
        while idx1 < len(ab) and ab[idx1] == tmp1:
            idx1 += 1
            cnt1 += 1
        while idx2 < len(cd) and cd[idx2] == tmp2:
            idx2 += 1
            cnt2 += 1
        result += cnt1 * cnt2


print(result)

