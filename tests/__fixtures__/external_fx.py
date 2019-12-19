import pytest

@pytest.fixture()
def demo_external_fx():
    print('Start EXTERNAL fx')
    yield
    print('Done EXTERNAL fx')
