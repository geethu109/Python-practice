def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1): # doubt in this condition
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
result=bubble_sort(arr)
print(*result)