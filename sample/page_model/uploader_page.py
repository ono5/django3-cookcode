from selenium.webdriver.common.by import By

from pravas.locators.base_page import BasePageLocators


class PageLocators(BasePageLocators):
    conn = (By.ID, 'CONN')
    yahh = (By.ID, 'YAHH')
    hello = (By.ID, 'HELLO')
    ha_ma = (By.ID, 'HA_MA')