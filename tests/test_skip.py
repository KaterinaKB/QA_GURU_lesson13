"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, be


@pytest.fixture(
    params=[
        (1920, 1280, "desktop"),
        (1600, 900, "desktop"),
        (390, 844, "mobile"),
        (320, 658, "mobile"),
    ],
    ids=["1920*1280", "1600*900", "iPhone 12 Pro", "Samsung Galaxy S9+"],
)
def init_browser(request):
    browser.config.base_url = "https://github.com/"
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    if request.param[2] == "desktop":
        is_desktop = True
    else:
        is_desktop = False

    yield is_desktop

    browser.quit()


def test_github_desktop(init_browser):
    if not init_browser:
        pytest.skip(reason="Тест предназначен для mobile")
    browser.open("/")

    browser.element(".HeaderMenu-link--sign-in").should(be.visible)


def test_github_mobile(init_browser):
    if init_browser:
        pytest.skip(reason="Тест предназначен для desktop")
    browser.open("/")

    browser.element(".Button--link").click()

    browser.element(".HeaderMenu-link--sign-in").should(be.visible)
