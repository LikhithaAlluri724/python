1
# def size_of_tuple(numbers):
#     size=0
#     for num in numbers:
#         size +=1
#     return size
# numbers=tuple(map(int,input("enter numbers: ").split()))
# print(size_of_tuple(numbers))
#2
# def add_list_tuple(l1,t1):
#     length = min(len(l1),len(t1))
#     for i in range(length):
#         l1.append(t1[i])
#     return l1
# l1=list(map(int,input("enter the numbers: ").split()))
# t1=tuple(map(int,input("enter numbers: ").split()))
# print(add_list_tuple(l1,t1))
#3
# def tuple_of_k_min_max(tup,k):
#     if k<=0 and k>len(tup):
#         return "k is invalid"
#     sorted_tup=sorted(tup)
#     min_k_elements=sorted_tup[:k]
#     max_k_elements=sorted_tup[-k:]
#     return min_k_elements,max_k_elements
# tup=tuple(map(int,input("enter numbers: ").split()))
# k=int(input("enter a number: "))
# print(tuple_of_k_min_max(tup,k))
#4
# def list_of_tuples(lst):
#     lst1=[]
#     for num in lst:
#         t1=(num,num**3)    
#         lst1.append(t1)
#     return lst1
# lst=list(map(int,input("enter the numbers: ").split()))
# print(list_of_tuples(lst))
#5
# def remove_tuples_k_length(list,k):
#     for tples in list:
#         if len(tples) ==k:
#             list.remove(tples)
#     return list
# user_input=input("enter the tuples: ")
# list=[tuple(map(int,tup.strip("()").split(','))) for tup in user_input.split()]
# k=int(input("enter the size: "))
# print(remove_tuples_k_length(list,k))