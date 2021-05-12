# 파를 먹고 싶어요! 알려주세요 MLP
> toy project

- 프로젝트 시작 이유?
- 파절이는 삽겹살의 소울 프렌드이다..
- But 미쳐가는 파가격 때문에 살까 말까 고민을 하다가 개발하게 되었습니다.

> 가정
- **오늘의 파 가격**은 어제 최고,최저,평균 온도, 강수량, 파격으로 예측 가능할것이다.

> Project Flow

![Screenshot from 2021-05-12 15-43-04](https://user-images.githubusercontent.com/72845895/117930295-ca63a300-b338-11eb-9b1d-42e0a79d8c2c.png)


> 사용 모델 
- tensorflow version 2.6.0 night version
- MLP(3 layers linear regression)  
- 과적합을 피하기 위해 dropout 사용 


![Screenshot from 2021-05-12 16-07-55](https://user-images.githubusercontent.com/72845895/117933358-73f86380-b33c-11eb-90e5-5643ed3d0beb.png)


> Parameter
- learning-rate = 000005
- epoch = 10000
- batchsize = 8
- callback = earlystop

> 결과 
![Screenshot from 2021-05-12 16-21-09](https://user-images.githubusercontent.com/72845895/117934895-19600700-b33e-11eb-9a6b-1dc98d1b24f0.png)

