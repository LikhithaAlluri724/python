#1
# def max_of_numbers(a,b,c):
#     if(a>b and a>c):
#         return f"{a} is maximum number"
#     if(b>a and b>c):
#         return f"{b} is maximum number"
#     if (c>a and c>b):
#         return f"{c} is maximum number"
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# c=int(input("enter a number: "))
# print(max_of_numbers(a,b,c))
#2
# def sum_of_elements(lst):
#     sum=0
#     for num in lst:
#         sum +=num
#     return sum
# lst=list(map(int,input("enter the numbers: ").split()))
# print(sum_of_elements(lst))
#3
# def even_or_odd(num):
#     if num%2 ==0:
#         return f"{num} is even number"
#     else:
#         return f"{num} is odd number"
# num=int(input("enter a number: "))
# print(even_or_odd(num))
#4
# def longest_word(lst):
#     word=lst[0]
#     for item in lst:
#         if len(item) > len(word):
#             word=item
#     return word
# lst=list(map(str,input("enter the numbers: ").split()))
# print(longest_word(lst))
#5
# def is_leap_year(year):
#     if (year%4 ==0 and year%100 !=0) or (year%400 ==0):
#         return f"{year} is leap year" 
#     else:
#         return f"{year} is not a leap year"   
# year=int(input("enter a number: "))
# print(is_leap_year(year))
#6
# def vowels_in_string(string):
#     vowels=["a","e","i","o","u"]
#     count=0
#     for char in string.lower():
#         if char in vowels:
#             count +=1
#     return count
# string=input("enter a string: ")
# print(vowels_in_string(string))
#7
# def reverse_string(string):
#     reversed_string=""
#     for char in string:
#         reversed_string = char +reversed_string
#     return reversed_string
# string=input("enter a word: ")
# print(reverse_string(string))
#8
# def area_of_circle(r):
#     pi=3.14
#     area=pi*(r**2)
#     return area
# r=int(input("enter a number:"))
# print(area_of_circle(r))
#9
# def celsius_to_fahrenheit(celsius):
#     fahrenheit=(celsius * 9/5)+3212
#     return fahrenheit
# celsius=int(input("enter a number: "))
# print(celsius_to_fahrenheit(celsius))
#10
def product_of_elements(lst):
    product=1
    for num in lst:
        product *= num
    return product
lst_1=list(map(int,input("enter the numbers: ").split()))
print(product_of_elements(lst_1))

