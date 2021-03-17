import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
#starts the browser
driver = webdriver.Chrome()
driver.get('https://www.supremenewyork.com/shop/skate/wkey7l9m8')
#finds add cart button
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input').click()
time.sleep(1)
#goes to checkout page
driver.get('https://www.supremenewyork.com/checkout')
#fills in the payment info
driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys('J Pollock')
driver.find_element_by_xpath('//*[@id="order_email"]').send_keys('JPol@bigman.web')
driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys('1-111-111-1111')
driver.find_element_by_xpath('//*[@id="bo"]').send_keys('111 One Street')
driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys('11111')
driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys('One City')
driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[3]/select/option[43]').click()
driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys('1111-1111-1111-1111')
driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[3]/div[3]/div[1]/select[1]/option[9]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[3]/div[3]/div[1]/select[2]/option[10]').click()
driver.find_element_by_xpath('//*[@id="orcer"]').send_keys('111')
driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p/label/div/ins').click()