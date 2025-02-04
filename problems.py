#1
# def sorted_list_of_tuple(input_list):
#     input_list.sort(key=lambda x:x[-1])
#     return input_list
# input_list_of_tuples=eval(input("enter the list of tuples:"))
# print(sorted_list_of_tuple(input_list_of_tuples))
#2
# def common_elements(lst1,lst2):
#     for element1 in lst1:
#         for element2 in lst2:
#             if element1==element2:
#                 return True
# lst1=eval(input("enter the list1:"))
# lst2=eval(input("enter the list2:"))
# print(common_elements(lst1,lst2))
#3
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i ==0:
#             return False
#     return True
# def check_primes(lst):
#     return all(is_prime(num) for num in lst)
# lst=eval(input("enter a list of numbers:"))
# print(check_primes(lst))
#4
# def convert_pair_of_values(lst):
#     merge=lst[0]+lst[1]
#     return sorted(set(merge))
# lst=eval(input("enter the tuple of two lists:"))
# print(convert_pair_of_values(lst))
#5
# def reverse_at_specific_location(lst,index):
#     if index<0 or index>len(lst):
#         return "invalid"
#     lst[index:]=lst[index:][::-1]
#     return lst
# lst=eval(input("enter a list:"))
# index=int(input("enter a index number:"))
# print(reverse_at_specific_location(lst,index))
#6
# def minimun_sum_sub_sequence(lst):
#     sequence=[num for num in lst if num<0]
#     if not sequence:
#         sequence=[min(lst)]
#     return sequence
# lst=eval(input("enter a list:"))
# print(minimun_sum_sub_sequence(lst))
#7
# def concatenate_dicts(*dictionary):
#     result={}
#     for dicts in dictionary:
#         result.update(dicts)
#     return result
# dictionary1={1:10,2:20}
# dictionary2={3:30,4:40}
# dictionary3={5:50,6:60}
# print(concatenate_dicts(dictionary1,dictionary2,dictionary3))
##
# def reverse_string_at_specific_index(word,index):
#     if index<0 or index>len(word):
#         return "invalid"
#     reversed_word =word[index:][::-1]
#     result=word[:index]+reversed_word
#     return result
# word=input("enter any word:")
# index=int(input("enter a number"))
# print(reverse_string_at_specific_index(word,index))
#8
# def add_common_keys(d1,d2):
#     d3={}
#     for key in d1:
#         if key in d2:
#             d3[key]=d1[key]+d2[key]
#     return d3
# d1=eval(input("enter d1:"))
# d2=eval(input("enter d2:"))
# print(add_common_keys(d1,d2))
#9
# def count_of_letters(string):
#     dict={}
#     for char in string:
#         if char in dict:
#             dict[char]+=1
#         else:
#             dict[char]=1
#     return dict
# string=input("enter a string:")
# print(count_of_letters(string))
#10
# def sum_of_values(dict):
#     total=sum(dict.values())
#     for keys in dict:
#         dict[keys]=total
#     return dict
# dict=eval(input("enter a dictionary:"))
# print(sum_of_values(dict))
#11
# def student_height_weight(dict):
#     dict1={}
#     dict2={}
#     for key,value in dict.items():
#         if 

#12
# def even_numbers_from_dict(dict):
#     dict1={}
#     for key,value in dict.items():
#         if value%2 ==0:
#             dict1[key]=value
#     return dict1
# dict=eval(input("enter a dictionary:"))
# print(even_numbers_from_dict(dict))
#13
# def unpack_tuple(tuple1):
#     name,age,*other_details=tuple1
#     return name,age,*other_details
# tuple1=eval(input("enter the values:"))
# print(unpack_tuple(tuple1))
#14
# def replace_last_value(list_of_tuple):
#     modified_list = []
#     for tuple in list_of_tuple:
#         modified_list.append(tuple[:-1] + (100,))
#     return modified_list
# list_of_tuple = eval(input("Enter a list of tuples: "))
# print(replace_last_value(list_of_tuple))
#15
def avg_of_tuple(list_of_tuples):
    avg_list=[]
    sum=0
    for tuple in list_of_tuples:
        for t in tuple:
            sum+=t
            avg= sum/len(tuple)
        avg_list.append(avg)
    return avg_list
list_of_tuples=eval(input("Enter a list of tuples: "))
print(avg_of_tuple(list_of_tuples))