import time
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Onboarding.onboardingScreens import login

des_cap = dict(
    deviceName='adp',
    platformName='Android',
    app='//Users//freshworksstudio//PycharmProjects//healthGatewayMobile//APK//healthGateway-stage.apk',
)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_cap)
driver.implicitly_wait(10)
driver.execute_script('mobile: shell', {'command': 'am start -a android.settings.SECURITY_SETTINGS && '
                                                   'locksettings set-pin 0000'})
# driver.start_activity('ca.bc.gov.myhealth','ca.bc.gov.bchealth.MainActivity')
driver.launch_app()

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Next').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Next').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Get started').click()


def keyPadClick(x, y):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.click()
    actions.w3c_actions.perform()


driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_auth').click()
# time.sleep(3)
# keyPadClick(147, 2150)
for i in range(4):
    driver.press_keycode(7)
driver.press_keycode(66)

driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_login').click()
driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_continue').click()

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ('new UiScrollable(new UiSelector().scrollable('
                                                   'true)).scrollIntoView(new UiSelector().textContains("Log in with '
                                                   'Virtual testing"))')).click()

driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="csn"]').send_keys('HTHGTWY11')
driver.hide_keyboard()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="passcode"]').send_keys('98911')
driver.hide_keyboard()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()

time.sleep(3)
driver.quit()
