# 1 -masala ----------------------------------------------
# k = int(input("son kiriting: "))
# n = int(input("son kiriting: "))
#
# if n > 0:
#     [print(k) for i in range(n)]
#
# 2 -masala ----------------------------------------------
#
# a = int(input("son kiriting: "))
# b = int(input("son kiriting: "))
#
# if a < b:
#     list1 = [i for i in range(b, a+1)]
#     print(list1, len(list1))
#
# 3 -masala ----------------------------------------------
#
# a = int(input("son kiriting: "))
# b = int(input("son kiriting: "))
#
# if a < b:
#     list1 = [i for i in range(b-1, a, -1)]
#     print(list1, len(list1))
#
# 4 -masala ----------------------------------------------
#
# from decimal import Decimal
#
# narxi = Decimal("1.200")
#
# [print(Decimal(i*narxi)) for i in range(1, 10)]
#
# 5 -masala ----------------------------------------------
#
# text = "hello world"
#
# text2 = (str(i).upper() for i in text)
#
# print(list(text2))
#
# 6 -masala ----------------------------------------------
#
# text = "HeLlo wORld"
#
# text2 = (str(i).lower() for i in text)
# print(list(text2))
#
# 7 -masala ----------------------------------------------
#
# list1 = [(i, i**3) for i in range(1, 20+1)]
# print(list1)
#
# 8 -masala ----------------------------------------------
#
# list1 = [(i, i/2) for i in range(1, 20+1) if i % 2 == 0]
# print(list1)
#
# 9 -masala ----------------------------------------------
#
# dict_gen = ((i, i**2) for i in range(1, 10+1))
# print(dict(dict_gen))
#
# 10 -masala ----------------------------------------------
#
# text = "salom dunyo"
# dict_gen = ((i, str(i).upper()) for i in text)
# print(dict(dict_gen))
#