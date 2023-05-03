# 2023_05_03
* projcet를 준비하며 사용될 것으로 예상되는 모델을 간단하게 조사해보았다.
# K-GPT2

- GPT-2
    - 주어진 텍스트의 다음 단어를 잘 예측할 수 있도록 학습된 언어모델 문장 생성에 최적화 되어 있다.
- KoGPT2
    - 부족한 한국어 성능을 극복하기 위해 40GB 이상의 텍스트로 학습된 한국어 디코더(decoder)모델
    - Performances
        
        ### Classification or Regression
        
        |  | https://github.com/e9t/nsmc(acc) | https://github.com/kakaobrain/KorNLUDatasets(spearman) |
        | --- | --- | --- |
        | KoGPT2 2.0 | 89.1 | 77.8 |

[https://github.com/SKT-AI/KoGPT2](https://github.com/SKT-AI/KoGPT2)

# KoBERT

- 기존 BERT한국어 성능 한계를 극복하기 위해 개발되었다.
- 위키피디아나 뉴스 등에서 수집한 수백만 개의 한국어 문장으로 이루어진 대규모 말뭉치를 학습
- 대량의 데이터를 빠른시간에 학습하기 위해 링 리듀스 (ring-reduce)기법을 활용 하였다.
    - 그래디언트를 각 노드에서 연속적인 블록으로 나누고 동시에 이전 노드를 사용하여 각 블록을 업데이트하고 다음 노드에도 업데이르틀 제공하여 링 패턴을 만듬
    - 뭔소리인지 모르겠음 하여튼 재원의 부탐을 줄이고자 행하는 기법

[https://github.com/SKTBrain/KoBERT](https://github.com/SKTBrain/KoBERT)

[https://sktelecom.github.io/project/kobert/](https://sktelecom.github.io/project/kobert/)

# KpfBERT

- 신문기사에 특화됨
    - BERT의 특징은 대량의 데이터를 사전학습을 하는 모델
    - 그렇기에 데이터 수집과 모델 트레이닝의 과한 비용이 요구됨
    - 데이터의 집단에 따라서 모델의 편향성이 생길 수 있음
    - 언론에 특화된 사전학습된 BERT모델을 생성함으로써 언론 관련 산업에서 자연어처리 착업에 활용할 수 있는 기반을 만듬

![Untitled](image\project\Bert\성능비교.png)

### KPF-BERT 모델의 적용 예시

[https://github.com/KPFBERT/kpfSBERT_Clustering](https://github.com/KPFBERT/kpfSBERT_Clustering)

[https://github.com/KPFBERT/kpfbertsum](https://github.com/KPFBERT/kpfbertsum)

[https://github.com/KPFBERT/kpfSBERT](https://github.com/KPFBERT/kpfSBERT)