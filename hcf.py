'''def hcf(a,b):
    if (b==0):
        return a
    else:
        return hcf(b, a % b)
    
print(hcf(2,3)) '''

def occ(lst,x):
    count = 0
    for ele in lst:
        if (ele==x):
            count +=1
    return count

lst=[1,2,3,4,5,6,6,6,6]
x=6
print(occ(lst,x))
