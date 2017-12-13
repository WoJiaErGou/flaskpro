from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import time
import re
import pandas as pd
# SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
profile = '/home/260138/.mozilla/firefox/wu6maupj.default'
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('http://list.gome.com.cn/cat10000188.html?intcmp=sy-1000053150_1')
driver.maximize_window()
driver.get_screenshot_as_file('sn.png')
results = driver.find_element_by_xpath(".//div[@class='nSearchWarp nSearch-crumb-category-results']/span[2]/em[@id='searchTotalNumber']").text
print(results)
max_number = driver.find_element_by_xpath(".//div[@class='min-pager-box']/span[@id='min-pager-number']").text
max_number=re.sub('1/','',max_number)
print(max_number)
print('国美搜索结果页面为' + max_number + '页')
print('电饭煲一共有' + results + '个')
listurl = []
# elements = []
for i in range(1, int(max_number) + 1):
    # print('第%d页' % i)
    element = driver.find_elements_by_xpath(".//p[@class='item-name']/a")
    for each in element:
        listurl.append(each.get_attribute('href'))
    try:
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # time.sleep(5)
        nowpage=driver.find_element_by_xpath(".//div[@class='min-pager-box']/span[@id='min-pager-number']").text.split('/')[0]
        print('第%s页' % nowpage)
        driver.find_element_by_id('mp-next').click()
        time.sleep(5)
    except:
        print('点击失败！')
        try:
            driver.refresh()
            time.sleep(2)
            driver.find_element_by_xpath(".//div[@id='j-page']/label[@class='txt-wrap']/input[@id='pNum']").clear()
            driver.find_element_by_xpath(".//div[@id='j-page']/label[@class='txt-wrap']/input[@id='pNum']").send_keys('%d' % i+1)
            driver.find_element_by_xpath(".//div[@id='product-pager']/div[@id='j-page']/a[@class='btn']").send_keys(Keys.ENTER)
        except:
            print('失败！')
            break
driver.quit()
dataframe = pd.DataFrame(columns=['url'])
dataframe['url'] = listurl
dataframe.to_csv('国美电饭煲.csv', index=None)