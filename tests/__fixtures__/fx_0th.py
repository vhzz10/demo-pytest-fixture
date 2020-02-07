import pytest


@pytest.fixture()  # default scope is function
def demo_shared_fx():
    print('Start SHARED fx')
    yield
    print('End SHARED fx')


@pytest.fixture()
def demo_no_yield():
    print('Start NO YIELD fx')
    print('End NO YIELD fx')
    # yield be default called here
