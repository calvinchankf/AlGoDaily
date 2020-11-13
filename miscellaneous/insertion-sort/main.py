def insertionSort(arr):
    for i in range(1, len(arr)): 
        cur = arr[i]
        # Move elements of arr[0..i-1], that are 
        # greater than cur, to one position ahead 
        # of their current position 
        j = i - 1
        while j >= 0 and cur < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = cur

a = [6,5,3,1,8,7,2,4]
insertionSort(a)
print(a)