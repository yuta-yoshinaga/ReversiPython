################################################################################
#	@file			ReversiAnzTest.py
#	@brief			リバーシ解析テストクラス実装ファイル
#	@author			Yuta Yoshinaga
#	@date			2018.11.06
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

import ReversiAnz

################################################################################
#	@class		ReversiAnzTest
#	@brief		リバーシ解析テストクラス
#
################################################################################


class ReversiAnzTest:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def __init__(self):
        self.tgt = ReversiAnz.ReversiAnz()

    def test_case1(self):
        self.tgt.min = 1
        if self.tgt.min == 1:
            print("TEST CASE1 OK")
        else:
            print("TEST CASE1 NG")

    def test_case2(self):
        self.tgt.max = 1
        if self.tgt.max == 1:
            print("TEST CASE2 OK")
        else:
            print("TEST CASE2 NG")

    def test_case3(self):
        self.tgt.avg = 1.1
        if self.tgt.avg == 1.1:
            print("TEST CASE3 OK")
        else:
            print("TEST CASE3 NG")

    def test_case4(self):
        self.tgt.pointCnt = 1
        if self.tgt.pointCnt == 1:
            print("TEST CASE4 OK")
        else:
            print("TEST CASE4 NG")

    def test_case5(self):
        self.tgt.edgeCnt = 1
        if self.tgt.edgeCnt == 1:
            print("TEST CASE5 OK")
        else:
            print("TEST CASE5 NG")

    def test_case6(self):
        self.tgt.edgeSideOneCnt = 1
        if self.tgt.edgeSideOneCnt == 1:
            print("TEST CASE6 OK")
        else:
            print("TEST CASE6 NG")

    def test_case7(self):
        self.tgt.edgeSideTwoCnt = 1
        if self.tgt.edgeSideTwoCnt == 1:
            print("TEST CASE7 OK")
        else:
            print("TEST CASE7 NG")

    def test_case8(self):
        self.tgt.edgeSideThreeCnt = 1
        if self.tgt.edgeSideThreeCnt == 1:
            print("TEST CASE8 OK")
        else:
            print("TEST CASE8 NG")

    def test_case9(self):
        self.tgt.edgeSideOtherCnt = 1
        if self.tgt.edgeSideOtherCnt == 1:
            print("TEST CASE9 OK")
        else:
            print("TEST CASE9 NG")

    def test_case10(self):
        self.tgt.ownMin = 1
        if self.tgt.ownMin == 1:
            print("TEST CASE10 OK")
        else:
            print("TEST CASE10 NG")

    def test_case11(self):
        self.tgt.ownMax = 1
        if self.tgt.ownMax == 1:
            print("TEST CASE11 OK")
        else:
            print("TEST CASE11 NG")

    def test_case12(self):
        self.tgt.ownAvg = 1.1
        if self.tgt.ownAvg == 1.1:
            print("TEST CASE12 OK")
        else:
            print("TEST CASE12 NG")

    def test_case13(self):
        self.tgt.ownPointCnt = 1
        if self.tgt.ownPointCnt == 1:
            print("TEST CASE13 OK")
        else:
            print("TEST CASE13 NG")

    def test_case14(self):
        self.tgt.ownEdgeCnt = 1
        if self.tgt.ownEdgeCnt == 1:
            print("TEST CASE14 OK")
        else:
            print("TEST CASE14 NG")

    def test_case15(self):
        self.tgt.ownEdgeSideOneCnt = 1
        if self.tgt.ownEdgeSideOneCnt == 1:
            print("TEST CASE15 OK")
        else:
            print("TEST CASE15 NG")

    def test_case16(self):
        self.tgt.ownEdgeSideTwoCnt = 1
        if self.tgt.ownEdgeSideTwoCnt == 1:
            print("TEST CASE16 OK")
        else:
            print("TEST CASE16 NG")

    def test_case17(self):
        self.tgt.ownEdgeSideThreeCnt = 1
        if self.tgt.ownEdgeSideThreeCnt == 1:
            print("TEST CASE17 OK")
        else:
            print("TEST CASE17 NG")

    def test_case18(self):
        self.tgt.ownEdgeSideOtherCnt = 1
        if self.tgt.ownEdgeSideOtherCnt == 1:
            print("TEST CASE18 OK")
        else:
            print("TEST CASE18 NG")

    def test_case19(self):
        self.tgt.badPoint = 1
        if self.tgt.badPoint == 1:
            print("TEST CASE19 OK")
        else:
            print("TEST CASE19 NG")

    def test_case20(self):
        self.tgt.goodPoint = 1
        if self.tgt.goodPoint == 1:
            print("TEST CASE20 OK")
        else:
            print("TEST CASE20 NG")

    def test_case21(self):
        self.tgt.reset()
        if self.tgt.min == 0 and self.tgt.max == 0 and self.tgt.avg == 0.0 and self.tgt.pointCnt == 0 and self.tgt.edgeCnt == 0 and self.tgt.edgeSideOneCnt == 0 and self.tgt.edgeSideTwoCnt == 0 and self.tgt.edgeSideThreeCnt == 0 and self.tgt.edgeSideOtherCnt == 0 and self.tgt.ownMin == 0 and self.tgt.ownMax == 0 and self.tgt.ownAvg == 0.0 and self.tgt.ownPointCnt == 0 and self.tgt.ownEdgeCnt == 0 and self.tgt.ownEdgeSideOneCnt == 0 and self.tgt.ownEdgeSideTwoCnt == 0 and self.tgt.ownEdgeSideThreeCnt == 0 and self.tgt.ownEdgeSideOtherCnt == 0 and self.tgt.badPoint == 0 and self.tgt.goodPoint == 0:
            print("TEST CASE21 OK")
        else:
            print("TEST CASE21 NG")


obj = ReversiAnzTest()
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
