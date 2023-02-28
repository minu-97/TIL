arr = [1,2,6,5,4,2]
dat = [0 for _ in range(0,7)]
for i in range(len(arr)):
    dat[arr[i]]=1

for i in range(len(dat)):
    if dat[i] == 0:
        continue
    print(i)

def meet(index):
    return (index * 3+11) % 10

dat = [0 for _ in range(10)]

old = -1
start = 1

while True:
    start = meet(start)
    if(dat[start]) == 1:
        break
    dat[start] = 1

    if old == start:
        break
print(start)