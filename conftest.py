import pytest

@pytest.fixture()  # default scope is function
def demo_share_fx():
    print('Start SHARE fx')
    yield
    print('Done SHARE fx')

@pytest.fixture()
def demo_no_yield():
    print('Start NO YIELD')
    print('STOP NO YIELD')
    # yield be default called here
