#title-finding average
#Nilay Pedram
#M-45



total=0                             #initializing
n=0
count=0
while n>=0:                         #while loop
   total+=n
   count+=1                         #refresh the count variable after one cycle by increasing it by 1
   n=int(input())                   
avg=total/(count-1)
print(avg)
