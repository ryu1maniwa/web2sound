from gtts import gTTS

mytext = """こんにちは。大企業情報収集チャンネル管理者です。
これから日本の大企業の時事ニュースを業界ごとに更新していく予定ですので、是非チャンネル登録よろしくお願いします！"""

language = "ja"

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("hello.mp3")