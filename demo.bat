@echo off

rem -------------------------------------------
rem --- 
rem --- GoogleMapSikuli�L���v�`���f�����s�o�b�`
rem --- 
rem -------------------------------------------

rem -- �J�����g�f�B���N�g������Ƃ���
cd /d %~dp0


rem -- ���C���Ώہ�
rem -- runsikulix.cmd �̃t���p�X
SET SIKULI_PATH=C:\Development\Sikuli\runsikulix.cmd

rem -- Main�v���O�����̑��΃p�X
SET MAIN_PATH=GoogleMapSikuliDemo\GMSDMain.sikuli

rem -- �ݒ�XML�̑��΃p�X
SET SETTING_PATH=setting.xml


ECHO ���� GoogleMapSikuli�L���v�`���f���J�n
ECHO ���� �J�n�܂ŏ������Ԃ�������܂�
ECHO ���� �f���𒆒f����ꍇ�A�uCTRL+���v�Œ��f�m�F�|�b�v�A�b�v���o�܂�

CALL %SIKULI_PATH% -r %MAIN_PATH% -- %SETTING_PATH%



pause
