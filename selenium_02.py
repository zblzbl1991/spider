from selenium import webdriver
from selenium.webdriver.common.keys import Keys

edge = webdriver.Edge()
# driver = webdriver.Edge()
get = edge.get('http://www.baidu.com')

# elem = edge.find_element_by_id('kw')
#
# elem.send_keys('hello world')
#
# edge.find_element_by_id('su').click()
# for handle in edge.window_handles:
#     print(handle)

edge.back()
# edge.switch_to.window('')
# edge.close()
# elem.send_keys(Keys.RETURN)
# driver.get("http://www.python.org")
#
#
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

