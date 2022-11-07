def argss(*args,**kwargs):
    for item in args:
        print(item)
        
        
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
hes=("alish","gautam","aashutosh","bikram","karki")
kw= {"hehe":1,"lolol":2,"shut":3}
argss(*hes,**kw)


   
        
        
    