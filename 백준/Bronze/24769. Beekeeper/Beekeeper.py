import sys

vowels = "aeiouy"

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    ans = 0
    ans_word = ""
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        
        cnt = 0
        for i in range(1, len(word)):
            if word[i] in vowels and word[i - 1] == word[i]:
                cnt += 1
        if ans < cnt or ans == 0:
            ans = cnt
            ans_word = word

    print(ans_word)