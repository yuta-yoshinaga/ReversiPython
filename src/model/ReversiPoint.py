################################################################################
# 	@file			ReversiPoint.py
# 	@brief			リバーシポイントクラス実装ファイル
# 	@author			Yuta Yoshinaga
# 	@date			2018.11.06
# 	$Version:		$
# 	$Revision:		$
#
#  (c) 2018 Yuta Yoshinaga.
#
#  - 本ソフトウェアの一部又は全てを無断で複写複製（コピー）することは、
#    著作権侵害にあたりますので、これを禁止します。
#  - 本製品の使用に起因する侵害または特許権その他権利の侵害に関しては
#    当方は一切その責任を負いません。
#
################################################################################

################################################################################
# 	@class		ReversiPoint
# 	@brief		リバーシポイントクラス
#
################################################################################


class ReversiPoint:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@param[in]		self
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def __init__(self):
        self.__x = 0
        self.__y = 0

    ############################################################################
    # 	@brief			ゲッター
    # 	@fn				getX(self)
    # 	@param[in]		self
    # 	@return			x
    # 	@author			Yuta Yoshinaga
    # 	@date			2018.11.06
    #
    ############################################################################
    def getX(self):
        return self.__x

    ############################################################################
    # 	@brief			セッター
    # 	@fn				setX(self,x)
    # 	@param[in]		self
    # 	@param[in]		x
    # 	@return			ありません
    # 	@author			Yuta Yoshinaga
    # 	@date			2018.11.06
    #
    ############################################################################
    def setX(self, x):
        self.__x = x

    ############################################################################
    # 	@brief			ゲッター
    # 	@fn				getY(self)
    # 	@param[in]		self
    # 	@return			y
    # 	@author			Yuta Yoshinaga
    # 	@date			2018.11.06
    #
    ############################################################################
    def getY(self):
        return self.__y

    ############################################################################
    # 	@brief			セッター
    # 	@fn				setY(self,y)
    # 	@param[in]		self
    # 	@param[in]		y
    # 	@return			ありません
    # 	@author			Yuta Yoshinaga
    # 	@date			2018.11.06
    #
    ############################################################################
    def setY(self, y):
        self.__y = y

    x = property(getX, setX) # !< X座標
    y = property(getY, setY) # !< Y座標
