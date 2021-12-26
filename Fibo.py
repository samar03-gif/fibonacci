def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
# take input from the user
no_of_terms = int(input("How many terms : "))
# check if the number of terms is valid
if no_of_terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(no_of_terms):
       print(recur_fibo(i))
