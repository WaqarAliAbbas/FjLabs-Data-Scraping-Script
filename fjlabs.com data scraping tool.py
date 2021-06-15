# ---> Web Scraping Script By Waqar Ali Abbas <---
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv
driver = webdriver.Chrome()
url="https://fjlabs.com/portfolio/"
driver.maximize_window()
driver.delete_all_cookies()
driver.get(url)
scroll_val=None
while True:
    page_height=driver.execute_script("return document.body.scrollHeight")
    if page_height==scroll_val: 
        break
    driver.find_element_by_tag_name("body").send_keys(Keys.END)
    time.sleep(3)
    scroll_val=page_height
main_div=driver.find_elements_by_xpath("//div[@id='companies']/div")[1:]
with open("websitedetails.csv","a",newline="",encoding="UTF-8") as f:
    csv_file=csv.DictWriter(f,fieldnames=["Business Name","Website","Business Title","Year","Seed"])
    csv_file.writeheader()
    for main in main_div:
        try:
            business_name=main.find_element_by_xpath(".//h3[@class='Centered']").get_attribute("innerText")
        except Exception as s:
            business_name=""
        try:
            website=main.find_element_by_xpath(".//a[@class='websiteUrl']").get_attribute("href")
        except Exception as s:
            website=""
        try:
            business_title=main.find_element_by_xpath(".//div[@class='description']/p").get_attribute("innerText")
        except Exception as s:
            business_title=""
        try:
            year=main.find_element_by_xpath(".//span[@class='year']").get_attribute("innerText")
        except Exception as s:
            year=""
        try:
            seed=main.find_element_by_xpath(".//span[@class='investment_stage']").get_attribute("innerText")
        except Exception as s:
            seed="k"
        csv_file.writerow({
            "Business Name":business_name,"Website":website,"Business Title":business_title,"Year":year,"Seed":seed
        })
        print(f"Business Name:  {business_name}  Website:  {website}  Business Title:  {business_title}  Year:  {year}  Seed {seed}")
