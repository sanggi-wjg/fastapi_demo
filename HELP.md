### To Do List
* [ ] MySQL, Redis Docker-compose 세팅
* [ ] MySQL User REST API 개발
* [ ] Redis User Session 연동 개발

### Help
```shell
uvicorn main:app --reload

uvicorn --help
```

### Install
```shell
# 애플리케이션을 운영 환경에 배포하려는 경우 다음과 같이 합니다
pip install fastapi
# 추가로 서버 역할을 하는 uvicorn을 설치합니다
pip install uvicorn
# config Settings .env 적용을 위해서 
pip install pydantic[dotenv]
```

