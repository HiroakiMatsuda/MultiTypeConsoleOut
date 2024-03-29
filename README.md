MultiTypeConsoleOut
======================
MultiTypeConsoleOutはRTミドルウェア開発を支援するRTCです  
ConsoleOutを拡張して複数の型のデータを受け取ることができます  
また受け取ったデータをCSVファイルとして出力するLogger機能を持っています   

動作確認環境
------
Python:  
2.6.6  

OS:  
Windows 7 64bit / 32bit  
Ubuntu 10.04 LTS / 12.04 LTS 32bit  
 
ファイル構成
------
MultiTypeConsoleOut  
│―MultiTypeConsoleOut.py  
│―tkmtcocont.py  
│―ini   
│　　│―consoleout.ini   
│  
│―rtc.conf  

* MultiTypeConsoleOut.py  
RTC本体です  
* tkmtcocont.py  
RTCのGUIをTkinterにて生成しています
* consoleout.ini  
データポートの型や保存するCSVのデリミターを指定することができます
* rtc.conf  
ポートの設定や動作周期を設定できます

注:本RTCにおいてユーザーが操作すると想定しているファイルのみ説明しています  

RTCの構成
------  
<img src="http://cloud.github.com/downloads/HiroakiMatsuda/MultiTypeConsoleOut/readme_01.png" width="400px" />    
任意のデータ型でデータを受け取り、それをCSVファイルに書き出すことができます  
ファイルの設定はiniファイルを通して行えるので、簡単に設定を変えられます  
iniファイルの設定はInitialize時に読み込むので、設定を変更した場合はRTCを再起動してください

* data port :InPort データ型; 任意のデータ型  

TimedXXX型の場合  
[x1]  
1つの指定した型のデータ  

TimedXXXSeq型の場合  
[x1, x2, ..... xN]  
指定した型のN個のデータ

使い方
------
###1. 使用するデータ型を設定する###
1. consoleout.iniをテキストエディタなどで開き編集します  
   ```type = XXX```  
XXXの部分を編集してください。現在対応している型は以下の通りです  
 ・TimedShort  
 ・TimedUShort  
 ・TimedLong  
 ・TimedULong  
 ・TimedFloat  
 ・TimedDouble  
 ・TimedString  
 ・TimedWString  
 ・TimedChar  
 ・TimedWChar  
 ・TimedBool  
 ・TimedOctet  
 ・TimedShortSeq  
 ・TimedUShortSeq  
 ・TimedLongSeq  
 ・TimedULongSeq  
 ・TimedFloatSeq  
 ・TimedDoubleSeq  
 ・TimedStringSeq  
 ・TimedWStringSeq  
 ・TimedCharSeq  
 ・TimedWCharSeq  
 ・TimedOctetSeq  
 ・TimedBoolSeq	  

2. CSVファイルのデリミターを例のように設定します  
   ```delimiter = X   ```  
Xに以下のデリミターから選択し入力してください  
・,  
・  (半角スペース)  
・&    

###2. データをコンソールに表示する###
1. MultiTypeConsoleOut.py起動する  
ダブルクリックするなどして起動してください  
2. データを入力する  
ConsoleInなどの適当なデータを出力するRTCを使用してデータを入力します  
データが入力されると入力されたデータがコンソールに出力されます   
  
###3. データをCSVファイルに保存する###
1. CSVファイルの名前を入力する  
下図のGUIのエントリーに保存するファイル名を入力します    
<img src="https://github.com/downloads/HiroakiMatsuda/MultiTypeConsoleOut/readme_02.png" width="200px" />  

2. ログ取得を開始する
GUIのボタンを押すとボタンの色が赤く変わり、コンソールに'Start logging'と表示されます  
この表示以降のデータをCSVファイルに保存します  

3. ログ取得を終了する
もう一度ボタンを押すと'End logging'と表示されCSVファイルが保存されます 
<img src="https://github.com/downloads/HiroakiMatsuda/MultiTypeConsoleOut/readme_03.png" width="500px" />  
      
4. ログデータを確認する  
保存されたCSVファイルを開くと、受信したデータが保存されていることがわかります  
<img src="https://github.com/downloads/HiroakiMatsuda/MultiTypeConsoleOut/readme_04.png" width="500px" />  

以上が本RTCの使い方となります  

ライセンス
----------
Copyright &copy; 2012 Hiroaki Matsuda  
Licensed under the [Apache License, Version 2.0][Apache]  
Distributed under the [MIT License][mit].  
Dual licensed under the [MIT license][MIT] and [GPL license][GPL].  
 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php
[GPL]: http://www.gnu.org/licenses/gpl.html