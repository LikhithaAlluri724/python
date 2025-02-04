#1
# def is_palindrome(string):
#     reverse_word=string[::-1]
#     if string==reverse_word:
#         return "Given string is a palindrome"
#     else:
#         return "Given string is not a palindrome"
# string=input("enter a word: ")
# print(is_palindrome(string))
#3
# def remove_ith_char(string,i):
#     # word=string[:i]+string[i+1:]
#     # return word
#     word=""
#     for j in range(len(string)):
#         if j!=i:
#             word+=string[j]
#     return word
# string=input("enter a string: ")
# i=int(input("enter a index:"))
# print(remove_ith_char(string,i))
#4
# def length_of_string(string):
    # length=len(string)               #1
    # return length
    # count=0                           #2
    # for char in string.lower():
    #     count+=1
    # return count
    # length=len([char for char in string])    #3
    # return length
    # length=0                         #4
    # while length<len(string):
    #     length+=1
    # return length
# string=input("enter a string: ")
# print(length_of_string(string))
#5
# def avoid_spaces_in_length(word):
#     count=0
#     for char in word:
#         if char!=" ":
#             count+=1
#     return count
# word=input("enter a word: ")
# print(avoid_spaces_in_length(word))
#6
# def even_length_words(string):
#     even_string=""
#     for i in range(len(string)):
#         if i%2==0:
#             even_string+=string[i]
#     return even_string
# string=input("enter a string: ")
# print(even_length_words(string))
#10
# def vowels_in_string(string):
#     l1=["a","e","i","o","u"]
#     words=""
#     for char in l1:
#         if char in string.lower():
#             words
#     return words
# string=input("enter a string: ")
# print(vowels_in_string(string))
a=int(input("enter a num:"))
print(a)