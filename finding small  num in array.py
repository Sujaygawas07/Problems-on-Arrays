
                     # Finding smallest number in array


array=list(map(int,input("enter values seprated by space").split())) # taking input as a list
print(array)

def small_no(array):                      # defining a function
    if not array:                     # checking if array is empty or not
        return"not array"
        
        
    smallest=array[0]                 # taking the arrays oth element
    
    for num in array:                 # here compare that 0th element with all the elemwnt
        if num<smallest:              #if found the smallest element update it to the smallest element
            smallest=num
    
    return smallest                   #call that smallest no
    
result=small_no(array)              #call the function here
print(result)
    
    
    
