#!/usr/bin/env python
# encoding: utf-8
# @author   : changhsing
# @time     : 2020/7/17 13:12
# @site     : 
# @file     : testcase.py
# @software : PyCharm
import pytest
import allure
import requests

try:
    from interfacetestcase.tool import *
except:
    from tool import *

project_name = '博客接口'
correct_register_data = [(random_string(7), random_string(10)),
                         (random_string(7), random_string(10)),
                         (random_string(7), random_string(10)),
                         (random_string(7), random_string(10)),
                         (random_string(7), random_string(10)),
                         (random_string(7), random_string(10))]
error_register_data_username_null = [('', random_string(10)),
                         ('', random_string(10)),
                         ('', random_string(10)),
                         ('', random_string(10)),
                         ('', random_string(10)),
                         ('', random_string(10))]
error_register_data_password_null = [(random_string(7), ''),
                         (random_string(7), ''),
                         (random_string(7), ''),
                         (random_string(7), ''),
                         (random_string(7), ''),
                         (random_string(7), '')]
base_url = 'http://120.24.148.131:9527'
register_path = base_url + '/register'
login_path = base_url + '/login'


@allure.epic(project_name)
@allure.feature('登陆')
@allure.severity(allure.severity_level.BLOCKER)
class TestRegister(object):
    @allure.story('测试案例：正常注册')
    @pytest.mark.parametrize('username,password', correct_register_data)
    def test_register(self, username, password, truncate_table_users):
        """
        正常的测试案例
        """
        with allure.step('测试步骤：请求接口'):
            rq = requests.post(register_path, json={'username': username, 'password': password})
        assert rq.json()['status'] == '0000'

    @allure.story('测试案例：用户名为空')
    @pytest.mark.parametrize('username,password', error_register_data_username_null)
    def test_register_username_null(self, username, password, truncate_table_users):
        """
        错误的测试案例
        """
        with allure.step('测试步骤：请求接口'):
            rq = requests.post(register_path, json={'username': username, 'password': password})
        assert rq.json()['status'] == '0001'


