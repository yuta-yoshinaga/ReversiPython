################################################################################
#	@file			ReversiPlayTest.py
#	@brief			リバーシプレイテストクラス実装ファイル
#	@author			Yuta Yoshinaga
#	@date			2018.11.13
#	$Version:		$
#	$Revision:		$
#
# (c) 2018 Yuta Yoshinaga.
#
# - 本ソフトウェアの一部又は全てを無断で複写複製（コピー）することは、
#   著作権侵害にあたりますので、これを禁止します。
# - 本製品の使用に起因する侵害または特許権その他権利の侵害に関しては
#   当方は一切その責任を負いません。
#
################################################################################

from model import ReversiPlay
from model import Reversi
from model import ReversiConst
from model import ReversiSetting

################################################################################
#	@class		ReversiPlayTest
#	@brief		リバーシプレイテストクラス
#
################################################################################


class ReversiPlayTest:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.13
    #
    ############################################################################
    def __init__(self):
        self.tgt = ReversiPlay.ReversiPlay()
        self.tgt.mDelegate = self

    ############################################################################
    #	@brief			メッセージダイアログ
    #	@fn				ViewMsgDlg(self, title , msg)
    #	@param[in]		self
    #	@param[in]		title	タイトル
    #	@param[in]		msg		メッセージ
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.13
    #
    ############################################################################
    def ViewMsgDlg(self, title, msg):
        print('ViewMsgDlg : title = ' + str(title) + ' msg = ' + str(msg))

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
    #	@date			2018.11.13
    #
    ############################################################################
    def DrawSingle(self, y, x, sts, bk, text):
        print('DrawSingle : y = ' + str(y) + ' x = ' + str(x) + ' sts = ' + str(sts) +
              ' bk = ' + str(bk) + ' text = ' + str(text))

    ############################################################################
    #	@brief			現在の色メッセージ
    #	@fn				CurColMsg(self, text)
    #	@param[in]		self
    #	@param[in]		text	テキスト
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.13
    #
    ############################################################################
    def CurColMsg(self, text):
        print('CurColMsg : text = ' + str(text))

    ############################################################################
    #	@brief			現在のステータスメッセージ
    #	@fn				CurStsMsg(self, text)
    #	@param[in]		self
    #	@param[in]		text	テキスト
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.13
    #
    ############################################################################
    def CurStsMsg(self, text):
        print('CurStsMsg : text = ' + str(text))

    ############################################################################
    #	@brief			ウェイト
    #	@fn				Wait(self, time)
    #	@param[in]		self
    #	@param[in]		time	ウェイト時間(msec)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.13
    #
    ############################################################################
    def Wait(self, time):
        print('Wait : time = ' + str(time))

    def test_case1(self):
        self.tgt.mReversi = Reversi.Reversi(
            ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL, ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL)
        if self.tgt.mReversi != None:
            print("TEST CASE1 OK")
        else:
            print("TEST CASE1 NG " + str(self.tgt.mReversi))

    def test_case2(self):
        self.tgt.mSetting = ReversiSetting.ReversiSetting()
        if self.tgt.mSetting != None:
            print("TEST CASE2 OK")
        else:
            print("TEST CASE2 NG " + str(self.tgt.mSetting))

    def test_case3(self):
        self.tgt.mCurColor = 1
        if self.tgt.mCurColor == 1:
            print("TEST CASE3 OK")
        else:
            print("TEST CASE3 NG " + str(self.tgt.mCurColor))

    def test_case4(self):
        self.tgt.mCpu = [0 for i in range(
            ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL * ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL)]
        if self.tgt.mCpu != None:
            print("TEST CASE4 OK")
        else:
            print("TEST CASE4 NG " + str(self.tgt.mCpu))

    def test_case5(self):
        self.tgt.mEdge = [0 for i in range(
            ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL * ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL)]
        if self.tgt.mEdge != None:
            print("TEST CASE5 OK")
        else:
            print("TEST CASE5 NG " + str(self.tgt.mEdge))

    def test_case6(self):
        self.tgt.mPassEnaB = 1
        if self.tgt.mPassEnaB == 1:
            print("TEST CASE6 OK")
        else:
            print("TEST CASE6 NG " + str(self.tgt.mPassEnaB))

    def test_case7(self):
        self.tgt.mPassEnaW = 1
        if self.tgt.mPassEnaW == 1:
            print("TEST CASE7 OK")
        else:
            print("TEST CASE7 NG " + str(self.tgt.mPassEnaW))

    def test_case8(self):
        self.tgt.mGameEndSts = 1
        if self.tgt.mGameEndSts == 1:
            print("TEST CASE8 OK")
        else:
            print("TEST CASE8 NG " + str(self.tgt.mGameEndSts))

    def test_case9(self):
        self.tgt.mPlayLock = 1
        if self.tgt.mPlayLock == 1:
            print("TEST CASE9 OK")
        else:
            print("TEST CASE9 NG " + str(self.tgt.mPlayLock))

    def test_case10(self):
        self.tgt.mDelegate = self
        self.tgt.ViewMsgDlgLocal('テスト', 'メッセージ')
        self.tgt.DrawSingleLocal(0, 1, 2, 3, 'テキスト')
        self.tgt.CurColMsgLocal('テキスト')
        self.tgt.CurStsMsgLocal('テキスト')
        self.tgt.WaitLocal(500)
        if self.tgt.mDelegate != None:
            print("TEST CASE10 OK")
        else:
            print("TEST CASE10 NG " + str(self.tgt.mDelegate))


obj = ReversiPlayTest()
obj.test_case1()
obj.test_case2()
obj.test_case3()
obj.test_case4()
obj.test_case5()
obj.test_case6()
obj.test_case7()
obj.test_case8()
obj.test_case9()
obj.test_case10()
