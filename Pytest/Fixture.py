# #Reusable function
import pytest
#
# @pytest.fixture
# def setup():
#     print("setup")
#
# def test_demo(setup):
#     print("test 1")
# def test_demo2(setup):
#     print("test 2")
# def test_demo1(setup):
#     print("test 1")


# Return the value from fixtures

@pytest.fixture
def setup():
    print("Browser is chrome")
    yield
    print("teardown")

def test_demo(setup):        #setup also acts as a variable
    print("test 1")
def test_demo2(setup):
    print("test 2")

def test_demo1(setup):
    print("test 1")
