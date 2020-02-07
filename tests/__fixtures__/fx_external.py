import pytest

from tests.this_method import this_method


@pytest.fixture()
def demo_external_fx():
    print(f'\nStart fx at {this_method()}')
    yield
    print(f'End fx at {this_method()}')
