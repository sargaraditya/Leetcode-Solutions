def Print(n):
    if (n == 0):
        return 0 
    elif (n == 1):
        print (1)
       
    else :
        print(n)
    
        Print(n-1)
       

res = Print(3)
print(res)
