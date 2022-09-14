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

sauce_username = 'freshworks-studio'
sauce_access_key = '32f8ecd5-e87d-4eff-8e1b-53c596f16985'
url = "https://{}:{}@ondemand.us-west-1.saucelabs.com:443/wd/hub".format(sauce_username, sauce_access_key)
des_cap = dict(
    platformName='Android',
    automationName='UiAutomator2',
    app='storage:filename=app-stage-debug.apk',
    deviceName='Google Pixel 6 Pro GoogleAPI Emulator',
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
#     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ('new UiScrollable(new UiSelector().scrollable('
#                                                        'true)).scrollIntoView(new UiSelector().text(\"Log in '
#                                                        'with Virtual testing\"))')).click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Log in with Virtual testing").instance(0))')).click()
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
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Health resources")').click()
        driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/home').click()


def logout():
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/menu_settings').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/tv_log_out').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LOG OUT")').click()
    driver.quit()
    
    
def protected_medication():
    wait = WebDriverWait(driver, 60)
    wait.until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Log in with BC '
                                                                  'Services Card")'))
    )
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Log in with BC Services Card")').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_login').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_continue').click()
    driver.find_element(By.ID, 'tile_virtual_device_div_id').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log in with Virtual testing")').click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="csn"]').send_keys('HTHGTWY14')
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="passcode"]').send_keys('98914')
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/home').click()
    driver.open_notifications()
    wait = WebDriverWait(driver, 30)
    wait.until(
        EC.any_of(
            EC.text_to_be_present_in_element(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Records updated.")'),
                'Records updated.'),
            EC.text_to_be_present_in_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Failed to retrieve '
                                                                            'records.")'),
                                             'Failed to retrieve records.')
        )
    )
    driver.press_keycode(4)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Records').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_access').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/et_protective_word').send_keys('keyword')
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_continue').click()
    driver.quit()
def add_proofs_form():
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/health_pass').click()
    try:
        driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_add_card').click()
    except:
        driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/iv_add_card').click()
    # driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_not_now').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_enter_info').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/ed_phn').send_keys('9875023209')
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/ed_dob').send_keys('1995-10-23')
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/ed_dov').send_keys('2021-03-01')
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_submit').click()
    wait = WebDriverWait(driver, 30)
    wait.until(
        EC.text_to_be_present_in_element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BC Vaccine Cards")'), 'BC Vaccine Cards')
    )
    driver.find_element(By.XPATH, "//android.widget.ImageButton[@bounds='[28,84][224,280]']").click()


def add_proofs_upload():
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/health_pass').click()
    driver.push_file('/storage/emulated/0/Download/photo.jpg',
                     source_path='HGAndroidmobileapp/Assets/QR.png')
    try:
        driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_add_card').click()
    except:
        driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/iv_add_card').click()
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add a BC vaccine record').click()
    # driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_not_now').click()
    driver.find_element(By.ID, 'ca.bc.gov.myhealth:id/btn_image_picker').click()
    driver.find_element(By.XPATH, "//android.widget.ImageView[@bounds='[84,1058][489,1463]']").click()
    driver.find_element(By.XPATH, "//android.widget.ImageButton[@bounds='[28,84][224,280]']").click()
