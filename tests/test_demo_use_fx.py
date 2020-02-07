import pytest
from falcon import testing

from conftest import demo_no_yield, demo_share_fx, demo_external_fx
from tests.this_method import this_method

@pytest.fixture
def demo_local_fx():
    print('Start LOCAL fx')
    yield
    print('End LOCAL fx')


class Test1(testing.TestCase):

    @pytest.mark.usefixtures(demo_local_fx.__name__)
    def test1(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(demo_no_yield.__name__)
    def test2(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(demo_share_fx.__name__)
    def test3(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(
        demo_share_fx.__name__,
        demo_local_fx.__name__,
    )
    def test4(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(demo_external_fx.__name__)
    def test5(self):
        print(f'Run {this_method()}')
