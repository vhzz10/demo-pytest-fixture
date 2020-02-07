import pytest


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
