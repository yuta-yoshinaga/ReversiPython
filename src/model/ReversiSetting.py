################################################################################
#	@file			ReversiSetting.py
#	@brief			アプリ設定クラス
#	@author			Yuta Yoshinaga
#	@date			2018.11.07
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

import ReversiConst

################################################################################
#	@class		ReversiSetting
#	@brief		アプリ設定クラス
#
################################################################################


class ReversiSetting:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@param[in]		min
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def __init__(self):
        self.reset()

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmMode(self)
    #	@param[in]		self
    #	@return			mMode
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmMode(self):
        return self.__mMode

    ############################################################################
    #	@brief			セッター
    #	@fn				setmMode(self, mMode)
    #	@param[in]		self
    #	@param[in]		mMode
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmMode(self, mMode):
        self.__mMode = mMode

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmType(self)
    #	@param[in]		self
    #	@return			mType
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmType(self):
        return self.__mType

    ############################################################################
    #	@brief			セッター
    #	@fn				setmType(self, mType)
    #	@param[in]		self
    #	@param[in]		mType
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmType(self, mType):
        self.__mType = mType

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmPlayer(self)
    #	@param[in]		self
    #	@return			mPlayer
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmPlayer(self):
        return self.__mPlayer

    ############################################################################
    #	@brief			セッター
    #	@fn				setmPlayer(self, mPlayer)
    #	@param[in]		self
    #	@param[in]		mPlayer
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmPlayer(self, mPlayer):
        self.__mPlayer = mPlayer

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmAssist(self)
    #	@param[in]		self
    #	@return			mAssist
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmAssist(self):
        return self.__mAssist

    ############################################################################
    #	@brief			セッター
    #	@fn				setmAssist(self, mAssist)
    #	@param[in]		self
    #	@param[in]		mAssist
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmAssist(self, mAssist):
        self.__mAssist = mAssist

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmGameSpd(self)
    #	@param[in]		self
    #	@return			int mGameSpd
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmGameSpd(self):
        return self.__mGameSpd

    ############################################################################
    #	@brief			セッター
    #	@fn				setmGameSpd(self, mGameSpd)
    #	@param[in]		self
    #	@param[in]		mGameSpd
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmGameSpd(self, mGameSpd):
        self.__mGameSpd = mGameSpd

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmEndAnim(self)
    #	@param[in]		self
    #	@return			mEndAnim
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmEndAnim(self):
        return self.__mEndAnim

    ############################################################################
    #	@brief			セッター
    #	@fn				setmEndAnim(self, mEndAnim)
    #	@param[in]		self
    #	@param[in]		mEndAnim
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmEndAnim(self, mEndAnim):
        self.__mEndAnim = mEndAnim

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmMasuCntMenu(self)
    #	@param[in]		self
    #	@return			mMasuCntMenu
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmMasuCntMenu(self):
        return self.__mMasuCntMenu

    ############################################################################
    #	@brief			セッター
    #	@fn				setmMasuCntMenu(self, mMasuCntMenu)
    #	@param[in]		self
    #	@param[in]		mMasuCntMenu
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmMasuCntMenu(self, mMasuCntMenu):
        self.__mMasuCntMenu = mMasuCntMenu

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmMasuCnt(self)
    #	@param[in]		self
    #	@return			mMasuCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
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
    #	@date			2018.11.07
    #
    ############################################################################
    def setmMasuCnt(self, mMasuCnt):
        self.__mMasuCnt = mMasuCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmPlayCpuInterVal(self)
    #	@param[in]		self
    #	@return			mPlayCpuInterVal
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmPlayCpuInterVal(self):
        return self.__mPlayCpuInterVal

    ############################################################################
    #	@brief			セッター
    #	@fn				setmPlayCpuInterVal(self, mPlayCpuInterVal)
    #	@param[in]		self
    #	@param[in]		mPlayCpuInterVal
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmPlayCpuInterVal(self, mPlayCpuInterVal):
        self.__mPlayCpuInterVal = mPlayCpuInterVal

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmPlayDrawInterVal(self)
    #	@param[in]		self
    #	@return			mPlayDrawInterVal
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmPlayDrawInterVal(self):
        return self.__mPlayDrawInterVal

    ############################################################################
    #	@brief			セッター
    #	@fn				setmPlayDrawInterVal(self, mPlayDrawInterVal)
    #	@param[in]		self
    #	@param[in]		mPlayDrawInterVal
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmPlayDrawInterVal(self, mPlayDrawInterVal):
        self.__mPlayDrawInterVal = mPlayDrawInterVal

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmEndDrawInterVal(self)
    #	@param[in]		self
    #	@return			mEndDrawInterVal
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmEndDrawInterVal(self):
        return self.__mEndDrawInterVal

    ############################################################################
    #	@brief			セッター
    #	@fn				setmEndDrawInterVal(self, mEndDrawInterVal)
    #	@param[in]		self
    #	@param[in]		mEndDrawInterVal
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmEndDrawInterVal(self, mEndDrawInterVal):
        self.__mEndDrawInterVal = mEndDrawInterVal

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmEndInterVal(self)
    #	@param[in]		self
    #	@return			mEndInterVal
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmEndInterVal(self):
        return self.__mEndInterVal

    ############################################################################
    #	@brief			セッター
    #	@fn				setmEndInterVal(self, mEndInterVal)
    #	@param[in]		self
    #	@param[in]		mEndInterVal
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmEndInterVal(self, mEndInterVal):
        self.__mEndInterVal = mEndInterVal

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmPlayerColor1(self)
    #	@param[in]		self
    #	@return			mPlayerColor1
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmPlayerColor1(self):
        return self.__mPlayerColor1

    ############################################################################
    #	@brief			セッター
    #	@fn				setmPlayerColor1(self, mPlayerColor1)
    #	@param[in]		self
    #	@param[in]		mPlayerColor1
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmPlayerColor1(self, mPlayerColor1):
        self.__mPlayerColor1 = mPlayerColor1

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmPlayerColor2(self)
    #	@param[in]		self
    #	@return			mPlayerColor2
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmPlayerColor2(self):
        return self.__mPlayerColor2

    ############################################################################
    #	@brief			セッター
    #	@fn				setmPlayerColor2(self, mPlayerColor2)
    #	@param[in]		self
    #	@param[in]		mPlayerColor2
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmPlayerColor2(self, mPlayerColor2):
        self.__mPlayerColor2 = mPlayerColor2

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmBackGroundColor(self)
    #	@param[in]		self
    #	@return			mBackGroundColor
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmBackGroundColor(self):
        return self.__mBackGroundColor

    ############################################################################
    #	@brief			セッター
    #	@fn				setmBackGroundColor(self, mBackGroundColor)
    #	@param[in]		self
    #	@param[in]		mBackGroundColor
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmBackGroundColor(self, mBackGroundColor):
        self.__mBackGroundColor = mBackGroundColor

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getmBorderColor(self)
    #	@param[in]		self
    #	@return			mBorderColor
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def getmBorderColor(self):
        return self.__mBorderColor

    ############################################################################
    #	@brief			セッター
    #	@fn				setmBorderColor(self, mBorderColor)
    #	@param[in]		self
    #	@param[in]		mBorderColor
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def setmBorderColor(self, mBorderColor):
        self.__mBorderColor = mBorderColor

    ############################################################################
    #	@brief			リセット
    #	@fn				reset(self)
    #	@param[in]		self
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.07
    #
    ############################################################################
    def reset(self):
        self.__mMode = ReversiConst.ReversiConst.DEF_MODE_ONE
        self.__mType = ReversiConst.ReversiConst.DEF_TYPE_HARD
        self.__mPlayer = ReversiConst.ReversiConst.REVERSI_STS_BLACK
        self.__mAssist = ReversiConst.ReversiConst.DEF_ASSIST_ON
        self.__mGameSpd = ReversiConst.ReversiConst.DEF_GAME_SPD_MID
        self.__mEndAnim = ReversiConst.ReversiConst.DEF_END_ANIM_ON
        self.__mMasuCntMenu = ReversiConst.ReversiConst.DEF_MASU_CNT_8
        self.__mMasuCnt = ReversiConst.ReversiConst.DEF_MASU_CNT_8_VAL
        self.__mPlayCpuInterVal = ReversiConst.ReversiConst.DEF_GAME_SPD_MID_VAL2
        self.__mPlayDrawInterVal = ReversiConst.ReversiConst.DEF_GAME_SPD_MID_VAL
        self.__mEndDrawInterVal = 100
        self.__mEndInterVal = 500
        self.__mPlayerColor1 = "#000000"
        self.__mPlayerColor2 = "#FFFFFF"
        self.__mBackGroundColor = "#00FF00"
        self.__mBorderColor = "#000000"

    mMode = property(getmMode, setmMode)  # !< 現在のモード
    mType = property(getmType, setmType)  # !< 現在のタイプ
    mPlayer = property(getmPlayer, setmPlayer)  # !< プレイヤーの色
    mAssist = property(getmAssist, setmAssist)  # !< アシスト
    mGameSpd = property(getmGameSpd, setmGameSpd)  # !< ゲームスピード
    mEndAnim = property(getmEndAnim, setmEndAnim)  # !< ゲーム終了アニメーション
    mMasuCntMenu = property(getmMasuCntMenu, setmMasuCntMenu)  # !< マスの数
    mMasuCnt = property(getmMasuCnt, setmMasuCnt)  # !< マスの数
    mPlayCpuInterVal = property(getmPlayCpuInterVal, setmPlayCpuInterVal)  # !< CPU対戦時のインターバル(msec)
    mPlayDrawInterVal = property(getmPlayDrawInterVal, setmPlayDrawInterVal)  # !< 描画のインターバル(msec)
    mEndDrawInterVal = property(getmEndDrawInterVal, setmEndDrawInterVal) # !< 終了アニメーション描画のインターバル(msec)
    mEndInterVal = property(getmEndInterVal, setmEndInterVal) # !< 終了アニメーションのインターバル(msec)
    mPlayerColor1 = property(getmPlayerColor1, setmPlayerColor1)  # !< プレイヤー1の色
    mPlayerColor2 = property(getmPlayerColor2, setmPlayerColor2)  # !< プレイヤー2の色
    mBackGroundColor = property(getmBackGroundColor, setmBackGroundColor)  # !< 背景の色
    mBorderColor = property(getmBorderColor, setmBorderColor)  # !< 枠線の色
