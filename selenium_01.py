from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
#使用无头模式

# options
options = EdgeOptions()
options.use_chromium = True
options.add_argument("--headless")
options.add_argument("disable-gpu")
w = Edge(options=options,executable_path='MicrosoftWebDriver.exe')
get = w.get('http://www.baidu.com')
print(w.page_source)
