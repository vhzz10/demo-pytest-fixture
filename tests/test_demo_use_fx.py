import pytest
from falcon import testing

from conftest import demo_no_yield, demo_share_fx


@pytest.fixture
def demo_local_fx():
    print('Start LOCAL fx')
    yield
    print('Done LOCAL fx')


class Test(testing.TestCase):

    @pytest.mark.usefixtures(demo_no_yield.__name__)
    def test1(self):
        print('Run test1')
        pass

    @pytest.mark.usefixtures(demo_local_fx.__name__)
    def test2(self):
        print('Run test2')
        pass

    @pytest.mark.usefixtures(demo_share_fx.__name__)
    def test3(self):
        print('Run test3')
        pass

    @pytest.mark.usefixtures(
        demo_share_fx.__name__,
        demo_local_fx.__name__,
    )
    def test4(self):
        print('Run test4 - multiple fixtures')
        pass
