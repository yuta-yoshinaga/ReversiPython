# ReversiPython
リバーシアルゴリズムをPythonで実装

## Description
リバーシのアルゴリズムをPythonで実装したプロジェクトです。
フロントエンドからクリックされたマスの座標を通知されると、そのマスに置けるか否か、置いた結果のマス状況などをレスポンスするようにサーバーサイドが実装されています。
マスの状況はセッションに保存されており、フロントエンドのGUI設定などはWeb Storageに保存されて、ゲーム開始時にフロントエンドからサーバーへ通知されます。

## Usage
### Install
```sh
git clone https://github.com/yuta-yoshinaga/ReversiPython.git
cd reversipython
```

### Deploy
[render live](https://reversipython.onrender.com/)
[render dev](https://reversipython-dev.onrender.com/)
[API Document](https://yuta-yoshinaga.github.io/ReversiPython/)

## Future Releases
TensorFlowを使って、AIの更新がしたい。

## Contribution
1. Fork it  
2. Create your feature branch  
3. Commit your changes  
4. Push to the branch  
5. Create new Pull Request

## License
[MIT](LICENSE)