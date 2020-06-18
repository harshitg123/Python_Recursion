# program for checking
# value present in list

def fun(a,ind,se,le):
    if ind >= le:
        return("Did not find!")

    if a[ind]==se:
        return True
    else:
        return(fun(a,ind+1,se,le))
    
arr=[12,10,30,50,100]
index=0
length=len(arr)
check=10               #for any we want 
print(fun(arr,index,check,length))

