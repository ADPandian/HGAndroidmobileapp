import pytest

from Onboarding.onboardingScreens import onBoard, login, nav_from_home, logout, biometrics, driver, record_sync


def test_onboarding_next():
    onBoard().next()


def test_biometrics():
    biometrics()


def test_bcsc_login():
    login()


def test_record_sync():
    record_sync()


def test_homescreen_nav():
    nav_from_home()


def test_logout():
    logout()
    
def test_promed():
    protected_medication()
