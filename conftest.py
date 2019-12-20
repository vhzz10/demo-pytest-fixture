import pytest
from tests.__fixtures__.external_fx import demo_external_fx

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

#region fx_123
@pytest.fixture()
def fx_1():
    print('Start fx1')
    print('End fx1')
    # yield be default called here

@pytest.fixture()
def fx_2():
    print('Start fx2')
    print('End fx2')
    # yield be default called here

@pytest.fixture()
def fx_3():
    print(f'Start {fx_3.__name__}')
    print(f'End {fx_3.__name__}')
    # yield be default called here

#endregion fx_123
