# -*- coding: utf-8 -*-

import sys
import os

# 自作ライブラリインポート
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import GMSDLib
reload(GMSDLib)
from GMSDLib import *

import GMSDParams
reload(GMSDParams)
from GMSDParams import *

import GMSDCapture
reload(GMSDCapture)
from GMSDCapture import *

# デフォルト最小類似度。find等での画像ヒット率に影響する
Settings.MinSimilarity = 0.9
#ログの出力
Settings.UserLogs = True
#ログのプレフィックス
Settings.UserLogPrefix = "GMSD"
#ログに時間を出力するか
Settings.UserLogTime = True
#ログの種類別出力是非
Settings.ActionLogs = True
Settings.InfoLogs = True
Settings.DebugLogs = True

#中断ホットキー追加(CTRL + ↑)
Env.addHotkey(Key.UP, KeyModifier.CTRL, GMSDLib.confirmStop)

# Main
if __name__ == '__main__':
    #引数を取得する
    argv = sys.argv

    #引数が足りなければエラー終了
    #0番目には自身のパスが入るため、使うのは1番目以降
    if len(argv) < 2:
        print u"引数不足のため、終了します。設定XMLファイルパスを指定してください。"
        sys.exit()

    #初期化処理実行
    params = GMSDParams.ParamCls(argv[1])

    #キャプチャ処理実行
    GMSDCapture.main(params)

    #処理終了
    GMSDLib.logger(u"GoogleMapSikuliキャプチャデモ終了")

    #ポップアップも出す
    popup(u"GoogleMapSikuliキャプチャデモ終了")


    