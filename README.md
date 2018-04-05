# R-CNN OBJECT DETECTION

본 프로젝트는 "Rich features hierarchies for accurate object detection and semantic" 논문에 있는 아키텍쳐를 Keras를 이용하여 구현하는 것이 목표입니다.
ImageNet 데이터로 pretrain된 모델을 PASCAL VOC 데이터로 fine-tuning한 모델을 사용하였습니다.
아직 Bounding box regression 부분을 구현하지 않았고, Non-maximum surpression도 되지 않아, 겹치는 영역이 매우 많다는 문제점을 가지고 있습니다.
추후 시간나는 대로 구현하여 추가할 예정입니다.
감사합니다!

This project is aim to implement R-CNN in the paper "Rich features hierarchies for accurate object detection and semantic".
I use ImageNet pretrained vgg-16 model and fine-tune with PASCAL VOC dataset. 
Since now, I have worked on the neither ounding box regression nor non-maximum surpression which causes overlapped results.
I will implement these things later.

Thank you!

## 설치 방법

별 다른 설치가 필요하지 않습니다.
복잡한 실행방법을 요하는 코드는 지양합니다.

It's not needed any installation process.
I don't like any 'complicated' things.

## 사용 예제
터미널 창에서 다음과 같이 실행하세요.
```sh
python3 keras_vgg_16.py
```
Fine-tuning architecture를 사용하려면 다음과 같이 실행하세요.
```sh
python3 keras_vgg_16_fine_tune.py
```
## 개발 환경 설정
Python 3.x 버젼과, tensorflow, keras, opencv 가 필요합니다.
Pycharm IDE를 사용하였지만, 코드 실행에 특별히 필요하지는 않습니다.
```sh
pip3 install tensorflow
pip3 install keras
```
 
## 업데이트 내역

* 0.0.1
    * Scratch training architecture 추가하였습니다.
* 0.0.2
    * Fine-tuning architecture 추가하였습니다.
* 0.0.3
    * Inference model을 추가하였습니다. 원하는 이미지를 넣으면 분류 결과를 얻을 수 있습니다.

* 0.1.1
    * Detection model을 추가하였습니다. 이제 이미지를 입력하면 detection 결과를 얻을 수 있습니다. 
## 정보

김동현 – seru_s@me.com
Donghyun Kim / Henniekim

## 라이센스

MIT © henniekim

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
