import pytest
from falcon import testing

from tests.__fixtures__.fx_0th import demo_no_yield, demo_shared_fx
from tests.__fixtures__.external_fx import demo_external_fx
from tests.this_method import this_method


@pytest.fixture
def demo_local_fx():
    print('Start LOCAL fx')
    yield  # unittest method run here - the one marked with @pytest.mark.usefixtures('this_method_name')
    print('End LOCAL fx')


class Test1(testing.TestCase):

    @pytest.mark.usefixtures(demo_local_fx.__name__)
    def test1(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(demo_no_yield.__name__)
    def test2(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(demo_shared_fx.__name__)
    def test3(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(
        demo_shared_fx.__name__,
        demo_local_fx.__name__,
    )
    def test4__use_multi_fx(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(demo_external_fx.__name__)
    def test5(self):
        print(f'Run {this_method()}')
