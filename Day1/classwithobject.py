# class start():
#     def newfunc(self):
#         pass
#
#     def newfunc2(self,name):
#         print(name)
#
#when you put () to the class then it becomes an object
# obj1=start()           #obj1 = instance variable to refre the class
# obj1.newfunc()
# obj1.newfunc2("hello raghu")

#static method: use method directly from the class and declare when two or three methods have same data

#static methods can be access thorugh class
# 3. example

# class newclass:
#     def method1(self):
#         print("hello")
#
#     @staticmethod
#     def method2(self,a):
#         print(self, a)
#
# newclass.method2(10,20)
# newclass.method1()
# newobj1=newclass()
# newobj1.method1()


# 4th example class variables

# class newWindow:
#     a,b = 34,24
#     def methosd3(self):
#         print(self.a+self.b)
#
#
# obj4=newWindow()
# obj4.methosd3()



# 5TH EXAMPLE  accessing global, local, and class variables

a= 30     #global
b=80

class forvariables:

    a=90    #class
    b=100
    def meth6(self, a, b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])

obj6=forvariables()
obj6.meth6(a,b)                 #local











































