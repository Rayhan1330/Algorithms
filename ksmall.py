def insertion_sort(arr):
    n = len(arr)
    for i in range(2,n+1):
        j = i - 1
        while(arr[j]<arr[j-1] and j>0):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j = j-1
    return arr

def quickSelect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[0]
    leS = [num for num in arr if num < pivot]
    right = [num for num in arr if num > pivot]
    if k <= len(leS):
        return quickSelect(leS, k)
    elif k == len(leS) + 1:
        return pivot
    else:
        return quickSelect(right, k - len(leS) - 1)


l = eval(input("Enter an array: "))
k = int(input("Enter the value of k: "))
#l = insertion_sort(l)
#l = quicksort(l)
#print("K smallest value is:",l[k-1])
print(quickSelect(l,k))
