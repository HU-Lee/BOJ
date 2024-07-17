import sys

def get_ans(arr, me):
    for i in range(3):
        if sorted(arr[i]) == ['-', me, me]:
            arr[i] = [me, me, me]
            return arr
        if sorted(arr[j][i] for j in range(3)) == ['-', me, me]:
            for j in range(3):
                arr[j][i] = me
            return arr
    if sorted([arr[0][0], arr[1][1], arr[2][2]]) == ['-', me, me]:
        arr[0][0] = me
        arr[1][1] = me
        arr[2][2] = me
        return arr
    if sorted([arr[0][2], arr[1][1], arr[2][0]]) == ['-', me, me]:
        arr[0][2] = me
        arr[1][1] = me
        arr[2][0] = me
    return arr


n = int(sys.stdin.readline())
for k in range(n):
    arr = []
    for _ in range(3):
        arr.append(list(sys.stdin.readline().rstrip()))
    me = sys.stdin.readline().rstrip()

    arr = get_ans(arr, me)
    
    print(f'Case {k+1}:')
    for i in range(3):
        for j in range(3):
            print(arr[i][j], end='')
        print()
    