from selenium import webdriver
from selenium.webdriver.common.keys import Keys
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
url_open=webdriver.PhantomJS(service_args=SERVICE_ARGS)
url_open.get('https://www.jdbbs.com/')
try:
    url_open.find_element_by_xpath(".//td[@class='scbar_txt_td']/input[@id='scbar_txt']").send_keys('格力')
except:
    print('path错误')
try:
    url_open.find_element_by_xpath(".//td[@class='scbar_txt_td']/input[@id='scbar_txt']").send_keys(Keys.ENTER)
except:
    print('path错误！')
ttt=url_open.window_handles
url_open.switch_to.window(ttt[1])
now_url=url_open.current_url
print(now_url)
try:
    url_open.get_screenshot_as_file('search.png')
    url_open.find_element_by_partial_link_text('下一页').send_keys(Keys.ENTER)
except:
    print(1111)
if url_open.current_url!=now_url:
    print(url_open.current_url)