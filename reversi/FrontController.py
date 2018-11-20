################################################################################
# 	@file			FrontController.py
# 	@brief			フロントコントローラークラス実装ファイル
# 	@author			Yuta Yoshinaga
# 	@date			2018.11.19
# 	$Version:		$
# 	$Revision:		$
#
#  (c) 2018 Yuta Yoshinaga.
#
#  - 本ソフトウェアの一部又は全てを無断で複写複製（コピー）することは、
#    著作権侵害にあたりますので、これを禁止します。
#  - 本製品の使用に起因する侵害または特許権その他権利の侵害に関しては
#    当方は一切その責任を負いません。
#
################################################################################

import logging

################################################################################
# 	@class		FrontController
# 	@brief		フロントコントローラークラス
#
################################################################################


class FrontController:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@param[in]		self
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.19
    #
    ############################################################################
    def __init__(self):
        self.__callbacks = {}
        self.__callbacks['funcs'] = {}
        self.__callbacksIdx = 0

    ############################################################################
    #	@brief			メッセージダイアログ
    #	@fn				ViewMsgDlg(self, title , msg)
    #	@param[in]		self
    #	@param[in]		title	タイトル
    #	@param[in]		msg		メッセージ
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.19
    #
    ############################################################################
    def ViewMsgDlg(self, title, msg):
        #logging.debug('ViewMsgDlg : title = ' + str(title) + ' msg = ' + str(msg))
        self.__callbacks['funcs'].update({self.__callbacksIdx:{'func':'ViewMsgDlg','param1':title,'param2':msg}})
        self.__callbacksIdx += 1

    ############################################################################
    #	@brief			1マス描画
    #	@fn				DrawSingle(self, y, x, sts, bk, text)
    #	@param[in]		self
    #	@param[in]		y		Y座標
    #	@param[in]		x		X座標
    #	@param[in]		sts		ステータス
    #	@param[in]		bk		背景
    #	@param[in]		text	テキスト
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.19
    #
    ############################################################################
    def DrawSingle(self, y, x, sts, bk, text):
        #logging.debug('DrawSingle : y = ' + str(y) + ' x = ' + str(x) + ' sts = ' + str(sts) + ' bk = ' + str(bk) + ' text = ' + str(text))
        self.__callbacks['funcs'].update({self.__callbacksIdx:{'func':'DrawSingle','param1':y,'param2':x,'param3':sts,'param4':bk,'param5':text}})
        self.__callbacksIdx += 1

    ############################################################################
    #	@brief			現在の色メッセージ
    #	@fn				CurColMsg(self, text)
    #	@param[in]		self
    #	@param[in]		text	テキスト
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.19
    #
    ############################################################################
    def CurColMsg(self, text):
        #logging.debug('CurColMsg : text = ' + str(text))
        self.__callbacks['funcs'].update({self.__callbacksIdx:{'func':'CurColMsg','param1':text}})
        self.__callbacksIdx += 1

    ############################################################################
    #	@brief			現在のステータスメッセージ
    #	@fn				CurStsMsg(self, text)
    #	@param[in]		self
    #	@param[in]		text	テキスト
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.19
    #
    ############################################################################
    def CurStsMsg(self, text):
        #logging.debug('CurStsMsg : text = ' + str(text))
        self.__callbacks['funcs'].update({self.__callbacksIdx:{'func':'CurStsMsg','param1':text}})
        self.__callbacksIdx += 1

    ############################################################################
    #	@brief			ウェイト
    #	@fn				Wait(self, time)
    #	@param[in]		self
    #	@param[in]		time	ウェイト時間(msec)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.19
    #
    ############################################################################
    def Wait(self, time):
        #logging.debug('Wait : time = ' + str(time))
        self.__callbacks['funcs'].update({self.__callbacksIdx:{'func':'Wait','param1':time}})
        self.__callbacksIdx += 1

    ############################################################################
    # 	@brief			ゲッター
    # 	@fn				getCallbacks(self)
    # 	@param[in]		self
    # 	@return			callbacks
    # 	@author			Yuta Yoshinaga
    # 	@date			2018.11.19
    #
    ############################################################################
    def getCallbacks(self):
        return self.__callbacks

    ############################################################################
    # 	@brief			セッター
    # 	@fn				setCallbacks(self,callbacks)
    # 	@param[in]		self
    # 	@param[in]		callbacks
    # 	@return			ありません
    # 	@author			Yuta Yoshinaga
    # 	@date			2018.11.19
    #
    ############################################################################
    def setCallbacks(self, callbacks):
        self.__callbacks = callbacks

    ############################################################################
    # 	@brief			ゲッター
    # 	@fn				getCallbacks(self)
    # 	@param[in]		self
    # 	@return			callbacksIdx
    # 	@author			Yuta Yoshinaga
    # 	@date			2018.11.19
    #
    ############################################################################
    def getCallbacksIdx(self):
        return self.__callbacksIdx

    ############################################################################
    # 	@brief			セッター
    # 	@fn				setCallbacksIdx(self,callbacksIdx)
    # 	@param[in]		self
    # 	@param[in]		callbacksIdx
    # 	@return			ありません
    # 	@author			Yuta Yoshinaga
    # 	@date			2018.11.19
    #
    ############################################################################
    def setCallbacksIdx(self, callbacksIdx):
        self.__callbacksIdx = callbacksIdx

    callbacks = property(getCallbacks, setCallbacks)  # !< コールバック
    callbacksIdx = property(getCallbacksIdx, setCallbacksIdx)  # !< コールバックインデックス
