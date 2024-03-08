n = int(input())
p = list(map(int,input().split()))
v = list(map(int,input().split()))

friends = [(p[i],v[i]) for i in range(n)]
friends.sort()

def validate(time):
    right_limit = float("inf")
    left_limit = 0
    for i in range(n):
        
        distance = friends[i][1]*time
        
        left_limit = max(left_limit,friends[i][0]-distance )
        
        right_limit = min(right_limit,friends[i][0]+distance )
    
    
    return right_limit>=left_limit


l = 0
r = max(p)

while r-l>10e-7:
    mid = (r+l)/2
    if validate(mid):
        # ans = mid
        r= mid
    else:
        l=mid

print(r)