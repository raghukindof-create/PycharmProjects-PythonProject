scope = 'function'
scope = 'class'
scope = 'module'
scope = 'sessopm'

import pytest

@pytest.fixture
def setup(scope='module'):
    print("setup")

def test_demo(setup):
    print("test 1")
def test_demo2(setup):
    print("test 2")
def test_demo1(setup):
    print("test 1")