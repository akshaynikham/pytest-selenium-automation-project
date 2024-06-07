import pytest
from amazon.utils import initialize_driver


@pytest.fixture
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()
