# GoogleMapSikuliDemo
Sikuliを使ってGoogleMapのキャプチャその他を行うデモプログラムです。


## 0. はじめに

このプログラムは、Sikuliを用いたデモンストレーション用プログラムです。

#### Sikuliとは

画像認識(OpenCV)を利用したGUI自動操作ツールです。
モニタ上でマウスカーソルやキーボードを用いて画面を自動的に操作することが可能です。

- http://www.sikuli.org/
- http://doc.sikuli.org/


- [test][automation] sikuliを使ってGUI操作を自動化する
  - http://qiita.com/YHayama@github/items/483198cba0e7c4baa78c
- Sikuliを使ってUIの操作を自動化
  - http://www.urong-answer.org/2015/02/automate-ui-operation-using-sikuli/

## 1. 実行環境

以下の環境で動作する事を想定しています。

- Windows 7 / 10
- Sikuli ver1.1.0 / 1.1.1 (Jython 2.7)
- Google Chrome ver58
- Microsoft Excel 2003 / 2010 / 2013

実際に確認した組合せは以下の通りです。
画像認識を行うため、環境が異なると正しく認識できない場合があります。

- Windows7 + Sikuli 1.1.0 + Excel2003 + Chrome 58
- Windows7 + Sikuli 1.1.0 + Excel2010 + Chrome 58
- Windows7 + Sikuli 1.1.0 + Excel2013 + Chrome 58
- Windows10 + Sikuli 1.1.1 + Excel2003 + Chrome 58


## 2. デモの流れ

デモ動画: 

https://youtu.be/506WM-ADnJs

具体的には以下のような動作を行います。
- Chrome を開く
- Excel を開く
- 以下を指定されたランドマークの数だけ繰り返す
  - Chrome で GoogleMap を開く
  - GoogleMap上で指定されたランドマークを検索する
  - ランドマークの検索結果をキャプチャして画像を保存する
  - Excelに切り替える
  - ランドマークの画像をExcelに貼り付ける
  - ランドマークへのリンクをExcelに貼り付け
 - Excelを保存する


## 3. Sikuliを動かすために

SikuliはJythonで動くため、Javaがインストールされている事が前提条件です。
Javaインストール後、公式からSikuliをインストールしてください。


参考) インストール手順

http://qiita.com/YHayama@github/items/483198cba0e7c4baa78c


## 4. デモを実行する前に

- 実行バッチファイル(demo.bat)で各種パス等の設定を行ってください。
- 設定ファイル(setting.xml)で各種パス等の設定を行ってください。
- 不確定要素を減らすため、他のプログラム等はすべて閉じてください。
- デモ実行中はマウスカーソル、キーボードが自動で動く為、手入力が入ると予期せぬ動作を起こすことがあります。
- Chromeは全画面表示を解除し、縦サイズを短くしてください（Google Mapのメニューで「地形」以降がスクロールしてないと表示されないくらい）
- デモは Ctrl＋↑ で中断することができます。

すべて完了いたしましたら、demo.batを実行してください。

## 5. 解説

Sikuliデモプログラムを作ってみた(準備編)

http://qiita.com/miz21358/items/d301297dcb9d925172f6

上記に他説明リンクもあり

## 6. 免責事項他

本デモプログラムは、本readmeにある通り動作することを期待し、
また、その通りに動作し皆様のお役に立つことを意図して作成しておりますが、
その動作の保証、性能の保証は致しません。

本デモプログラムを使用することによって
生じたいかなる他の損害に対して、作者は一切責任を負いません。
また、本デモプログラムが使用できなかったことによって
生じたいかなる他の損害に対して、作者は一切責任を負いません。

ご使用の前に、バックアップ等のデータの保全対策や、運用のテストを行って下さい。

