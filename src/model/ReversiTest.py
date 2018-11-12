################################################################################
#	@file			ReversiTest.py
#	@brief			リバーシテストクラス実装ファイル
#	@author			Yuta Yoshinaga
#	@date			2018.11.12
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

import Reversi
import ReversiConst

################################################################################
#	@class		ReversiTest
#	@brief		リバーシテストクラス
#
################################################################################


class ReversiTest:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.12
    #
    ############################################################################
    def __init__(self):
        self.tgt = Reversi.Reversi(8, 8)

    def test_case1(self):
        self.tgt.mMasuSts = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuSts != None:
            print("TEST CASE1 OK")
        else:
            print("TEST CASE1 NG " + str(self.tgt.mMasuSts))

    def test_case2(self):
        self.tgt.mMasuStsOld = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsOld != None:
            print("TEST CASE2 OK")
        else:
            print("TEST CASE2 NG " + str(self.tgt.mMasuStsOld))

    def test_case3(self):
        self.tgt.mMasuStsEnaB = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsEnaB != None:
            print("TEST CASE3 OK")
        else:
            print("TEST CASE3 NG " + str(self.tgt.mMasuStsEnaB))

    def test_case4(self):
        self.tgt.mMasuStsCntB = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsCntB != None:
            print("TEST CASE4 OK")
        else:
            print("TEST CASE4 NG " + str(self.tgt.mMasuStsCntB))

    def test_case5(self):
        self.tgt.mMasuStsPassB = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsPassB != None:
            print("TEST CASE5 OK")
        else:
            print("TEST CASE5 NG " + str(self.tgt.mMasuStsPassB))

    def test_case6(self):
        self.tgt.mMasuStsAnzB = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsAnzB != None:
            print("TEST CASE6 OK")
        else:
            print("TEST CASE6 NG " + str(self.tgt.mMasuStsAnzB))

    def test_case7(self):
        self.tgt.mMasuPointB = [0 for i in range(8 * 8)]
        if self.tgt.mMasuPointB != None:
            print("TEST CASE7 OK")
        else:
            print("TEST CASE7 NG " + str(self.tgt.mMasuPointB))

    def test_case8(self):
        self.tgt.mMasuPointCntB = 1
        if self.tgt.mMasuPointCntB == 1:
            print("TEST CASE8 OK")
        else:
            print("TEST CASE8 NG " + str(self.tgt.mMasuPointCntB))

    def test_case9(self):
        self.tgt.mMasuBetCntB = 1
        if self.tgt.mMasuBetCntB == 1:
            print("TEST CASE9 OK")
        else:
            print("TEST CASE9 NG " + str(self.tgt.mMasuBetCntB))

    def test_case10(self):
        self.tgt.mMasuStsEnaW = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsEnaW != None:
            print("TEST CASE10 OK")
        else:
            print("TEST CASE10 NG " + str(self.tgt.mMasuStsEnaW))

    def test_case11(self):
        self.tgt.mMasuStsCntW = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsCntW != None:
            print("TEST CASE11 OK")
        else:
            print("TEST CASE11 NG " + str(self.tgt.mMasuStsCntW))

    def test_case12(self):
        self.tgt.mMasuStsPassW = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsPassW != None:
            print("TEST CASE12 OK")
        else:
            print("TEST CASE12 NG " + str(self.tgt.mMasuStsPassW))

    def test_case13(self):
        self.tgt.mMasuStsAnzW = [[0 for i in range(8)] for j in range(8)]
        if self.tgt.mMasuStsAnzW != None:
            print("TEST CASE13 OK")
        else:
            print("TEST CASE13 NG " + str(self.tgt.mMasuStsAnzW))

    def test_case14(self):
        self.tgt.mMasuPointW = [0 for i in range(8 * 8)]
        if self.tgt.mMasuPointW != None:
            print("TEST CASE14 OK")
        else:
            print("TEST CASE14 NG " + str(self.tgt.mMasuPointW))

    def test_case15(self):
        self.tgt.mMasuPointCntW = 1
        if self.tgt.mMasuPointCntW == 1:
            print("TEST CASE15 OK")
        else:
            print("TEST CASE15 NG " + str(self.tgt.mMasuPointCntW))

    def test_case16(self):
        self.tgt.mMasuBetCntW = 1
        if self.tgt.mMasuBetCntW == 1:
            print("TEST CASE16 OK")
        else:
            print("TEST CASE16 NG " + str(self.tgt.mMasuBetCntW))

    def test_case17(self):
        self.tgt.mMasuCnt = 1
        if self.tgt.mMasuCnt == 1:
            print("TEST CASE17 OK")
        else:
            print("TEST CASE17 NG " + str(self.tgt.mMasuCnt))

    def test_case18(self):
        self.tgt.mMasuCntMax = 1
        if self.tgt.mMasuCntMax == 1:
            print("TEST CASE18 OK")
        else:
            print("TEST CASE18 NG " + str(self.tgt.mMasuCntMax))

    def test_case19(self):
        self.tgt.mMasuHist = [0 for i in range(8 * 8)]
        if self.tgt.mMasuHist != None:
            print("TEST CASE19 OK")
        else:
            print("TEST CASE19 NG " + str(self.tgt.mMasuHist))

    def test_case20(self):
        self.tgt.mMasuHistCur = 1
        if self.tgt.mMasuHistCur == 1:
            print("TEST CASE20 OK")
        else:
            print("TEST CASE20 NG " + str(self.tgt.mMasuHistCur))

    def test_case21(self):
        self.tgt = Reversi.Reversi(8, 8)
        self.tgt.reset()
        if self.tgt.mMasuBetCntB == 2 and self.tgt.mMasuBetCntW == 2:
            print("TEST CASE21 OK")
        else:
            print("TEST CASE21 NG " + str(self.tgt.mMasuBetCntB))

    def test_case22(self):
        self.tgt.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
        self.tgt.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE)
        print("TEST CASE22 OK")

    def test_case23(self):
        self.tgt.revMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK, 0, 0)
        self.tgt.revMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE, 0, 0)
        print("TEST CASE23 OK")

    def test_case24(self):
        ret = self.tgt.checkPara(0, 0, 1)
        if ret == 0:
            print("TEST CASE24 OK")
        else:
            print("TEST CASE24 NG " + str(ret))

    def test_case25(self):
        self.tgt.AnalysisReversiBlack()
        print("TEST CASE25 OK")

    def test_case26(self):
        self.tgt.AnalysisReversiWhite()
        print("TEST CASE26 OK")

    def test_case27(self):
        self.tgt.AnalysisReversi(1, 1)
        print("TEST CASE27 OK")

    def test_case28(self):
        ret = self.tgt.getMasuSts(3, 3)
        if ret == ReversiConst.ReversiConst.REVERSI_STS_BLACK:
            print("TEST CASE28 OK")
        else:
            print("TEST CASE28 NG " + str(ret))

    def test_case29(self):
        ret = self.tgt.getMasuStsOld(3, 3)
        if ret == ReversiConst.ReversiConst.REVERSI_STS_BLACK:
            print("TEST CASE29 OK")
        else:
            print("TEST CASE29 NG " + str(ret))

    def test_case30(self):
        ret = self.tgt.getMasuStsEna(
            ReversiConst.ReversiConst.REVERSI_STS_BLACK, 2, 4)
        if ret != 0:
            print("TEST CASE30 OK")
        else:
            print("TEST CASE30 NG " + str(ret))

    def test_case31(self):
        ret = self.tgt.setMasuStsForcibly(
            ReversiConst.ReversiConst.REVERSI_STS_BLACK, 2, 4)
        if ret == 0:
            print("TEST CASE31 OK")
        else:
            print("TEST CASE31 NG " + str(ret))

    def test_case32(self):
        ret = self.tgt.setMasuCnt(6)
        if ret == 0:
            print("TEST CASE32 OK")
        else:
            print("TEST CASE32 NG " + str(ret))
        ret = self.tgt.setMasuCnt(8)

    def test_case33(self):
        ret = self.tgt.getPoint(ReversiConst.ReversiConst.REVERSI_STS_BLACK, 0)
        if ret != None:
            print("TEST CASE33 OK")
        else:
            print("TEST CASE33 NG " + str(ret))

    def test_case34(self):
        ret = self.tgt.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
        if ret == 4:
            print("TEST CASE34 OK")
        else:
            print("TEST CASE34 NG " + str(ret))

    def test_case35(self):
        ret = self.tgt.getBetCnt(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
        if ret == 2:
            print("TEST CASE35 OK")
        else:
            print("TEST CASE35 NG " + str(ret))

    def test_case36(self):
        ret = self.tgt.getPassEna(ReversiConst.ReversiConst.REVERSI_STS_BLACK,2,4)
        if ret == 0:
            print("TEST CASE36 OK")
        else:
            print("TEST CASE36 NG " + str(ret))

    def test_case37(self):
        ret = self.tgt.getHistory(0)
        if ret != None:
            print("TEST CASE37 OK")
        else:
            print("TEST CASE37 NG " + str(ret))

    def test_case38(self):
        ret = self.tgt.getHistoryCnt()
        if ret == 0:
            print("TEST CASE38 OK")
        else:
            print("TEST CASE38 NG " + str(ret))

    def test_case39(self):
        ret = self.tgt.getPointAnz(ReversiConst.ReversiConst.REVERSI_STS_BLACK,2,4)
        if ret != None:
            print("TEST CASE39 OK")
        else:
            print("TEST CASE39 NG " + str(ret))

    def test_case40(self):
        ret = self.tgt.checkEdge(ReversiConst.ReversiConst.REVERSI_STS_BLACK,2,4)
        if ret == 0:
            print("TEST CASE40 OK")
        else:
            print("TEST CASE40 NG " + str(ret))

    def test_case41(self):
        ret = self.tgt.getEdgeSideZero(0,0)
        if ret == 0:
            print("TEST CASE41 OK")
        else:
            print("TEST CASE41 NG " + str(ret))

    def test_case42(self):
        ret = self.tgt.getEdgeSideOne(0,1)
        if ret == 0:
            print("TEST CASE42 OK")
        else:
            print("TEST CASE42 NG " + str(ret))

    def test_case43(self):
        ret = self.tgt.getEdgeSideTwo(0,2)
        if ret == 0:
            print("TEST CASE43 OK")
        else:
            print("TEST CASE43 NG " + str(ret))

    def test_case44(self):
        ret = self.tgt.getEdgeSideThree(0,3)
        if ret == 0:
            print("TEST CASE44 OK")
        else:
            print("TEST CASE44 NG " + str(ret))

obj = ReversiTest()
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
obj.test_case18()
obj.test_case19()
obj.test_case20()
obj.test_case21()
obj.test_case22()
obj.test_case23()
obj.test_case24()
obj.test_case25()
obj.test_case26()
obj.test_case27()
obj.test_case28()
obj.test_case29()
obj.test_case30()
obj.test_case31()
obj.test_case32()
obj.test_case33()
obj.test_case34()
obj.test_case35()
obj.test_case36()
obj.test_case37()
obj.test_case38()
obj.test_case39()
obj.test_case40()
obj.test_case41()
obj.test_case42()
obj.test_case43()
obj.test_case44()
