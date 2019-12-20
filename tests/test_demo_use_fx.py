import pytest
from falcon import testing

from conftest import demo_no_yield, demo_share_fx, demo_external_fx


@pytest.fixture
def demo_local_fx():
    print('Start LOCAL fx')
    yield
    print('End LOCAL fx')


class Test1(testing.TestCase):

    @pytest.mark.usefixtures(demo_no_yield.__name__)
    def test1(self):
        print('Run Test1.test1')


    @pytest.mark.usefixtures(demo_local_fx.__name__)
    def test2(self):
        print('Run Test1.test2')


    @pytest.mark.usefixtures(demo_share_fx.__name__)
    def test3(self):
        print('Run Test1.test3')


    @pytest.mark.usefixtures(
        demo_share_fx.__name__,
        demo_local_fx.__name__,
    )
    def test4(self):
        print('Run Test1.test4 - multiple fixtures')


    @pytest.mark.usefixtures(demo_external_fx.__name__)
    def test5(self):
        print('Run Test1.test1')


@pytest.mark.usefixtures(demo_share_fx.__name__)
class Test2_usefixtures_at_class_level(testing.TestCase):

    def test1(self):
        print('Run Test2.test1')

    def test2(self):
        print('Run Test2.test2')
