import sys

n,m,k = map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 세그먼트 트리 길이
# (n보다 큰 2제곱수) * 2 < 2n * 2 = 4n
segments = [0]*n*4

# 세그먼트 트리 초기화
def init_tree(start: int, end: int, target: int) -> int:
    if start == end:
        # start == end 일 경우 단순 업데이트
        segments[target] = arr[start]
    else:
        # 아닐 경우 좌우 트리를 초기화하고 그 합을 업데이트
        mid = (start + end) // 2
        segments[target] = init_tree(start, mid, target*2) + init_tree(mid+1, end, target*2+1)
    return segments[target]

# 세그먼트 트리 합 (left ~ right)
def sum(start: int, end: int, target: int, left: int, right: int) -> int:
    if left > end or right < start:
        # start ~ end가 범위 밖이면 0
        return 0
    if left <= start and end <= right:
        # start ~ end가 범위 안이면 반환
        return segments[target]
    # 아니면 나누어 합 구하기
    mid = (start + end) // 2
    return sum(start, mid, target*2, left, right) + sum(mid+1, end, target*2+1, left, right)

# 세그먼트 트리 변경
def update_tree(start: int, end: int, target: int, index: int, new_val: int) -> None:
    if index < start or index > end:
        # 범위 밖이면 바꿀 게 없음
        return
    if start == end:
        # start == end 면 값 변경
        segments[target] = new_val
    else:
        # 아니면 나누어 업데이트하고 그 합을 업데이트
        mid = (start + end) // 2
        update_tree(start, mid, target*2, index, new_val)
        update_tree(mid+1, end, target*2+1, index, new_val)
        segments[target] = segments[target*2] + segments[target*2+1]


init_tree(0, n-1, 1)

cnt = 0
for _ in range(m+k):
    a,b,c = map(int,sys.stdin.readline().split())

    if a == 1:
        update_tree(0, n-1, 1, b-1, c)
    else:
        print(sum(0, n-1, 1, b-1, c-1))