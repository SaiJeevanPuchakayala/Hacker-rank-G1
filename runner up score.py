n = int(input())
m = list(map(int,input().split()))[:n]
k = max(m)
for i in range(len(m)):
    if k in m:
        m.remove(k)
print(max(m))
