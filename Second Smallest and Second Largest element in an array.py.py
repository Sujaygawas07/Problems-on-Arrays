array=list(map(int,input("enter number seprated by space:-").split()))   #taking input from user
#print(array)

if len(array)<2:                                     #checking sixe of the array 
    print("size should be greater")
    
else:
    
    sorted_array=sorted(set(array))                    #sort the array
    
    second_smallest=sorted_array[1]                 #assing first index value to the second smallest no
    second_largest=sorted_array[-2]                 #assing second last index value to the second largest no                   #

#print(sorted_array)    
print(f"second smallest element:{second_smallest}")       #print second_smallest
print(f"second largest element;{second_largest}")         #print second largest

    
    