# Input
n = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(1, n):
    ans += max(0, arr[i-1]-arr[i])
    arr[i] = max(arr[i], arr[i-1])

print(ans, end="")