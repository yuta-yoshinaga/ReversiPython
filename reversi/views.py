from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import JsonResponse
import json
import logging
from .model import ReversiPlay
from .model import ReversiSetting
from . import FrontController


def index_template(request):
    return render(request, 'reversi/index.html')


@csrf_protect
def frontController(request):
    logging.debug('frontController')
    logging.debug(request)
    frc = FrontController.FrontController()
    resJson = {}
    rvPlay = None
    if 'rvPlay' in request.session:
        # オブジェクト生成済み
        rvPlay = request.session['rvPlay']
    else:
        # 初めてのアクセス
        rvPlay = ReversiPlay.ReversiPlay()
        request.session['rvPlay'] = rvPlay
    if (rvPlay == None):
        rvPlay = ReversiPlay.ReversiPlay()
        request.session['rvPlay'] = rvPlay
    # コールバック登録
    rvPlay.mDelegate = frc

    func = request.POST['func']
    if (func == 'setSetting'):
        para = request.POST['para']
        datas = json.loads(para)
        print(datas)
        setting = ReversiSetting.ReversiSetting()
        setting.mMode = datas['mMode']
        setting.mType = datas['mType']
        setting.mPlayer = datas['mPlayer']
        setting.mAssist = datas['mAssist']
        setting.mGameSpd = datas['mGameSpd']
        setting.mEndAnim = datas['mEndAnim']
        setting.mMasuCntMenu = datas['mMasuCntMenu']
        setting.mMasuCnt = datas['mMasuCnt']
        setting.mPlayCpuInterVal = datas['mPlayCpuInterVal']
        setting.mPlayDrawInterVal = datas['mPlayDrawInterVal']
        setting.mEndDrawInterVal = datas['mEndDrawInterVal']
        setting.mEndInterVal = datas['mEndInterVal']
        setting.mPlayerColor1 = datas['mPlayerColor1']
        setting.mPlayerColor2 = datas['mPlayerColor2']
        setting.mBackGroundColor = datas['mBackGroundColor']
        setting.mBorderColor = datas['mBorderColor']
        rvPlay.mSetting = setting
        rvPlay.reset()
        resJson['auth'] = '[SUCCESS]'
    elif (func == 'reset'):
        rvPlay.reset()
        resJson['auth'] = '[SUCCESS]'
    elif (func == 'reversiPlay'):
        y = request.POST['y']
        x = request.POST['x']
        rvPlay.reversiPlay(y, x)
        resJson['auth'] = '[SUCCESS]'

    resJson['callbacks'] = frc.callbacks
    request.session['rvPlay'] = rvPlay
    logging.debug(resJson)

    return JsonResponse(resJson)
