#1
# def all_numbers(n):
#     for num in range(n+1):
#         print(num)
# n=int(input("enter a number: "))
# print(all_numbers(n))
#2
# def sum_of_numbers(n):
#     sum=0
#     for num in range(n+1):
#         sum += num
#     return sum
# n= int(input("enter a number: "))
# print(sum_of_numbers(n))
#3
# def even_numbers(n):
#     num =0
#     while num<=n:
#         if num%2 ==0:
#             print(num)
#         num +=1
# n=int(input("enter a number: "))
# print(even_numbers(n))
#4
# def factorial_of_number(n):
#     factorial=1
#     for num in range(1,n):
#         factorial *= num
#     return factorial
# n=int(input("enter a number: "))
# print(factorial_of_number(n))
#5
# def fibonacci_series(n):
#     a,b=0,1
#     series=[]
#     while(n>0):
#         series.append(a)
#         a,b=b,a+b
#         n -=1
#     return series
# n=int(input("enter a number: "))
# print(fibonacci_series(n))
#6
# def max_number(lst):
#     max_num=lst[0]
#     for num in lst:
#         if max_num<num:
#             max_num=num
#     return max_num
# lst=list(map(int,input("enter the numbers: ").split()))
# print(max_number(lst))
#9
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i ==0:
#             return False
#     else:
#         return True
# n=int(input("enter a number: "))
# print(is_prime(n))

# def is_anagram(word1,word2):
#     if len(word1) != len(word2):
#         return False
#     if sorted(word1) == sorted(word2):
#         return True
# word1=input("enter a word:")
# word2=input("enter a word:")
# if is_anagram(word1,word2):
#     print("given words are anagram")
# else:
#         print("given words are not anagram")