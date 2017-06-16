@echo off

rem -------------------------------------------
rem --- 
rem --- GoogleMapSikuliキャプチャデモ実行バッチ
rem --- 
rem -------------------------------------------

rem -- カレントディレクトリを基準とする
cd /d %~dp0


rem -- ■修正対象■
rem -- runsikulix.cmd のフルパス
SET SIKULI_PATH=C:\Development\Sikuli\runsikulix.cmd

rem -- Mainプログラムの相対パス
SET MAIN_PATH=GoogleMapSikuliDemo\GMSDMain.sikuli

rem -- 設定XMLの相対パス
SET SETTING_PATH=setting.xml


ECHO ■■ GoogleMapSikuliキャプチャデモ開始
ECHO ■■ 開始まで少し時間がかかります
ECHO ■■ デモを中断する場合、「CTRL+↑」で中断確認ポップアップが出ます

CALL %SIKULI_PATH% -r %MAIN_PATH% -- %SETTING_PATH%



pause
