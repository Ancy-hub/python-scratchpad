number=12321
reverse_number=0
n=number
# while we have not reached the end of the number
while(n !=0):
   # finding the last element of number 'n'
   rem = n % 10
   reverse_number = reverse_number * 10 + rem
   n=int(n / 10)
if(number == reverse_number):
   print("Palindrome")
else:
   print("Not a Palindrome")

