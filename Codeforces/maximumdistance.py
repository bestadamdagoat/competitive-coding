N = int(input())
xvals = [int(x) for x in input().split()]
yvals = [int(x) for x in input().split()]
 
maxd = -1
 
for f in range(0, N):
    for s in range(f+1, N):
        dist = (xvals[s]-xvals[f])**2 + (yvals[s]-yvals[f])**2
        maxd = max(maxd, dist)
print(maxd)
