from selenium import webdriver

browser = webdriver.Chrome(r"C:\chromedriver.exe")
browser.get("http://127.0.0.1:8000")

assert 'Django' in browser.title