import time
import pytest
from selenium.webdriver.common.by import By
from pageObject.LoginPage import Login
from utilities.ReadConfigValue import ReadValue
from utilities.Logger import GenerateLogs



class Test_Url:
    NAME = ReadValue.getName()
    EMAIL = ReadValue.getEmail()
    PASSWORD = ReadValue.getPassword()
    DOB = ReadValue.getDateOfBirth()
    URL = ReadValue.getURL()
    LOCATION = ReadValue.getLocation()
    log = GenerateLogs.LogGen()

    @pytest.mark.test_URL_01
    def test_url_01(self, setup):
        self.driver = setup
        # self.driver.implicitly_wait(5)
        self.driver.get(self.URL)
        self.log.info(f"Visit on URL : {self.URL}")
        self.log.info("Opening Browser")
        self.driver.implicitly_wait(5)
        self.log.info("Checking Page Title")
        if self.driver.title == "ProtoCommerce":
            self.log.info(f"Page Title Confirmed : {self.driver.title}")
            self.driver.save_screenshot(
                r"F:\Testing Documents\Pycharm Practice\ParaBankFramework\Screenshorts\test_url_Pass.png")
            assert True
            self.log.info("test_url_01 : Completed")

            self.driver.close()
        else:
            self.log.info("Page Title Not Found")
            self.driver.save_screenshot(
                r"F:\Testing Documents\Pycharm Practice\ParaBankFramework\Screenshorts\test_url_Fail.png")
            assert False

    @pytest.mark.test_Submit_02
    def test_Detail_Submit_02(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.URL)
        self.log.info(f"Visit on URL : {self.URL}")
        self.log.info("Opening Browser")
        self.lp = Login(self.driver)
        self.lp.Enter_Name(self.NAME)
        self.log.info(f"Enter Name : {self.NAME}")
        self.lp.Enter_Email(self.EMAIL)
        self.log.info(f'Enter Email id : {self.EMAIL}')
        self.lp.Enter_Passwd(self.PASSWORD)
        self.log.info(f"Enter Password : {self.PASSWORD}")
        self.lp.Click_CheckBox()
        self.log.info(f"Click on CheckBox")
        self.lp.Dropdown()
        self.log.info(f"Select Gender")
        self.lp.Click_RadioButtion()
        self.log.info(f"Click on Radio Button")
        self.lp.Enter_DateOfBirth(self.DOB)
        self.log.info(f"Enter Date of Birth : {self.DOB}")
        self.lp.Click_Submit()
        self.log.info("Click on Submit Button")
        success_alert = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        self.log.info(f"test_Detail_Submit_02 : Completed {success_alert}")
        self.driver.close()

    @pytest.mark.test_Shop_03
    def test_Shop_item(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.driver.get(self.URL)
        self.log.info(f"Visit on URL : {self.URL}")
        self.lp.Click_Shop_Title()
        self.log.info(f"Click on Shop Button")
        self.lp.Click_AddToCart()
        self.log.info(f"Select item and click Add to Cart button")
        self.lp.Click_Checkout_Item()
        self.log.info(f"Click on Cart Checkout item button")
        self.lp.Click_Checkout_Button()
        self.log.info(f"Click on Final Checkout Button")
        self.lp.Enter_Location(self.LOCATION)
        self.log.info(f"Enter Location {self.LOCATION}")
        time.sleep(2)
        self.lp.Agree_Checkbox()
        self.log.info(f"Agree Terms and Conditions")
        time.sleep(3)
        # Sometime Closing Terms and conditions require
        # self.lp.Close_Terms_Conditions()
        # time.sleep(3)
        self.lp.Click_Purchase_Button()
        self.log.info(f"Click on Purchase Button")
        self.driver.save_screenshot(
                r"F:\Testing Documents\Pycharm Practice\ParaBankFramework\Screenshorts\Item_Purchase_Pass.png")
        self.log.info(f"Successfully Purchase item")
        order_alert = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        self.log.info(f"test_Detail_Submit : Completed {order_alert}")

        self.driver.close()



