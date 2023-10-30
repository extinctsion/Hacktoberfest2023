# Move all negative numbers to beginning and positive to end with constant extra space.

def rearrange(arr, n ) : 
  
    # Please refer partition() in  
    #  / quick-sort / j = 0 
    j = 0 
    for i in range(0, n) : 
        if (arr[i] < 0) : 
            temp = arr[i] 
            arr[i] = arr[j] 
            arr[j]= temp 
            j = j + 1
    print(arr) 
  
# Driver code 
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9] 
n = len(arr) 
rearrange(arr, n) 

Time complexity: O(N) 
Auxiliary Space: O(1)
  
  
