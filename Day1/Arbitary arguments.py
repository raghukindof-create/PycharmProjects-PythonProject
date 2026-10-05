#1. Arbitary variables or variable length arguments

def sumallnum(*numbers):                    #*numbers is used
    total = 0
    for i in numbers:
        total = total + i
    return total
print(sumallnum(1,2,3,4,5,6,7,8,9))

def smallnum2(*num):
    for i in num:
        return i
print(smallnum2(2,3,4,5))



from sys import set_int_max_str_digits


#2. Positional and keyword arguments


# def sumallnum(i=90, j=10):                    #*numbers is used
#     print(i, j)
#
# sumallnum(1, 2)  #positional arguments
# sumallnum(i=10, j=20) #keyword arguments. Also, keyword arguments should come all after positional arguments
# sumallnum(10)         #default values when j is present but not i
# sumallnum(100,200)   #overwrite the default values
# sumallnum()
# sumallnum( 34,j=24)  #passing positional and keyword arguments
# sumallnum(i =34,10)   #invalid syntax
# sumallnum(10, i= 20)  #logical error


#
# def largest(a,b):
#     if a>b:
#         return a, b
#     else:
#         return b,a
# print(largest(34,76))


# Scope of variables
# 1.
# r=100               #global variable
#
# def func2():
#     r=99;
#     print(r)            #local variable
#
# func2()
# print(r)

# 2.

#




