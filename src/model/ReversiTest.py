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
        self.tgt = Reversi.Reversi(8,8)

    def test_case1(self):
        self.tgt.reset()
        if self.tgt.mMasuBetCntB == 2 and self.tgt.mMasuBetCntW == 2:
            print("TEST CASE1 OK")
        else:
            print("TEST CASE1 NG")



obj = ReversiTest()
obj.test_case1()
