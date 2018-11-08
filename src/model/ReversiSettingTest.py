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

obj = ReversiSettingTest()
obj.test_case1()
