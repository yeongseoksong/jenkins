# 0. Jenkins Image Build
>><img width="920" alt="basic jenkins" src="https://github.com/yeongseoksong/jenkins/assets/76511428/19118b24-0a8d-4f70-a3a6-e49aca18aded">

>linux 환경에서 jenkins 를 설치하는 방법은 다음과 같다.

>> a. container
>> 
>> b. jenkins install

  
#### Issue
> Docker 는 호스트 머신의 docker daemon 에의하여 실행된다.
>>![screenshot2](https://github.com/yeongseoksong/jenkins/assets/76511428/2636a061-aca3-4275-807e-d3f2d9fcb8fa)


>  그렇기 때문에 container 환경 jenkins 환경을 구성하고 container 내부에서 docker 관련 스크립트를 실행 하기 위해서는 다음 방법중 하나를 택해야한다.
>>  + DinD ( docker in docker)        ->   container 내부에 docker 를 설치한다. docker 제작사에서 권장하지 않는 방법이다.
>>  + Dood ( docker out of docker )   ->   Hostmachine 의 docker.so 를 mnt 한다. 이때, docker.so 의 권한을 777로 바꾸어 주거나 docker.so의 Gid를 container user 에 적용해 주어야 한다.    
    
    RUN groupadd -g {Gid} docker 
    RUN usermod -aG docker go 
#### ./jenkins/Dockerfile
> Jenkins Container 를 생성하기전에 이미지를 빌드한다
> Jenkins Image 의 Lts 버전을 빌드 한후에 container 내부에  Docker 를 설치해준다.
>> Dood 방식으로 Container를 제작 하여도 Container 는 Docker 명령어를 알지 못한다. 따라서 추가적으로 이를 설치해주는 Dockerfile을 빌드한다


###  < ToDo >
 - [x] change container os Debian -> alpine

---
# 1. Jenkins Image push
>  서버에 적용하기 위하여 Docker Hub 에 0. 에서 생성한 이미지를 Push 한다
>> https://hub.docker.com/repository/docker/asdaafwe/jenkins_img/general

    docker image ls
    docker login -u -p
    docker push {docker_image_name}

#### ./jenkins/docker-compse.yml
> Docker Image 를 컨테이너로 실행할때 Option을 설정해둔 파일이다.
> 여러 Container 를 연결시킬때 주로 사용된다.

    docker-compose up ./path/

#### Jenkins Memory Issue
> + Jenkins memory
>> container 는 run 될때 default 로 pc의 메모리 전체를 할당 받는다. 뿐더러 , jenkins 는 별다른 설정이 없다면 jenkins의 권장사양인 16G 까지 메모리를 사용한다. 
>> ondemand 방식인 aws 에서 사용하기 힘들기 때문에 jenkins의 실행 환경의 memory 를 제한해야한다.

>> https://community.jenkins.io/t/high-memory-usage-jenkins-in-docker/4909
>   + using Docker
    
    docker run --name {container_name} -m {meory_size} {image_name}
>   + install on Linux
    
    vi /etc/default/jenkins
    JAVA_ARGS="-Xmx1024m"


>> ** 1gb ram이 할당되는 ec2 프리티어에서는 swap 메모리를 확장해주어야 한다.

# 2. docker image build server
#### ./server/Dockerfile.yml
#### ./server/requirements.txt
> WAS 를 Container 환경에서 실행시키기 위하여 Dockerfile 을 server Directory의 root path에 위치 시킨다.

     docker build -t {image_name}:{tag} ./path/

> 해당 Dockerfile 은 server폴더를 Docker Image 로 build 하고 Flask 서버를 실행시킨다.     

### < ToDo >
 - [x] change container os Debian -> alpine
 - [x] change python slim ver

 # 3. jenkins pipeline script
>> <img width="706" alt="result" src="https://github.com/yeongseoksong/jenkins/assets/76511428/430439ca-bf70-4bde-b491-083a1ee79821">

 
# 4. jenkins setting
 
