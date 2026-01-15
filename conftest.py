# conftest.py
import pytest
from framework.browser import Browser
# Session-scoped fixture so it can be used by teardown
@pytest.fixture(scope="session")
def browser():
    b = Browser()
    yield b
    b.quit()

@pytest.fixture
def timeout():
    return 10


