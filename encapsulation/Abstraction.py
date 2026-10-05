from abc import ABC, abstractmethod

class Duration(ABC):
    @abstractmethod
    def time(self,a):
        if a <30:
            print("pass")
        else:
            print("fail")

class Duration1(Duration):
    def time(self,a):
        if a <30:
            print("pass")
        else:
            print("fail")


c=Duration1()
c.time(80)