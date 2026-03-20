arr=list(map(int, input().split())) # slow
for i in range(len(arr)):
    if arr.count(arr[i])%2 !=0:
        print(arr[i])
        


# arr=list(map(int, input().split())) # fast
# result=0
# for i in arr:
#     result^=i
# print(result)