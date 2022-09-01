import datetime
import time

from selenium.webdriver.common.by import By


class Maintenance:
   #Corrective Maintenance
   menu_maintenance_Xpath="//span[normalize-space()='Maintenance']"
   submenu_correctiveMaintenance_Xpath="//a[@href='/maintenance/corrective']"
   add_correctiveMaintenance_Xpath="//em[@class='icon ni ni-plus']"
   input_correctiveMaintenance_taskName_Xpath="//input[@name='title']"
   DD_correctiveMaintenance_Priority_Xpath="(//div[contains(@class,'react-select__control css-yk16xz-control')])[5]"
   DD_correctiveMaintenance_SLA_Xpath="(//div)[266]"
   DD_correctiveMaintenance_status_Xpath="(//div)[279]"
   DD_correctiveMaintenance_plantName_Xpath="(//div)[290]"
   DD_correctiveMaintenance_fieldEngineer_Xpath="(//div)[301]"
   DD_correctiveMaintenance_assignedTo_Xpath = "(//div[contains(@class,'react-select__input')])[10]"
   DD_correctiveMaintenance_assetCategory_Xpath="(//div[contains(@class,'form-group form-group')])[5]"
   input_correctiveMaintenance_Description_Xpath="(//textarea[@name='description'])[1]"
   DD_correctiveMaintenance_relatedTask_Xpath="(//div[contains(@class,'react-select__control css-yk16xz-control')])[12]"
   btn_correctiveMaintenance_add_Xpath="(//button[normalize-space()='Add'])[1]"

   def __init__(self,driver):
      self.driver=driver
   def Maintenance(self):
      self.driver.find_element(By.XPATH,self.menu_maintenance_Xpath).click()
   def correctiveMaintenance(self):
      self.driver.find_element(By.XPATH,self.submenu_correctiveMaintenance_Xpath).click()
   def add_CorrectiveMaintenance(self):
      self.driver.find_element(By.XPATH,self.add_correctiveMaintenance_Xpath).click()
   def taskName(self,name):
      self.driver.find_element(By.XPATH,self.input_correctiveMaintenance_taskName_Xpath).send_keys(name)
   def priority(self,priority):
      self.driver.find_element(By.XPATH,self.DD_correctiveMaintenance_Priority_Xpath).click()
      self.driver.find_element(By.XPATH,'//div[contains(text(),"'+priority+'")]').click()
   def SLA(self,sla):
      self.driver.find_element(By.XPATH, self.DD_correctiveMaintenance_SLA_Xpath).click()
      self.driver.find_element(By.XPATH, '//div[contains(text(),"' + sla + '")]').click()
   def status(self,status):
      self.driver.find_element(By.XPATH, self.DD_correctiveMaintenance_status_Xpath).click()
      self.driver.find_element(By.XPATH, '//div[contains(text(),"' + status + '")]').click()
   def plantName(self,p_name):
      self.driver.find_element(By.XPATH, self.DD_correctiveMaintenance_plantName_Xpath).click()
      self.driver.find_element(By.XPATH, '//div[contains(text(),"' + p_name + '")]').click()
   def fieldEngineer(self,f_engineer):
      self.driver.find_element(By.XPATH, self.DD_correctiveMaintenance_fieldEngineer_Xpath).click()
      self.driver.find_element(By.XPATH, '//div[contains(text(),"' + f_engineer + '")]').click()
   def startDate(self):
      self.driver.find_element(By.XPATH,"//div[@class='form-group']//div[@class='form-control-wrap']//div[@class='react-datepicker__input-container']").click()
      now=datetime.datetime.today()
      dt_string = now.strftime("%m/%d/%Y %H:%M")
      input_dt = self.driver.find_element(By.XPATH,'//input[@class="form-control date-picker react-datepicker-ignore-onclickoutside"]')
      self.driver.execute_script("arguments[0].value = arguments[1]",input_dt,dt_string)
   def assignedTo(self,assigned):
      self.driver.find_element(By.XPATH, self.DD_correctiveMaintenance_assignedTo_Xpath).click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, '//div[contains(text(),"' + assigned + '")]').click()
   def resolvedDate(self):
      self.driver.find_element(By.XPATH,"(//div[contains(@class,'react-datepicker-wrapper')])[4]").click()
      now= datetime.datetime.today() + datetime.timedelta(days=1)
      dt_string = now.strftime("%m/%d/%Y %H:%M")
      input_dt = self.driver.find_element(By.XPATH,'//input[@class="form-control date-picker react-datepicker-ignore-onclickoutside"]').send_keys(dt_string)
      #self.driver.execute_script("arguments[0].value = arguments[1]",input_dt,dt_string)
   def assetCategory(self,category):
      self.driver.find_element(By.XPATH, self.DD_correctiveMaintenance_assetCategory_Xpath).click()
      self.driver.find_element(By.XPATH, '//div[contains(text(),"' + category + '")]').click()
   def description(self,description):
      self.driver.find_element(By.XPATH,self.input_correctiveMaintenance_Description_Xpath).send_keys(description)
   def relatedTask(self,task):
      self.driver.find_element(By.XPATH,self.DD_correctiveMaintenance_relatedTask_Xpath).click()
      self.driver.find_element(By.XPATH, '//div[contains(text(),"' + task + '")]').click()
   def add_maintanance(self):
      self.driver.find_element(By.XPATH,self.btn_correctiveMaintenance_add_Xpath).click()
      self.Message = self.driver.find_element(By.XPATH, "(//div[@class='toastr-text'])[1]").text
      print(self.Message)
      #time.sleep(2)
      if "Success" in self.Message:
         assert True
      else:
         #print("DNO not Created")
         assert False


