#def oddX3_evenX2(n):
#    return n*2 if n%2==0 else n*3

#oddX3_evenX2 = lambda n: n*2 if n%2==0 else n*3

#print(oddX3_evenX2(5))

a_list = [i for i in range(10)]

print(a_list)

b_list = list(map(lambda n: n*2 if n%2==0 else n*3, a_list))
print(b_list)

c_list = [i for i in range(21)]

turnToMinus_list = list(map(lambda n: -n if n%2 == 0 or n%5 == 0 else n/2,c_list)) 

print(turnToMinus_list)