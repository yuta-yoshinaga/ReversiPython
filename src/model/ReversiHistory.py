################################################################################
#	@file			ReversiHistory.py
#	@brief			リバーシ履歴クラス実装ファイル
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

import ReversiPoint

################################################################################
#	@class		ReversiHistory
#	@brief		リバーシ履歴クラス
#
################################################################################


class ReversiHistory:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2014.07.23
    #
    ############################################################################
    def __init__(self):
        self.__point = ReversiPoint.ReversiPoint()
        self.__color = 0
        self.reset()

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getPoint(self)
    #	@param[in]		self
    #	@return			ReversiPoint point
    #	@author			Yuta Yoshinaga
    #	@date			2018.04.01
    #
    ############################################################################
    def getPoint(self):
        return self.__point

    ############################################################################
    #	@brief			セッター
    #	@fn				setPoint(self, point)
    #	@param[in]		self
    #	@param[in]		point
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.04.01
    #
    ############################################################################
    def setPoint(self, point):
        self.__point = point

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getColor(self)
    #	@param[in]		self
    #	@return			color
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getColor(self):
        return self.__color

    ############################################################################
    #	@brief			セッター
    #	@fn				setColor(self, color)
    #	@param[in]		self
    #	@param[in]		color
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setColor(self, color):
        self.__color = color

    ############################################################################
    #	@brief			リセット
    #	@fn				reset(self)
    #	@param[in]		self
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def reset(self):
        self.__point.x = -1
        self.__point.y = -1
        self.__color = -1

    point = property(getPoint, setPoint) # !< リバーシポイント
    color = property(getColor, setColor) # !< カラー
