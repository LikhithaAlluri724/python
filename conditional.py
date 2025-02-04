#3
# def swap_two_numbers(a,b):
#     a=a+b
#     b=a-b
#     a=a-b
#     return a,b
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# print(swap_two_numbers(a,b))
#10
# def type_of_triangle(s1,s2,s3):
#     if s1==s2==s3:
#         return "given triangle is equilateral triangle"
#     elif s1==s2 or s2==s3 or s3==s1:
#         return "given triangle is isoseles triangle"
#     else:
#         return "given triangle is scalen triangle"
# s1=int(input("enter a first side:"))
# s2=int(input("enter a second side:"))
# s3=int(input("enter a third side:"))
# print(type_of_triangle(s1,s2,s3))

#9
# def is_vowel_or_consonsnt(char):
#     if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#         return "char you entered is vowel "
#     else:
#         return "char you entered is consonant"
# char = input("enter a character: ")
# print(is_vowel_or_consonsnt(char))
#11
# def quadratic_roots(a,b,c):
#     d= b**2 + 4*a*c
#     if d>0:
#         return f"{(-b+d**0.5)/2*a}/\n {(-b-d**0.5)/2*a}"
#     elif d==0:
#         return f"{-b}/{a}"
#     elif d<0:
#         return f"{-b}+{d**0.5}i/{2*a}\n {-b}-{d**0.5}i/{2*a}"
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# c=int(input("enter a number: "))
# print(quadratic_roots(a,b,c))
#12
# def electricity_bills(units):
#     if units<0:
#         return "units can't be negative"
#     elif units<=100:
#         return f"{units*1.5}"
#     elif units>=101 and units <=200:
#         return f"{(units*1.5) + (units-100)*2.5}"
#     elif units>=201 and units<=300:
#         return f"{(units*1.5) + (units*2.5)+ (units-200)*4}"
# units=int(input("enter the number of units: "))
# print(electricity_bills(units))