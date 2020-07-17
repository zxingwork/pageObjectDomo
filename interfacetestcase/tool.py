#!/usr/bin/env python
# encoding: utf-8
# @author   : changhsing
# @time     : 2020/7/17 13:29
# @site     : 
# @file     : tool.py
# @software : PyCharm
import pymysql
import string
import random
try:
    from interfacetestcase.Logger import *
except:
    from Logger import *


log = Logger('app.log', level='debug')


class Mysql:
    ALiyun_host = '120.24.148.131'
    TencentYun_host = '106.55.33.244'
    ALiyun_passwd = "ZXSSJDY"
    TencentYun_passwd = "zxssjdy111899"

    def __init__(self,
                 host=TencentYun_host,
                 port=3306,
                 db='admin1',
                 user='root',
                 passwd= TencentYun_passwd,
                 charset='utf8'):
        self.__host = host
        self.__port = port
        self.__db = db
        self.__user = user
        self.__passwd = passwd
        self.charset = charset
        pass

    def connect(self):
        con = pymysql.connect(host=self.__host,
                              port=self.__port,
                              db=self.__db,
                              user=self.__user,
                              passwd=self.__passwd,
                              charset=self.charset)
        return con

    def truncate_table(self, table):
        sql = f'truncate table {table }'
        try:
            con = self.connect()
            cursor = con.cursor()
            cursor.execute(sql)
        except Exception as e:
            log.logger.error(e)
        finally:
            con.close()
            cursor.close()


def random_string(n):
    """
    get a random string
    :param n: len of string
    :return: string
    """
    s = ''.join(random.sample(string.digits + string.digits + string.digits, n))
    return s
