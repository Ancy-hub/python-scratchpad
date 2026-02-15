def longest(s):
    n=len(s)
    longest= " "
    if n==0:
        return 0
    else:
        for i in range(n):
            temp=expand(s,i,i)
            if len(temp)>len(longest):
                longest=temp

            temp=expand(s,i,i+1)
            if len(temp)>len(longest):
                longest=temp
    return longest

def expand(s,l,h):
    if l<=0 and h<len(s) and s[l]==s[h]:
        l-=1
        h+=1
    return s[l+1:h]

s='bababababebebebababeeb'
print(longest(s))
    

    