################################################################################
#	@file			Reversi.py
#	@brief			リバーシクラス実装ファイル
#	@author			Yuta Yoshinaga
#	@date			2018.11.11
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

import copy
from . import ReversiAnz
from . import ReversiPoint
from . import ReversiHistory
from . import ReversiConst

################################################################################
#	@class		Reversi
#	@brief		リバーシクラス
#
################################################################################


class Reversi:

	############################################################################
	#	@brief			コンストラクタ
	#	@fn				__init__(self,masuCnt,masuMax)
	#	@param[in]		self
	#	@param[in]		masuCnt		縦横マス数
	#	@param[in]		masuMax		縦横マス最大数
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def __init__(self, masuCnt, masuMax):
		self.__mMasuCnt = masuCnt
		self.__mMasuCntMax = masuMax
		self.__mMasuSts = [[0 for i in range(self.__mMasuCntMax)]
		                                     for j in range(self.__mMasuCntMax)]
		self.__mMasuStsOld = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
		self.__mMasuStsEnaB = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
		self.__mMasuStsCntB = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
		self.__mMasuStsPassB = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
		self.__mMasuStsAnzB = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]

		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				self.__mMasuStsAnzB[i][j] = ReversiAnz.ReversiAnz()

		self.__mMasuPointB = [0 for i in range(
		    self.__mMasuCntMax * self.__mMasuCntMax)]
		for i in range(self.__mMasuCntMax * self.__mMasuCntMax):
			self.__mMasuPointB[i] = ReversiPoint.ReversiPoint()

		self.__mMasuPointCntB = 0
		self.__mMasuStsEnaW = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
		self.__mMasuStsCntW = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
		self.__mMasuStsPassW = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
		self.__mMasuStsAnzW = [
		    [0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				self.mMasuStsAnzW[i][j] = ReversiAnz.ReversiAnz()

		self.__mMasuPointW = [0 for i in range(
		    self.__mMasuCntMax * self.__mMasuCntMax)]
		for i in range(self.__mMasuCntMax * self.__mMasuCntMax):
			self.mMasuPointW[i] = ReversiPoint.ReversiPoint()

		self.__mMasuPointCntW = 0
		self.__mMasuBetCntB = 0
		self.__mMasuBetCntW = 0
		self.__mMasuHist = [0 for i in range(
		    self.__mMasuCntMax * self.__mMasuCntMax)]
		for i in range(self.__mMasuCntMax * self.__mMasuCntMax):
			self.__mMasuHist[i] = ReversiHistory.ReversiHistory()

		self.__mMasuHistCur = 0
		for i in range(self.__mMasuCntMax):
			self.__mMasuStsOld[i] = copy.deepcopy(self.__mMasuSts[i])

		self.reset()

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuSts(self)
	#	@param[in]		self
	#	@return			mMasuSts[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuSts(self):
		return self.__mMasuSts

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuSts(self, mMasuSts)
	#	@param[in]		self
	#	@param[in]		mMasuSts
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuSts(self, mMasuSts):
		self.__mMasuSts = mMasuSts

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsOld(self)
	#	@param[in]		self
	#	@return			mMasuStsOld[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsOld(self):
		return self.__mMasuStsOld

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsOld(self, mMasuStsOld)
	#	@param[in]		self
	#	@param[in]		mMasuStsOld
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsOld(self, mMasuStsOld):
		self.__mMasuStsOld = mMasuStsOld

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsEnaB(self)
	#	@param[in]		self
	#	@return			mMasuStsEnaB[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsEnaB(self):
		return self.__mMasuStsEnaB

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsEnaB(self, mMasuStsEnaB)
	#	@param[in]		self
	#	@param[in]		mMasuStsEnaB
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsEnaB(self, mMasuStsEnaB):
		self.__mMasuStsEnaB = mMasuStsEnaB

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsCntB(self)
	#	@param[in]		self
	#	@return			mMasuStsCntB[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsCntB(self):
		return self.__mMasuStsCntB

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsCntB(self, mMasuStsCntB)
	#	@param[in]		self
	#	@param[in]		mMasuStsCntB
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsCntB(self, mMasuStsCntB):
		self.__mMasuStsCntB = mMasuStsCntB

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsPassB(self)
	#	@param[in]		self
	#	@return			mMasuStsPassB[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsPassB(self):
		return self.__mMasuStsPassB

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsPassB(self, mMasuStsPassB)
	#	@param[in]		self
	#	@param[in]		mMasuStsPassB
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsPassB(self, mMasuStsPassB):
		self.__mMasuStsPassB = mMasuStsPassB

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsAnzB(self)
	#	@param[in]		self
	#	@return			mMasuStsAnzB[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsAnzB(self):
		return self.__mMasuStsAnzB

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsAnzB(self, mMasuStsAnzB)
	#	@param[in]		self
	#	@param[in]		mMasuStsAnzB
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsAnzB(self, mMasuStsAnzB):
		self.__mMasuStsAnzB = mMasuStsAnzB

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuPointB(self)
	#	@param[in]		self
	#	@return			mMasuPointB[]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuPointB(self):
		return self.__mMasuPointB

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuPointB(self, mMasuPointB)
	#	@param[in]		self
	#	@param[in]		mMasuPointB
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuPointB(self, mMasuPointB):
		self.__mMasuPointB = mMasuPointB

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuPointCntB(self)
	#	@param[in]		self
	#	@return			mMasuPointCntB
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuPointCntB(self):
		return self.__mMasuPointCntB

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuPointCntB(self, mMasuPointCntB)
	#	@param[in]		self
	#	@param[in]		mMasuPointCntB
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuPointCntB(self, mMasuPointCntB):
		self.__mMasuPointCntB = mMasuPointCntB

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuBetCntB(self)
	#	@param[in]		self
	#	@return			mMasuBetCntB
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuBetCntB(self):
		return self.__mMasuBetCntB

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuBetCntB(self, mMasuBetCntB)
	#	@param[in]		self
	#	@param[in]		mMasuBetCntB
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuBetCntB(self, mMasuBetCntB):
		self.__mMasuBetCntB = mMasuBetCntB

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsEnaW()
	#	@param[in]		self
	#	@return			mMasuStsEnaW[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsEnaW(self):
		return self.__mMasuStsEnaW

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsEnaW(self, mMasuStsEnaW)
	#	@param[in]		self
	#	@param[in]		mMasuStsEnaW
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsEnaW(self, mMasuStsEnaW):
		self.__mMasuStsEnaW = mMasuStsEnaW

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsCntW(self)
	#	@param[in]		self
	#	@return			mMasuStsCntW[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsCntW(self):
		return self.__mMasuStsCntW

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsCntW(self, mMasuStsCntW)
	#	@param[in]		self
	#	@param[in]		mMasuStsCntW
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsCntW(self, mMasuStsCntW):
		self.__mMasuStsCntW = mMasuStsCntW

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsPassW(self)
	#	@param[in]		self
	#	@return			mMasuStsPassW[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsPassW(self):
		return self.__mMasuStsPassW

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsPassW(self, mMasuStsPassW)
	#	@param[in]		self
	#	@param[in]		mMasuStsPassW
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsPassW(self, mMasuStsPassW):
		self.__mMasuStsPassW = mMasuStsPassW

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuStsAnzW(self)
	#	@param[in]		self
	#	@return			mMasuStsAnzW[][]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuStsAnzW(self):
		return self.__mMasuStsAnzW

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuStsAnzW(self, mMasuStsAnzW)
	#	@param[in]		self
	#	@param[in]		mMasuStsAnzW
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuStsAnzW(self, mMasuStsAnzW):
		self.__mMasuStsAnzW = mMasuStsAnzW

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuPointW(self)
	#	@param[in]		self
	#	@return			mMasuPointW[]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuPointW(self):
		return self.__mMasuPointW

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuPointW(self, mMasuPointW)
	#	@param[in]		self
	#	@param[in]		mMasuPointW
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuPointW(self, mMasuPointW):
		self.__mMasuPointW = mMasuPointW

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuPointCntW(self)
	#	@param[in]		self
	#	@return			mMasuPointCntW
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuPointCntW(self):
		return self.__mMasuPointCntW

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuPointCntW(self, mMasuPointCntW)
	#	@param[in]		self
	#	@param[in]		mMasuPointCntW
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuPointCntW(self, mMasuPointCntW):
		self.__mMasuPointCntW = mMasuPointCntW

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuBetCntW(self)
	#	@param[in]		self
	#	@return			mMasuBetCntW
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuBetCntW(self):
		return self.__mMasuBetCntW

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuBetCntW(self, mMasuBetCntW)
	#	@param[in]		self
	#	@param[in]		mMasuBetCntW
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuBetCntW(self, mMasuBetCntW):
		self.__mMasuBetCntW = mMasuBetCntW

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuCnt(self)
	#	@param[in]		self
	#	@return			mMasuCnt
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuCnt(self):
		return self.__mMasuCnt

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuCnt(self, mMasuCnt)
	#	@param[in]		self
	#	@param[in]		mMasuCnt
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuCnt(self, mMasuCnt):
		self.__mMasuCnt = mMasuCnt

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuCntMax(self)
	#	@param[in]		self
	#	@return			mMasuCntMax
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuCntMax(self):
		return self.__mMasuCntMax

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuCntMax(self, mMasuCntMax)
	#	@param[in]		self
	#	@param[in]		mMasuCntMax
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuCntMax(self, mMasuCntMax):
		self.__mMasuCntMax = mMasuCntMax

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuHist(self)
	#	@param[in]		self
	#	@return			mMasuHist[]
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuHist(self):
		return self.__mMasuHist

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuHist(self, mMasuHist)
	#	@param[in]		self
	#	@param[in]		mMasuHist
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuHist(self, mMasuHist):
		self.__mMasuHist = mMasuHist

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmMasuHistCur(self)
	#	@param[in]		self
	#	@return			mMasuHistCur
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getmMasuHistCur(self):
		return self.__mMasuHistCur

	############################################################################
	#	@brief			セッター
	#	@fn				setmMasuHistCur(self, mMasuHistCur)
	#	@param[in]		self
	#	@param[in]		mMasuHistCur
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setmMasuHistCur(self, mMasuHistCur):
		self.__mMasuHistCur = mMasuHistCur

	############################################################################
	#	@brief			リセット
	#	@fn				reset(self)
	#	@param[in]		self
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def reset(self):
		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				self.__mMasuSts[i][j] = ReversiConst.ReversiConst.REVERSI_STS_NONE
				self.__mMasuStsPassB[i][j] = 0
				self.__mMasuStsAnzB[i][j].reset()
				self.__mMasuStsPassW[i][j] = 0
				self.__mMasuStsAnzW[i][j].reset()

		self.__mMasuSts[(self.__mMasuCnt >> 1) - 1][(self.__mMasuCnt >> 1) - 1] = ReversiConst.ReversiConst.REVERSI_STS_BLACK
		self.__mMasuSts[(self.__mMasuCnt >> 1) - 1][(self.__mMasuCnt >> 1)] = ReversiConst.ReversiConst.REVERSI_STS_WHITE
		self.__mMasuSts[(self.__mMasuCnt >> 1)][(self.__mMasuCnt >> 1) - 1] = ReversiConst.ReversiConst.REVERSI_STS_WHITE
		self.__mMasuSts[(self.__mMasuCnt >> 1)][(self.__mMasuCnt >> 1)] = ReversiConst.ReversiConst.REVERSI_STS_BLACK
		self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
		self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE)
		self.__mMasuHistCur = 0
		for i in range(self.__mMasuCntMax):
			self.__mMasuStsOld[i] = copy.deepcopy(self.__mMasuSts[i])

	############################################################################
	#	@brief			各コマの置ける場所等のステータス作成
	#	@fn				makeMasuSts(self color)
	#	@param[in]		self
	#	@param[in]		color		ステータスを作成するコマ
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def makeMasuSts(self, color):
		flg = 0
		okflg = 0
		cnt1 = 0
		cnt2 = 0
		count1 = 0
		count2 = 0
		ret = -1
		countMax = 0
		loop = 0

		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK) :
					self.__mMasuStsEnaB[i][j] = 0
					self.__mMasuStsCntB[i][j] = 0
				else:
					self.__mMasuStsEnaW[i][j] = 0
					self.__mMasuStsCntW[i][j] = 0

		loop = self.__mMasuCnt * self.__mMasuCnt
		for i in range(loop):
			if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK) :
				self.__mMasuPointB[i].setX(0)
				self.__mMasuPointB[i].setY(0)
			else:
				self.__mMasuPointW[i].setX(0)
				self.__mMasuPointW[i].setY(0)

		if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK) :
			self.__mMasuPointCntB = 0
		else:
			self.__mMasuPointCntW = 0

		self.__mMasuBetCntB = 0
		self.__mMasuBetCntW = 0

		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				okflg = 0
				count2 = 0
				if (self.__mMasuSts[i][j] == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					# 何も置かれていないマスなら
					cnt1 = i
					count1 = flg = 0
					# *** 上方向を調べる ***
					while ((cnt1 > 0) and (self.__mMasuSts[cnt1-1][j] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt1-1][j] != color)) :
						flg = 1
						cnt1 -= 1
						count1 += 1

					if ( (cnt1 > 0) and (flg == 1) and (self.__mMasuSts[cnt1-1][j] == color) ) :
						okflg = 1
						count2 += count1
					cnt1 = i
					count1 = flg = 0
					# *** 下方向を調べる ***
					while ((cnt1 < (self.__mMasuCnt-1)) and (self.__mMasuSts[cnt1+1][j] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt1+1][j] != color)) :
						flg = 1
						cnt1 += 1
						count1 += 1
					if ( (cnt1 < (self.__mMasuCnt-1)) and (flg == 1) and (self.__mMasuSts[cnt1+1][j] == color) ) :
						okflg = 1
						count2 += count1
					cnt2 = j
					count1 = flg = 0
					# *** 右方向を調べる ***
					while((cnt2 < (self.__mMasuCnt-1)) and (self.__mMasuSts[i][cnt2+1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[i][cnt2+1] != color)) :
						flg = 1
						cnt2 += 1
						count1 += 1
					if( (cnt2 < (self.__mMasuCnt-1)) and (flg == 1) and (self.__mMasuSts[i][cnt2+1] == color) ) :
						okflg = 1
						count2 += count1
					cnt2 = j
					count1 = flg = 0
					# *** 左方向を調べる ***
					while ((cnt2 > 0) and (self.__mMasuSts[i][cnt2-1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[i][cnt2-1] != color)) :
						flg = 1
						cnt2 -= 1
						count1 += 1
					if ( (cnt2 > 0) and (flg == 1) and (self.__mMasuSts[i][cnt2-1] == color) ) :
						okflg = 1
						count2 += count1
					cnt2 = j
					cnt1 = i
					count1 = flg = 0
					# *** 右上方向を調べる ***
					while (((cnt2 < (self.__mMasuCnt-1)) and (cnt1 > 0)) and (self.__mMasuSts[cnt1-1][cnt2+1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt1-1][cnt2+1] != color)) :
						flg = 1
						cnt1 -= 1
						cnt2 += 1
						count1 += 1
					if (((cnt2 < (self.__mMasuCnt-1)) and (cnt1 > 0)) and (flg == 1) and (self.__mMasuSts[cnt1-1][cnt2+1] == color)) :
						okflg = 1
						count2 += count1
					cnt2 = j
					cnt1 = i
					count1 = flg = 0
					# *** 左上方向を調べる ***
					while (((cnt2 > 0) and (cnt1 > 0)) and (self.__mMasuSts[cnt1-1][cnt2-1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt1-1][cnt2-1] != color)) :
						flg = 1
						cnt1 -= 1
						cnt2 -= 1
						count1 += 1
					if (((cnt2 > 0) and (cnt1 > 0)) and (flg == 1) and (self.__mMasuSts[cnt1-1][cnt2-1] == color)) :
						okflg = 1
						count2 += count1
					cnt2 = j
					cnt1 = i
					count1 = flg = 0
					# *** 右下方向を調べる ***
					while (((cnt2 < (self.__mMasuCnt-1)) and (cnt1 < (self.__mMasuCnt-1))) and (self.__mMasuSts[cnt1+1][cnt2+1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt1+1][cnt2+1] != color)) :
						flg = 1
						cnt1 += 1
						cnt2 += 1
						count1 += 1
					if(((cnt2 < (self.__mMasuCnt-1)) and (cnt1 < (self.__mMasuCnt-1))) and (flg == 1) and (self.__mMasuSts[cnt1+1][cnt2+1] == color)) :
						okflg = 1
						count2 += count1
					cnt2 = j
					cnt1 = i
					count1 = flg = 0
					# *** 左下方向を調べる ***
					while (((cnt2 > 0) and (cnt1 < (self.__mMasuCnt-1))) and (self.__mMasuSts[cnt1+1][cnt2-1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt1+1][cnt2-1] != color)) :
						flg = 1
						cnt1 += 1
						cnt2 -= 1
						count1 += 1
					if (((cnt2 > 0) and (cnt1 < (self.__mMasuCnt-1))) and (flg == 1) and (self.__mMasuSts[cnt1+1][cnt2-1] == color)) :
						okflg = 1
						count2 += count1
					if (okflg == 1) :
						if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK) :
							self.__mMasuStsEnaB[i][j] = 1
							self.__mMasuStsCntB[i][j] = count2
							# *** 置ける場所をリニアに保存、置けるポイント数も保存 ***
							self.__mMasuPointB[self.__mMasuPointCntB].setY(i)
							self.__mMasuPointB[self.__mMasuPointCntB].setX(j)
							self.__mMasuPointCntB += 1
						else:
							self.__mMasuStsEnaW[i][j] = 1
							self.__mMasuStsCntW[i][j] = count2
							# *** 置ける場所をリニアに保存、置けるポイント数も保存 ***
							self.__mMasuPointW[self.__mMasuPointCntW].setY(i)
							self.__mMasuPointW[self.__mMasuPointCntW].setX(j)
							self.__mMasuPointCntW += 1
						ret = 0
						if(countMax < count2):
							countMax = count2
				elif(self.__mMasuSts[i][j] == ReversiConst.ReversiConst.REVERSI_STS_BLACK) :
					self.__mMasuBetCntB += 1
				elif(self.__mMasuSts[i][j] == ReversiConst.ReversiConst.REVERSI_STS_WHITE) :
					self.__mMasuBetCntW += 1

		# *** 一番枚数を獲得できるマスを設定 ***
		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK) :
					if(self.__mMasuStsEnaB[i][j] != 0 and self.__mMasuStsCntB[i][j] == countMax) :
						self.__mMasuStsEnaB[i][j] = 2
				else:
					if(self.__mMasuStsEnaW[i][j] != 0 and self.__mMasuStsCntW[i][j] == countMax) :
						self.__mMasuStsEnaW[i][j] = 2
		return ret

	############################################################################
	#	@brief			コマをひっくり返す
	#	@fn				revMasuSts(self, color, y, x)
	#	@param[in]		self
	#	@param[in]		color		ひっくり返す元コマ
	#	@param[in]		y			ひっくり返す元コマのY座標
	#	@param[in]		x			ひっくり返す元コマのX座標
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def revMasuSts(self, color, y, x):
		cnt1 = 0
		cnt2 = 0
		rcnt1 = 0
		rcnt2 = 0
		flg = 0

		# *** 左方向にある駒を調べる ***
		flg = 0
		cnt1 = x
		cnt2 = y
		while (cnt1 > 0) :
			if(self.__mMasuSts[cnt2][cnt1-1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt2][cnt1-1] != color) :
				# *** プレイヤー以外の色の駒があるなら ***
				cnt1 -= 1
			elif(self.__mMasuSts[cnt2][cnt1-1] == color) :
				flg = 1
				break
			elif(self.__mMasuSts[cnt2][cnt1-1] == ReversiConst.ReversiConst.REVERSI_STS_NONE) :
				break

		if (flg == 1) :
			# *** 駒をひっくり返す ***
			rcnt1 = cnt1
			while (rcnt1 < x) :
				self.__mMasuSts[cnt2][rcnt1] = color
				rcnt1 += 1

		# *** 右方向にある駒を調べる ***
		flg = 0
		cnt1 = x
		cnt2 = y
		while (cnt1 < (self.__mMasuCnt-1)) :
			if(self.__mMasuSts[cnt2][cnt1+1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt2][cnt1+1] != color):
				# *** プレイヤー以外の色の駒があるなら ***
				cnt1 += 1
			elif(self.__mMasuSts[cnt2][cnt1+1] == color) :
				flg = 1
				break
			elif(self.__mMasuSts[cnt2][cnt1+1] == ReversiConst.ReversiConst.REVERSI_STS_NONE) :
				break

		if (flg == 1) :
			# *** 駒をひっくり返す ***
			rcnt1 = cnt1
			while(rcnt1 > x) :
				self.__mMasuSts[cnt2][rcnt1] = color
				rcnt1 -= 1

		# *** 上方向にある駒を調べる ***
		flg = 0
		cnt1 = x
		cnt2 = y
		while (cnt2 > 0) :
			if (self.__mMasuSts[cnt2-1][cnt1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt2-1][cnt1] != color) :
				# *** プレイヤー以外の色の駒があるなら ***
				cnt2 -= 1
			elif(self.__mMasuSts[cnt2-1][cnt1] == color) :
				flg = 1
				break
			elif(self.__mMasuSts[cnt2-1][cnt1] == ReversiConst.ReversiConst.REVERSI_STS_NONE) :
				break

		if (flg == 1) :
			# *** 駒をひっくり返す ***
			rcnt1 = cnt2
			while (rcnt1 < y) :
				self.__mMasuSts[rcnt1][cnt1] = color
				rcnt1 += 1

		# *** 下方向にある駒を調べる ***
		flg = 0
		cnt1 = x
		cnt2 = y
		while (cnt2 < (self.__mMasuCnt-1)) :
			if(self.__mMasuSts[cnt2+1][cnt1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt2+1][cnt1] != color) :
				# *** プレイヤー以外の色の駒があるなら ***
				cnt2 += 1
			elif(self.__mMasuSts[cnt2+1][cnt1] == color) :
				flg = 1
				break
			elif(self.__mMasuSts[cnt2+1][cnt1] == ReversiConst.ReversiConst.REVERSI_STS_NONE) :
				break

		if (flg == 1) :
			# *** 駒をひっくり返す ***
			rcnt1 = cnt2
			while (rcnt1 > y) :
				self.__mMasuSts[rcnt1][cnt1] = color
				rcnt1 -= 1

		# *** 左上方向にある駒を調べる ***
		flg = 0
		cnt1 = x
		cnt2 = y
		while (cnt2 > 0 and cnt1 > 0) :
			if (self.__mMasuSts[cnt2-1][cnt1-1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt2-1][cnt1-1] != color) :
				# *** プレイヤー以外の色の駒があるなら ***
				cnt2 -= 1
				cnt1 -= 1
			elif(self.__mMasuSts[cnt2-1][cnt1-1] == color) :
				flg = 1
				break
			elif(self.__mMasuSts[cnt2-1][cnt1-1] == ReversiConst.ReversiConst.REVERSI_STS_NONE) :
				break

		if (flg == 1) :
			# *** 駒をひっくり返す ***
			rcnt1 = cnt2
			rcnt2 = cnt1
			while ((rcnt1 < y) and (rcnt2 < x)) :
				self.__mMasuSts[rcnt1][rcnt2] = color
				rcnt1 += 1
				rcnt2 += 1

		# *** 左下方向にある駒を調べる ***
		flg = 0
		cnt1 = x
		cnt2 = y
		while (cnt2 < (self.__mMasuCnt-1) and cnt1 > 0) :
			if(self.__mMasuSts[cnt2+1][cnt1-1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt2+1][cnt1-1] != color) :
				# *** プレイヤー以外の色の駒があるなら ***
				cnt2 += 1
				cnt1 -= 1
			elif(self.__mMasuSts[cnt2+1][cnt1-1] == color) :
				flg = 1
				break
			elif(self.__mMasuSts[cnt2+1][cnt1-1] == ReversiConst.ReversiConst.REVERSI_STS_NONE) :
				break

		if (flg == 1) :
			# *** 駒をひっくり返す ***
			rcnt1 = cnt2
			rcnt2 = cnt1
			while ((rcnt1 > y) and (rcnt2 < x)) :
				self.__mMasuSts[rcnt1][rcnt2] = color
				rcnt1 -= 1
				rcnt2 += 1

		# *** 右上方向にある駒を調べる ***
		flg = 0
		cnt1 = x
		cnt2 = y
		while (cnt2 > 0 and cnt1 < (self.__mMasuCnt-1)) :
			if (self.__mMasuSts[cnt2-1][cnt1+1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt2-1][cnt1+1] != color) :
				# *** プレイヤー以外の色の駒があるなら ***
				cnt2 -= 1
				cnt1 += 1
			elif(self.__mMasuSts[cnt2-1][cnt1+1] == color) :
				flg = 1
				break
			elif(self.__mMasuSts[cnt2-1][cnt1+1] == ReversiConst.ReversiConst.REVERSI_STS_NONE) :
				break

		if (flg == 1) :
			# *** 駒をひっくり返す ***
			rcnt1 = cnt2
			rcnt2 = cnt1
			while ((rcnt1 < y) and (rcnt2 > x)) :
				self.__mMasuSts[rcnt1][rcnt2] = color
				rcnt1 += 1
				rcnt2 -= 1

		# *** 右下方向にある駒を調べる ***
		flg = 0
		cnt1 = x
		cnt2 = y
		while (cnt2 < (self.__mMasuCnt-1) and cnt1 < (self.__mMasuCnt-1)) :
			if (self.__mMasuSts[cnt2+1][cnt1+1] != ReversiConst.ReversiConst.REVERSI_STS_NONE and self.__mMasuSts[cnt2+1][cnt1+1] != color) :
				# *** プレイヤー以外の色の駒があるなら ***
				cnt2 += 1
				cnt1 += 1
			elif(self.__mMasuSts[cnt2+1][cnt1+1] == color) :
				flg = 1
				break
			elif(self.__mMasuSts[cnt2+1][cnt1+1] == ReversiConst.ReversiConst.REVERSI_STS_NONE) :
				break

		if (flg == 1) :
			# *** 駒をひっくり返す ***
			rcnt1 = cnt2
			rcnt2 = cnt1
			while ((rcnt1 > y) and (rcnt2 > x)) :
				self.__mMasuSts[rcnt1][rcnt2] = color
				rcnt1 -= 1
				rcnt2 -= 1

	############################################################################
	#	@brief			パラメーター範囲チェック
	#	@fn				checkPara(self, para, min, max)
	#	@param[in]		self
	#	@param[in]		para		チェックパラメーター
	#	@param[in]		min			パラメーター最小値
	#	@param[in]		max			パラメーター最大値
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def checkPara(self, para, min, max) :
		ret = -1
		if (min <= para and para <= max) :
			ret = 0
		return ret

	############################################################################
	#	@brief			解析を行う(黒)
	#	@fn				AnalysisReversiBlack(self)
	#	@param[in]		self
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def AnalysisReversiBlack(self) :
		tmpX = 0
		tmpY = 0
		sum = 0
		sumOwn = 0
		tmpGoodPoint = 0
		tmpBadPoint = 0
		tmpD1 = 0.0
		tmpD2 = 0.0

		cnt = 0
		while (cnt < self.__mMasuPointCntB ):
			# *** 現在ステータスを一旦コピー ***
			tmpMasu = [[0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
			tmpMasuEnaB = [[0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
			tmpMasuEnaW = [[0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
			for i in range(self.__mMasuCntMax) :
				tmpMasu[i] = copy.deepcopy(self.__mMasuSts[i])
				tmpMasuEnaB[i] = copy.deepcopy(self.__mMasuStsEnaB[i])
				tmpMasuEnaW[i] = copy.deepcopy(self.__mMasuStsEnaW[i])

			tmpY = self.__mMasuPointB[cnt].getY()
			tmpX = self.__mMasuPointB[cnt].getX()
			self.__mMasuSts[tmpY][tmpX] = ReversiConst.ReversiConst.REVERSI_STS_BLACK	# 仮に置く
			self.revMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK,tmpY,tmpX)		# 仮にひっくり返す
			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE)
			# *** このマスに置いた場合の解析を行う ***
			if (self.getColorEna(ReversiConst.ReversiConst.REVERSI_STS_WHITE) != 0) :	# 相手がパス
				self.__mMasuStsPassB[tmpY][tmpX] = 1

			if (self.getEdgeSideZero(tmpY,tmpX) == 0) :									# 置いた場所が角
				self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeCnt() + 1)
				self.__mMasuStsAnzB[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzB[tmpY][tmpX].getGoodPoint() + 10000 * self.__mMasuStsCntB[tmpY][tmpX])
			elif(self.getEdgeSideOne(tmpY,tmpX) == 0) :								# 置いた場所が角の一つ手前
				self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeSideOneCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeSideOneCnt() + 1)
				if(self.checkEdge(ReversiConst.ReversiConst.REVERSI_STS_BLACK,tmpY,tmpX) != 0) :		# 角を取られない
					self.__mMasuStsAnzB[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzB[tmpY][tmpX].getGoodPoint() + 10 * self.__mMasuStsCntB[tmpY][tmpX])
				else:																	# 角を取られる
					self.__mMasuStsAnzB[tmpY][tmpX].setBadPoint(self.__mMasuStsAnzB[tmpY][tmpX].getBadPoint() + 100000)
			elif(self.getEdgeSideTwo(tmpY,tmpX) == 0):								# 置いた場所が角の二つ手前
				self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeSideTwoCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeSideTwoCnt() + 1)
				self.__mMasuStsAnzB[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzB[tmpY][tmpX].getGoodPoint() + 1000 * self.__mMasuStsCntB[tmpY][tmpX])
			elif(self.getEdgeSideThree(tmpY,tmpX) == 0):								# 置いた場所が角の三つ手前
				self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeSideThreeCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeSideThreeCnt() + 1)
				self.__mMasuStsAnzB[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzB[tmpY][tmpX].getGoodPoint() + 100 * self.__mMasuStsCntB[tmpY][tmpX])
			else:																		# 置いた場所がその他
				self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeSideOtherCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeSideOtherCnt() + 1)
				self.__mMasuStsAnzB[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzB[tmpY][tmpX].getGoodPoint() + 10 * self.__mMasuStsCntB[tmpY][tmpX])

			sum = 0
			sumOwn = 0
			for i in range(self.__mMasuCntMax):
				for j in range(self.__mMasuCntMax):
					tmpBadPoint = 0
					tmpGoodPoint = 0
					if (self.getMasuStsEna(ReversiConst.ReversiConst.REVERSI_STS_WHITE,i,j) != 0) :
						sum += self.__mMasuStsCntW[i][j]								# 相手の獲得予定枚数
						# *** 相手の獲得予定の最大数保持 ***
						if (self.__mMasuStsAnzB[tmpY][tmpX].getMax() < self.__mMasuStsCntW[i][j]):
							self.__mMasuStsAnzB[tmpY][tmpX].setMax(self.__mMasuStsCntW[i][j])
						# *** 相手の獲得予定の最小数保持 ***
						if (self.__mMasuStsCntW[i][j] < self.__mMasuStsAnzB[tmpY][tmpX].getMin()):
							self.__mMasuStsAnzB[tmpY][tmpX].setMin(self.__mMasuStsCntW[i][j])
						self.__mMasuStsAnzB[tmpY][tmpX].setPointCnt(self.__mMasuStsAnzB[tmpY][tmpX].getPointCnt() + 1) # 相手の置ける場所の数
						if (self.getEdgeSideZero(i,j) == 0):							# 置く場所が角
							self.__mMasuStsAnzB[tmpY][tmpX].setEdgeCnt(self.__mMasuStsAnzB[tmpY][tmpX].getEdgeCnt() + 1)
							tmpBadPoint = 100000 * self.__mMasuStsCntW[i][j]
						elif (self.getEdgeSideOne(i,j) == 0):						# 置く場所が角の一つ手前
							self.__mMasuStsAnzB[tmpY][tmpX].setEdgeSideOneCnt(self.__mMasuStsAnzB[tmpY][tmpX].getEdgeSideOneCnt() + 1)
							tmpBadPoint = 0
						elif (self.getEdgeSideTwo(i,j) == 0):						# 置く場所が角の二つ手前
							self.__mMasuStsAnzB[tmpY][tmpX].setEdgeSideTwoCnt(self.__mMasuStsAnzB[tmpY][tmpX].getEdgeSideTwoCnt() + 1)
							tmpBadPoint = 1 * self.__mMasuStsCntW[i][j]
						elif (self.getEdgeSideThree(i,j) == 0):						# 置く場所が角の三つ手前
							self.__mMasuStsAnzB[tmpY][tmpX].setEdgeSideThreeCnt(self.__mMasuStsAnzB[tmpY][tmpX].getEdgeSideThreeCnt() + 1)
							tmpBadPoint = 1 * self.__mMasuStsCntW[i][j]
						else:															# 置く場所がその他
							self.__mMasuStsAnzB[tmpY][tmpX].setEdgeSideOtherCnt(self.__mMasuStsAnzB[tmpY][tmpX].getEdgeSideOtherCnt() + 1)
							tmpBadPoint = 1 * self.__mMasuStsCntW[i][j]
						
						if(tmpMasuEnaW[i][j] != 0):
							tmpBadPoint = 0												# ステータス変化していないなら

					if(self.getMasuStsEna(ReversiConst.ReversiConst.REVERSI_STS_BLACK,i,j) != 0) :
						sumOwn += self.__mMasuStsCntB[i][j]								# 自分の獲得予定枚数
						# *** 自分の獲得予定の最大数保持 ***
						if (self.__mMasuStsAnzB[tmpY][tmpX].getOwnMax() < self.__mMasuStsCntB[i][j]):
							self.__mMasuStsAnzB[tmpY][tmpX].setOwnMax(self.__mMasuStsCntB[i][j])
						# *** 自分の獲得予定の最小数保持 ***
						if (self.__mMasuStsCntB[i][j] < self.__mMasuStsAnzB[tmpY][tmpX].getOwnMin()) :
							self.__mMasuStsAnzB[tmpY][tmpX].setOwnMin(self.__mMasuStsCntB[i][j])
						self.__mMasuStsAnzB[tmpY][tmpX].setOwnPointCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnPointCnt() + 1)	# 自分の置ける場所の数
						if (self.getEdgeSideZero(i,j) == 0):							# 置く場所が角
							self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeCnt() + 1)
							tmpGoodPoint = 100 * self.__mMasuStsCntB[i][j]
						elif (self.getEdgeSideOne(i,j) == 0):						# 置く場所が角の一つ手前
							self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeSideOneCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeSideOneCnt() + 1)
							tmpGoodPoint = 0
						elif (self.getEdgeSideTwo(i,j) == 0):						# 置く場所が角の二つ手前
							self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeSideTwoCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeSideTwoCnt() + 1)
							tmpGoodPoint = 3 * self.__mMasuStsCntB[i][j]
						elif (self.getEdgeSideThree(i,j) == 0):						# 置く場所が角の三つ手前
							self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeSideThreeCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeSideThreeCnt() + 1)
							tmpGoodPoint = 2 * self.__mMasuStsCntB[i][j]
						else:															# 置く場所がその他
							self.__mMasuStsAnzB[tmpY][tmpX].setOwnEdgeSideOtherCnt(self.__mMasuStsAnzB[tmpY][tmpX].getOwnEdgeSideOtherCnt() + 1)
							tmpGoodPoint = 1 * self.__mMasuStsCntB[i][j]
						
						if(tmpMasuEnaB[i][j] != 0) :
							tmpGoodPoint = 0											# ステータス変化していないなら

					if (tmpBadPoint != 0):
						self.__mMasuStsAnzB[tmpY][tmpX].setBadPoint(self.__mMasuStsAnzB[tmpY][tmpX].getBadPoint()	+ tmpBadPoint)
					if (tmpGoodPoint != 0):
						self.__mMasuStsAnzB[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzB[tmpY][tmpX].getGoodPoint() + tmpGoodPoint)

			# *** 相手に取られる平均コマ数 ***
			if (self.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_WHITE) != 0) :
				tmpD1 = sum
				tmpD2 = self.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_WHITE)
				self.__mMasuStsAnzB[tmpY][tmpX].setAvg(tmpD1 / tmpD2)

			# *** 自分が取れる平均コマ数 ***
			if (self.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_BLACK) != 0) :
				tmpD1 = sumOwn
				tmpD2 = self.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
				self.__mMasuStsAnzB[tmpY][tmpX].setOwnAvg(tmpD1 / tmpD2)

			# *** 元に戻す ***
			for i in range(self.__mMasuCntMax) :
				self.__mMasuSts[i] = copy.deepcopy(tmpMasu[i])

			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE)

			cnt += 1

	############################################################################
	#	@brief			解析を行う(白)
	#	@fn				AnalysisReversiWhite(self)
	#	@param[in]		self
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def AnalysisReversiWhite(self):
		tmpX = 0
		tmpY = 0
		sum = 0
		sumOwn = 0
		tmpGoodPoint = 0
		tmpBadPoint = 0
		tmpD1 = 0.0
		tmpD2 = 0.0

		cnt = 0
		while (cnt < self.__mMasuPointCntW):
			# *** 現在ステータスを一旦コピー ***
			tmpMasu = [[0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
			tmpMasuEnaB = [[0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
			tmpMasuEnaW = [[0 for i in range(self.__mMasuCntMax)] for j in range(self.__mMasuCntMax)]
			for i in range(self.__mMasuCntMax) :
				tmpMasu[i] = copy.deepcopy(self.__mMasuSts[i])
				tmpMasuEnaB[i] = copy.deepcopy(self.__mMasuStsEnaB[i])
				tmpMasuEnaW[i] = copy.deepcopy(self.__mMasuStsEnaW[i])

			tmpY = self.__mMasuPointW[cnt].getY()
			tmpX = self.__mMasuPointW[cnt].getX()
			self.__mMasuSts[tmpY][tmpX] = ReversiConst.ReversiConst.REVERSI_STS_WHITE				# 仮に置く
			self.revMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE,tmpY,tmpX)					# 仮にひっくり返す
			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE)
			# *** このマスに置いた場合の解析を行う ***
			if (self.getColorEna(ReversiConst.ReversiConst.REVERSI_STS_BLACK) != 0) :				# 相手がパス
				self.__mMasuStsPassW[tmpY][tmpX] = 1

			if(self.getEdgeSideZero(tmpY,tmpX) == 0):												# 置いた場所が角
				self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeCnt() + 1)
				self.__mMasuStsAnzW[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzW[tmpY][tmpX].getGoodPoint() + 10000 * self.__mMasuStsCntW[tmpY][tmpX])
			elif(self.getEdgeSideOne(tmpY,tmpX) == 0):											# 置いた場所が角の一つ手前
				self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeSideOneCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeSideOneCnt() + 1)
				if(self.checkEdge(ReversiConst.ReversiConst.REVERSI_STS_WHITE,tmpY,tmpX) != 0):		# 角を取られない
					self.__mMasuStsAnzW[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzW[tmpY][tmpX].getGoodPoint() + 10 * self.__mMasuStsCntW[tmpY][tmpX])
				else:																				# 角を取られる
					self.__mMasuStsAnzW[tmpY][tmpX].setBadPoint(self.__mMasuStsAnzW[tmpY][tmpX].getBadPoint() + 100000)
			elif(self.getEdgeSideTwo(tmpY,tmpX) == 0):											# 置いた場所が角の二つ手前
				self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeSideTwoCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeSideTwoCnt() + 1)
				self.__mMasuStsAnzW[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzW[tmpY][tmpX].getGoodPoint() + 1000 * self.__mMasuStsCntW[tmpY][tmpX])
			elif(self.getEdgeSideThree(tmpY,tmpX) == 0):											# 置いた場所が角の三つ手前
				self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeSideThreeCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeSideThreeCnt() + 1)
				self.__mMasuStsAnzW[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzW[tmpY][tmpX].getGoodPoint() + 100 * self.__mMasuStsCntW[tmpY][tmpX])
			else:																					# 置いた場所がその他
				self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeSideOtherCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeSideOtherCnt() + 1)
				self.__mMasuStsAnzW[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzW[tmpY][tmpX].getGoodPoint() + 10 * self.__mMasuStsCntW[tmpY][tmpX])

			sum = 0
			sumOwn = 0
			for i in range(self.__mMasuCntMax):
				for j in range(self.__mMasuCntMax):
					tmpBadPoint = 0
					tmpGoodPoint = 0
					if (self.getMasuStsEna(ReversiConst.ReversiConst.REVERSI_STS_BLACK,i,j) != 0):
						sum += self.__mMasuStsCntB[i][j]											# 相手の獲得予定枚数
						# *** 相手の獲得予定の最大数保持 ***
						if (self.__mMasuStsAnzW[tmpY][tmpX].getMax() < self.__mMasuStsCntB[i][j]):
							self.__mMasuStsAnzW[tmpY][tmpX].setMax(self.__mMasuStsCntB[i][j])
						# *** 相手の獲得予定の最小数保持 ***
						if (self.__mMasuStsCntB[i][j] < self.__mMasuStsAnzW[tmpY][tmpX].getMin()):
							self.__mMasuStsAnzW[tmpY][tmpX].setMin(self.__mMasuStsCntB[i][j])
						self.__mMasuStsAnzW[tmpY][tmpX].setPointCnt(self.__mMasuStsAnzW[tmpY][tmpX].getPointCnt() + 1)	# 相手の置ける場所の数
						if (self.getEdgeSideZero(i,j) == 0):										# 置く場所が角
							self.__mMasuStsAnzW[tmpY][tmpX].setEdgeCnt(self.__mMasuStsAnzW[tmpY][tmpX].getEdgeCnt() + 1)
							tmpBadPoint = 100000 * self.__mMasuStsCntB[i][j]
						elif (self.getEdgeSideOne(i,j) == 0):									# 置く場所が角の一つ手前
							self.__mMasuStsAnzW[tmpY][tmpX].setEdgeSideOneCnt(self.__mMasuStsAnzW[tmpY][tmpX].getEdgeSideOneCnt() + 1)
							tmpBadPoint = 0
						elif (self.getEdgeSideTwo(i,j) == 0):									# 置く場所が角の二つ手前
							self.__mMasuStsAnzW[tmpY][tmpX].setEdgeSideTwoCnt(self.__mMasuStsAnzW[tmpY][tmpX].getEdgeSideTwoCnt() + 1)
							tmpBadPoint = 1 * self.__mMasuStsCntB[i][j]
						elif (self.getEdgeSideThree(i,j) == 0):									# 置く場所が角の三つ手前
							self.__mMasuStsAnzW[tmpY][tmpX].setEdgeSideThreeCnt(self.__mMasuStsAnzW[tmpY][tmpX].getEdgeSideThreeCnt() + 1)
							tmpBadPoint = 1 * self.__mMasuStsCntB[i][j]
						else:																		# 置く場所がその他
							self.__mMasuStsAnzW[tmpY][tmpX].setEdgeSideOtherCnt(self.__mMasuStsAnzW[tmpY][tmpX].getEdgeSideOtherCnt() + 1)
							tmpBadPoint = 1 * self.__mMasuStsCntB[i][j]
						if (tmpMasuEnaB[i][j] != 0):
							tmpBadPoint = 0															# ステータス変化していないなら

					if (self.getMasuStsEna(ReversiConst.ReversiConst.REVERSI_STS_WHITE,i,j) != 0):
						sumOwn += self.__mMasuStsCntW[i][j]											# 自分の獲得予定枚数
						# *** 自分の獲得予定の最大数保持 ***
						if (self.__mMasuStsAnzW[tmpY][tmpX].getOwnMax() < self.__mMasuStsCntW[i][j]):
							self.__mMasuStsAnzW[tmpY][tmpX].setOwnMax(self.__mMasuStsCntW[i][j])
						# *** 自分の獲得予定の最小数保持 ***
						if (self.__mMasuStsCntW[i][j] < self.__mMasuStsAnzW[tmpY][tmpX].getOwnMin()):
							self.__mMasuStsAnzW[tmpY][tmpX].setOwnMin(self.__mMasuStsCntW[i][j])
						self.__mMasuStsAnzW[tmpY][tmpX].setOwnPointCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnPointCnt() + 1)	# 自分の置ける場所の数
						if (self.getEdgeSideZero(i,j) == 0):										# 置く場所が角
							self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeCnt() + 1)
							tmpGoodPoint = 100 * self.__mMasuStsCntW[i][j]
						elif (self.getEdgeSideOne(i,j) == 0):									# 置く場所が角の一つ手前
							self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeSideOneCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeSideOneCnt() + 1)
							tmpGoodPoint = 0
						elif (self.getEdgeSideTwo(i,j) == 0):									# 置く場所が角の二つ手前
							self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeSideTwoCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeSideTwoCnt() + 1)
							tmpGoodPoint = 3 * self.__mMasuStsCntW[i][j]
						elif (self.getEdgeSideThree(i,j) == 0):									# 置く場所が角の三つ手前
							self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeSideThreeCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeSideThreeCnt() + 1)
							tmpGoodPoint = 2 * self.__mMasuStsCntW[i][j]
						else:																		# 置く場所がその他
							self.__mMasuStsAnzW[tmpY][tmpX].setOwnEdgeSideOtherCnt(self.__mMasuStsAnzW[tmpY][tmpX].getOwnEdgeSideOtherCnt() + 1)
							tmpGoodPoint = 1 * self.__mMasuStsCntW[i][j]
						if(tmpMasuEnaW[i][j] != 0):
							tmpGoodPoint = 0														# ステータス変化していないなら

					if (tmpBadPoint != 0):
						self.__mMasuStsAnzW[tmpY][tmpX].setBadPoint(self.__mMasuStsAnzW[tmpY][tmpX].getBadPoint() + tmpBadPoint)
					if (tmpGoodPoint != 0):
						self.__mMasuStsAnzW[tmpY][tmpX].setGoodPoint(self.__mMasuStsAnzW[tmpY][tmpX].getGoodPoint() + tmpGoodPoint)

			# *** 相手に取られる平均コマ数 ***
			if (self.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_BLACK) != 0) :
				tmpD1 = sum
				tmpD2 = self.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
				self.__mMasuStsAnzW[tmpY][tmpX].setAvg(tmpD1 / tmpD2)

			# *** 自分が取れる平均コマ数 ***
			if (self.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_WHITE) != 0) :
				tmpD1 = sumOwn
				tmpD2 = self.getPointCnt(ReversiConst.ReversiConst.REVERSI_STS_WHITE)
				self.__mMasuStsAnzW[tmpY][tmpX].setOwnAvg(tmpD1 / tmpD2)

			# *** 元に戻す ***
			for i in range(self.__mMasuCntMax) :
				self.__mMasuSts[i] = copy.deepcopy(tmpMasu[i])

			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE)

			cnt += 1

	############################################################################
	#	@brief			解析を行う
	#	@fn				AnalysisReversi(self, bPassEna, wPassEna)
	#	@param[in]		self
	#	@param[in]		bPassEna		1=黒パス有効
	#	@param[in]		wPassEna		1=白パス有効
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def AnalysisReversi(self, bPassEna, wPassEna):
		# *** 相手をパスさせることができるマス検索 ***
		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				self.__mMasuStsPassB[i][j] = 0
				self.__mMasuStsAnzB[i][j].reset()
				self.__mMasuStsPassW[i][j] = 0
				self.__mMasuStsAnzW[i][j].reset()

		self.AnalysisReversiBlack()										# 黒解析
		self.AnalysisReversiWhite()										# 白解析

		self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
		self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE)

		# *** パスマスを取得 ***
		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				if (self.__mMasuStsPassB[i][j] != 0) :
					if (bPassEna != 0):
						self.__mMasuStsEnaB[i][j] = 3
				if (self.__mMasuStsPassW[i][j] != 0) :
					if (wPassEna != 0):
						self.__mMasuStsEnaW[i][j] = 3

	############################################################################
	#	@brief			マスステータスを取得
	#	@fn				getMasuSts(self, y, x)
	#	@param[in]		self
	#	@param[in]		y			取得するマスのY座標
	#	@param[in]		x			取得するマスのX座標
	#	@return			-1 : 失敗 それ以外 : マスステータス
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getMasuSts(self, y, x):
		ret = -1
		if (self.checkPara(y,0,self.__mMasuCnt) == 0 and self.checkPara(x,0,self.__mMasuCnt) == 0):
			ret = self.__mMasuSts[y][x]
		return ret

	############################################################################
	#	@brief			以前のマスステータスを取得
	#	@fn				getMasuStsOld(self, y, x)
	#	@param[in]		self
	#	@param[in]		y			取得するマスのY座標
	#	@param[in]		x			取得するマスのX座標
	#	@return			-1 : 失敗 それ以外 : マスステータス
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getMasuStsOld(self, y, x):
		ret = -1
		if (self.checkPara(y, 0, self.__mMasuCnt) == 0 and self.checkPara(x, 0, self.__mMasuCnt) == 0) :
			ret = self.__mMasuStsOld[y][x]
		return ret

	############################################################################
	#	@brief			指定座標に指定色を置けるかチェック
	#	@fn				getMasuStsEna(self, color, y, x)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@param[in]		y			マスのY座標
	#	@param[in]		x			マスのX座標
	#	@return			1 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getMasuStsEna(self, color, y, x):
		ret = 0
		if (self.checkPara(y,0,self.__mMasuCnt) == 0 and self.checkPara(x,0,self.__mMasuCnt) == 0):
			if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
				ret = self.__mMasuStsEnaB[y][x]
			else:
				ret = self.__mMasuStsEnaW[y][x]
		return ret

	############################################################################
	#	@brief			指定座標の獲得コマ数取得
	#	@fn				getMasuStsCnt(self, color, y, x)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@param[in]		y			マスのY座標
	#	@param[in]		x			マスのX座標
	#	@return			-1 : 失敗 それ以外 : 獲得コマ数
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getMasuStsCnt(self, color, y, x):
		ret = -1
		if (self.checkPara(y,0,self.__mMasuCnt) == 0 and self.checkPara(x,0,self.__mMasuCnt) == 0):
			if(color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
				ret = self.__mMasuStsCntB[y][x]
			else:
				ret = self.__mMasuStsCntW[y][x]
		return ret

	############################################################################
	#	@brief			指定色が現在置ける場所があるかチェック
	#	@fn				getColorEna(self, color)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getColorEna(self, color):
		ret = -1
		for i in range(self.__mMasuCntMax):
			for j in range(self.__mMasuCntMax):
				if (self.getMasuStsEna(color,i,j) != 0):
					ret = 0
					break
		return ret

	############################################################################
	#	@brief			ゲーム終了かチェック
	#	@fn				getGameEndSts(self)
	#	@param[in]		self
	#	@return			0 : 続行 それ以外 : ゲーム終了
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getGameEndSts(self):
		ret = 1
		if (self.getColorEna(ReversiConst.ReversiConst.REVERSI_STS_BLACK) == 0):
			ret = 0
		if (self.getColorEna(ReversiConst.ReversiConst.REVERSI_STS_WHITE) == 0):
			ret = 0
		return ret

	############################################################################
	#	@brief			指定座標にコマを置く
	#	@fn				setMasuSts(self, color, y, x)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@param[in]		y			マスのY座標
	#	@param[in]		x			マスのX座標
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setMasuSts(self, color, y, x):
		ret = -1
		if (self.getMasuStsEna(color,y,x) != 0) :
			ret = 0
			for i in range(self.__mMasuCntMax) :
				self.__mMasuStsOld[i] = copy.deepcopy(self.__mMasuSts[i])

			self.__mMasuSts[y][x] = color
			self.revMasuSts(color,y,x)
			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
			self.makeMasuSts(ReversiConst.ReversiConst.REVERSI_STS_WHITE)
			# *** 履歴保存 ***
			if (self.__mMasuHistCur < (self.__mMasuCntMax * self.__mMasuCntMax)):
				self.__mMasuHist[self.__mMasuHistCur].setColor(color)
				self.__mMasuHist[self.__mMasuHistCur].getPoint().setY(y)
				self.__mMasuHist[self.__mMasuHistCur].getPoint().setX(x)
				self.__mMasuHistCur += 1

		return ret

	############################################################################
	#	@brief			指定座標にコマを強制的に置く
	#	@fn				setMasuStsForcibly(self, color, y, x)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@param[in]		y			マスのY座標
	#	@param[in]		x			マスのX座標
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setMasuStsForcibly(self, color, y, x):
		ret = 0
		for i in range(self.__mMasuCntMax) :
			self.__mMasuStsOld[i] = copy.deepcopy(self.__mMasuSts[i])
		self.__mMasuSts[y][x] = color
		return ret

	############################################################################
	#	@brief			マスの数変更
	#	@fn				setMasuCnt(self, cnt)
	#	@param[in]		self
	#	@param[in]		cnt		マスの数
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def setMasuCnt(self, cnt):
		ret = -1
		chg = 0
		if (self.checkPara(cnt,0,self.__mMasuCntMax) == 0):
			if (self.__mMasuCnt != cnt):
				chg = 1
			self.__mMasuCnt = cnt
			ret = 0
			if (chg == 1):
				self.reset()
		return ret

	############################################################################
	#	@brief			ポイント座標取得
	#	@fn				getPoint(self, color,int num)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@param[in]		num			ポイント
	#	@return			ポイント座標 null : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getPoint(self, color, num):
		ret = None
		if(self.checkPara(num,0,(self.__mMasuCnt * self.__mMasuCnt)) == 0):
			if(color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
				ret = self.__mMasuPointB[num]
			else:
				ret = self.__mMasuPointW[num]
		return ret

	############################################################################
	#	@brief			ポイント座標数取得
	#	@fn				getPointCnt(self, color)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@return			ポイント座標数取得
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getPointCnt(self, color):
		ret = 0
		if(color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
			ret = self.__mMasuPointCntB
		else:
			ret = self.__mMasuPointCntW
		return ret

	############################################################################
	#	@brief			コマ数取得
	#	@fn				getBetCnt(self, color)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@return			コマ数取得
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getBetCnt(self, color):
		ret = 0
		if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
			ret = self.__mMasuBetCntB
		else:
			ret = self.__mMasuBetCntW
		return ret

	############################################################################
	#	@brief			パス判定
	#	@fn				getPassEna(self, color, y, x)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@param[in]		y			マスのY座標
	#	@param[in]		x			マスのX座標
	#	@return			パス判定
	#					- 0 : NOT PASS
	#					- 1 : PASS
	#
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getPassEna(self, color, y, x):
		ret = 0
		if (self.checkPara(y,0,self.__mMasuCnt) == 0 and self.checkPara(x,0,self.__mMasuCnt) == 0):
			if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
				ret = self.__mMasuStsPassB[y][x]
			else:
				ret = self.__mMasuStsPassW[y][x]
		return ret

	############################################################################
	#	@brief			履歴取得
	#	@fn				getHistory(self, num)
	#	@param[in]		self
	#	@param[in]		num			ポイント
	#	@return			履歴 null : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getHistory(self, num):
		ret = None
		if (self.checkPara(num,0,(self.__mMasuCnt * self.__mMasuCnt)) == 0):
			ret = self.__mMasuHist[num]
		return ret

	############################################################################
	#	@brief			履歴数取得
	#	@fn				getHistoryCnt(self)
	#	@param[in]		self
	#	@return			履歴数
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getHistoryCnt(self):
		ret = self.__mMasuHistCur
		return ret

	############################################################################
	#	@brief			ポイント座標解析取得
	#	@fn				getPointAnz(self, color, y, x)
	#	@param[in]		self
	#	@param[in]		color		コマ色
	#	@param[in]		y			マスのY座標
	#	@param[in]		x			マスのX座標
	#	@return			ポイント座標解析 null : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getPointAnz(self, color, y, x):
		ret = None
		if (self.checkPara(y,0,self.__mMasuCnt) == 0 and self.checkPara(x,0,self.__mMasuCnt) == 0):
			if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
				ret = self.__mMasuStsAnzB[y][x]
			else:
				ret = self.__mMasuStsAnzW[y][x]
		return ret

	############################################################################
	#	@brief			角の隣に置いても角を取られないマス検索
	#	@fn				checkEdge(self, color, y, x)
	#	@param[in]		self
	#	@param[in]		color		色
	#	@param[in]		y			Y座標
	#	@param[in]		x			X座標
	#	@return			0 : 取られる それ以外 : 取られない
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def checkEdge(self, color, y, x):
		style = 0
		flg1 = 0
		flg2 = 0
		loop = 0
		loop2 = 0
		if (y == 0 and x == 1):
			loop = x
			flg1 = 0
			flg2 = 0
			while (loop < self.__mMasuCnt):
				if (self.getMasuSts(y,loop) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(y,loop) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(y,loop) != color) and (self.getMasuSts(y,loop) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop += 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == 1 and x == 0):
			loop = y
			flg1 = 0
			flg2 = 0
			while (loop < self.__mMasuCnt):
				if (self.getMasuSts(loop,x) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(loop,x) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(loop,x) != color) and (self.getMasuSts(loop,x) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop += 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if(y == 1 and x == 1):
			loop = y
			flg1 = 0
			flg2 = 0
			while (loop < self.__mMasuCnt):
				if (self.getMasuSts(loop,loop) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(loop,loop) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(loop,loop) != color) and (self.getMasuSts(loop,loop) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop += 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == 0 and x == (self.__mMasuCnt-2)):
			loop = x
			flg1 = 0
			flg2 = 0
			while (loop > 0):
				if (self.getMasuSts(y,loop) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(y,loop) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(y,loop) != color) and (self.getMasuSts(y,loop) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop -= 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == 1 and x == (self.__mMasuCnt-1)):
			loop = y
			flg1 = 0
			flg2 = 0
			while (loop < self.__mMasuCnt):
				if (self.getMasuSts(loop,x) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(loop,x) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(loop,x) != color) and (self.getMasuSts(loop,x) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop += 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == 1 and x == (self.__mMasuCnt-2)):
			loop = y
			loop2 = x
			flg1 = 0
			flg2 = 0
			while (loop < self.__mMasuCnt):
				if (self.getMasuSts(loop,loop2) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(loop,loop2) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(loop,loop2) != color) and (self.getMasuSts(loop,loop2) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop += 1
				loop2 -= 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == (self.__mMasuCnt-2) and x == 0):
			loop = y
			flg1 = 0
			flg2 = 0
			while (loop > 0):
				if (self.getMasuSts(loop,x) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(loop,x) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(loop,x) != color) and (self.getMasuSts(loop,x) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop -= 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == (self.__mMasuCnt-1) and x == 1):
			loop = x
			flg1 = 0
			flg2 = 0
			while (loop < self.__mMasuCnt):
				if (self.getMasuSts(y,loop) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(y,loop) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(y,loop) != color) and (self.getMasuSts(y,loop) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop += 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == (self.__mMasuCnt-2) and x == 1):
			loop = y
			loop2 = x
			flg1 = 0
			flg2 = 0
			while (loop > 0):
				if (self.getMasuSts(loop,loop2) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(loop,loop2) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(loop,loop2) != color) and (self.getMasuSts(loop,loop2) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop -= 1
				loop2 += 1

			if ((flg1 == 1) and (flg2 == 0)):
				style = 1

		if(y == (self.__mMasuCnt-2) and x == (self.__mMasuCnt-1)):
			loop = y
			flg1 = 0
			flg2 = 0
			while (loop > 0):
				if (self.getMasuSts(loop,x) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(loop,x) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(loop,x) != color) and (self.getMasuSts(loop,x) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop -= 1

			if ((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == (self.__mMasuCnt-1) and x == (self.__mMasuCnt-2)):
			loop = x
			flg1 = 0
			flg2 = 0
			while (loop > 0):
				if (self.getMasuSts(y,loop) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(y,loop) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(y,loop) != color) and (self.getMasuSts(y,loop) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop -= 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		if (y == (self.__mMasuCnt-2) and x == (self.__mMasuCnt-2)):
			loop = y
			loop2 = x
			flg1 = 0
			flg2 = 0
			while (loop > 0):
				if (self.getMasuSts(loop,loop2) == color):
					flg1 = 1
				if (flg1 == 1 and self.getMasuSts(loop,loop2) == ReversiConst.ReversiConst.REVERSI_STS_NONE):
					break
				if ((flg1 == 1) and (self.getMasuSts(loop,loop2) != color) and (self.getMasuSts(loop,loop2) != ReversiConst.ReversiConst.REVERSI_STS_NONE)):
					flg2 = 1
				loop -= 1
				loop2 -= 1

			if((flg1 == 1) and (flg2 == 0)):
				style = 1

		return style

	############################################################################
	#	@brief			指定座標が角か取得
	#	@fn				getEdgeSideZero(self, y,int x)
	#	@param[in]		self
	#	@param[in]		y			Y座標
	#	@param[in]		x			X座標
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getEdgeSideZero(self, y, x):
		ret = -1
		if (y == 0 and x == 0): ret = 0
		if (y == 0 and x == (self.__mMasuCnt-1)): ret = 0
		if (y == (self.__mMasuCnt-1) and x == 0): ret = 0
		if (y == (self.__mMasuCnt-1) and x == (self.__mMasuCnt-1)): ret = 0
		return ret

	############################################################################
	#	@brief			指定座標が角の一つ手前か取得
	#	@fn				getEdgeSideOne(self, y, x)
	#	@param[in]		self
	#	@param[in]		y			Y座標
	#	@param[in]		x			X座標
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getEdgeSideOne(self, y, x):
		ret = -1
		if (y == 0 and x == 1): ret = 0
		if (y == 0 and x == (self.__mMasuCnt-2)): ret = 0
		if (y == 1 and x == 0): ret = 0
		if (y == 1 and x == 1): ret = 0
		if (y == 1 and x == (self.__mMasuCnt-2)): ret = 0
		if (y == 1 and x == (self.__mMasuCnt-1)): ret = 0
		if (y == (self.__mMasuCnt-2) and x == 0): ret = 0
		if (y == (self.__mMasuCnt-2) and x == 1): ret = 0
		if (y == (self.__mMasuCnt-2) and x == (self.__mMasuCnt-2)): ret = 0
		if (y == (self.__mMasuCnt-2) and x == (self.__mMasuCnt-1)): ret = 0
		if (y == (self.__mMasuCnt-1) and x == 1): ret = 0
		if (y == (self.__mMasuCnt-1) and x == (self.__mMasuCnt-2)): ret = 0
		return ret

	############################################################################
	#	@brief			指定座標が角の二つ手前か取得
	#	@fn				getEdgeSideTwo(self, y, x)
	#	@param[in]		self
	#	@param[in]		y			Y座標
	#	@param[in]		x			X座標
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getEdgeSideTwo(self, y, x):
		ret = -1
		if (y == 0 and x == 2): ret = 0
		if (y == 0 and x == (self.__mMasuCnt-3)): ret = 0
		if (y == 2 and x == 0): ret = 0
		if (y == 2 and x == 2): ret = 0
		if (y == 2 and x == (self.__mMasuCnt-3)): ret = 0
		if (y == 2 and x == (self.__mMasuCnt-1)): ret = 0
		if (y == (self.__mMasuCnt-3) and x == 0): ret = 0
		if (y == (self.__mMasuCnt-3) and x == 2): ret = 0
		if (y == (self.__mMasuCnt-3) and x == (self.__mMasuCnt-3)): ret = 0
		if (y == (self.__mMasuCnt-3) and x == (self.__mMasuCnt-1)): ret = 0
		if (y == (self.__mMasuCnt-1) and x == 2): ret = 0
		if (y == (self.__mMasuCnt-1) and x == (self.__mMasuCnt-3)): ret = 0
		return ret

	############################################################################
	#	@brief			指定座標が角の三つ以上手前か取得
	#	@fn				getEdgeSideThree(self, y, x)
	#	@param[in]		self
	#	@param[in]		y			Y座標
	#	@param[in]		x			X座標
	#	@return			0 : 成功 それ以外 : 失敗
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.11
	#
	############################################################################
	def getEdgeSideThree(self, y, x):
		ret = -1
		if (y == 0 and (3 <= x and x <= (self.__mMasuCnt-4))): ret = 0
		if ((3 <= y and y <= (self.__mMasuCnt-4)) and x == 0): ret = 0
		if (y == (self.__mMasuCnt-1) and (3 <= x and x <= (self.__mMasuCnt-4))): ret = 0
		if ((3 <= y and y <= (self.__mMasuCnt-4)) and x == (self.__mMasuCnt-1)): ret = 0
		return ret

	mMasuSts = property(getmMasuSts,setmMasuSts)					# !< マスの状態
	mMasuStsOld = property(getmMasuStsOld,setmMasuStsOld)			# !< 以前のマスの状態
	mMasuStsEnaB = property(getmMasuStsEnaB,setmMasuStsEnaB)		# !< 黒の置ける場所
	mMasuStsCntB = property(getmMasuStsCntB,setmMasuStsCntB)		# !< 黒の獲得コマ数
	mMasuStsPassB = property(getmMasuStsPassB,setmMasuStsPassB)		# !< 黒が相手をパスさせる場所
	mMasuStsAnzB = property(getmMasuStsAnzB,setmMasuStsAnzB)		# !< 黒がその場所に置いた場合の解析結果
	mMasuPointB = property(getmMasuPointB,setmMasuPointB)			# !< 黒の置ける場所座標一覧
	mMasuPointCntB = property(getmMasuPointCntB,setmMasuPointCntB)	# !< 黒の置ける場所座標一覧数
	mMasuBetCntB = property(getmMasuBetCntB,setmMasuBetCntB)		# !< 黒コマ数
	mMasuStsEnaW = property(getmMasuStsEnaW,setmMasuStsEnaW)		# !< 白の置ける場所
	mMasuStsCntW = property(getmMasuStsCntW,setmMasuStsCntW)		# !< 白の獲得コマ数
	mMasuStsPassW = property(getmMasuStsPassW,setmMasuStsPassW)		# !< 白が相手をパスさせる場所
	mMasuStsAnzW = property(getmMasuStsAnzW,setmMasuStsAnzW)		# !< 白がその場所に置いた場合の解析結果
	mMasuPointW = property(getmMasuPointW,setmMasuPointW)			# !< 白の置ける場所座標一覧
	mMasuPointCntW = property(getmMasuPointCntW,setmMasuPointCntW)	# !< 白の置ける場所座標一覧数
	mMasuBetCntW = property(getmMasuBetCntW,setmMasuBetCntW)		# !< 白コマ数
	mMasuCnt = property(getmMasuCnt,setmMasuCnt)					# !< 縦横マス数
	mMasuCntMax = property(getmMasuCntMax,setmMasuCntMax)			# !< 縦横マス最大数
	mMasuHist = property(getmMasuHist,setmMasuHist)					# !< 履歴
	mMasuHistCur = property(getmMasuHistCur,setmMasuHistCur)		# !< 履歴現在位置
