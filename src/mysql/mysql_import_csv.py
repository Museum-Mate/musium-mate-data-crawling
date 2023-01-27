import os
import json

import pymysql

# Load secrets.json
with open('../secrets.json') as f:

    json_data = json.load(f)

#####################################################
DB_USER_NAME = json_data['MYSQL_USERNAME']
DB_USER_PASSWORD= json_data['MYSQL_PASSWORD']
DB_HOST = json_data['MYSQL_HOST']
DB_TABLE_NAME = json_data['MYSQL_DB_NAME']
#####################################################

# DB 연결
db = pymysql.connect(
    user = DB_USER_NAME,
    password = DB_USER_PASSWORD,
    host = DB_HOST,
    db =  DB_TABLE_NAME,
    charset = 'utf8',
)

# 커서 획득 
cursor = db.cursor(pymysql.cursors.DictCursor)

# 데이터 입력. list 형 데이터 
insert_data = [['raul', 10],
               ['zidane', 7],
               ['ronaldo', 9]]
insert_sql = "INSERT INTO `people` VALUES (%s, %s);"

cursor.executemany(insert_sql, insert_data)

db.commit()