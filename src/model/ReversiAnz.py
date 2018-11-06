################################################################################
#	@file			ReversiAnz.py
#	@brief			リバーシ解析クラス実装ファイル
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

################################################################################
#	@class		ReversiAnz
#	@brief		リバーシ解析クラス
#
################################################################################


class ReversiAnz:

    ############################################################################
    #	@brief			コンストラクタ
    #	@fn				__init__(self)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def __init__(self):
        self.reset()

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getMin(self)
    #	@return			min
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getMin(self):
        return self.__min

    ############################################################################
    #	@brief			セッター
    #	@fn				setMin(self, min)
    #	@param[in]		min
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setMin(self, min):
        self.__min = min

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getMax(self)
    #	@return			max
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getMax(self):
        return self.__max

    ############################################################################
    #	@brief			セッター
    #	@fn				setMax(self, max)
    #	@param[in]		max
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setMax(self, max):
        self.__max = max

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getAvg(self)
    #	@return			avg
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getAvg(self):
        return self.__avg

    ############################################################################
    #	@brief			セッター
    #	@fn				setAvg(self, avg)
    #	@param[in]		avg
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setAvg(self, avg):
        self.__avg = avg

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getPointCnt(self)
    #	@return			pointCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getPointCnt(self):
        return self.__pointCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setPointCnt(self, pointCnt)
    #	@param[in]		pointCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setPointCnt(self, pointCnt):
        self.__pointCnt = pointCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getEdgeCnt(self)
    #	@return			edgeCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getEdgeCnt(self):
        return self.__edgeCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setEdgeCnt(self, edgeCnt)
    #	@param[in]		edgeCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setEdgeCnt(self, edgeCnt):
        self.__edgeCnt = edgeCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getEdgeSideOneCnt(self)
    #	@return			edgeSideOneCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getEdgeSideOneCnt(self):
        return self.__edgeSideOneCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setEdgeSideOneCnt(self, edgeSideOneCnt)
    #	@param[in]		edgeSideOneCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setEdgeSideOneCnt(self, edgeSideOneCnt):
        self.__edgeSideOneCnt = edgeSideOneCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getEdgeSideTwoCnt(self)
    #	@return			edgeSideTwoCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getEdgeSideTwoCnt(self):
        return self.__edgeSideTwoCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setEdgeSideTwoCnt(self, edgeSideTwoCnt)
    #	@param[in]		edgeSideTwoCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setEdgeSideTwoCnt(self, edgeSideTwoCnt):
        self.__edgeSideTwoCnt = edgeSideTwoCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getEdgeSideThreeCnt()
    #	@return			edgeSideThreeCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getEdgeSideThreeCnt(self):
        return self.__edgeSideThreeCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setEdgeSideThreeCnt(self, edgeSideThreeCnt)
    #	@param[in]		edgeSideThreeCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setEdgeSideThreeCnt(self, edgeSideThreeCnt):
        self.__edgeSideThreeCnt = edgeSideThreeCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getEdgeSideOtherCnt(self)
    #	@return			edgeSideOtherCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getEdgeSideOtherCnt(self):
        return self.__edgeSideOtherCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setEdgeSideOtherCnt(self, edgeSideOtherCnt)
    #	@param[in]		edgeSideOtherCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setEdgeSideOtherCnt(self, edgeSideOtherCnt):
        self.__edgeSideOtherCnt = edgeSideOtherCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnMin(self)
    #	@return			ownMin
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnMin(self):
        return self.__ownMin

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnMin(self, ownMin)
    #	@param[in]		ownMin
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnMin(self, ownMin):
        self.__ownMin = ownMin

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnMax(self)
    #	@return			ownMax
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnMax(self):
        return self.__ownMax

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnMax(self, ownMax)
    #	@param[in]		ownMax
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnMax(self, ownMax):
        self.__ownMax = ownMax

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnAvg(self)
    #	@return			ownAvg
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnAvg(self):
        return self.__ownAvg

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnAvg(self, ownAvg)
    #	@param[in]		ownAvg
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnAvg(self, ownAvg):
        self.__ownAvg = ownAvg

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnPointCnt(self)
    #	@return			ownPointCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnPointCnt(self):
        return self.__ownPointCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnPointCnt(self, ownPointCnt)
    #	@param[in]		ownPointCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnPointCnt(self, ownPointCnt):
        self.__ownPointCnt = ownPointCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnEdgeCnt(self)
    #	@return			ownEdgeCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnEdgeCnt(self):
        return self.__ownEdgeCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnEdgeCnt(self, ownEdgeCnt)
    #	@param[in]		ownEdgeCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnEdgeCnt(self, ownEdgeCnt):
        self.__ownEdgeCnt = ownEdgeCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnEdgeSideOneCnt(self)
    #	@return			ownEdgeSideOneCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnEdgeSideOneCnt(self):
        return self.__ownEdgeSideOneCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnEdgeSideOneCnt(self, ownEdgeSideOneCnt)
    #	@param[in]		ownEdgeSideOneCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnEdgeSideOneCnt(self, ownEdgeSideOneCnt):
        self.__ownEdgeSideOneCnt = ownEdgeSideOneCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnEdgeSideTwoCnt(self)
    #	@return			ownEdgeSideTwoCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnEdgeSideTwoCnt(self):
        return self.__ownEdgeSideTwoCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnEdgeSideTwoCnt(self, ownEdgeSideTwoCnt)
    #	@param[in]		ownEdgeSideTwoCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnEdgeSideTwoCnt(self, ownEdgeSideTwoCnt):
        self.__ownEdgeSideTwoCnt = ownEdgeSideTwoCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnEdgeSideThreeCnt(self)
    #	@return			ownEdgeSideThreeCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnEdgeSideThreeCnt(self):
        return self.__ownEdgeSideThreeCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnEdgeSideThreeCnt(self, ownEdgeSideThreeCnt)
    #	@param[in]		ownEdgeSideThreeCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnEdgeSideThreeCnt(self, ownEdgeSideThreeCnt):
        self.__ownEdgeSideThreeCnt = ownEdgeSideThreeCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getOwnEdgeSideOtherCnt(self)
    #	@return			ownEdgeSideOtherCnt
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getOwnEdgeSideOtherCnt(self):
        return self.__ownEdgeSideOtherCnt

    ############################################################################
    #	@brief			セッター
    #	@fn				setOwnEdgeSideOtherCnt(self, ownEdgeSideOtherCnt)
    #	@param[in]		ownEdgeSideOtherCnt
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setOwnEdgeSideOtherCnt(self, ownEdgeSideOtherCnt):
        self.__ownEdgeSideOtherCnt = ownEdgeSideOtherCnt

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getBadPoint(self)
    #	@return			badPoint
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getBadPoint(self):
        return self.__badPoint

    ############################################################################
    #	@brief			セッター
    #	@fn				setBadPoint(self, badPoint)
    #	@param[in]		badPoint
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setBadPoint(self, badPoint):
        self.__badPoint = badPoint

    ############################################################################
    #	@brief			ゲッター
    #	@fn				getGoodPoint(self)
    #	@return			goodPoint
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def getGoodPoint(self):
        return self.__goodPoint

    ############################################################################
    #	@brief			セッター
    #	@fn				setGoodPoint(self, goodPoint)
    #	@param[in]		goodPoint
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def setGoodPoint(self, goodPoint):
        self.__goodPoint = goodPoint

    ############################################################################
    #	@brief			リセット
    #	@fn				reset(self)
    #	@return			ありません
    #	@author			Yuta Yoshinaga
    #	@date			2018.11.06
    #
    ############################################################################
    def reset(self):
        self.__min = 0
        self.__max = 0
        self.__avg = 0.0
        self.__pointCnt = 0
        self.__edgeCnt = 0
        self.__edgeSideOneCnt = 0
        self.__edgeSideTwoCnt = 0
        self.__edgeSideThreeCnt = 0
        self.__edgeSideOtherCnt = 0
        self.__ownMin = 0
        self.__ownMax = 0
        self.__ownAvg = 0.0
        self.__ownPointCnt = 0
        self.__ownEdgeCnt = 0
        self.__ownEdgeSideOneCnt = 0
        self.__ownEdgeSideTwoCnt = 0
        self.__ownEdgeSideThreeCnt = 0
        self.__ownEdgeSideOtherCnt = 0
        self.__badPoint = 0
        self.__goodPoint = 0

    min = property(getMin, setMin)  # !< 最小値
    max = property(getMax, setMax)  # !< 最大値
    avg = property(getAvg, setAvg)  # !< 平均
    pointCnt = property(getPointCnt, setPointCnt)  # !< 置けるポイント数
    edgeCnt = property(getEdgeCnt, setEdgeCnt)  # !< 角を取れるポイント数
    edgeSideOneCnt = property(
        getEdgeSideOneCnt, setEdgeSideOneCnt)  # !< 角一つ前を取れるポイント数
    edgeSideTwoCnt = property(
        getEdgeSideTwoCnt, setEdgeSideTwoCnt)  # !< 角二つ前を取れるポイント数
    edgeSideThreeCnt = property(
        getEdgeSideThreeCnt, setEdgeSideThreeCnt)  # !< 角三つ前を取れるポイント数
    edgeSideOtherCnt = property(
        getEdgeSideOtherCnt, setEdgeSideOtherCnt)  # !< それ以外を取れるポイント数
    ownMin = property(getOwnMin, setOwnMin)  # !< 最小値
    ownMax = property(getOwnMax, setOwnMax)  # !< 最大値
    ownAvg = property(getOwnAvg, setOwnAvg)  # !< 平均
    ownPointCnt = property(getOwnPointCnt, setOwnPointCnt)  # !< 置けるポイント数
    ownEdgeCnt = property(getOwnEdgeCnt, setOwnEdgeCnt)  # !< 角を取れるポイント数
    ownEdgeSideOneCnt = property(
        getOwnEdgeSideOneCnt, setOwnEdgeSideOneCnt)  # !< 角一つ前を取れるポイント数
    ownEdgeSideTwoCnt = property(
        getOwnEdgeSideTwoCnt, setOwnEdgeSideTwoCnt)  # !< 角二つ前を取れるポイント数
    ownEdgeSideThreeCnt = property(
        getOwnEdgeSideThreeCnt, setOwnEdgeSideThreeCnt)  # !< 角三つ前を取れるポイント数
    ownEdgeSideOtherCnt = property(
        getOwnEdgeSideOtherCnt, setOwnEdgeSideOtherCnt)  # !< それ以外を取れるポイント数
    badPoint = property(getBadPoint, setBadPoint)  # !< 悪手ポイント
    goodPoint = property(getGoodPoint, setGoodPoint)  # !< 良手ポイント
