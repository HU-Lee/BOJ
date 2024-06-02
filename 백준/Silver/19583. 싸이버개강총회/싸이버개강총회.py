import sys

def convert_time(s: str) -> int:
    h, m = s.split(":")
    return int(h) * 60 + int(m)

s,e,q = sys.stdin.readline().split()
s = convert_time(s)
e = convert_time(e)
q = convert_time(q)

attend = set()
cnt = 0
while True:
    try:
        t, name = sys.stdin.readline().split()
        t = convert_time(t)
        if t <= s:
            attend.add(name)
        elif e <= t <= q:
            if name in attend:
                cnt += 1
                attend.remove(name)
    except:
        break

print(cnt)
