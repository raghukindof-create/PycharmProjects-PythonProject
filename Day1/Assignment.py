# Program for positive, zero and negative number
from tkinter import Menu

# i = -899
#
# if i>0:
#     print("i is a positive number")
# elif i == 0:
#     print("i is a zero")
# else:
#     print("i is a negative number")

# program for vowel and consonant
# l = "u"
# if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
#     print("l is a vowel")
# else:
#     print("l is a consonant")

# Program for grading
# c=908
#
# if c>=1 and c<20:
#     print("A")
# elif c>=20 and c<40:
# #     print("B")
# elif c >=40 and c < 60:
#     print("C")
# elif c >=60 and c < 80:
#     print("D")
# elif c>=80 and c < 90:
# #     print("E")
# elif c >=90 and c <= 100:
#     print("F")
# else:
#     print("No grade defined")

#
# sum of 123
# k = 123
# sum_digits = 0
#
# while k > 0:
#     digit = k % 10
#     sum_digits = sum_digits + digit
#     k = k // 10

#
# print(sum_digits)


# # tables
#
# a=20
# b=1
#
# for i in range(1,11):
#     multiply = a*b
#     print(a, "*", b, multiply)
#     b= b+1


# squares
# for i in range(1,11):
#     multiply = i*i
#     print(multiply)


# n = int(input("Enter a number: "))
# sum = 0
#
# for i in range(1, n+1):
#     sum = sum + i
#
# print("Sum of", n, "natural numbers is:", sum)


# Count vowels

# a=e=i=o=u=1
# b=c=d=f=g=h=j=k=l=m=n=p=q=r=s=t=v=w=x=y=z=0
#
# word = int(input("enter a word: "))
# for iq in range (a,z):



# string = input("Enter a string: ")
# count = 0
#
# for i in string:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         count = count + 1
#
# print("Number of vowels:", count)


# # fibonnacci serires
#
# n = int(input("enter a number: "))
# sum_of_numbers =0
#
# for i in range(0,n+1):
#     sum_of_numbers = sum_of_numbers +  i
#
# print("sum of first 2 numbers: ",sum_of_numbers)


# valid numbers

# n = int(input("enter a number: "))
# while n<=100:
#         print ("valid number: ", n)
#         n = n+1
# if n>100:
#     pass


# n=1
# for n in range(1,21):
#     if n % 3== 0:
#      continue
#      if n>20:
#          break
#     print(n)
#
#
#
# balance = 10000  # initial balance
#
# while True:
#     print("\n===== ATM MENU =====")
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         amount = int(input("Enter withdraw amount: "))
#         if amount > balance:
#             print("Insufficient balance!")
#         else:
#             balance -= amount
#             print("Withdrawn successfully! Remaining balance:", balance)
#
#     elif choice == 2:
#         amount = int(input("Enter deposit amount: "))
#         balance += amount
#         print("Deposited successfully! Current balance:", balance)
#
#     elif choice == 3:
#         print("Thank you for using ATM. Goodbye!")
#         break       # exits the loop when user selects Exit
#
#     else:
#         print("Invalid choice! Please try again.")



# password = ""
# while password != "admin123":
#     password = input("Enter password: ")
# print("Access Granted!")


# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print(fruit)


# word = "python"
# for letter in word:
#         print(letter)
#
#
# word = input("Enter a word: ")
#
# count_a = 0
# count_b = 0
#
# for letter in word:
#     if letter == 'a' or letter == 'A':
#         count_a += 1
#     elif letter == 'b' or letter == 'B':
#         count_b += 1
#
# print("Count of a's:", count_a)
# print("Count of b's:", count_b)




# word = input("Enter a word: ")
#
# count_a = 0
# count_b = 0
#
# for letter in word:
#     if letter == 'a' or letter == 'A':
#         count_a += 1
#     elif letter == 'b' or letter == 'B':
#         count_b += 1
#
# print("Count of a's:", count_a)
# print("Count of b's:", count_b)


# d = {"name": "Alice"}
#
# # Key doesn't exist → sets and returns default
# d.setdefault("age", 25)
# print(d)  # {'name': 'Alice', 'age': 25}
#
# # Key already exists → returns existing value, no change
# d.setdefault("name", "Bob")
# print(d)  # {'name': 'Alice', 'age': 25}


d = {"a":1}
d2 = d
d2["a"] = 100
print(d["a"])
print(d)









































