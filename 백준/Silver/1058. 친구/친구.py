import sys
import collections

n = int(sys.stdin.readline())
graph = collections.defaultdict(list)

for i in range(n):
    s = sys.stdin.readline().rstrip()
    for j, friend in enumerate(s):
        if friend == 'Y':
            graph[i].append(j)
            graph[j].append(i)

def get_2_friends(val: int):
    friends = set()
    for friend in graph[val]:
        friends.add(friend)
        for f in graph[friend]:
            if f != val:
                friends.add(f)

    return len(friends)

ans = 0
for i in range(n):
    ans = max(ans, get_2_friends(i))

print(ans)