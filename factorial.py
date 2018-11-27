#title-factorial of a no
#Nilay Pedram
#M-45


def factorial(n):                                 #defining the fun
   f=1
   if n<0:                                        #if-elif statement
      print('enter positive no.')
   elif n==0 or n==1:
      print('1')
   else:
      while n>1:                                  
       f=f*n
       n=n-1                                      #refreshing the value of n after every one loop until its 1
      print(f)
n=int(input("enter a no."))                       #user input
result=factorial(n)
print(result)
