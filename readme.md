##### 작성자: 권영호 (yhkwon@euclidsoft.co.kr)
##### 작성일 2020.11.06
### 초안 작성 중 
# 개요
- 프로젝트 설명
- 사용방법
    - 개발모드
    - 배포모드
- 사전 세팅 상세 설명(커스터마이징 시 참고)

# django base pack
django server 개발 및 배포용 base container 세팅.
설치 및 초기 설정의 번거로움을 피하고자 기본적인 내용만을 미리 세팅해놓음.

# 사용방법
### 개발 mode
```
$ cd {project_root}/was_server
$ docker-compose up --build
```
웹브라우저에서 localhost/admin 입력 시
django admin 페이지 나오면 성공
### 배포 mode

admin page 가 나온다면 성공

# static files 처리
static_volume이라는 볼륨컨테이너를 생성하여 nginx와 django app의 static 파일들을 묶었습니다.
    1. 빌드 시 prod_server_start.sh 에서 collectstatic을 수행하여 django 컨테이너 내 /.static_root 경로에 static file을 모읍니다.
    2. django 컨테이너의 /.static_root/ 는 static_volume 컨테이너와 bind 되어있습니다.
    3. nginx 컨테이너의 /static 폴더와 static_volume 컨테이너를 bind 하여 
    django container /.static_root <=> static_volume <=> nginx container /static 를 연결합니다.
    4. nginx 설정에서 /static/ 경로 요청 시 /static 폴더를 바라보도록 location 설정을 해놨습니다.

## trobule shooting
### 개발용 db build 시 access denied 에러 발생 시
- db접속 시 remote 계정 설정 없이 localhost 가 아닌 remote 계정으로 접근 시 발생 가능. 
- 최초 셋업 시 발생하였다면 1차로 
(- down -v 는 불륨컨테이너를 삭제하므로 기존에 넣었던 db 자료도 삭제되므로 주의요망
)
```
$ docker-compose down -v 
```
로 database 
volume 삭제 후 
```
docker-compose up --build 
```
재실행

- 개발 도중 db 접근이 안되는 경우
```
$ docker ps  
```
로 db container 의 process id 확인 후
```
$ docker exec -it {process_id} /bin/bash
$ mysql -uroot -p
root_password 입력

mysql 접속 후 root remote 계정 추가 및 모든 권한 부여 (user 계정으로 작업 시 root 대신 user명 입력)
> use mysql
mysql>  create user 'root'@'%' identified by 'password';
mysql> grant all privileges on *.* to 'root'@'%';
mysql> flush privileges
mysql> exit

$ exit 

$ docker-compose down #-v 옵션 넣으면 안됨
$ docker-compose up
```