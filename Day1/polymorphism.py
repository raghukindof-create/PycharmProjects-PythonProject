#polymorphism: same function/method can work diff types of data

#compile time (overloading)  & runtime polymorphism (overriding)

# 1st program:


class H:
     def human(self, name=None):     #None is a default parameter
          if name is not None:
               print(name)
          else:
               print("none")

obj4=H()
obj4.human()


# 2nd program:
# we can pass 1 or two parameters if we use the default parameters in polymorphism


class Add:
     def addition(self, f=2,g=3,h=5):
          print(f+g+h)

Add().addition(3,4,3)








