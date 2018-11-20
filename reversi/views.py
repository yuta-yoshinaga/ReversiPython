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
        setting = ReversiSetting.ReversiSetting()
        setting.mMode = int(datas['mMode'])
        setting.mType = int(datas['mType'])
        setting.mPlayer = int(datas['mPlayer'])
        setting.mAssist = int(datas['mAssist'])
        setting.mGameSpd = int(datas['mGameSpd'])
        setting.mEndAnim = int(datas['mEndAnim'])
        setting.mMasuCntMenu = int(datas['mMasuCntMenu'])
        setting.mMasuCnt = int(datas['mMasuCnt'])
        setting.mPlayCpuInterVal = int(datas['mPlayCpuInterVal'])
        setting.mPlayDrawInterVal = int(datas['mPlayDrawInterVal'])
        setting.mEndDrawInterVal = int(datas['mEndDrawInterVal'])
        setting.mEndInterVal = int(datas['mEndInterVal'])
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
        y = int(request.POST['y'])
        x = int(request.POST['x'])
        rvPlay.reversiPlay(y, x)
        resJson['auth'] = '[SUCCESS]'

    resJson['callbacks'] = frc.callbacks
    request.session['rvPlay'] = rvPlay
    logging.debug(resJson)

    return JsonResponse(resJson)
