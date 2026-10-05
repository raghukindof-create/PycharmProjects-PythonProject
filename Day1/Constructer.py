# # Constructer is used to initialize the data
# # invoked automatically when object is created
#
#
# class constructer:
#     def __init__(self):
#         print("hello world")
#
# obj1=constructer()
#
#
# # 2. constructer with parameters and class variables
#
# class constructer1:
#     name="raghu"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# obj2=constructer1("RC")



# 3. A class with constructor and method

class constructer1:

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def meth6(self):
        print(self.name, self.age, self.salary)

obj3=constructer1("raghu", 30, 100000)
obj3.meth6()


obj4=constructer1("lakshmi", 28, 50000)
obj4.meth6()


