n=11
flag= "TRUE"
for i in range(2,n):
    if (n % i== 0):
        flag = "FALSE"
        

if (flag== "TRUE"):
    print("PRIME")
else:
    print("NOT PRIME")