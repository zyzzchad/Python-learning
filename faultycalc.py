from ast import operator
print("\t\t\t\tFaulty calculator\n\n")
print ("Enter a operator:")
num1=input()
print("Enter a number:")
num2=int(input())
print("Enter another number")
num3=int(input())

if num2==45 and num3==3 and num1=='*':
    print("555")
elif num2==56 and num3==9 and num1=="+":
    print("77")
elif num2==56  and num3==6  and num1=="/":
    print("4")
elif num1=="*":
  num4=num3*num2
  print(num4)
        