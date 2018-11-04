# ////////////////////////////////////////////////////////////////////////////////
# ///	@file			ReversiPointTest.java
# ///	@brief			リバーシポイントテストクラス実装ファイル
# ///	@author			Yuta Yoshinaga
# ///	@date			2018.04.01
# ///	$Version:		$
# ///	$Revision:		$
# ///
# /// (c) 2018 Yuta Yoshinaga.
# ///
# /// - 本ソフトウェアの一部又は全てを無断で複写複製（コピー）することは、
# ///   著作権侵害にあたりますので、これを禁止します。
# /// - 本製品の使用に起因する侵害または特許権その他権利の侵害に関しては
# ///   当方は一切その責任を負いません。
# ///
# ////////////////////////////////////////////////////////////////////////////////

import ReversiPoint

# ////////////////////////////////////////////////////////////////////////////////
# ///	@class		ReversiPointTest
# ///	@brief		リバーシポイントテストクラス
# ///
# ////////////////////////////////////////////////////////////////////////////////
class ReversiPointTest:

	# ////////////////////////////////////////////////////////////////////////////////
	# ///	@brief			コンストラクタ
	# ///	@fn				__init__(self)
	# ///	@return			ありません
	# ///	@author			Yuta Yoshinaga
	# ///	@date			2018.04.01
	# ///
	# ////////////////////////////////////////////////////////////////////////////////
	def __init__(self):
		self.tgt = ReversiPoint.ReversiPoint()

	def test_case1(self):
		self.tgt.x = 1
		if self.tgt.x == 1:
			print("TEST CASE1 OK")
		else:
			print("TEST CASE1 NG")

	def test_case2(self):
		self.tgt.y = 1
		if self.tgt.y == 1:
			print("TEST CASE2 OK")
		else:
			print("TEST CASE2 NG")

obj = ReversiPointTest()
obj.test_case1()
obj.test_case2()
