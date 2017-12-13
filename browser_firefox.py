from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
qnq_url='https://list.suning.com/0-20370-0.html'
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
try:
    url_open.find_element_by_xpath(".//div[@id='second-filter']/div[@class='sort fl clearfix']/a[@class='pjs']").click()
except:
    url_open.find_element_by_name('ssdln_20370_sort_assess').click()
time.sleep(15)
listurl=[]
elements=[]
for i in range(0,int(max_number)):
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
    if i < int(max_number)-1:
        try:
            nextpage=url_open.find_element_by_xpath(".//div[@id='filter-results']/div[@id='bottom_pager']/a[@id='nextPage']").click()
        except:
            # url_open.refresh()
            url_open.get('https://list.suning.com/0-20370-%d.html' % (i+1))
df=pd.DataFrame(columns=['url','page'])
df['url']=listurl
df['page']=elements
df.to_csv('snqnq12122.csv')
url_open.quit()
