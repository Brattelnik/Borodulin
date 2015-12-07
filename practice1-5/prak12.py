n = int(input())
print(tuple(sorted(map(str, input().split())))[n//2])
