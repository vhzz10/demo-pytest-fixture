# basic idea
```python
@pytest.fixture
def your_fx():  # fx aka fixture
    print('Start fx')
    yield  # unittest method run here - the one marked with @pytest.mark.usefixtures('this_method_name')
    print('End fx')
```

# prerequisites
- python 3.6.10 via pyenv ref. bit.ly/nnpipenv
- pipenv ref. bit.ly/nnpipenv

# install packages
```bash
pipenv sync
```

# run test 
```bash
pipenv run pytest

# with tests' output
pipenv run pytest -s
```

# about demo tests
This demo will run:

    - TC1: No yield in pytest.fixture
        + Start NO YIELD
        + STOP NO YIELD
        + Run TC 1

    - TC2: local pytest.fixture
        + Start LOCAL fx
        + Run TC 2
        + Done LOCAL fx

    - TC3: shared pytest.fixture
        + Start SHARE fx
        + Run TC 3
        + Done SHARE fx
