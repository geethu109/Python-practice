def insertion_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        newarr=[]
        for i in range(len(arr)):
            newarr.append(arr[i])
            for j in range(len(newarr)-1,0,-1):
                if newarr[j] < newarr[j-1]:
                    newarr[j],newarr[j-1]=newarr[j-1],newarr[j]
                else:
                    break
        return(newarr)
arr=list(map(int, input().split()))
result=insertion_sort(arr)
print(*result)