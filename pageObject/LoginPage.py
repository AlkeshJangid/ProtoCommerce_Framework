from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    Text_Name_NAME = (By.NAME, "name")
    Text_Email_NAME = (By.NAME, "email")
    Text_Password_ID = (By.ID, "exampleInputPassword1")
    Click_CheckBox_ID = (By.ID, "exampleCheck1")
    Dropdown_ID = (By.ID, "exampleFormControlSelect1")
    RadioButton_ID = (By.ID, "inlineRadio2")
    DOB_NAME = (By.NAME, "bday")
    Click_Submit_XPATH = (By.XPATH, "//input[@value='Submit']")
    # Alert_Message_XPATH = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    Click_Shop_Title_XPATH = (By.XPATH, "//a[normalize-space()='Shop']")
    Click_AddToCart_XPATH = (By.XPATH, "//app-card[1]//div[1]//div[2]//button[1]")
    Click_Checkout_XPATH = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    Click_CheckOut_Button_XPATH = (By.XPATH, "//button[normalize-space()='Checkout']")
    Enter_Location_XPATH = (By.XPATH, "//input[@id='country']")
    Agree_Terms_Condition_XPATH = (By.XPATH,"//label[@for='checkbox2']")
    Close_Terms_and_Condition_XPATH = (By.XPATH,"//button[@class='btn btn-info']")
    Click_Purchase_Button_XPATH = (By.XPATH, "//input[@value='Purchase']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def Enter_Name(self,name):
        self.driver.find_element(*Login.Text_Name_NAME).send_keys(name)

    def Enter_Email(self,email):
        self.driver.find_element(*Login.Text_Email_NAME).send_keys(email)

    def Enter_Passwd(self,password):
        self.driver.find_element(*Login.Text_Password_ID).send_keys(password)

    def Click_CheckBox(self):
        self.driver.find_element(*Login.Click_CheckBox_ID).click()

    def Dropdown(self):
        try:
            ele = self.driver.find_element(*Login.Dropdown_ID)
            dropdown = Select(ele)
            Gender = dropdown.select_by_index(0)
            print(Gender)
            assert True
        except NoSuchElementException:
            return False

    def Click_RadioButtion(self):
        self.driver.find_element(*Login.RadioButton_ID).click()
        self.wait.until(ec.presence_of_element_located(self.RadioButton_ID))
    def Enter_DateOfBirth(self, dob):
        self.driver.find_element(*Login.DOB_NAME).send_keys(dob)
        self.wait.until(ec.presence_of_element_located(self.DOB_NAME))

    def Click_Submit(self):
        self.driver.find_element(*Login.Click_Submit_XPATH).click()
        self.wait.until(ec.presence_of_element_located(self.Click_Submit_XPATH))

    def Click_Shop_Title(self):
        self.driver.find_element(*Login.Click_Shop_Title_XPATH).click()

    def Click_AddToCart(self):
        self.driver.find_element(*Login.Click_AddToCart_XPATH).click()

    def Click_Checkout_Item(self):
        self.driver.find_element(*Login.Click_Checkout_XPATH).click()

    def Click_Checkout_Button(self):
        self.driver.find_element(*Login.Click_CheckOut_Button_XPATH).click()

    def Enter_Location(self, location):
        self.driver.find_element(*Login.Enter_Location_XPATH).send_keys(location)
        # self.wait.until(ec.presence_of_element_located(self.Enter_Location_XPATH))

    def Agree_Checkbox(self):
        self.driver.find_element(*Login.Agree_Terms_Condition_XPATH).click()
        # self.wait.until(ec.presence_of_element_located(self.Agree_Terms_Condition_XPATH))


    def Close_Terms_Conditions(self):
        # self.wait.until(ec.presence_of_element_located(self.Close_Terms_and_Condition_XPATH))
        self.driver.find_element(*Login.Close_Terms_and_Condition_XPATH).click()


    def Click_Purchase_Button(self):
        self.wait.until(ec.presence_of_element_located(self.Click_Purchase_Button_XPATH))
        self.driver.find_element(*Login.Click_Purchase_Button_XPATH).click()








