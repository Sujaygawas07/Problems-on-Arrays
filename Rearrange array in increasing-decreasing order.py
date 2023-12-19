array=list(map(int,input("enter the no nu space:-").split())) # taking input as an array
print(array)

array.sort()                                          # sorting of array

#a_array=sorted(array)

increasing_order=array[:]                            #creating list for increasing order
decreasing_order=array[::-1]                          #creating list for decreasing order

result=increasing_order+decreasing_order            #combining both list 
print(result)
