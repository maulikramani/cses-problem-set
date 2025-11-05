n = int(input())
arr = list(map(int, input().split()))

# Sort array
arr.sort()

# Iterate and check for missing number
i = 1
while i <= n:
    if i-1 < n-1 and arr[i-1] != i:
        print(i, end="")
        break
    i += 1

if i > n:
    print(i-1, end="")
