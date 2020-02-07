import pytest

from tests.this_method import this_method


@pytest.fixture()
def fx_1():
    print(f'\nStart fx at {this_method()}')
    print(f'End fx at {this_method()}')
    # yield be default called here


@pytest.fixture()
def fx_2():
    print(f'\nStart fx at {this_method()}')
    print(f'End fx at {this_method()}')
    # yield be default called here


@pytest.fixture()
def fx_3():
    print(f'\nStart fx at {this_method()}')
    print(f'End fx at {this_method()}')
    # yield be default called here
