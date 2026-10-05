# Example 1:
#
# try:
#     print(x)
# except:
#     print("Something went wrong.")

# Example 2:

# a=10
# b=20
#
# try:
#     print(a)
#     print(c)
# except:
#         print("Something went wrong.")
# print(b)


# Example 3:

# try:
#     age = int(input("Enter your age: "))
#     try:
#         age = str(input("Enter your name: "))
#     except:
#             print("enter other correct format")
# except:
#     print("enter the age")



# ex: 4

# def set(age):
#     if age < 20:
#         raise ValueError ("age should be less than 20")
#     print(age)
#
# set(10)

# ex:5

x=-1

if x<0:
    raise Exception ("age should be less than 0")