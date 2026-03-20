#prime number or not
# n=int(input())
# if (n<=1):
#     print("not prime")
# else:
#     isprime=True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             isprime=False
#             print("not prime")
#             break
#     if isprime==True:
#         print("prime")

#factorial of a number
# n=int(input())
# fact=1
# i=1
# while i<=n:
#     fact=fact*(i)
#     i+=1
# print(fact)

#fibonacci series
# n=int(input())
# a=0
# b=1
# for i in range(n):
#     print(a, end=" ")
#     next=a+b
#     a=b
#     b=next

#reverse a number
# n = input()
# print(int(n[::-1]))
#or
# n=int(input())
# rev=0
# while n>0:
#     x=n%10
#     rev=rev*10+x
#     n=n//10
# print(rev)

#palindrome
# n=input()
# if n==n[::-1]:
#     print("yes")
# else:
#     print("no")

#armstrong number
# n=int(input())
# s=len(str(n))
# sum=0
# for i in str(n):
#     sum+=int(i)**s
# if sum==n:
#     print("yes")
# else:
#     print("no")

#sum of digits
# n=int(input())
# print(n*(n+1)//2)

#largest of 3 numbers
x,y,z=map(int, input().split())
print(max(x,y,z))