from pravas.locators.callbarring_page import PageLocators
from pravas.page_model.login_page import LoginPage


class UploaderPage(LoginPage):
    @property
    def url(self):
        """トップ画面のURLを取得"""
        return super(UploaderPage, self).url
    @property
    def conn(self):
        """CONNを取得"""
        return self.webdriver.find_element(*UploaderPageLocators.CONN)
    @property
    def yahh(self):
        """YAHHを取得"""
        return self.webdriver.find_element(*UploaderPageLocators.YAHH)
    @property
    def hello(self):
        """HELLOを取得"""
        return self.webdriver.find_element(*UploaderPageLocators.HELLO)
    @property
    def ha_ma(self):
        """HA_MAを取得"""
        return self.webdriver.find_element(*UploaderPageLocators.HA_MA)