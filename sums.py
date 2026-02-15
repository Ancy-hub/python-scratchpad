n=int(input("Enter the number"))
def sumo(n):
    x=0
    for digits in str(n):
        x = x + int(digits)
    return x

print(sumo(n))

