#title-Armstrong No.
#NILAY PEDRAM
#ROLL NO-45,DIV-M 



def amstrong_number(x):
   s=0
   z=x
   while x>0:
    y=x%10
    s=y**3+s
    x=x//10
   print(s)
   if s==z:
     print('Amstrong no.')
   else:
     print('Not an amstrong no.')
x=int(input())
result=amstrong_number(x)
print(result)
