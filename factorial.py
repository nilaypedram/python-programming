def factorial(n):
   f=1
   if n<0:
      print('enter positive no.')
   elif n==0 or n==1:
      print('1')
   else:
      while n>1:
       f=f*n
       n=n-1
      print(f)
n=int(input("enter a no."))
result=factorial(n)
print(result)
