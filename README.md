# 0.  Jenkins Image Build
>linux 환경에서 jenkins 를 설치하는 방법은 다음과 같다.

>> a. container
>> 
>> b. jenkins install

  
## Issue
> Docker 는 호스트 머신의 docker daemon 에의하여 실행된다.
>>  ![screenshot2](https://github.com/yeongseoksong/jenkins/assets/76511428/2d6a2397-ee79-41a1-b836-a3958f8d5971)

>  그렇기 때문에 container 환경 jenkins 환경을 구성하고 container 내부에서 docker 관련 스크립트를 실행 하기 위해서는 다음 방법중 하나를 택해야한다.
>>  + DinD ( docker in docker)        ->   container 내부에 docker 를 설치한다. docker 제작사에서 권장하지 않는 방법이다.
>>  + Dood ( docker out of docker )   ->   Hostmachine 의 docker.so 를 mnt 한다. 이때, docker.so 의 권한을 777로 바꾸어 주거나 docker.so의 Gid를 container user 에 적용해 주어야 한다.    
    
    RUN groupadd -g {Gid} docker 
    RUN usermod -aG docker go 
## ./jenkins/Dockerfile
> Jenkins Container 를 생성하기전에 이미지를 빌드한다
> Jenkins Image 의 Lts 버전을 빌드 한후에 container 내부에  Docker 를 설치해준다.
>> Dood 방식으로 Container를 제작 하여도 Container 는 Docker 명령어를 알지 못한다. 따라서 추가적으로 이를 설치해주는 Dockerfile을 빌드한다


### > ToDo
 - [x] change container os Debian -> alpine

---
# 1. Jenkins Image push
https://hub.docker.com/repository/docker/asdaafwe/jenkins_img/general
## ./jenkins/dockdr-compse.yml
> 

