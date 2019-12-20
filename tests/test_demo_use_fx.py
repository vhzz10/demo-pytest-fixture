import pytest
from falcon import testing

from conftest import demo_no_yield, demo_share_fx, demo_external_fx, fx_1, fx_2, fx_3


@pytest.fixture
def demo_local_fx():
    print('Start LOCAL fx')
    yield
    print('End LOCAL fx')


class Test1(testing.TestCase):

    @pytest.mark.usefixtures(demo_no_yield.__name__)
    def test1(self):
        print(f'Run {self.test1.__name__}')


    @pytest.mark.usefixtures(demo_local_fx.__name__)
    def test2(self):
        print(f'Run {self.test2.__name__}')


    @pytest.mark.usefixtures(demo_share_fx.__name__)
    def test3(self):
        print(f'Run {self.test3.__name__}')


    @pytest.mark.usefixtures(
        demo_share_fx.__name__,
        demo_local_fx.__name__,
    )
    def test4(self):
        print(f'Run {self.test4.__name__} - multiple fixtures')


    @pytest.mark.usefixtures(demo_external_fx.__name__)
    def test5(self):
        print(f'Run {self.test5.__name__}')


@pytest.mark.usefixtures(fx_1.__name__)
class Test2_usefixtures_at_class_level(testing.TestCase):

    def test1(self):
        print(f'Run {self.test1.__name__}')

    @pytest.mark.usefixtures(fx_2.__name__)
    def test2(self):
        print(f'Run {self.test2.__name__}')

    @pytest.mark.usefixtures(
        fx_2.__name__,
        fx_3.__name__,
    )
    def test3(self):
        print(f'Run {self.test3.__name__} - multiple fixtures')
