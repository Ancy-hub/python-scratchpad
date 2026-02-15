def lcm(a,b):
    g=max(a,b) 
    lcm=0
    while True:
        if (g % a == 0) & (g % b == 0):
            lcm = g
            break
        g+=1
    return lcm

print(lcm(2,3))