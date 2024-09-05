import pymysql
import random
import string
import os
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
class database(object):
    @classmethod
    def init_DB(cls):
        db = pymysql.connect(
            host ="localhost",
            user ="root",
            passwd ="123456",
            database = "test"
        )
        cursor = db.cursor()
        with open(BASE_DIR+os.sep+"databases"+os.sep+'test.sql',encoding='utf-8',mode='r') as f:
            sql_list = f.read().split(';')[:-1]
            for x in sql_list:
                if '\n' in x:
                     x = x.replace('\n', ' ')
                if '    ' in x:
                     x = x.replace('    ', '')
                     sql_item = x+';'
                     print(sql_item)
                     cursor.execute(sql_item)
        db.close()

    @classmethod
    def generate_random_str(cls,randomlength=16):
        """
        string.digits=0123456789
        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        """
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
        random_str = ''.join(str_list)
        return random_str
    
    @classmethod
    def get_data(cls,query_sql):
        lst = []
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db="test")
        cursor = db.cursor()
        cursor.execute(query_sql)
        lst = cursor.fetchall()
        db.close()
        return lst

    @classmethod
    def delete_data(cls,delete_sql):
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db="test")
        cursor = db.cursor()
        cursor.execute(delete_sql)
        db.commit()
        db.close()

    @classmethod
    def insert_data(cls,insert_sql):
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db="test")
        cursor = db.cursor()
        cursor.execute(insert_sql)
        db.commit()
        db.close()

    @classmethod
    def update_data(cls,update_sql):
        db = pymysql.connect(host='10.226.68.67', port=3306, user='root', passwd='123456', db="test")
        cursor = db.cursor()
        cursor.execute(update_sql)
        db.commit()
        db.close()


