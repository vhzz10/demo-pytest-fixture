import pytest
from falcon import testing

from tests.__fixtures__.fx_at_class_level import fx_1, fx_2, fx_3
from tests.this_method import this_method


@pytest.mark.usefixtures(fx_1.__name__)  # class-level fixture will run after method-level fixture(s)
class Test_usefixtures_at_class_level(testing.TestCase):

    def test1(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(fx_2.__name__)
    def test2(self):
        print(f'Run {this_method()}')


    @pytest.mark.usefixtures(
        fx_2.__name__,
        fx_3.__name__,
    )
    def test3(self):
        print(f'Run {this_method()}')
