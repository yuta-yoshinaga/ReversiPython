################################################################################
#	@file			ReversiSettingTest.py
#	@brief			アプリ設定テストクラス
#	@author			Yuta Yoshinaga
#	@date			2018.11.08
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

import ReversiConst
import ReversiSetting

################################################################################
#	@class		ReversiSettingTest
#	@brief		アプリ設定テストクラス
#
################################################################################


class ReversiSettingTest:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.08
    #
    ############################################################################
    def __init__(self):
        self.tgt = ReversiSetting.ReversiSetting()

    def test_case1(self):
        self.tgt.mMode = 1
        if self.tgt.mMode == 1:
            print("TEST CASE1 OK")
        else:
            print("TEST CASE1 NG")

    def test_case2(self):
        self.tgt.mType = 1
        if self.tgt.mType == 1:
            print("TEST CASE2 OK")
        else:
            print("TEST CASE2 NG")

    def test_case3(self):
        self.tgt.mPlayer = 1
        if self.tgt.mPlayer == 1:
            print("TEST CASE3 OK")
        else:
            print("TEST CASE3 NG")

    def test_case4(self):
        self.tgt.mAssist = 1
        if self.tgt.mAssist == 1:
            print("TEST CASE4 OK")
        else:
            print("TEST CASE4 NG")

    def test_case5(self):
        self.tgt.mGameSpd = 1
        if self.tgt.mGameSpd == 1:
            print("TEST CASE5 OK")
        else:
            print("TEST CASE5 NG")

    def test_case6(self):
        self.tgt.mEndAnim = 1
        if self.tgt.mEndAnim == 1:
            print("TEST CASE6 OK")
        else:
            print("TEST CASE6 NG")

    def test_case7(self):
        self.tgt.mMasuCntMenu = 1
        if self.tgt.mMasuCntMenu == 1:
            print("TEST CASE7 OK")
        else:
            print("TEST CASE7 NG")

    def test_case8(self):
        self.tgt.mMasuCnt = 1
        if self.tgt.mMasuCnt == 1:
            print("TEST CASE8 OK")
        else:
            print("TEST CASE8 NG")

    def test_case9(self):
        self.tgt.mPlayCpuInterVal = 1
        if self.tgt.mPlayCpuInterVal == 1:
            print("TEST CASE9 OK")
        else:
            print("TEST CASE9 NG")

    def test_case10(self):
        self.tgt.mPlayDrawInterVal = 1
        if self.tgt.mPlayDrawInterVal == 1:
            print("TEST CASE10 OK")
        else:
            print("TEST CASE10 NG")

    def test_case11(self):
        self.tgt.mEndDrawInterVal = 1
        if self.tgt.mEndDrawInterVal == 1:
            print("TEST CASE11 OK")
        else:
            print("TEST CASE11 NG")

    def test_case12(self):
        self.tgt.mEndInterVal = 1
        if self.tgt.mEndInterVal == 1:
            print("TEST CASE12 OK")
        else:
            print("TEST CASE12 NG")

    def test_case13(self):
        self.tgt.mPlayerColor1 = '#FFFFFF'
        if self.tgt.mPlayerColor1 == '#FFFFFF':
            print("TEST CASE13 OK")
        else:
            print("TEST CASE13 NG")

    def test_case14(self):
        self.tgt.mPlayerColor2 = '#000000'
        if self.tgt.mPlayerColor2 == '#000000':
            print("TEST CASE14 OK")
        else:
            print("TEST CASE14 NG")

    def test_case15(self):
        self.tgt.mBackGroundColor = '#FFFFFF'
        if self.tgt.mBackGroundColor == '#FFFFFF':
            print("TEST CASE15 OK")
        else:
            print("TEST CASE15 NG")

    def test_case16(self):
        self.tgt.mBorderColor = '#FFFFFF'
        if self.tgt.mBorderColor == '#FFFFFF':
            print("TEST CASE16 OK")
        else:
            print("TEST CASE16 NG")

    def test_case17(self):
        self.tgt.reset()
        self.error = False
        if self.tgt.mMode != ReversiConst.ReversiConst.DEF_MODE_ONE:
            self.error = True
        if self.tgt.mType != ReversiConst.ReversiConst.DEF_TYPE_HARD:
            self.error = True
        if self.tgt.mPlayer != ReversiConst.ReversiConst.REVERSI_STS_BLACK:
            self.error = True
        if self.tgt.mAssist != ReversiConst.ReversiConst.DEF_ASSIST_ON:
            self.error = True
        if self.tgt.mGameSpd != ReversiConst.ReversiConst.DEF_GAME_SPD_MID:
            self.error = True
        if self.tgt.mEndAnim != ReversiConst.ReversiConst.DEF_END_ANIM_ON:
            self.error = True
        if self.tgt.mMasuCntMenu != ReversiConst.ReversiConst.DEF_MASU_CNT_8:
            self.error = True
        if self.tgt.mPlayCpuInterVal != ReversiConst.ReversiConst.DEF_GAME_SPD_MID_VAL2:
            self.error = True
        if self.tgt.mPlayDrawInterVal != ReversiConst.ReversiConst.DEF_GAME_SPD_MID_VAL:
            self.error = True
        if self.tgt.mEndDrawInterVal != 100:
            self.error = True
        if self.tgt.mEndInterVal != 500:
            self.error = True
        if self.tgt.mPlayerColor1 != '#000000':
            self.error = True
        if self.tgt.mPlayerColor2 != '#FFFFFF':
            self.error = True
        if self.tgt.mBackGroundColor != '#00FF00':
            self.error = True
        if self.tgt.mBorderColor != '#000000':
            self.error = True
        if self.error == False:
            print("TEST CASE17 OK")
        else:
            print("TEST CASE17 NG")


obj = ReversiSettingTest()
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
obj.test_case11()
obj.test_case12()
obj.test_case13()
obj.test_case14()
obj.test_case15()
obj.test_case16()
obj.test_case17()
