# FastAPI Demo
A simple example of using FastAPI in Python3.   

## Dev conditions
* Language : Python 3.10
* Framework : FastAPI
    * Docs: https://fastapi.tiangolo.com/
* Database : MySQL 8.0
    * SqlAlchemy
        * SqlAlchemy Docs: https://docs.sqlalchemy.org/en/14/orm/quickstart.html
        * SQLAlchemy의 연결 풀링 이해하기
          * https://spoqa.github.io/2018/01/17/connection-pool-of-sqlalchemy.html
    * Alembic(simple sample)
        * Alembic Docs: https://alembic.sqlalchemy.org/en/latest
        * Alembic 설명 Blog : https://blog.neonkid.xyz/257
* etc
    * Redis (not yet)
    * requirement.txt

## Run
1. create and set `.env.local` file
2. run app/main.py 

## Run with docker
```shell
comming soon
```



## Access URLs
check port `in .env file` 

* http://localhost:8090/~
* http://localhost:8090/redoc
* http://localhost:8090/docs
