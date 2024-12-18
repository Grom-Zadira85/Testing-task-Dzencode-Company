import pytest
from playwright.sync_api import Page

from base_page import BasePage


@pytest.fixture(scope="session")
def browser_context_args():
    return {

        "viewport": {
            "width": 1440,
            "height": 900,
        }
    }


@pytest.fixture
def base_page(page: Page):
    return BasePage(page)




