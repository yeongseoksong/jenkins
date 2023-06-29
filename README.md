# 0.  Jenkins Image Build
linux 환경에서 jenkins 를 설치하는 방법은 다음과 같다.

  + a. container
+ b. jenkins install

  
## Issue
  + Docker 는 호스트 머신의 docker daemon 에의하여 실행된다.
  ![screenshot2](https://github.com/yeongseoksong/jenkins/assets/76511428/2d6a2397-ee79-41a1-b836-a3958f8d5971)

  + 그렇기 때문에 container 환경 jenkins 환경을 구성하고 container 내부에서 docker 관련 스크립트를 실행 하기 위해서는 다음 방법중 하나를 택해야한다.
    + Dood ( docker out of docker ) -> container 내부에 docker 를 설치한다. docker 제작사에서 권장하지 않는 방법이다.
    + DinD ( docker in docker) [ o ] 

## DinD

    

## 0.1 ./jenkins/Dockerfile
  
