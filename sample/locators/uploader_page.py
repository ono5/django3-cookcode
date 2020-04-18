from selenium.webdriver.common.by import By

from pravas.locators.base_page import BasePageLocators


class PageLocators(BasePageLocators):
    CONN = (By.ID, 'test')
    YAHH = (By.ID, 'test2')
    HELLO = (By.ID, 'test3')
    HA_MA = (By.ID, 'test4')