
## BART

- Bidrectional 과 Auto-Regressive Transformer를 합친 모델
- noising유연성 어떤 임의의 변형이라도 기존 텍스트에 바로 적용이 가능하다, 길이변환마저 가능하다
- BERT의 기존 방법론에 따르는 단어 mask와 next sentence prediction을일반화 한 것으로, 모델이 전체적인 문장 길이에 대해 학습해야하고, 변형된 입력에 더 많이 집중해야 하는 효과가 있다고 합니다.
- BART는 텍스트 생성에 fine-tuning하였을 때 특히 효율적이지만, comprehension(이해) 테스크에서도 역시 잘 동작 합니다.
- fine-tuning의 새로운 방법에 대해서도 제안했습니다.
    - 추가적인 transfomer 레이어를 쌓아 올리는 것으로는 기계번역에 대한 새로운 방버론을 제시하였다고 합니다.

## model 구조

- BART 표준 seq2seq Transformer 구조를 사용한다고 한다.
- 디코더에서는 GPT에서 사용하는 RELU 활성화 함수를 GeLU로 바꾸었고 파라미터 초기화를 N(0,0.2)로 하였다고 한다. (표준 정규 분포를 따르는데 평균이 0, std 0.2의 분포를 갖게 하였다는 뜻)
- bass 와 large 크기의 모델이 있는데, base 모델은 엔코더와 디코더에 각각 6개의 레이어를 사용하였고, large모델은 12개의 레이어를 사용하였습니다. 구조 bert에서 사용하는 것과 아주 비슷하다.
- 차이점
    - 디코더와 각 레이어가 엔코더의 최종 hidden레이어와 cross-attention을 수행한다.
    - bert는 단어를 유추해내기 위해 추자적인 feed-forward 네트워크를 사용하지만 BART는 그렇지 않다.( 인코더가 마스킹된 단어를 유추하지 않기 때문)
    - BART는 BERT보다 약 10% 더 많은 파라미터를 가지게 됩니다.

![https://dladustn95.github.io/assets/images/bart_figure1.png](https://dladustn95.github.io/assets/images/bart_figure1.png)