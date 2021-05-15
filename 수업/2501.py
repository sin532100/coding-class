inMain = int(input())
inSub = int(input())

a_list = []

for i in range(1,inMain+1):
    if inMain % i == 0:
        a_list.append(i)

if len(a_list) < inSub:
    print(0)
else:
    print(a_list[inSub-1])