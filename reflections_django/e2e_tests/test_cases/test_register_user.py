import pytest

@pytest.yield_fixture()
def setup():
    print('SETUP')
    yield
    print('Teardown')

def test_demo(setup):
    print('This is pytest demo!')

def test_demo2(setup):
    print('This is demo 2')