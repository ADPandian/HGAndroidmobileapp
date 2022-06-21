import time

import self as self
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

des_cap = dict(
    deviceName='adp',
    platformName='Android',
    automationName='UiAutomator2',
    app='//Users//freshworksstudio//PycharmProjects//healthGatewayMobile//APK//healthGateway-stage.apk'
)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_cap)
driver.implicitly_wait(60)


class onBoard:
    # @staticmethod
    def next(self):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Next').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Next').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Get started').click()

    def skip(self):
        driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/tv_skip').click()
        driver.quit()


onBoard().next()
driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_auth').click()


def keyPadClick(x, y):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.click()
    actions.w3c_actions.perform()


keyPadClick(147, 2150)
time.sleep(3)
for x in range(4):
    keyPadClick(537, 2056)
keyPadClick(817, 2030)

driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_login').click()
driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_continue').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Log in with Virtual testing")').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="csn"]').send_keys('HTHGTWY11')
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="passcode"]').send_keys('98911')
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()

driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/home').click()
# Opening notification and checking message
driver.open_notifications()
wait = WebDriverWait(driver, 30)

wait.until(
    EC.any_of(
        EC.text_to_be_present_in_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Records updated.")'), 'Records updated.'),
        EC.text_to_be_present_in_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Failed to retrieve '
                                                                        'records.")'), 'Failed to retrieve records.')
    )
)
driver.press_keycode(4)
# wait.until(EC.text_to_be_present_in_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Records updated.")'), 'Records updated.'))

nav = ['Records', 'Proofs', 'Resources']
for nav in nav:
    if nav == 'Records':
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("View records")').click()
    elif nav == 'Proofs':
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add proofs")').click()
    else:
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Learn more")').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/home').click()

time.sleep(10)
driver.quit()
