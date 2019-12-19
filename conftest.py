import pytest

@pytest.fixture()  # default scope is function
def demo_share_fx():
    print('Start SHARE fx')
    yield
    print('End SHARE fx')

@pytest.fixture()
def demo_no_yield():
    print('Start NO YIELD fx')
    print('End NO YIELD fx')
    # yield be default called here
