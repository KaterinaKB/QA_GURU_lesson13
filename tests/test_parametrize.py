"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be


@pytest.fixture(params=[(1920, 1280), (1600, 900), (390, 844), (320, 658)])
def init_browser(request):
    browser.config.base_url = "https://github.com/"
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


@pytest.mark.parametrize(
    "init_browser",
    [(1920, 1280), (1600, 900)],
    indirect=True,
    ids=["1920*1280", "1600*900"],
)
def test_github_desktop(init_browser):
    browser.open("/")

    browser.element(".HeaderMenu-link--sign-in").should(be.visible)


@pytest.mark.parametrize(
    "init_browser",
    [(390, 844), (320, 658)],
    indirect=True,
    ids=["iPhone 12 Pro", "Samsung Galaxy S9+"],
)
def test_github_mobile(init_browser):
    browser.open("/")

    browser.element(".Button--link").click()

    browser.element(".HeaderMenu-link--sign-in").should(be.visible)
