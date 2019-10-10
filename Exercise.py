import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="E:\Downloads\chromedriver.exe")
driver.get("https://www.airbnb.com//")
driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/airbnbsc.png")


class AirBnb(object):
    def visit(self):

        driver.maximize_window()

        links = driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))

        driver.find_element_by_xpath("//button[@class='optanon-allow-all accept-cookies-button']").click()




        driver.find_element_by_xpath("//input[@id='Koan-magic-carpet-koan-search-bar__input']").send_keys("Tel Aviv")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[contains(text(),'Tel Aviv-Yafo, Israel')]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//input[@id='checkin_input']")
        driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'23')]").click()
        driver.find_element_by_xpath("//input[@id='checkout_input']")
        driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'30')]").click()

        driver.find_element_by_xpath(" //button[@class='_7ykwo4']").click()
        driver.find_element_by_xpath("//div[@id='StepIncrementerRow-title-GuestCountFilter-GuestPicker-p0_magic_carpet-marquee_search_bar-adults']")
        driver.find_element_by_xpath("//body[@class='with-new-header']/div/div/main[@id='site-content']/section/div[@id='FMP-target']/div[@class='_1xrzfjy']/div[@class='_ogalm0']/div[@class='_djxl322']/div[@class='_ni9axhe']/div[@class='_ctrm83']/div[@class='_26hc67j']/div[@class='_1n8ekdm']/div/div[@class='_slilk2']/form/div/div/div[@class='_e296pg']/div/div[@class='_9cfq872']/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/*[1] ").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//body[@class='with-new-header']/div/div/main[@id='site-content']/section/div[@id='FMP-target']/div[@class='_1xrzfjy']/div[@class='_ogalm0']/div[@class='_djxl322']/div[@class='_ni9axhe']/div[@class='_ctrm83']/div[@class='_26hc67j']/div[@class='_1n8ekdm']/div/div[@class='_slilk2']/form/div/div/div[@class='_e296pg']/div/div[@class='_9cfq872']/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/*[1] ").click()
        driver.find_element_by_xpath("//div[@id='StepIncrementerRow-title-GuestCountFilter-GuestPicker-p0_magic_carpet-marquee_search_bar-children'] ")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//body[@class='with-new-header']/div/div/main[@id='site-content']/section/div[@id='FMP-target']/div[@class='_1xrzfjy']/div[@class='_ogalm0']/div[@class='_djxl322']/div[@class='_ni9axhe']/div[@class='_ctrm83']/div[@class='_26hc67j']/div[@class='_1n8ekdm']/div/div[@class='_slilk2']/form/div/div/div[@class='_e296pg']/div/div[@class='_9cfq872']/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]/span[1]/*[1] ").click()
        driver.find_element_by_xpath("//button[@class='_b0ybw8s']").click()
        driver.find_element_by_xpath("//span[@class='_ftj2sg4']").click()

        driver.execute_script("window.scrollBy(0,5000) ", "")

#driver.implicitly_wait(10)

        login = driver.find_element_by_xpath("//div[contains(text(),'Log in')]")
        actions = ActionChains(driver)
        actions.move_to_element(login).click().perform()
        driver.quit()

a=AirBnb()
a.visit()

