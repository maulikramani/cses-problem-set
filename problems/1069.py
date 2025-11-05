# Input
s = input()

ans = 1
ch, frq = s[0], 1

for i in range(1, len(s)):
    if ch == s[i]:
        frq += 1
    else:
        ans = max(ans, frq)
        ch, frq = s[i], 1

print(max(ans, frq), end="")