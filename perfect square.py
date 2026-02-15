import math
def perfect_sq(n):
    if n<1:
        return False
    
    else:
        sq=int(math.sqrt(n))
        return sq*sq==n
    
print(perfect_sq(5))
