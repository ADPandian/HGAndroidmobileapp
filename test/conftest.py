import sys
from os.path import dirname as d
from os.path import abspath, join
# from appium import webdriver as appiumdriver
# import pytest
# from appium import webdriver
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)


# @pytest.fixture()
# def driver():
#     sauce_username = 'freshworks-studio'
#     sauce_access_key = '32f8ecd5-e87d-4eff-8e1b-53c596f16985'
#     url = "https://{}:{}@ondemand.us-west-1.saucelabs.com:443/wd/hub".format(sauce_username, sauce_access_key)
#     des_cap = dict(
#         platformName='Android',
#         automationName='UiAutomator2',
#         app='storage:filename=app-stage-debug.apk',
#         deviceName='Google Pixel 4a (5G) GoogleAPI Emulator',
#         platformVersion='12.0',
#         appiumVersion='1.22.1',
#         name='first test run',
#         build='test-1'
#     )
#     driver = appiumdriver.Remote(url, des_cap)
#     yield driver
#     driver.quit()
