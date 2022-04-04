
 
def findMin(arr, low, high):
    
    if high < low:
        return arr[0]
 
  
    if high == low:
        return arr[low]

    mid = int((low + high)/2)
 
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]
 
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]

    if arr[high] > arr[mid]:
        return findMin(arr, low, mid-1)
    return findMin(arr, mid+1, high)
 
if __name__=="__main__":
    #test case 001
    arr1 = [5, 6, 1, 2, 3, 4]
    n1 = len(arr1)
    print("The minimum element is " + str(findMin(arr1, 0, n1-1)))
 
    #test case002
    arr1 = [1, 2, 3, 4]
    n1 = len(arr1)
    print("The minimum element is " + str(findMin(arr1, 0, n1-1)))

 
