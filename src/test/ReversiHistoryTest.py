################################################################################
#	@file			ReversiHistoryTest.py
#	@brief			リバーシ履歴テストクラス実装ファイル
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

from model import ReversiHistory

################################################################################
#	@class		ReversiHistoryTest
#	@brief		リバーシ履歴テストクラス
#
################################################################################


class ReversiHistoryTest:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def __init__(self):
        self.tgt = ReversiHistory.ReversiHistory()

    def test_case1(self):
        self.tgt.color = 1
        if self.tgt.color == 1:
            print("TEST CASE1 OK")
        else:
            print("TEST CASE1 NG " + str(self.tgt.color))

    def test_case2(self):
        self.tgt.point.x = 1
        self.tgt.point.y = 2
        if self.tgt.point.x == 1 and self.tgt.point.y == 2:
            print("TEST CASE2 OK")
        else:
            print("TEST CASE2 NG " + str(self.tgt.point.x) +
                  " " + str(self.tgt.point.y))

    def test_case3(self):
        self.tgt.reset()
        if self.tgt.color == -1 and self.tgt.point.x == -1 and self.tgt.point.y == -1:
            print("TEST CASE3 OK")
        else:
            print("TEST CASE3 NG " + str(self.tgt.color) + " " +
                  str(self.tgt.point.x) + " " + str(self.tgt.point.y))


obj = ReversiHistoryTest()
obj.test_case1()
obj.test_case2()
obj.test_case3()
