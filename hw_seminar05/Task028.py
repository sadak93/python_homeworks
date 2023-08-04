# def summ_ (a,b):
#     if b == 0:
#         return a
#     return summ_(a+1,b-1)
#
# print(summ_(10,21))

def sum (a,b):
    if b == 0:
        return a
    return sum(a+1,b-1)

print(sum(2,2))