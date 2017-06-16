# -*- coding: utf-8 -*-

import os
import sys
import datetime
import shutil
from sikuli import * 

WINDOWS_7 = "Windows7"
WINDOWS_10 = "Windows10"

#Excelのバージョン
EXCEL_VERSION_2003 = "2003"
EXCEL_VERSION_2010 = "2010"
EXCEL_VERSION_2013 = "2013"

# 自作ライブラリインポート
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

# 画像ファイル読み取りのため、自身のディレクトリパスを追加する
addImagePath(os.path.dirname(getBundlePath()) + "/GMSDLib.sikuli")

###-------------
# ログをコンソールとファイルに出力する
#
def logger(msg):
    #コンソール出力
    #windowsのコマンドプロンプトの文字コードにエンコード
    print msg.encode('cp932')
    
    #ログファイルに出力する
    Debug.user(msg)

###-------------
# ブラウザにフォーカスを当てる
# ブラウザが最前面にくるまで、処理を待機する
#
def focusBrowser(params):
    
    # ブラウザにフォーカスを当てる
    params.browserApp.focus()
    
    #ブラウザが開ききるまで待つ
    try:
        wait(params.browserImg, 10)
    except FindFailed as e:
        # 指定時間待っても画像が取得できなかった場合、検索失敗エラーが発生する
        logger(u"ブラウザfocus失敗。*** message:{0}".format(e.message))
        sys.exit()
    except Exception as e2:
        #検索失敗以外はそのままエラーを投げる
        raise e2

###-------------
# Excelにフォーカスを当てる
# Excelが最前面にくるまで、処理を待機する
#
def focusExcel(params):
    params.excelApp.focus()
    
    # エクセルが開ききるまで待つ
    try:
        wait(params.excelImg, 10)
    except FindFailed as e:
        # 指定時間待っても画像が取得できなかった場合、検索失敗エラーが発生する
        logger(u"エクセルfocus失敗。*** message:{0}".format(e.message))
        sys.exit()
    except Exception as e2:
        #検索失敗以外はそのままエラーを投げる
        raise e2

###-------------
# ブラウザのキャプチャを行う
#
def captureBrowser(params):

    #念のため、ブラウザにフォーカスを合わせる
    focusBrowser(params)
    
    #ブラウザだけを範囲選択し、キャプチャを行う
    #この時点ではテンポラリ等、どこに保存されるかは確実ではない
    tmpPath = SCREEN.capture(params.browserReg.getTopLeft().getX(), \
            params.browserReg.getTopLeft().getY(), \
            params.browserReg.getW(), params.browserReg.getH())

    logger(u"isinstance: {0}".format(isinstance(tmpPath, str)))
    
    if isinstance(tmpPath, basestring) == False:
        # 文字列が取得できてない場合、
        # ファイルオブジェクトである可能性があるので、ファイルパスを再取得する
        tmpPath = tmpPath.getFile()
    
    logger(u"captureTmpPath={0}".format(tmpPath))

    #キャプチャの保存先を取得する
    captureDirPath = params.tree.findtext(u'.//capture/path', None)    
    #キャプチャファイルの画像名を、日時に合わせて修正する
    capturePath = u"{0}{1}{2:%Y%m%d-%H%M%S}.png".format(captureDirPath, os.sep, datetime.datetime.now())
    logger(u"capturePath={0}".format(capturePath))

    #キャプチャファイルを移動する
    os.rename(tmpPath, capturePath)

    #キャプチャファイルフルパスを返す
    return capturePath
        

###-------------
# 処理の中断を行うか確認し、コマンドに応じて中断します
#
def confirmStop(event):
    if popAsk(u"デモスクリプトを中断しますか？") == True:
        sys.exit()


