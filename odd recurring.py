# code 1
arr=list(map(int, input().split())) # slow but only single number will be displayed
for i in range(len(arr)):
    if arr.count(arr[i])%2 !=0:
        print(arr[i])

# code 2        
arr=list(map(int, input().split())) # fast but only single number will be displayed
result=0
for i in arr:
    result^=i
print(result)
