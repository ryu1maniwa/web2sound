#! /usr/bin/python3
### -*- coding: utf-8 -*-
import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml.html
from gtts import gTTS

# Chrome Optionsの設定
options = Options()
options.add_argument("no-sandbox")                 # sandboxモードを解除する(セキュリティ)
# options.add_argument('--headless')                 # headlessモードを使用す 画面を表示せずにブラウザを起動させる
# options.add_argument('--disable-gpu')              # headlessモードで暫定的に必要なフラグ(そのうち不要になる)
options.add_argument('--disable-extensions')       # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
options.add_argument('--proxy-server="direct://"') # Proxy経由ではなく直接接続する
options.add_argument('--proxy-bypass-list=*')      # すべてのホスト名
options.add_argument('--use-fake-ui-for-media-stream') # 「カメラ(マイク)の使用を許可しますか」ダイアログを回避する
options.add_argument('--start-maximized')          # 起動時にウィンドウを最大化する
options.add_argument('--disable-desktop-notifications')
options.add_argument('--lang=ja')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')

"""""
このプログラムは、google alertのxmlファイルにアクセスし、ある企業のニュースを音声に変換する機能を持つ。（作成中）
"""""

# Chrome Driverを起動する
driver = webdriver.Chrome(options=options) 

# 要素が見つかるまで、最大10秒間待機する設定
driver.implicitly_wait(10) # 秒
# 我慢できる秒数を設定する
# driver.set_page_load_timeout(10) # 秒まで待つ

# google alertのxmlファイルにアクセスする
sony_alert_url = "https://www.google.co.jp/alerts/feeds/00796967841491901761/9442338860580001349"
driver.get(sony_alert_url)
time.sleep(1)

# link = driver.find_element(by=By.XPATH, value='//*[@class="html-tag" and text() = "<title"]')
# print(link)
# print(link.text)

# 表示されている記事たちのURLを配列に格納する
list = driver.find_elements(by=By.XPATH, value="//*[@href]")
links = [link.get_attribute('href') for link in list]

# 表示されている記事を順番に見ていき、タイトルとURLを表示する
for link in links[1:]:
    try:
        driver.get(link)
    except Exception as e:
        print(e)
        continue

    # 現在のタイトルとURLを表示
    print(f'{driver.title}')
    print(driver.current_url)

    # htmlを取得
    # html = driver.page_source

    # BeautifulSoupによってスクレイピングをさせる
    # BeautifulSoup(html, "lxml")

    """""ここにスクレイピングコードを記入
    ブラウザに表示されている HTML から BeautifulSoup オブジェクトを作りパースする
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.select('.css-u56bup')
    for article in articles:
        # プロフィールページに表示されている記事タイトルの一覧を取得
        print(article.select_one('.css-i9gxme a').get_text())
    time.sleep(1)

    # 2. 「最近の記事」に表示されている記事一覧の 2 ページ目に移動する
    # driver.find_element(By.XPATH, '//a[@rel="next" and text()="2"]').click()
    driver.find_element(By.XPATH, '//a[@rel="next"]').click()
    print(driver.current_url)
    # > https://qiita.com/Chanmoro?page=2
    time.sleep(1)

    # 3. 2 ページ目の一番最初に表示されている記事のタイトルを URL を取得する
    # article_links = driver.find_elements(By.XPATH, '//div[@class="ItemLink__title"]/a')
    article_links = driver.find_elements(By.XPATH, '//article[@class="css-u56bup"]/a')
    # print(article_links[0].text)
    # print(article_links[1].text)
    print(len(article_links))

    # > Python - 関数を文字列から動的に呼び出す
    print(article_links[0].get_attribute('href'))
    print(article_links[1].get_attribute('href'))
    """""

"""""スクレイピングの結果得たテキストを音声に変換するコード
mytext = "こんにちは。"
language = "ja"

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("news.mp3")
"""""

# x. ブラウザを終了する
time.sleep(1)
driver.close()
driver.quit()




