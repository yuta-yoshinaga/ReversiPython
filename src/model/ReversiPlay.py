################################################################################
#	@file			ReversiPlay.py
#	@brief			リバーシプレイクラス実装ファイル
#	@author			Yuta Yoshinaga
#	@date			2018.11.13
#	$Version:		$
#	$Revision:		$
#
# Copyright (c) 2018 Yuta Yoshinaga. All Rights reserved.
#
# - 本ソフトウェアの一部又は全てを無断で複写複製（コピー）することは、
#   著作権侵害にあたりますので、これを禁止します。
# - 本製品の使用に起因する侵害または特許権その他権利の侵害に関しては
#   当社は一切その責任を負いません。
#
################################################################################

import random

################################################################################
#	@class		ReversiPlay
#	@brief		リバーシプレイクラス
#
################################################################################
class ReversiPlay:

	############################################################################
	#	@brief			コンストラクタ
	#	@fn				__init__(self)
	#	@param[in]		self
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def __init__(self):
		self.__mReversi	= Reversi(ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL, ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL)
		self.__mSetting	= ReversiSetting()
		self.__mCpu		= [0 for i in range(ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL * ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL)]
		self.__mEdge	= [0 for i in range(ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL * ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL)]
		for i in range(ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL * ReversiConst.ReversiConst.DEF_MASU_CNT_MAX_VAL):
			self.__mCpu[i]	= ReversiPoint()
			self.__mEdge[i]	= ReversiPoint()

		self.__mCurColor	= 0
		self.__mPassEnaB	= 0
		self.__mPassEnaW	= 0
		self.__mGameEndSts	= 0
		self.__mPlayLock	= 0
		self.__mDelegate	= None
		self.__mCallbacks	= None

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmReversi()
	#	@param[in]		self
	#	@return			mReversi
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmReversi(self):
		return self.__mReversi

	############################################################################
	#	@brief			セッター
	#	@fn				setmReversi(self, mReversi)
	#	@param[in]		self
	#	@param[in]		mReversi
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmReversi(self, mReversi):
		self.__mReversi = mReversi

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmSetting()
	#	@param[in]		self
	#	@return			mSetting
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmSetting(self):
		return self.__mSetting

	############################################################################
	#	@brief			セッター
	#	@fn				setmSetting(self, mSetting)
	#	@param[in]		self
	#	@param[in]		mSetting
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmSetting(self, mSetting):
		self.__mSetting = mSetting

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmCurColor(self)
	#	@param[in]		self
	#	@return			mCurColor
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmCurColor(self):
		return self.__mCurColor

	############################################################################
	#	@brief			セッター
	#	@fn				setmCurColor(self, mCurColor)
	#	@param[in]		self
	#	@param[in]		mCurColor
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmCurColor(self, mCurColor):
		self.__mCurColor = mCurColor

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmCpu(self)
	#	@param[in]		self
	#	@return			mCpu
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmCpu(self):
		return self.__mCpu

	############################################################################
	#	@brief			セッター
	#	@fn				setmCpu(self, mCpu)
	#	@param[in]		self
	#	@param[in]		mCpu
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmCpu(self, mCpu):
		self.__mCpu = mCpu

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmEdge(self)
	#	@param[in]		self
	#	@return			mEdge
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmEdge(self):
		return self.__mEdge

	############################################################################
	#	@brief			セッター
	#	@fn				setmEdge(self, mEdge)
	#	@param[in]		self
	#	@param[in]		mEdge
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmEdge(self, mEdge):
		self.__mEdge = mEdge

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmPassEnaB(self)
	#	@param[in]		self
	#	@return			mPassEnaB
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmPassEnaB(self):
		return self.__mPassEnaB

	############################################################################
	#	@brief			セッター
	#	@fn				setmPassEnaB(self, mPassEnaB)
	#	@param[in]		self
	#	@param[in]		mPassEnaB
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmPassEnaB(self, mPassEnaB):
		self.__mPassEnaB = mPassEnaB

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmPassEnaW(self)
	#	@param[in]		self
	#	@return			mPassEnaW
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmPassEnaW(self):
		return self.__mPassEnaW

	############################################################################
	#	@brief			セッター
	#	@fn				setmPassEnaW(self, mPassEnaW)
	#	@param[in]		self
	#	@param[in]		mPassEnaW
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	setmPassEnaW(self, mPassEnaW):
		self.__mPassEnaW = mPassEnaW

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmGameEndSts(self)
	#	@param[in]		self
	#	@return			mGameEndSts
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmGameEndSts(self):
		return self.__mGameEndSts

	############################################################################
	#	@brief			セッター
	#	@fn				setmGameEndSts(self, mGameEndSts)
	#	@param[in]		self
	#	@param[in]		mGameEndSts
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmGameEndSts(self, mGameEndSts):
		self.__mGameEndSts = mGameEndSts

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmPlayLock(self)
	#	@param[in]		self
	#	@return			mPlayLock
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmPlayLock(self):
		return self.__mPlayLock

	############################################################################
	#	@brief			セッター
	#	@fn				setmPlayLock(self, mPlayLock)
	#	@param[in]		self
	#	@param[in]		mPlayLock
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmPlayLock(self, mPlayLock):
		self.__mPlayLock = mPlayLock

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmDelegate(self)
	#	@param[in]		self
	#	@return			mDelegate
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmDelegate(self):
		return self.__mDelegate

	############################################################################
	#	@brief			セッター
	#	@fn				setmDelegate(self, mDelegate)
	#	@param[in]		self
	#	@param[in]		mDelegate
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmDelegate(self, mDelegate):
		self.__mDelegate = mDelegate

	############################################################################
	#	@brief			ゲッター
	#	@fn				getmCallbacks(self)
	#	@param[in]		self
	#	@return			mCallbacks
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def getmCallbacks(self):
		return self.__mCallbacks

	############################################################################
	#	@brief			セッター
	#	@fn				setmCallbacks(self, mCallbacks)
	#	@param[in]		self
	#	@param[in]		mCallbacks
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def setmCallbacks(self, mCallbacks):
		self.__mCallbacks = mCallbacks

	############################################################################
	#	@brief			リバーシプレイ
	#	@fn				reversiPlay(self, y, x)
	#	@param[in]		self
	#	@param[in]		y			Y座標
	#	@param[in]		x			X座標
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def reversiPlay(self, y, x):
		update = 0
		cpuEna = 0
		tmpCol = self.__mCurColor
		pass = 0

		if (self.__mPlayLock == 1): return
		self.__mPlayLock = 1
		if (self.mReversi.getColorEna(self._mCurColor) == 0):
			if (self.mReversi.setMasuSts(self.__mCurColor, y, x) == 0):
				if (self.__mSetting.getmType() == ReversiConst.ReversiConst.DEF_TYPE_HARD) self.__mReversi.AnalysisReversi(self.__mPassEnaB, self.__mPassEnaW)
				if (self.__mSetting.getmAssist() == ReversiConst.ReversiConst.DEF_ASSIST_ON):
					# *** メッセージ送信 ***
					self.execMessage(ReversiConst.ReversiConst.LC_MSG_ERASE_INFO_ALL, None)
				}
				self.sendDrawMsg(y, x)																# 描画
				self.drawUpdate(ReversiConst.ReversiConst.DEF_ASSIST_OFF)							# その他コマ描画
				if (self.__mReversi.getGameEndSts() == 0):
					if (tmpCol == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
						tmpCol = ReversiConst.ReversiConst.REVERSI_STS_WHITE
					else:
						tmpCol = ReversiConst.ReversiConst.REVERSI_STS_BLACK

					if (self.__mReversi.getColorEna(tmpCol) == 0):
						if (self.__mSetting.getmMode() == ReversiConst.ReversiConst.DEF_MODE_ONE):	# CPU対戦
							cpuEna = 1
						else:																		# 二人対戦
							self.__mCurColor = tmpCol
							self.drawUpdate(self.__mSetting.getmAssist())							# 次のプレイヤーコマ描画
					else:
						# *** パスメッセージ ***
						self.reversiPlayPass(tmpCol)
						pass = 1
				else:
					# *** ゲーム終了メッセージ ***
					self.reversiPlayEnd()
				update = 1
			else:
				# *** エラーメッセージ ***
				self.ViewMsgDlgLocal('エラー', 'そのマスには置けません。')
		else:
			if (self.__mReversi.getGameEndSts() == 0):
				if (tmpCol == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
					tmpCol = ReversiConst.ReversiConst.REVERSI_STS_WHITE
				else:
					tmpCol = ReversiConst.ReversiConst.REVERSI_STS_BLACK

				if (self.__mReversi.getColorEna(tmpCol) == 0):
					if (self.__mSetting.getmMode() == ReversiConst.ReversiConst.DEF_MODE_ONE):		# CPU対戦
						update = 1
						cpuEna = 1
					else:																			# 二人対戦
						self.__mCurColor = tmpCol
				else:
					# *** パスメッセージ ***
					self.reversiPlayPass(tmpCol)
					pass = 1
			else:
				# *** ゲーム終了メッセージ ***
				self.reversiPlayEnd()

		if (pass == 1):
			if (self.__mSetting.getmMode() == ReversiConst.ReversiConst.DEF_MODE_ONE):				# CPU対戦
				if (self.__mSetting.getmAssist() == ReversiConst.ReversiConst.DEF_ASSIST_ON):
					# *** メッセージ送信 ***
					self.execMessage(ReversiConst.ReversiConst.LC_MSG_DRAW_INFO_ALL, None)

		if (update == 1):
			waitTime = 0
			if (cpuEna == 1):
				waitTime = self.__mSetting.getmPlayCpuInterVal()
			self.WaitLocal(waitTime)
			self.reversiPlaySub(cpuEna, tmpCol)
			self.__mPlayLock = 0
		else:
			self.__mPlayLock = 0

	############################################################################
	#	@brief			リバーシプレイサブ
	#	@fn				reversiPlaySub(self, cpuEna, tmpCol)
	#	@param[in]		self
	#	@param[in]		cpuEna
	#	@param[in]		tmpCol
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def reversiPlaySub(self, cpuEna, tmpCol):
		ret = 0
		roop = True
		while (True):
			ret = self.reversiPlayCpu(tmpCol, cpuEna)
			cpuEna = 0
			if (ret == 1):
				if (self.__mReversi.getGameEndSts() == 0):
					if (self.__mReversi.getColorEna(self.__mCurColor) != 0):
						# *** パスメッセージ ***
						self.reversiPlayPass(self.__mCurColor)
						cpuEna = 1
				else:
					# *** ゲーム終了メッセージ ***
					self.reversiPlayEnd()
			if (cpuEna == 0):
				break

	############################################################################
	#	@brief			リバーシプレイ終了
	#	@fn				reversiPlayEnd(self)
	#	@param[in]		self
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def reversiPlayEnd(self):
		if (self.__mGameEndSts == 0):
			self.__mGameEndSts = 1
			waitTime = self.gameEndAnimExec()					# 終了アニメ実行
			self.__mPlayLock = 1
			self.WaitLocal(waitTime)
			# *** ゲーム終了メッセージ ***
			tmpMsg1 = ''
			tmpMsg2 = ''
			msgStr = ''
			blk = 0
			whi = 0
			blk = self.__mReversi.getBetCnt(ReversiConst.ReversiConst.REVERSI_STS_BLACK)
			whi = self.__mReversi.getBetCnt(ReversiConst.ReversiConst.REVERSI_STS_WHITE)
			tmpMsg1 = 'プレイヤー1 = ' + str(blk) + ' プレイヤー2 = ' + str(whi)
			if (self.__mSetting.getmMode() == ReversiConst.ReversiConst.DEF_MODE_ONE):
				if (whi == blk):
					tmpMsg2 = '引き分けです。'
				elif (whi < blk):
					if (self.__mCurColor == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
						tmpMsg2 = 'あなたの勝ちです。'
					else:
						tmpMsg2 = 'あなたの負けです。'
				else:
					if (self.__mCurColor == ReversiConst.ReversiConst.REVERSI_STS_WHITE):
						tmpMsg2 = 'あなたの勝ちです。'
					else:
						tmpMsg2 = 'あなたの負けです。'
			else:
				if (whi == blk):
					tmpMsg2 = '引き分けです。'
				elif (whi < blk):
					tmpMsg2 = 'プレイヤー1の勝ちです。'
				else:
					tmpMsg2 = 'プレイヤー2の勝ちです。'

			msgStr = tmpMsg1 + tmpMsg2
			self.ViewMsgDlgLocal('ゲーム終了', msgStr)

			if (self.__mSetting.getmEndAnim() == ReversiConst.ReversiConst.DEF_END_ANIM_ON):
				# *** メッセージ送信 ***
				self.execMessage(ReversiConst.ReversiConst.LC_MSG_CUR_COL, None)
				# *** メッセージ送信 ***
				self.execMessage(ReversiConst.ReversiConst.LC_MSG_CUR_STS, None)

	############################################################################
	#	@brief			リバーシプレイパス
	#	@fn				reversiPlayPass(self, color)
	#	@param[in]		self
	#	@param[in]		color		パス色
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def reversiPlayPass(self, color):
		# *** パスメッセージ ***
		if (self.__mSetting.getmMode() == ReversiConst.ReversiConst.DEF_MODE_ONE):
			if (color == self.__mCurColor):
				self.ViewMsgDlgLocal('', 'あなたはパスです。')
			else:
				self.ViewMsgDlgLocal('', 'CPUはパスです。')
		else:
			if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
				self.ViewMsgDlgLocal('', 'プレイヤー1はパスです。')
			else:
				self.ViewMsgDlgLocal('', 'プレイヤー2はパスです。')

	############################################################################
	#	@brief			リバーシプレイコンピューター
	#	@fn				reversiPlayCpu(self, color, cpuEna)
	#	@param[in]		self
	#	@param[in]		color		CPU色
	#	@param[in]		cpuEna		CPU有効フラグ
	#	@return			ありません
	#	@author			Yuta Yoshinaga
	#	@date			2018.11.13
	#
	############################################################################
	def reversiPlayCpu(self, color, cpuEna):
		update = 0
		setY = 0
		setX = 0

		while (True):
			if (cpuEna == 1):
				cpuEna = 0
				# *** CPU対戦 ***
				pCnt = self.__mReversi.getPointCnt(color)
				pInfo = self.__mReversi.getPoint(color, random.randint(0, pCnt))
				if (pInfo != None):
					setY = pInfo.getY()
					setX = pInfo.getX()
					if (self.__mSetting.getmType() != ReversiConst.ReversiConst.DEF_TYPE_EASY):
						# 強いコンピューター
						cpuflg0 = 0
						cpuflg1 = 0
						cpuflg2 = 0
						cpuflg3 = 0
						mem = -1
						mem2 = -1
						mem3 = -1
						mem4 = -1
						rcnt1 = 0
						rcnt2 = 0
						kadocnt = 0
						loop = self.__mSetting.getmMasuCnt() * self.__mSetting.getmMasuCnt()
						pcnt = 0
						passCnt = 0
						if (color == ReversiConst.ReversiConst.REVERSI_STS_BLACK):
							othColor = ReversiConst.ReversiConst.REVERSI_STS_WHITE
						else:
							othColor = ReversiConst.ReversiConst.REVERSI_STS_BLACK
						othBet = self.__mReversi.getBetCnt(othColor)				# 対戦相手のコマ数
						ownBet = self.__mReversi.getBetCnt(color)					# 自分のコマ数
						endZone = 0
						if ((loop - (othBet + ownBet)) <= 16): endZone = 1			# ゲーム終盤フラグON
						for i in range(loop):
							self.__mCpu[i].setX(0)
							self.__mCpu[i].setY (0)
							self.__mEdge[i].setX(0)
							self.__mEdge[i].setY(0)

						for i in range(self.__mSetting.getmMasuCnt()):
							for j in range(self.__mSetting.getmMasuCnt()):
								if (self.__mReversi.getMasuStsEna(color, i, j) != 0):
									# *** 角の一つ手前なら別のとこに格納 *** //
									if (self.__mReversi.getEdgeSideOne(i, j) == 0):
										self.__mEdge[kadocnt].setX(j)
										self.__mEdge[kadocnt].setY(i)
										kadocnt += 1
									else:
										self.__mCpu[rcnt1].setX(j)
										self.__mCpu[rcnt1].setY(i)
										rcnt1 += 1

									if (self.__mSetting.getmType() == ReversiConst.ReversiConst.DEF_TYPE_NOR):
										# *** 角に置けるなら優先的にとらせるため場所を記憶させる ***
										if (self.__mReversi.getEdgeSideZero(i, j) == 0):
											cpuflg1 = 1
											rcnt2 = (rcnt1 - 1)
										# *** 角の二つ手前も優先的にとらせるため場所を記憶させる ***
										if (cpuflg1 == 0):
											if (self.__mReversi.getEdgeSideTwo(i, j) == 0):
												cpuflg2 = 1
												rcnt2 = (rcnt1 - 1)
										# *** 角の三つ手前も優先的にとらせるため場所を記憶させる ***
										if (cpuflg1 == 0 and cpuflg2 == 0):
											if (self.__mReversi.getEdgeSideThree(i, j) == 0):
												cpuflg0 = 1
												rcnt2 = (rcnt1 - 1)
									# *** パーフェクトゲームなら ***
									if (self.__mReversi.getMasuStsCnt(color, i, j) == othBet):
										setY = i
										setX = j
										pcnt = 1
									# *** 相手をパスさせるなら ***
									if (pcnt == 0):
										if (self.__mReversi.getPassEna(color, i, j) != 0):
											setY = i
											setX = j
											passCnt = 1

						if (pcnt == 0 and passCnt == 0):
							badPoint = -1
							goodPoint = -1
							pointCnt = -1
							ownPointCnt = -1
							tmpAnz = None
							if (rcnt1 != 0):
								for i in range(rcnt1):
									if (self.__mSetting.getmType() == ReversiConst.ReversiConst.DEF_TYPE_HARD):
										tmpAnz = self.__mReversi.getPointAnz(color, self.__mCpu[i].getY(), self.__mCpu[i].getX())
										if (tmpAnz != None):
											if (badPoint == -1):
												badPoint = tmpAnz.getBadPoint()
												goodPoint = tmpAnz.getGoodPoint()
												pointCnt = tmpAnz.getPointCnt()
												ownPointCnt = tmpAnz.getOwnPointCnt()
												mem2 = i
												mem3 = i
												mem4 = i
											else:
												if (tmpAnz.getBadPoint() < badPoint):
													badPoint = tmpAnz.getBadPoint()
													mem2 = i
												if (goodPoint < tmpAnz.getGoodPoint()):
													goodPoint = tmpAnz.getGoodPoint()
													mem3 = i
												if (tmpAnz.getPointCnt() < pointCnt):
													pointCnt = tmpAnz.getPointCnt()
													ownPointCnt = tmpAnz.getOwnPointCnt()
													mem4 = i
												elif (tmpAnz.getPointCnt() == pointCnt):
													if (ownPointCnt < tmpAnz.getOwnPointCnt()):
														ownPointCnt = tmpAnz.getOwnPointCnt()
														mem4 = i
									if (self.__mReversi.getMasuStsEna(color, self.__mCpu[i].getY(), self.__mCpu[i].getX()) == 2):
										mem = i

								if (mem2 != -1):
									if (endZone != 0):								# 終盤なら枚数重視
										if (mem3 != -1):
											mem2 = mem3
									else:
										if (mem4 != -1):
											mem2 = mem4
									mem = mem2
								if (mem == -1): mem = random.randint(0, rcnt1)
							elif (kadocnt != 0):
								for i in range(kadocnt):
									if (self.__mSetting.getmType() == ReversiConst.ReversiConst.DEF_TYPE_HARD) {
										tmpAnz = self.__mReversi.getPointAnz(color, self.__mEdge[i].getY(), self.__mEdge[i].getX())
										if (tmpAnz != null):
											if (badPoint == -1):
												badPoint = tmpAnz.getBadPoint()
												goodPoint = tmpAnz.getGoodPoint()
												pointCnt = tmpAnz.getPointCnt()
												ownPointCnt = tmpAnz.getOwnPointCnt()
												mem2 = i
												mem3 = i
												mem4 = i
											else:
												if (tmpAnz.getBadPoint() < badPoint):
													badPoint = tmpAnz.getBadPoint()
													mem2 = i
												if (goodPoint < tmpAnz.getGoodPoint()):
													goodPoint = tmpAnz.getGoodPoint()
													mem3 = i
												if (tmpAnz.getPointCnt() < pointCnt):
													pointCnt = tmpAnz.getPointCnt()
													ownPointCnt = tmpAnz.getOwnPointCnt()
													mem4 = i
												elif (tmpAnz.getPointCnt() == pointCnt):
													if (ownPointCnt < tmpAnz.getOwnPointCnt()):
														ownPointCnt = tmpAnz.getOwnPointCnt()
														mem4 = i
									if (self.__mReversi.getMasuStsEna(color, self.__mEdge[i].getY(), self.__mEdge[i].getX()) == 2):
										mem = i
								if (mem2 != -1):
									if (endZone != 0):								# 終盤なら枚数重視
										if (mem3 != -1):
											mem2 = mem3
									else:
										if (mem4 != -1):
											mem2 = mem4
									mem = mem2
								if (mem == -1): mem = random.randint(0, kadocnt)
								# *** 置いても平気な角があればそこに置く***
								for i in range(kadocnt):
									if (self.__mReversi.checkEdge(color, self.__mEdge[i].getY(), self.__mEdge[i].getX()) != 0):
										if ((cpuflg0 == 0) and (cpuflg1 == 0) and (cpuflg2 == 0)):
											cpuflg3 = 1
											rcnt2 = i
							if ((cpuflg1 == 0) and (cpuflg2 == 0) and (cpuflg0 == 0) and (cpuflg3 == 0)):
								rcnt2 = mem
							if (rcnt1 != 0):
								setY = self.__mCpu[rcnt2].getY()
								setX = self.__mCpu[rcnt2].getX()
							elif (kadocnt != 0):
								setY = self.__mEdge[rcnt2].getY()
								setX = self.__mEdge[rcnt2].getX()

					if (self.__mReversi.setMasuSts(color, setY, setX) == 0):
						if (self.__mSetting.getmType() == ReversiConst.ReversiConst.DEF_TYPE_HARD):
							self.__mReversi.AnalysisReversi(self.__mPassEnaB, self.__mPassEnaW)
						self.sendDrawMsg(setY, setX)								# 描画
						update = 1
			else:
				break

		if (update == 1):
			self.drawUpdate(ReversiConst.ReversiConst.DEF_ASSIST_OFF)
			if (self.__mSetting.getmAssist() == ReversiConst.ReversiConst.DEF_ASSIST_ON):
				# *** メッセージ送信 ***
				self.execMessage(ReversiConst.LC_MSG_DRAW_INFO_ALL, None)
		return update

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			マス描画更新
	///	@fn				void drawUpdate(int assist)
	///	@param[in]		int assist	アシスト設定
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void drawUpdate(int assist)
	{
		if (assist == ReversiConst.DEF_ASSIST_ON) {
			for (int i = 0 i < this.mSetting.getmMasuCnt() i++) {
				for (int j = 0 j < this.mSetting.getmMasuCnt() j++) {
					this.sendDrawInfoMsg(i, j)
				}
			}
		}
		int waitTime = this.mSetting.getmPlayDrawInterVal()
		for (int i = 0 i < this.mSetting.getmMasuCnt() i++) {
			for (int j = 0 j < this.mSetting.getmMasuCnt() j++) {
				if(this.mReversi.getMasuSts(i,j) != this.mReversi.getMasuStsOld(i,j)){
					this.WaitLocal(waitTime)
					this.sendDrawMsg(i, j)
				}
			}
		}
		// *** メッセージ送信 *** //
		this.execMessage(ReversiConst.LC_MSG_CUR_COL, null)
		// *** メッセージ送信 *** //
		this.execMessage(ReversiConst.LC_MSG_CUR_STS, null)
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			マス描画強制更新
	///	@fn				void drawUpdateForcibly(int assist)
	///	@param[in]		int assist	アシスト設定
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void drawUpdateForcibly(int assist)
	{
		// *** メッセージ送信 *** //
		this.execMessage(ReversiConst.LC_MSG_DRAW_ALL, null)
		if (assist == ReversiConst.DEF_ASSIST_ON) {
			// *** メッセージ送信 *** //
			this.execMessage(ReversiConst.LC_MSG_DRAW_INFO_ALL, null)
		} else {
			// *** メッセージ送信 *** //
			this.execMessage(ReversiConst.LC_MSG_ERASE_INFO_ALL, null)
		}
		// *** メッセージ送信 *** //
		this.execMessage(ReversiConst.LC_MSG_CUR_COL, null)
		// *** メッセージ送信 *** //
		this.execMessage(ReversiConst.LC_MSG_CUR_STS, null)
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			リセット処理
	///	@fn				void reset()
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void reset()
	{
		this.mPassEnaB = 0
		this.mPassEnaW = 0
		if (this.mSetting.getmGameSpd() == ReversiConst.DEF_GAME_SPD_FAST) {
			this.mSetting.setmPlayDrawInterVal(ReversiConst.DEF_GAME_SPD_FAST_VAL)					// 描画のインターバル(msec)
			this.mSetting.setmPlayCpuInterVal(ReversiConst.DEF_GAME_SPD_FAST_VAL2)					// CPU対戦時のインターバル(msec)
		} else if (this.mSetting.getmGameSpd() == ReversiConst.DEF_GAME_SPD_MID) {
			this.mSetting.setmPlayDrawInterVal( ReversiConst.DEF_GAME_SPD_MID_VAL)					// 描画のインターバル(msec)
			this.mSetting.setmPlayCpuInterVal(ReversiConst.DEF_GAME_SPD_MID_VAL2)					// CPU対戦時のインターバル(msec)
		} else {
			this.mSetting.setmPlayDrawInterVal(ReversiConst.DEF_GAME_SPD_SLOW_VAL)					// 描画のインターバル(msec)
			this.mSetting.setmPlayCpuInterVal(ReversiConst.DEF_GAME_SPD_SLOW_VAL2)					// CPU対戦時のインターバル(msec)
		}

		this.mCurColor = this.mSetting.getmPlayer()
		if (this.mSetting.getmMode() == ReversiConst.DEF_MODE_TWO) this.mCurColor = ReversiConst.REVERSI_STS_BLACK

		this.mReversi.setMasuCnt(this.mSetting.getmMasuCnt())										// マスの数設定

		this.mReversi.reset()
		if (this.mSetting.getmMode() == ReversiConst.DEF_MODE_ONE) {
			if (this.mCurColor == ReversiConst.REVERSI_STS_WHITE) {
				int pCnt = this.mReversi.getPointCnt(ReversiConst.REVERSI_STS_BLACK)
				ReversiPoint pInfo = this.mReversi.getPoint(ReversiConst.REVERSI_STS_BLACK, r.nextInt(pCnt))
				if (pInfo != null) {
					this.mReversi.setMasuSts(ReversiConst.REVERSI_STS_BLACK, pInfo.getY(), pInfo.getX())
					if (this.mSetting.getmType() == ReversiConst.DEF_TYPE_HARD) this.mReversi.AnalysisReversi(this.mPassEnaB, this.mPassEnaW)
				}
			}
		}

		this.mPlayLock = 1
		this.mGameEndSts = 0

		this.drawUpdateForcibly(this.mSetting.getmAssist())

		// *** 終了通知 *** //
		// *** メッセージ送信 *** //
		this.execMessage(ReversiConst.LC_MSG_DRAW_END, null)
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			ゲーム終了アニメーション
	///	@fn				int gameEndAnimExec()
	///	@return			ウェイト時間
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public int gameEndAnimExec()
	{
		int bCnt, wCnt
		int ret = 0

		if (this.mSetting.getmEndAnim() == ReversiConst.DEF_END_ANIM_ON) {
			bCnt = this.mReversi.getBetCnt(ReversiConst.REVERSI_STS_BLACK)
			wCnt = this.mReversi.getBetCnt(ReversiConst.REVERSI_STS_WHITE)

			// *** 色、コマ数表示消去 *** //
			// *** メッセージ送信 *** //
			this.execMessage(ReversiConst.LC_MSG_CUR_COL_ERASE, null)
			// *** メッセージ送信 *** //
			this.execMessage(ReversiConst.LC_MSG_CUR_STS_ERASE, null)

			this.WaitLocal(this.mSetting.getmEndInterVal())
			// *** マス消去 *** //
			for (int i = 0 i < this.mSetting.getmMasuCnt() i++) {
				for (int j = 0 j < this.mSetting.getmMasuCnt() j++) {
					this.mReversi.setMasuStsForcibly(ReversiConst.REVERSI_STS_NONE, i, j)
				}
			}
			// *** メッセージ送信 *** //
			this.execMessage(ReversiConst.LC_MSG_ERASE_ALL, null)

			// *** マス描画 *** //
			int bCnt2, wCnt2, bEnd, wEnd
			bCnt2 = 0
			wCnt2 = 0
			bEnd = 0
			wEnd = 0
			for (int i = 0 i < this.mSetting.getmMasuCnt() i++) {
				for (int j = 0 j < this.mSetting.getmMasuCnt() j++) {
					if (bCnt2 < bCnt) {
						bCnt2++
						this.mReversi.setMasuStsForcibly(ReversiConst.REVERSI_STS_BLACK, i, j)
						this.sendDrawMsg(i, j)
					} else {
						bEnd = 1
					}
					if (wCnt2 < wCnt) {
						wCnt2++
						this.mReversi.setMasuStsForcibly(ReversiConst.REVERSI_STS_WHITE, (this.mSetting.getmMasuCnt() - 1) - i, (this.mSetting.getmMasuCnt() - 1) - j)
						this.sendDrawMsg((this.mSetting.getmMasuCnt() - 1) - i, (this.mSetting.getmMasuCnt() - 1) - j)
					} else {
						wEnd = 1
					}
					if (bEnd == 1 and wEnd == 1) {
						break
					}else{
						this.WaitLocal(this.mSetting.getmEndDrawInterVal())
					}
				}
			}
			ret = 0
		}
		return ret
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			描画メッセージ送信
	///	@fn				void sendDrawMsg(int y, int x)
	///	@param[in]		int y			Y座標
	///	@param[in]		int x			X座標
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void sendDrawMsg(int y, int x)
	{
		ReversiPoint mTmpPoint = new ReversiPoint()
		mTmpPoint.setY(y)
		mTmpPoint.setX(x)
		// *** メッセージ送信 *** //
		this.execMessage(ReversiConst.LC_MSG_DRAW, mTmpPoint)
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			情報描画メッセージ送信
	///	@fn				void sendDrawInfoMsg(int y, int x)
	///	@param[in]		int y			Y座標
	///	@param[in]		int x			X座標
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void sendDrawInfoMsg(int y, int x)
	{
		ReversiPoint mTmpPoint = new ReversiPoint()
		mTmpPoint.setY(y)
		mTmpPoint.setX(x)
		// *** メッセージ送信 *** //
		this.execMessage(ReversiConst.LC_MSG_DRAW_INFO, mTmpPoint)
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			メッセージ
	///	@fn				void execMessage(int what, Object obj)
	///	@param[in]		int what
	///	@param[in]		Object obj
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	private void execMessage(int what, Object obj)
	{
		int dMode, dBack, dCnt
		if (what == ReversiConst.LC_MSG_DRAW) {
			// *** マス描画 *** //
			ReversiPoint msgPoint = (ReversiPoint)obj
			dMode = this.mReversi.getMasuSts(msgPoint.getY(), msgPoint.getX())
			dBack = this.mReversi.getMasuStsEna(this.mCurColor, msgPoint.getY(), msgPoint.getX())
			dCnt = this.mReversi.getMasuStsCnt(this.mCurColor, msgPoint.getY(), msgPoint.getX())
			this.DrawSingleLocal(msgPoint.getY(), msgPoint.getX(), dMode, dBack, String.valueOf(dCnt))
		} else if (what == ReversiConst.LC_MSG_ERASE) {
			// *** マス消去 *** //
			ReversiPoint msgPoint = (ReversiPoint)obj
			this.DrawSingleLocal(msgPoint.getY(), msgPoint.getX(), 0, 0, "0")
		} else if (what == ReversiConst.LC_MSG_DRAW_INFO) {
			// *** マス情報描画 *** //
			ReversiPoint msgPoint = (ReversiPoint)obj
			dMode = this.mReversi.getMasuSts(msgPoint.getY(), msgPoint.getX())
			dBack = this.mReversi.getMasuStsEna(this.mCurColor, msgPoint.getY(), msgPoint.getX())
			dCnt = this.mReversi.getMasuStsCnt(this.mCurColor, msgPoint.getY(), msgPoint.getX())
			this.DrawSingleLocal(msgPoint.getY(), msgPoint.getX(), dMode, dBack, String.valueOf(dCnt))
		} else if (what == ReversiConst.LC_MSG_ERASE_INFO) {
			// *** マス情報消去 *** //
			ReversiPoint msgPoint = (ReversiPoint)obj
			dMode = this.mReversi.getMasuSts(msgPoint.getY(), msgPoint.getX())
			this.DrawSingleLocal(msgPoint.getY(), msgPoint.getX(), dMode, 0, "0")
		} else if (what == ReversiConst.LC_MSG_DRAW_ALL) {
			// *** 全マス描画 *** //
			for (int i = 0 i < this.mSetting.getmMasuCnt() i++) {
				for (int j = 0 j < this.mSetting.getmMasuCnt() j++) {
					dMode = this.mReversi.getMasuSts(i, j)
					dBack = this.mReversi.getMasuStsEna(this.mCurColor, i, j)
					dCnt = this.mReversi.getMasuStsCnt(this.mCurColor, i, j)
					this.DrawSingleLocal(i, j, dMode, dBack, String.valueOf(dCnt))
				}
			}
		} else if (what == ReversiConst.LC_MSG_ERASE_ALL) {
			// *** 全マス消去 *** //
			for (int i = 0 i < this.mSetting.getmMasuCnt() i++) {
				for (int j = 0 j < this.mSetting.getmMasuCnt() j++) {
					this.DrawSingleLocal(i, j, 0, 0, "0")
				}
			}
		} else if (what == ReversiConst.LC_MSG_DRAW_INFO_ALL) {
			// *** 全マス情報描画 *** //
			for (int i = 0 i < this.mSetting.getmMasuCnt() i++) {
				for (int j = 0 j < this.mSetting.getmMasuCnt() j++) {
					dMode = this.mReversi.getMasuSts(i, j)
					dBack = this.mReversi.getMasuStsEna(this.mCurColor, i, j)
					dCnt = this.mReversi.getMasuStsCnt(this.mCurColor, i, j)
					this.DrawSingleLocal(i, j, dMode, dBack, String.valueOf(dCnt))
				}
			}
		} else if (what == ReversiConst.LC_MSG_ERASE_INFO_ALL) {
			// *** 全マス情報消去 *** //
			for (int i = 0 i < this.mSetting.getmMasuCnt() i++) {
				for (int j = 0 j < this.mSetting.getmMasuCnt() j++) {
					dMode = this.mReversi.getMasuSts(i, j)
					this.DrawSingleLocal(i, j, dMode, 0, "0")
				}
			}
		} else if (what == ReversiConst.LC_MSG_DRAW_END) {
			this.mPlayLock = 0
		} else if (what == ReversiConst.LC_MSG_CUR_COL) {
			String tmpStr = ""
			if (this.mSetting.getmMode() == ReversiConst.DEF_MODE_ONE) {
				if (this.mCurColor == ReversiConst.REVERSI_STS_BLACK) tmpStr = "あなたはプレイヤー1です "
				else tmpStr = "あなたはプレイヤー2です "
			} else {
				if (this.mCurColor == ReversiConst.REVERSI_STS_BLACK) tmpStr = "プレイヤー1の番です "
				else tmpStr = "プレイヤー2の番です "
			}
			this.CurColMsgLocal(tmpStr)
		} else if (what == ReversiConst.LC_MSG_CUR_COL_ERASE) {
			this.CurColMsgLocal("")
		} else if (what == ReversiConst.LC_MSG_CUR_STS) {
			String tmpStr = "プレイヤー1 = " + this.mReversi.getBetCnt(ReversiConst.REVERSI_STS_BLACK) + " プレイヤー2 = " + this.mReversi.getBetCnt(ReversiConst.REVERSI_STS_WHITE)
			this.CurStsMsgLocal(tmpStr)
		} else if (what == ReversiConst.LC_MSG_CUR_STS_ERASE) {
			this.CurStsMsgLocal("")
		} else if (what == ReversiConst.LC_MSG_MSG_DLG) {
		} else if (what == ReversiConst.LC_MSG_DRAW_ALL_RESET) {
		}
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			メッセージダイアログ
	///	@fn				void ViewMsgDlgLocal(String title , String msg)
	///	@param[in]		String title	タイトル
	///	@param[in]		String msg		メッセージ
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	private void ViewMsgDlgLocal(String title , String msg)
	{
		if(this.mDelegate != null) this.mCallbacks.getFuncs().add(this.mDelegate.ViewMsgDlg(title, msg))
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			1マス描画
	///	@fn				void DrawSingleLocal(int y, int x, int sts, int bk, String text)
	///	@param[in]		int y		Y座標
	///	@param[in]		int x		X座標
	///	@param[in]		int sts		ステータス
	///	@param[in]		int bk		背景
	///	@param[in]		String text	テキスト
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	private void DrawSingleLocal(int y, int x, int sts, int bk, String text)
	{
		if(this.mDelegate != null) this.mCallbacks.getFuncs().add(this.mDelegate.DrawSingle(y, x, sts, bk, text))
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			現在の色メッセージ
	///	@fn				void CurColMsgLocal(String text)
	///	@param[in]		String text	テキスト
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	private void CurColMsgLocal(String text)
	{
		if(this.mDelegate != null) this.mCallbacks.getFuncs().add(this.mDelegate.CurColMsg(text))
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			現在のステータスメッセージ
	///	@fn				void CurStsMsgLocal(String text)
	///	@param[in]		String text	テキスト
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	private void CurStsMsgLocal(String text)
	{
		if(this.mDelegate != null) this.mCallbacks.getFuncs().add(this.mDelegate.CurStsMsg(text))
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			ウェイト
	///	@fn				void WaitLocal(int time)
	///	@param[in]		int time	ウェイト時間(msec)
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	private void WaitLocal(int time)
	{
		if(this.mDelegate != null) this.mCallbacks.getFuncs().add(this.mDelegate.Wait(time))
	}

	private Reversi mReversi								//!< リバーシクラス
	private ReversiSetting mSetting						//!< リバーシ設定クラス
	private int mCurColor									//!< 現在の色
	private ReversiPoint[] mCpu							//!< CPU用ワーク
	private ReversiPoint[] mEdge							//!< CPU用角マスワーク
	private int mPassEnaB									//!< 黒のパス有効フラグ
	private int mPassEnaW									//!< 白のパス有効フラグ
	private int mGameEndSts								//!< ゲーム終了ステータス
	private int mPlayLock									//!< プレイロック
	private ReversiPlayDelegate mDelegate					//!< デリゲート
	private CallbacksJson mCallbacks						//!< コールバック

