from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import JsonResponse
import json
from .model import ReversiPlay
from . import FrontController


def index_template(request):
    return render(request, 'reversi/index.html')


def frontController(request):
    logging.debug('frontController')
    logging.debug(request)
    frc = FrontController.FrontController()
    resJson = []
    rvPlay = None
    if 'rvPlay' in request.session:
        # オブジェクト生成済み
        rvPlay = request.session['rvPlay']
    else:
        # 初めてのアクセス
        rvPlay = ReversiPlay()
        request.session['rvPlay'] = rvPlay
    if (rvPlay == None):
        rvPlay = ReversiPlay()
        request.session['rvPlay'] = rvPlay
    # コールバック登録
    rvPlay.mDelegate = frc

    func = request.POST['func']
    if (func == 'setSetting'):
        para = request.POST['para']
        datas = json.loads(para)
        print(datas)
        rvPlay.mSetting = datas
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

    return JsonResponse(resJson)
