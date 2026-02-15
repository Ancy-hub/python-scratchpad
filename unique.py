n=int(input("number of elements in list"))
list1=[]
for i in range(1,n+1):
    x=int(input())
    list1.append(x)

uni=[]

[uni.append(x) for x in list1 if not x in uni]

print(uni)
