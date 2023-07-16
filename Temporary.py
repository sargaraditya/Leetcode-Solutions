
def Numberpositive(j):
    for i in range(len(j)):
        if j[i]>= 0 :
            print ("it is positive")
        else:
            print ("it is negative")


j = [1,2,3,0,-1,-2]

res = Numberpositive(j)

print(res)

