# 使い方とエラー処理
## エラー処理
### versionが違いますみたいなエラーが出てスクレイピングできないときの対処法
google chromeを起動してバージョンを最新にする  
インストールできるchromedriver-binaryのバージョンを確認  
`$ pip3 install chromedriver-binary==`  
表示されたバージョンの中から、最新のバージョンに近いものをインストールする  
`$ pip3 install chromedriver-binary=="103.0.5060.53.0"`  

クロムドライバーをダウンロードする  
https://chromedriver.chromium.org/downloads  
解凍する  
`unzip ~/Download/chromedriver_linux64.zip -d /usr/bin`  

参考：https://qiita.com/hanzawak/items/2ab4d2a333d6be6ac760  

## WSLとVScodeの操作法
1. Windowsデスクトップからwslを開く  
`$ cd /home/`  
2. vscodeを起動する  
`$ code .`  
3. （以下VSCode内）仮想環境へ入る  
`$ source /home/"username"/development/web2sound/bin/activate`  
4. VSCode画面右下にある”インタープリターを選択”をクリック  
5. VSCodeのインタープリターを仮想環境内のものに変更する  
以下を貼り付けて使用  
`/home/"username"/development/web2sound/bin/python`  

## XServerの操作法
Xlaunchを起動  
Addition al parameter for VcXsrvに以下を追加  
-nowgl -ac  
開発を終わるときはXserverからexitする  

## pythonライブラリ管理ツールpipの使い方
- 現状のインストール済みパッケージを確認  
`$ pip list`  
- pip自体の更新
pipコマンドを使う場合、常に以下のコマンドを実行する  
`$ python -m pip install --upgrade pip`  
- ライブラリのバージョンを指定してインストール  
`$ pip install ライブラリ名==バージョン`  
- インストール可能なバージョン番号を表示  
`$ pip install ライブラリ名==`  
- ライブラリのアップグレード  
`$ pip install -U ライブラリ名`  
- インストール済のライブラリ確認  
`$ pip list`  
- インストール済のライブラリの保存  
`$ pip freeze > requirements.txt`  
- 依存するライブラリを確認  
`$ pip show ライブラリ名`  

