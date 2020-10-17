x = int(input())
y = int(input())
z = int(input())
n = int(input())
for x in range(x+1):
    for y in range(y+1):
        for z in range(z+1):
            arr = [[x,y,z]]
            arr.split(',')
            if x+y+z != n:
                print(arr,end=" ")
