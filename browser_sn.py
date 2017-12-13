from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd
import random
# it=list(range(1,5))
# it=random.sample(it,4)
# print(it)

qnq_url='https://list.suning.com/0-20329-0.html'
profile='/home/260138/.mozilla/firefox/wu6maupj.default'
url_open = webdriver.Firefox(firefox_profile=profile)
url_open.maximize_window()
url_open.get(qnq_url)
try:
    max_page=url_open.find_element_by_xpath(".//div[@id='filter-results']/div[@id='bottom_pager']/span[@class='page-more']").text
    results=url_open.find_element_by_xpath(".//span[@class='total-result']/strong[@id='totalNum']").text
except:
    url_open.refresh()
    max_page=url_open.find_element_by_xpath(".//div[@id='filter-results']/div[@id='bottom_pager']/span[@class='page-more']").text
    results=url_open.find_element_by_xpath(".//span[@class='total-result']/strong[@id='totalNum']").text
max_number = re.findall('共(.*?)页', max_page)[0]
print('苏宁电饭煲搜索结果页面为' + max_number + '页')
print('电饭煲一共有' + results + '个')

# try:
#     url_open.find_element_by_xpath(".//div[@id='second-filter']/div[@class='sort fl clearfix']/a[@class='prive']").click()
# except:
#     url_open.find_element_by_name('ssdln_20370_sort_price').click()
# time.sleep(15)
# try:
#     url_open.find_element_by_xpath(".//div[@id='second-filter']/div[@class='sort fl clearfix']/a[@class='pjs']").click()
# except:
#     url_open.find_element_by_name('ssdln_20370_sort_assess').click()
# time.sleep(15)
listurl=[]
elements=[]
numbers=list(range(1,int(max_number)+1))
numbers=random.sample(numbers,int(max_number))
for i in numbers:
    try:
        url_open.find_element_by_xpath(".//span[@class='page-more']/input[@id='bottomPage']").clear()
        url_open.find_element_by_xpath(".//span[@class='page-more']/input[@id='bottomPage']").send_keys('%d' % i)
        url_open.find_element_by_xpath(".//div[@id='bottom_pager']/a[@class='page-more ensure']").send_keys(Keys.ENTER)
        time.sleep(10)
    except:
        print("再试一次!!")
        input_ele=url_open.find_element_by_xpath(".//span[@class='page-more']/input[@id='bottomPage']")
        input_ele.clear()
        input_ele.send_keys('%d' % i)
        url_open.find_element_by_xpath(".//div[@id='bottom_pager']/a[@class='page-more ensure']").click()
        time.sleep(10)
    js="var q=document.documentElement.scrollTop=6000"
    url_open.execute_script(js)
    time.sleep(10)
    element=url_open.find_elements_by_xpath(".//div[@class='res-info']/p[@class='sell-point']/a")
    if len(element)<1:
        url_open.get('https://list.suning.com/0-20370-%d.html' % i)
        time.sleep(5)
    for each in element:
        listurl.append(each.get_attribute('href'))
        elements.append(i)
    nowpage = url_open.find_element_by_xpath(".//div[@class='second-box fr']/div[@class='little-page']/span/i").text
    print('第%s页' % nowpage)
df=pd.DataFrame(columns=['url','page'])
df['url']=listurl
df['page']=elements
df.to_csv('dfb_sn1212.csv',index=None)
url_open.quit()
