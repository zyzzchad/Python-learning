from operator import truediv
print("Enter the no of rows you want to print:")
num=int(input())
print("Enter the boolean value 1 or 0")
num1=int(input())
new=bool(num1)
if num1==True:
    for i in range(1,num+1):
        print("*"*i)
        
if num1==0:
    for i in range(num,0,-1):
        print("*"*i)
    
    