
# Desired Capability for real device:
# des_cap = dict(
#     deviceName='adp',
#     platformName='Android',
#     app='//Users//freshworksstudio//PycharmProjects//healthGatewayMobile//APK//healthGateway-stage.apk'
# )
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_cap)




# Desired Capability for sauce labs:
# sauce_username = 'freshworks-studio'
# sauce_access_key = '32f8ecd5-e87d-4eff-8e1b-53c596f16985'
# url = "https://{}:{}@ondemand.us-west-1.saucelabs.com:443/wd/hub".format(sauce_username, sauce_access_key)
# des_cap = dict(
#     platformName='Android',
#     automationName='UiAutomator2',
#     app='storage:filename=app-stage-debug.apk',
#     deviceName='Google Pixel 4a (5G) GoogleAPI Emulator',
#     platformVersion='12.0',
#     appiumVersion='1.22.1',
#     name='first test run',
#     build='test-1'
# )
# driver = webdriver.Remote(url, des_cap)
#
# Actionsbuilder
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(x, y)
# actions.w3c_actions.pointer_action.click()
# actions.w3c_actions.perform()