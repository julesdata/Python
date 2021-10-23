###source from 'https://bit.ly/3CagHQi'###

import pandas as pd


#######mysql.connector########
###데이터 불러오기

import mysql.connector

config = {
    'user': 'admin',
    'password': 'password',
    'host': '서버ip or 주소',
    'port': '포트',  #미입력 시 기본 포트 디폴트
    'db': '데이터베이스'
}

conn = mysql.connector.connect(**config)

sql = """
SELECT  *
  FROM  TEST_TABLE
"""

data = pd.read_sql(sql=sql, con=conn)

#######create_engine#######
###데이터 불러오기

from sqlalchemy import create_engine

engine = create_engine(f"mysql+mysqldb://{iid}:{pw}@{host}/{db_name}", encoding='utf-8')

sql = """
SELECT  *
  FROM  TEST_TABLE
"""

data = pd.read_sql(sql=sql, con=engine)

####파이썬에서 제작한 데이터 db에 입력하기(insert문 X)
from sqlalchemy import create_engine

engine = create_engine(f"mysql+mysqldb://{iid}:{pw}@{host}/{db_name}", encoding='utf-8')

data # python 에서 사용한 or 제작한 데이터

data.to_sql(name="테이블 이름", con=engine, if_exists='append', index = False)

#######pymysql#######
#mysql만 가능

###데이터 불러오기
import pymysql

host = '서버ip or 주소'
iid ='아이디'
pw = '비밀번호'
db_name = '데이터베이스'

conn = pymysql.connect(host=host, user= iid, password=pw, db=db_name, charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

# 데이터 사용 version 1 (데이터 조작하기 함께할 경우 커서 필요)
sql = """
SELECT  *
  FROM  TEST_TABLE
"""

curs.execute(sql)
rows = curs.fetchall()

data =pd.DataFrame(rows)

###데이터 조작하기
import pymysql

# 데이터 수정 및 삭제 
conn = pymysql.connect(host=host, user= iid, password=pw, db=db_name, charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

date = datetime.datetime.now().strftime("%Y%m%d")
sql = \
f"DELETE FROM TEST_TABLE WHERE DATE_FORMAT(operdt,'%Y%m%d') = '{date}'"
curs.execute(sql)

curs.close()
conn.commit()

### 데이터 사용 version 2 (데이터 불러오기만 할 경우)
import pymysql

host = '서버ip or 주소'
iid ='아이디'
pw = '비밀번호'
db_name = '데이터베이스'

conn = pymysql.connect(host=host, 
                       user= iid, 
                       password=pw, 
                       db=db_name,
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

sql = """
SELECT  *
  FROM  TEST_TABLE
"""

pd.read_sql(sql, conn)
