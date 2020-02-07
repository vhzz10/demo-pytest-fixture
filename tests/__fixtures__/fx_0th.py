import pytest

from tests.this_method import this_method


@pytest.fixture()  # default scope is function
def demo_shared_fx():
    print(f'\nStart fx at {this_method()}')
    yield
    print(f'End fx at {this_method()}')


@pytest.fixture()
def demo_no_yield():
    print(f'\nStart fx at {this_method()}')
    print(f'End fx at {this_method()}')
    # yield be default called here
