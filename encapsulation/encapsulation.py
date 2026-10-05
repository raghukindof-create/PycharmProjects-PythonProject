class Encapsulation:
    name=''
    __marks=0                                   #private variables =. cannot edit directly

    def set_marks(self,name,__marks):      #setters
        self.__marks=__marks
        if self.__marks>35:
            print("pass")
        else:
            print("fail")uc vv2V         UU

    def get_marks(self):           #getters
        return self.__marks



obj1=Encapsulation()
obj1.set_marks("raghu",90)
print(obj1.get_marks())
