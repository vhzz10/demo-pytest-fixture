import pytest
from falcon import testing

@pytest.fixture
def demo_local_fx():
    print('Start LOCAL fx')
    yield
    print('Done LOCAL fx')

class Test(testing.TestCase):

    @pytest.mark.usefixtures('demo_no_yield')
    def test1(self):
        print('Run TC 1')
        pass

    @pytest.mark.usefixtures('demo_local_fx')
    def test2(self):
        print('Run TC 2')
        pass

    @pytest.mark.usefixtures('demo_share_fx')
    def test3(self):
        print('Run TC 3')
        pass