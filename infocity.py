from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = './chromedriver.exe'
option = Options()
option.add_argument('--log-level=3')
option.headless = True
driver = webdriver.Chrome(path,0,option)

def getTemp(city):
    driver.get('https://www.google.com/search?q=temperatura+{}'.format(city))
    search = True
    temp = ''
    while(search):
        try:
            temp = driver.find_element_by_id('wob_tm').text
            return temp
            search = False
        except a:
            return a

def getClimate(city):
    driver.get('https://www.google.com/search?q=temperatura+{}'.format(city))
    search = True
    climate = ''
    while(search):
        try:
            climate = driver.find_element_by_id('wob_dc').text
            return climate
            search = False
        except a:
            return a

def getRain(city):
    driver.get('https://www.google.com/search?q=temperatura+{}'.format(city))
    search = True
    rain = ''
    while(search):
        try:
            rain = driver.find_element_by_id('wob_pp').text
            return rain
            search = False
        except a:
            return a

def getHumidity(city):
    driver.get('https://www.google.com/search?q=temperatura+{}'.format(city))
    search = True
    humidity = ''
    while(search):
        try:
            humidity = driver.find_element_by_id('wob_hm').text
            return humidity
            search = False
        except a:
            return a

def getWind(city):
    driver.get('https://www.google.com/search?q=temperatura+{}'.format(city))
    search = True
    wind = ''
    while(search):
        try:
            wind = driver.find_element_by_id('wob_ws').text
            return wind
            search = False
        except a:
            return a
    
def getfirstnews(city):
    driver.get('https://news.google.com/search?q={}'.format(city))
    search = True
    first = ''
    while(search):
        try:
            first = driver.find_element_by_class_name('RZIKme').text
            return first
            search = False
        except a:
            return a

def getNews(city, num):
    driver.get('https://news.google.com/search?q={}'.format(city))
    search = True
    news = ''
    send = []
    while(search):
        try:
            news = driver.find_elements_by_class_name('RZIKme')
            search = False
        except a:
            return a
    try:
        for i in range(num):
            send.append(news[i].text)
    except a:
        return a
    return send
