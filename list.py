#1
# def print_list(numbers):
#     return numbers
# numbers=list(map(int,input("enter the numbers: ").split())) 
# print(print_list(numbers))
#2
# def print_list_elements(list1):
#     # return [item for item in list1]
#     for item in range(len(list1)):
#         print(f"{item}:{list1[item]}")
# list1=list(map(int,input("enter the numbers: ").split())) 
# print(print_list_elements(list1))
#3
# def add_remove_elements(lst):
#     lst.insert(1,45)
#     lst.remove(34)
#     return lst
# lst=list(map(int,input("enter the numbers: ").split())) 
# print(add_remove_elements(lst))
#4
# def print_list(lst):
#     for item in lst:
#         print(item)
# lst=list(map(int,input("enter the numbers: ").split())) 
# print(print_list(lst))
#5
# def insert_element(lst):
#     lst.insert(2,77)
#     return lst
# lst=list(map(int,input("enter the numbers: ").split())) 
# print(insert_element(lst))
#6
# def remove_first_occurence(lst,element):
#     if element in lst:
#         lst.remove(element)
#     return lst
# lst=list(map(int,input("enter the numbers: ").split()))
# element=int(input("enter the element: "))
# print(remove_first_occurence(lst,element))
#7
# def remove_all_occurence(lst,element):
#     while element in lst:
#         lst.remove(element)
#     return lst
# lst=list(map(int,input("enter the numbers: ").split()))
# element=int(input("enter the element: "))
# print(remove_all_occurence(lst,element))
#8
# def remove_elements(lst,starting_range,ending_range):
#     for num in lst:
#         if num>starting_range and num<ending_range:
#             lst.remove(num)
#     return lst
# lst=list(map(int,input("enter the numbers: ").split()))
# starting_range=int(input("enter starting range: "))
# ending_range=int(input("enter ending range: "))
# print(remove_elements(lst,starting_range,ending_range))
#9
# def sort_elements_in_ascending(lst):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i]>lst[j]:
#                 lst[i],lst[j] = lst[j],lst[i]
#     return lst
# lst=list(map(int,input("enter the numbers: ").split()))
# print(sort_elements_in_ascending(lst))
# def sort_elements_in_decending(lst):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i]<lst[j]:
#                 lst[i],lst[j] = lst[j],lst[i]
#     return lst
# lst=list(map(int,input("enter the numbers: ").split()))
# print(sort_elements_in_decending(lst))
#10
def list_difference(lst1,lst2):
    length=min(len(lst1),len(lst2))
    lst3=[]
    for i in range(length):
        lst3.append(lst1[i] - lst2[i])
    return lst3
lst1=list(map(int,input("enter the numbers: ").split()))
lst2=list(map(int,input("enter the numbers: ").split()))
print(list_difference(lst1,lst2))
