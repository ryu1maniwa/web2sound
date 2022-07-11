#! /usr/bin/python3
### -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import lxml.html
from gtts import gTTS

# ブラウザーを起動
options = webdriver.ChromeOptions()
# 画面を表示せずにブラウザを起動させる
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options) 
time.sleep(1) # 1秒待機

# サイトにアクセス
driver.get('https://www.google.com/')
print(f'title is {driver.title}')
# pageのhtmlを表示
# print(driver.page_source)

# 検索ボックスを特定
search_box = driver.find_element(by=By.NAME, value='q')
# 'selenium wsl2'と入力して、"ENTER"を押す
search_box.send_keys('selenium wsl2' + Keys.RETURN)
# + Keys.RETURNの代わりに search_box.submit() を用いてもいい

# 検索結果のタイトルとURLを上から順番に表示する
for elem_h3 in driver.find_elements("xpath", '//a/h3'):
    elem_a = elem_h3.find_element("xpath", '..')  
    print(elem_h3.text)
    print(elem_a.get_attribute('href'))

# htmlを取得・表示
data = driver.page_source
data = lxml.html.fromstring(data)
data = data.xpath("//h1")[0].text
print(data)

# スクリーンショットを撮影
driver.save_screenshot('search_results.png')
time.sleep(2) # 2秒待機
# ブラウザーを終了
driver.quit()