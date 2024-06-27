import sys

def insert_trie(trie, words):
    cur = trie
    for c in words:
        if c not in cur:
            cur[c] = {}
        cur = cur[c]

def print_trie(trie, level=0):
    for c in sorted(trie.keys()):
        print('--' * level + c)
        print_trie(trie[c], level + 1)

trie = {}

n = int(sys.stdin.readline())
for _ in range(n):
    arr = sys.stdin.readline().split()
    insert_trie(trie, arr[1:])

print_trie(trie)