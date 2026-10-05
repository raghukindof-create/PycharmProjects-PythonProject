a,b,c=39,29,0

# print("a is greater than b") if a>b else print("a is less than b")

if a>b and a>c:
    print("a is the largest number")
elif b>a and b>c:
    print("b is the largest number")
elif c>a and c>b:
    print("c is the largest number")

else :
    print("random number")