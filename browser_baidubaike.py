from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
qnq_url='https://baike.baidu.com/item/%E7%8F%A0%E6%B5%B7'
profile='/home/260138/.mozilla/firefox/wu6maupj.default'
driver = webdriver.Firefox(firefox_profile=profile)
driver.maximize_window()
driver.get(qnq_url)
df1=pd.read_excel('天气ID.xlsx')
city_list=df1['二级']
city_city=df1['城市']
url_list=[]
with open('baike1.txt','w') as file:
    for i in range(len(city_list)):
        if city_city[i] == city_list[i]:
            each=city_list[i]+'市'
        elif city_list[i] in '北京上海天津重庆' and city_city[i] != city_list[i]:
            each=city_city[i]+'区'
        elif city_city[i] in '台北高雄台中澳门香港':
            each=city_city[i]
        else:
            each=city_city[i]+'县'
        time.sleep(3)
        search=driver.find_element_by_xpath(".//div[@class='search']/div[@class='form']/form[@id='searchForm']/input[@id='query']")
        search.clear()
        search.send_keys(each)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        # 搜索结果不存在时
        try:
            no_result=driver.find_element_by_xpath(".//div[@class='searchResult']/div[@class='create-entrance']/p[1]")
            if no_result:
                driver.find_element_by_xpath(".//dl[@class='search-list']/dd[1]/a[@class='result-title']").click()
                time.sleep(3)
                other_handle = driver.window_handles[-1]
                driver.close()
                driver.switch_to_window(other_handle)
        except:
            pass
        if len(driver.page_source)<10000:
            search.clear()
            search.send_keys(city_city[i]+'区')
            time.sleep(3)
            if len(driver.page_source) < 10000:
                search.clear()
                search.send_keys(each + '市')
                time.sleep(3)
        line=each+':'+driver.current_url
        print(line)
        file.write(line+'\n')
df2=pd.DataFrame(columns=['super_city','city','url'])
df2['super_city']=city_list
df2['city']=city_city
df2['url']=url_list
df2.to_csv('baidu.csv',index=None)