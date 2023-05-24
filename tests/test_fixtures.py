"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, be


@pytest.fixture()
def init_browser():
    browser.config.base_url = "https://github.com/"


@pytest.fixture(params=[(1920, 1280), (1600, 900)], ids=["1920*1280", "1600*900"])
def browse_for_desktop(request, init_browser):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


@pytest.fixture(
    params=[(390, 844), (320, 658)], ids=["iPhone 12 Pro", "Samsung Galaxy S9+"]
)
def browse_for_mobile(request, init_browser):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


def test_github_desktop(browse_for_desktop):
    browser.open("/")

    browser.element(".HeaderMenu-link--sign-in").should(be.visible)


def test_github_mobile(browse_for_mobile):
    browser.open("/")

    browser.element(".Button--link").click()

    browser.element(".HeaderMenu-link--sign-in").should(be.visible)
