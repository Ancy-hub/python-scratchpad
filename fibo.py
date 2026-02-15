def fibo(n):
    if (n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
nterm=5

if nterm < 0:
    print("PLS print positive")
else:
    for i in range(nterm):
        print (fibo(i))