# 概要
slackbot宛にメンションをつけてslackに投稿すると
slackbotから軽量webフレームワークのbottleにアクセスして
getしたJSON形式のデータをslackに投稿する。

# 使い方
http://qiita.com/txt_only/items/90e019479b62a7ee4ad1

# フォルダとファイルの説明
## 以下のファイル・フォルダはslackbot用のファイルです。
- run.py
- slackbot_settings.py
- pluginsフォルダ

## 以下はbottle用のファイルです。
- hello_world.py

# どうしてbottleを介したのか。
決まったJSONを返すだけならslackbotだけでもできたけども、  
そうするとslackに投稿する以外の方法でそのデータを取得して、  
使用することができなそうなのでbottleを使いました。
