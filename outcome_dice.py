#title-outcome of rolling dice
#Nilay Pedram
#M-45


from random import randint as rt                     #importing randint 
def game(dice,faces):                                #defining a fun
      result=0
      for roll in range (0,dice):                    #for loop
         result+=rt(1,faces)
      return result
result=game(2,6)
print(result)
