
no_of_tries=1
print("You've got 5 tries")
while (no_of_tries<9):
    num=int(input("Enter a number"))
    if num>18:
        print("Enter lesser number:")
    if num<18:
        print("Enter greater number")
    if num==18:
        print("You entered right")
        print(no_of_tries,"no of tries it took to get it right")
        break
    print(5-no_of_tries," tries left")
    no_of_tries=no_of_tries+1
    
    if no_of_tries>5:
        print("You lose")
        
       
        