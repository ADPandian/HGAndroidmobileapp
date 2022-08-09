import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# des_cap = dict(
#     deviceName='adp',
#     platformName='Android',
#     app='//Users//freshworksstudio//PycharmProjects//healthGatewayMobile//APK//healthGateway-stage.apk'
# )
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_cap)
# driver.implicitly_wait(10)
sauce_username = 'freshworks-studio'
sauce_access_key = '32f8ecd5-e87d-4eff-8e1b-53c596f16985'
url = "https://{}:{}@ondemand.us-west-1.saucelabs.com:443/wd/hub".format(sauce_username, sauce_access_key)
des_cap = dict(
    platformName='Android',
    automationName='UiAutomator2',
    app='storage:filename=app-stage-debug.apk',
    deviceName='Google Pixel 4a (5G) GoogleAPI Emulator',
    platformVersion='12.0',
    appiumVersion='1.22.1',
    name='first test run',
    build='test-1'
)
driver = webdriver.Remote(url, des_cap)


class onBoard:
    @staticmethod
    def next():
        driver.execute_script('mobile: shell', {'command': 'am start -a android.settings.SECURITY_SETTINGS && '
                                                           'locksettings set-pin 0000'})
        driver.launch_app()
        wait1 = WebDriverWait(driver, 60)
        wait1.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Next'))
        )
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Next').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Next').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Get started').click()

    def skip(self):
        driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/tv_skip').click()
        driver.quit()


def biometrics():
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_auth').click()
    for i in range(4):
        driver.press_keycode(7)
    driver.press_keycode(66)


def login():
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_login').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_continue').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ('new UiScrollable(new UiSelector().scrollable('
                                                       'true)).scrollIntoView(new UiSelector().textContains("Log in '
                                                       'with '
                                                       'Virtual testing"))')).click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="csn"]').send_keys('HTHGTWY11')
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="passcode"]').send_keys('98911')
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
    time.sleep(3)
    wait = WebDriverWait(driver, 60)
    wait.until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("OK")'))
    )
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("OK")').click()


def record_sync():
    driver.open_notifications()
    wait = WebDriverWait(driver, 60)
    wait.until(
        EC.any_of(
            EC.text_to_be_present_in_element(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Records updated.")'), 'Records updated.'),
            EC.text_to_be_present_in_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Failed to retrieve '
                                                                            'records.")'),
                                             'Failed to retrieve records.')
        )
    )
    driver.press_keycode(4)
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/home').click()


def nav_from_home():
    nav = ['Records', 'Proofs', 'Resources']
    for nav in nav:
        if nav == 'Records':
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("View records")').click()
        elif nav == 'Proofs':
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add proofs")').click()
        else:
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Learn more")').click()
        driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/home').click()


def logout():
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/menu_settings').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/tv_log_out').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LOG OUT")').click()
    driver.quit()

#
# time.sleep(10)
# driver.quit()
