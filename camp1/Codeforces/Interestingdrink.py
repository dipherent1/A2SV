from bisect import bisect_right
n = int(input())
a = list(map(int,input().split()))
q = int(input())
qs = [int(input()) for _ in range(q)]
a.sort()

for i in range(q):
    print(bisect_right(a,qs[i]))