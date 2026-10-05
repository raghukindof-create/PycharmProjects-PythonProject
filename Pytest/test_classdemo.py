import pytest

class TestOne:
    def test_demo(self):
        print("test 1")
    def test_demo2(self):
         print("test 2")
    def test_demo1(self):
        print("test 1")


##pytest Pytest/test_pytestdemo.py to run all teste
# pytest Pytest/test_pytestdemo.py -s --it will give the display the print
# pytest Pytest/test_pytestdemo.py -v --it will show passed or not
# pytest Pytest/test_pytestdemo.py::test_demo1   it will execute specific testcase
