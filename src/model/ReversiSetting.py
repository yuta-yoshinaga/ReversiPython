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

################################################################################
#	@class		ReversiSetting
#	@brief		アプリ設定クラス
#
################################################################################
class ReversiSetting

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
		self.__mMode = mMode;

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
	#	@date			2018.04.01
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
	#	@date			2018.04.01
	#
    ############################################################################
	def setmEndDrawInterVal(self, mEndDrawInterVal):
		self.__mEndDrawInterVal = mEndDrawInterVal

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			ゲッター
	///	@fn				int getmEndInterVal()
	///	@return			int mEndInterVal
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public int getmEndInterVal() {
		return mEndInterVal;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			セッター
	///	@fn				void setmEndInterVal(int mEndInterVal)
	///	@param[in]		int mEndInterVal
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void setmEndInterVal(int mEndInterVal) {
		this.mEndInterVal = mEndInterVal;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			ゲッター
	///	@fn				String getmPlayerColor1()
	///	@return			String mPlayerColor1
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public String getmPlayerColor1() {
		return mPlayerColor1;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			セッター
	///	@fn				void setmPlayerColor1(String mPlayerColor1)
	///	@param[in]		String mPlayerColor1
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void setmPlayerColor1(String mPlayerColor1) {
		this.mPlayerColor1 = mPlayerColor1;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			ゲッター
	///	@fn				String getmPlayerColor2()
	///	@return			String mPlayerColor2
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public String getmPlayerColor2() {
		return mPlayerColor2;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			セッター
	///	@fn				void setmPlayerColor2(String mPlayerColor2)
	///	@param[in]		String mPlayerColor2
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void setmPlayerColor2(String mPlayerColor2) {
		this.mPlayerColor2 = mPlayerColor2;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			ゲッター
	///	@fn				String getmBackGroundColor()
	///	@return			String mBackGroundColor
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public String getmBackGroundColor() {
		return mBackGroundColor;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			セッター
	///	@fn				void setmBackGroundColor(String mBackGroundColor)
	///	@param[in]		String mBackGroundColor
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void setmBackGroundColor(String mBackGroundColor) {
		this.mBackGroundColor = mBackGroundColor;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			ゲッター
	///	@fn				String getmBorderColor()
	///	@return			String mBorderColor
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public String getmBorderColor() {
		return mBorderColor;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			セッター
	///	@fn				void setmBorderColor(String mBorderColor)
	///	@param[in]		String mBorderColor
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2018.04.01
	///
	////////////////////////////////////////////////////////////////////////////////
	public void setmBorderColor(String mBorderColor) {
		this.mBorderColor = mBorderColor;
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			コンストラクタ
	///	@fn				ReversiSetting()
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2017.10.20
	///
	////////////////////////////////////////////////////////////////////////////////
	public ReversiSetting()
	{
		this.reset();
	}

	////////////////////////////////////////////////////////////////////////////////
	///	@brief			リセット
	///	@fn				void reset()
	///	@return			ありません
	///	@author			Yuta Yoshinaga
	///	@date			2017.10.20
	///
	////////////////////////////////////////////////////////////////////////////////
	public void reset()
	{
		this.mMode = ReversiConst.DEF_MODE_ONE;								// 現在のモード
		this.mType = ReversiConst.DEF_TYPE_HARD;							// 現在のタイプ
		this.mPlayer = ReversiConst.REVERSI_STS_BLACK;						// プレイヤーの色
		this.mAssist = ReversiConst.DEF_ASSIST_ON;							// アシスト
		this.mGameSpd = ReversiConst.DEF_GAME_SPD_MID;						// ゲームスピード
		this.mEndAnim = ReversiConst.DEF_END_ANIM_ON;						// ゲーム終了アニメーション
		this.mMasuCntMenu = ReversiConst.DEF_MASU_CNT_8;					// マスの数
		this.mMasuCnt = ReversiConst.DEF_MASU_CNT_8_VAL;					// マスの数
		this.mPlayCpuInterVal = ReversiConst.DEF_GAME_SPD_MID_VAL2;			// CPU対戦時のインターバル(msec)
		this.mPlayDrawInterVal = ReversiConst.DEF_GAME_SPD_MID_VAL;			// 描画のインターバル(msec)
		this.mEndDrawInterVal = 100;										// 終了アニメーション描画のインターバル(msec)
		this.mEndInterVal = 500;											// 終了アニメーションのインターバル(msec)
		this.mPlayerColor1 = "#000000";										// プレイヤー1の色
		this.mPlayerColor2 = "#FFFFFF";										// プレイヤー2の色
		this.mBackGroundColor = "#00FF00";									// 背景の色
		this.mBorderColor = "#000000";										// 枠線の色
	}

	mMode;														# !< 現在のモード
	mType;														# !< 現在のタイプ
	mPlayer;													# !< プレイヤーの色
	mAssist;													# !< アシスト
	mGameSpd;													# !< ゲームスピード
	mEndAnim;													# !< ゲーム終了アニメーション
	mMasuCntMenu;												# !< マスの数
	mMasuCnt;													# !< マスの数
	mPlayCpuInterVal;											# !< CPU対戦時のインターバル(msec)
	mPlayDrawInterVal;											# !< 描画のインターバル(msec)
	mEndDrawInterVal;											# !< 終了アニメーション描画のインターバル(msec)
	mEndInterVal;												# !< 終了アニメーションのインターバル(msec)
	mPlayerColor1;												# !< プレイヤー1の色
	mPlayerColor2;												# !< プレイヤー2の色
	mBackGroundColor;											# !< 背景の色
	mBorderColor;												# !< 枠線の色
