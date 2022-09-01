from selenium.webdriver.common.by import By


class Login:
    input_email_Xpath = '//input[@name="email"]'
    input_password_Xpath = '//input[@name="password"]'
    btn_Login_Xpath = "(//button[normalize-space()='Login'])[1]"

    def __init__(self,driver):
      self.driver = driver
    def email(self,email):
      self.driver.find_element(By.XPATH,self.input_email_Xpath).clear()
      self.driver.find_element(By.XPATH, self.input_email_Xpath).send_keys(email)
    def password(self,password):
      self.driver.find_element(By.XPATH,self.input_password_Xpath).clear()
      self.driver.find_element(By.XPATH,self.input_password_Xpath).send_keys(password)
    def login(self):
      self.driver.find_element(By.XPATH,self.btn_Login_Xpath).click()