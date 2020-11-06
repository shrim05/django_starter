##### 작성자: 권영호 (yhkwon@euclidsoft.co.kr)
##### 작성일 2020.11.06

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
django 기본 welcome page가 나오면 성공

### 배포 mode
admin page 가 나온다면 성공

# static files 처리
static_volume이라는 볼륨컨테이너를 생성하여 nginx와 django app의 static 파일들을 묶었습니다.
    1. 빌드 시 prod_server_start.sh 에서 collectstatic을 수행하여 django 컨테이너 내 /.static_root 경로에 static file을 모읍니다.
    2. django 컨테이너의 /.static_root/ 는 static_volume 컨테이너와 bind 되어있습니다.
    3. nginx 컨테이너의 /static 폴더와 static_volume 컨테이너를 bind 하여 
    django container /.static_root <=> static_volume <=> nginx container /static 를 연결합니다.
    4. nginx 설정에서 /static/ 경로 요청 시 /static 폴더를 바라보도록 location 설정을 해놨습니다.