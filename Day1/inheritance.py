# #single inheritance
#
# class New:
#     x,y= 10,20
#     def add(self):
#         print(self.x+self.y)
#
# class Child(New):
#     r,lc =24,24
#     def mul(self):
#         print(self.r*self.lc)
#
# obj1=Child()
# obj1.add()
# obj1.mul()
#
#
#
# #hireachy inheritance - one parent has multiple child clasess
#
# class New:
#     x,y= 10,20
#     def add(self):
#         print(self.x+self.y)
#
# class Child(New):
#     r,lc =24,24
#     def mul(self):
#         print(self.r*self.lc)
#
# class Child2(Child):
#     g,h =24,24
#     def sub(self):
#         print(self.g-self.h)
#
#
# obj1=Child2()
# obj1.add()
# obj1.mul()
# obj1.sub()



#multipls inheritance - one child has multiple parent clases



# class New:
#     x,y= 10,20
#     def add(self):
#         print(self.x+self.y)
#
# class Child1:
#     r,lc =24,24
#     def mul(self):
#         print(self.r*self.lc)
#
# class Child2:
#     g,h =24,24
#     def sub(self):
#         print(self.g-self.h)
#
#
# class mulpar(New, Child2):
#     l= 'Raghu'
#     def leng(self):
#         print(len(self.l))
#
#
#
# obj1=mulpar()
# obj1.leng()


#overerite

class New:
   def add(self):
         print("print parent")

class B(New):
    def add(self):
        print("updated")
        super().add()       #invokr from parent class

obj6=B()
obj6.add()




#calling parent class variables using child class

class K:

    a,v = 902, 892

class J(K):
    o,p=955,675
    def add(self, e,f):
        print(e+f)
        print(self.o+self.p)
        print(self.a+self.v)

obj8=J()
obj8.add(10,8789)








