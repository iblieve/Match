#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
import json
import os
import os.path
import subprocess
import xlrd
import xlwt
import re
import socket
import urllib.request
from urllib import parse
import pymysql
import sys


class XUtils(object):
    G_DIGIT_DICT = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}

    # @staticmethod
    # def has_valid_lat_lng(p_address_dict=None):
    #     """
    #
    #     :param p_address_dict:
    #     :return:
    #     """
    #     rst = False
    #     try:
    #         a = 1.0 / p_address_dict['longitude']
    #         a = 1.0 / p_address_dict['latitude']
    #         rst = True
    #     except Exception as e:
    #         rst = False
    #     return rst

    @staticmethod
    def convert_chinese_numerals_2_arabic_numerals_for_dict(p_address_dict=None, p_key=None):
        p_str = p_address_dict[p_key]
        return XUtils.convert_chinese_numerals_2_arabic_numerals_4_str(p_str=p_str)

    @staticmethod
    def convert_chinese_numerals_2_arabic_numerals_4_str(p_str=None):
        """ 将汉字数字转换为阿拉伯数字

        :param p_str:
        :return:
        """
        result = ''
        for i in range(0, len(p_str)):
            tmp_char = p_str[i]
            if tmp_char in XUtils.G_DIGIT_DICT.keys():
                tmp_char = XUtils.G_DIGIT_DICT[tmp_char]
            result = result + str(tmp_char)
        return result

    @staticmethod
    def remove_noise_province_city_district(p_address_dict=None, p_key=None):
        """ 丢弃噪音数据
        比如省市县啥的， 就不应该参与比较， 这个没意义
        :param p_address_dict:
        :param p_key:
        :return:
        """
        provinceName = p_address_dict['provinceName'] if p_address_dict['provinceName'] is not None else ''
        cityName = p_address_dict['cityName'] if p_address_dict['cityName'] is not None else ''
        districtName = p_address_dict['districtName'] if p_address_dict['districtName'] is not None else ''
        townName = p_address_dict['townName'] if p_address_dict['townName'] is not None else ''
        # 去除噪音数据(省市县)
        s = p_address_dict[p_key]
        s = s.replace(provinceName, '').replace(cityName, '').replace(districtName, '').replace(townName, '')
        return s

    @staticmethod
    def remove_noise_empty_punctuation(p_address_dict=None, p_key=None):
        """ 丢弃噪音数据
        :param p_address_dict:
        :param p_key:
        :return:
        """
        #
        # 去除噪音数据(空格, 标点符号...)
        s = str(p_address_dict[p_key])
        s = XUtils.trim(s)
        s = XUtils.remove_punctuation(s)
        return s

    @staticmethod
    def remove_punctuation(text):
        """删除标点符号
        :param text:
        :return:
        """
        punctuation = '!,;:?"\''
        text = re.sub(r'[{}]+'.format(punctuation), '', text)
        return text.strip().lower()

    @staticmethod
    def trim(str):
        newstr = ''
        for ch in str:  # 遍历每一个字符串
            if ch != ' ':
                newstr = newstr + ch
        return newstr

    @staticmethod
    def process_and_dump_2_excel(p_excel_title=None, p_new_excel_list=None, p_new_file=None):
        stus = [p_excel_title]
        for tmp_dict in p_new_excel_list:
            arr = []
            for title in p_excel_title:
                value = tmp_dict[title]
                arr.append(value)
            stus.append(arr)

        if os.path.exists(p_new_file):
            os.remove(p_new_file)
        success = XUtils.dict_to_excel(p_write_excel_file_path=p_new_file, p_sheet_name='Sheet1', p_dict_content=stus,
                                       p_excel_title_list=p_excel_title)

    @staticmethod
    def findlogandlat(full_address):
        """

        :param full_address:
        :return:
        """
        query = {
            'key': 'lD4KiCvXfGho6afGao2ztKXiUq9rQNmZ',
            'address': full_address,
            'output': 'json',
        }

        base = 'http://api.map.baidu.com/geocoder?'
        url = base + parse.urlencode(query)

        doc = urllib.request.urlopen(url)
        s = doc.read().decode('utf-8')
        try:
            jsonData = json.loads(s)
            lat = jsonData['result']['location']['lat']
            lng = jsonData['result']['location']['lng']
        except Exception as e:
            lat = 0.0
            lng = 0.0
        return lat, lng

    @staticmethod
    def read_excel(p_read_excel_file_path=None) -> (None):
        """
        读入excel文件
        :rtype : object
        :param p_read_excel_file_path:
        :return: 数据对象
        """
        try:
            data = xlrd.open_workbook(p_read_excel_file_path)
            return data
        except Exception as err:
            print(err)

    @staticmethod
    def excel_to_list(p_read_excel_file_path=None, p_sheet_name=None, p_excel_title_list=None) -> (list):
        """
        :rtype : object
        :return list
        """
        my_list = []
        data = XUtils.read_excel(p_read_excel_file_path=p_read_excel_file_path)
        table = data.sheet_by_name(p_sheet_name)
        for i in range(1, table.nrows):
            row_content = table.row_values(i, 0, table.ncols)
            dict_column = dict(zip(p_excel_title_list, row_content))

            dict_column = XUtils.cn_2_en(dict_column)

            my_list.append(dict_column)
        return my_list

    @staticmethod
    def cn_2_en(p_dict: str = None):
        """

        :param p_dict:
        :return:
        """
        excel_titles = [{'cn': 'group_id', 'en': 'group_id'},
                        {'cn': '序号', 'en': 'rowid'},
                        {'cn': '地址编号', 'en': 'locationId'},
                        {'cn': '省份', 'en': 'provinceName'},
                        {'cn': '城市', 'en': 'cityName'},
                        {'cn': '区/县', 'en': 'districtName'},
                        {'cn': '乡', 'en': 'townName'},
                        {'cn': '详细地址（拼接省市区）', 'en': 'locationName'},
                        {'cn': '详细地址(PROD地址)', 'en': 'address'},
                        {'cn': '经度', 'en': 'longitude'},
                        {'cn': '纬度', 'en': 'latitude'}]
        for title_dict in excel_titles:
            if title_dict['cn'] in p_dict.keys():
                p_dict[title_dict['en']] = p_dict[title_dict['cn']]
                if title_dict['en'] != title_dict['cn']:
                    del p_dict[title_dict['cn']]
        return p_dict

    @staticmethod
    def dict_to_excel(p_write_excel_file_path: str = None, p_sheet_name: str = None, p_dict_content=None,
                      p_excel_title_list=None) -> (bool):
        """
        将字典写入excel中
        :type dict_content: object dict
        excel_title 列标题
        """
        book = xlwt.Workbook()
        sheet = book.add_sheet(p_sheet_name)
        row_index = 0
        for stu in p_dict_content:
            col_index = 0
            for value in stu:
                sheet.write(row_index, col_index, value)
                col_index += 1
            row_index += 1
        book.save(p_write_excel_file_path)
        return True

    @staticmethod
    def fetch_all_mobiles(p_text=None) -> (list):
        """
        :param p_text: 文本
        :return: 返回手机号列表
        """
        if p_text is None:
            mobiles = []
        else:
            mobiles = re.findall(r"1\d{10}", p_text)
        return mobiles

    @staticmethod
    def fetch_all_emails(p_text=None) -> (list):
        """
        :param text: 文本
        :return: 返回电子邮件列表
        """
        if p_text is None:
            emails = []
        else:
            emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", p_text)
        return emails

    @staticmethod
    def fetch_all_urls(p_text=None) -> (list):
        """
        :param text: 文本
        :return: 返回url列表
        """
        if p_text is None:
            urls = []
        else:
            urls = re.findall(
                r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)",
                p_text)
            urls = list(sum(urls, ()))
            urls = [x for x in urls if x != '']
        return urls

    @staticmethod
    def fetch_all_ips(p_text=None) -> (list):
        """
        :param text: 文本
        :return: 返回ip列表
        """
        if p_text is None:
            ips = []
        else:
            ips = re.findall(
                r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",
                p_text)
        return ips

    @staticmethod
    def get_git_info() -> (dict):
        """get version dict

        :return: version info
        :rtype: dict
        Usage::
        """
        d = dict()
        g_git_active_branch_name = 'unknown'
        g_git_last_update_time_std_fmt = 'unknown'
        g_git_last_update_time_int_fmt = 'unknown'
        g_git_last_update_version_int = -1
        g_git_last_update_version_hexsha = 'unknown_version'
        g_git_last_update_message = 'unknown'
        g_git_last_update_author_name = 'unknown'
        g_git_last_update_author_email = 'unknown'
        # gitpython==2.1.7
        # try:
        #     from git import Repo
        #     repo_path = './'
        #     repo = Repo(repo_path)
        #     # check that the repository loaded correctly
        #     if not repo.bare:
        #         g_git_active_branch_name = repo.active_branch.name
        #
        #         headcommit = repo.head.commit
        #         # __git_md5_version__
        #         g_git_last_update_version_hexsha = str(headcommit.hexsha)
        #         #
        #         cmd = 'git log --since="Oct 27 9:16:10 2000 +0800"  --pretty=oneline | wc -l'
        #         status, output = subprocess.getstatusoutput(cmd)
        #         g_git_last_update_version_int = output.strip(' ')
        #
        #         g_git_last_update_message = str(headcommit.message)
        #         g_git_last_update_author_name = str(headcommit.author.name)
        #         g_git_last_update_author_email = str(headcommit.author.email)
        #
        #         # standard format
        #         g_git_last_update_time_std_fmt = str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(headcommit.committed_date)))
        #         # int format
        #         g_git_last_update_time_int_fmt = str(time.strftime("%Y%m%d%H%M%S", time.gmtime(headcommit.committed_date)))
        # except Exception as e:
        #     print(str(e))
        #     pass
        
        # NOTE https://www.jianshu.com/p/b2fec735e7cf
        try:
            import re
            import subprocess
            output = os.popen('git status | head -1').read()
            try:
                g_git_active_branch_name = re.match(r'On branch (.*)', output).groups(0)[0]
            except Exception as e:
                try:
                    g_git_active_branch_name = re.match(r'HEAD detached at (.*)', output).groups(0)[0]
                except Exception as e:
                    pass

            status, output = subprocess.getstatusoutput('git log --since="Oct 27 9:16:10 2017 +0800"  --pretty=oneline | wc -l')
            g_git_last_update_version_int = output.strip()

            status, output = subprocess.getstatusoutput('git show -s --format=%an')
            g_git_last_update_author_name = output

            status, output = subprocess.getstatusoutput('git show -s --format=%ae')
            g_git_last_update_author_email = output

            status, output = subprocess.getstatusoutput('git show -s --format=%H')
            g_git_last_update_version_hexsha = output

            status, output = subprocess.getstatusoutput('git show -s --format=%B')
            g_git_last_update_message = output

            status, output = subprocess.getstatusoutput('git config log.date iso')
            status, output = subprocess.getstatusoutput('git show --summary')
            g_git_last_update_time = output.split('\n')[2]
            if g_git_last_update_time.find('Date:') < 0:
                g_git_last_update_time = output.split('\n')[3]
            g_git_last_update_time = g_git_last_update_time.replace('Date:', '').replace('+0800', '').strip()
            time_array = time.strptime(g_git_last_update_time, "%Y-%m-%d %H:%M:%S")
            g_git_last_update_time_std_fmt = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
            g_git_last_update_time_int_fmt = time.strftime("%Y%m%d%H%M%S", time_array)
        except Exception as e:
            pass

        d['__debug_git_active_branch_name__'] = g_git_active_branch_name
        d['__debug_git_last_update_time_std_fmt__'] = g_git_last_update_time_std_fmt
        d['__debug_git_last_update_time_int_fmt__'] = g_git_last_update_time_int_fmt
        d['__debug_git_last_update_version_int__'] = g_git_last_update_version_int
        d['__debug_git_last_update_version_hexsha__'] = g_git_last_update_version_hexsha
        d['__debug_git_last_update_message__'] = g_git_last_update_message
        d['__debug_git_last_update_author_name__'] = g_git_last_update_author_name
        d['__debug_git_last_update_author_email__'] = g_git_last_update_author_email
        return d

    @staticmethod
    def get_host_name() -> (str):
        """get host name

        :return: git infoascii
        :rtype: dict

        Usage::
        """
        v = 'unknown'
        try:
            v = str(os.popen('hostname').read()).replace('\n', '')
        except Exception as e:
            v = 'unknown'
        return v

    @staticmethod
    def get_host_ipv4() -> (str):
        """
        :return: ipv4
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ipv4 = s.getsockname()[0]
        except Exception as e:
            ipv4 = '0.0.0.0'
        finally:
            s.close()

        return ipv4

    @staticmethod
    def get_debug_info() -> (dict):
        d = XUtils.get_git_info()
        d['__debug_host_ipv4__'] = XUtils.get_host_ipv4()
        d['__debug_host_name__'] = XUtils.get_host_name()
        return d

    @staticmethod
    def dump_list_2_excel(p_title_list=None, p_data_list=None, p_excel_name: str = None, p_sheet_name: str = 'Sheet1'):
        """
        create a new excel and dump the data to this excel

        p_title_list 列标题
        p_data_list
        p_excel_name
        p_sheet_name
        """
        to_excel = [p_title_list]
        book = xlwt.Workbook()
        sheet = book.add_sheet(p_sheet_name)
        row_index = 0
        for i in range(len(p_data_list)):
            sing_address = []
            for value in p_data_list[i].values():
                sing_address.append(value)
            to_excel.append(sing_address)

        for i in range(len(to_excel)):
            col_index = 0
            for val in to_excel[i]:
                sheet.write(row_index, col_index, val)
                col_index += 1
            row_index += 1

        if os.path.exists(p_excel_name):
            os.remove(p_excel_name)
        book.save(p_excel_name)

    @staticmethod
    def db_connect_with_pymysql(p_user=None, p_host=None, p_passwd=None, p_db_name=None, p_charset=None):
        '''

        :param p_db_name:
        :param p_conf:
        :return: success    : true indicate connect success, otherwise not.
                 conn       : connection
                 cursor     : cursor
        '''

        success = False
        conn = None
        cur = None
        try:
            conn = pymysql.connect(user=p_user, host=p_host, port=3306, passwd=p_passwd, db=p_db_name, charset=p_charset)
            cur = conn.cursor()
            success = True
        except Exception as e:
            print
            e.message
            import traceback
            traceback.print_exc()
            if conn is not None:
                conn.rollback()
            success = False
            conn = None
            cur = None

        return success, conn, cur

    @staticmethod
    def db_close(p_cursor=None, p_conn=None):
        try:
            p_cursor.close()
            p_conn.close()
        except Exception as e:
            print >> sys.stderr, "MySQLException", str(e)

    @staticmethod
    def execute_sql(p_sql=None, p_cur=None, p_conn=None):
        success = False
        if p_sql is not None:
            try:
                p_cur.execute(p_sql)
                p_conn.commit()
                success = True
            except Exception as e:
                success = False
                print >> sys.stderr, "MySQLException", p_sql, str(e)
        return success

    @staticmethod
    def executemany_sql(p_sql=None, p_cur=None, p_conn=None, p_param=None):
        success = False
        if p_sql is not None and p_param is not None and len(p_param) > 0:
            try:
                p_cur.executemany(p_sql, p_param)
                p_conn.commit()
                success = True
            except Exception as e:
                success = False
                print >> sys.stderr, "MySQLException", p_sql, str(e)
        return success

    @staticmethod
    def fetchall_sql(p_sql=None, p_cur=None):
        success = False
        results = tuple()
        try:
            p_cur.execute(p_sql)
            results = p_cur.fetchall()
            success = True
        except Exception as e:
            success = False
            results = tuple()
            print >> sys.stderr, "MySQLException", p_sql, str(e)
        return success, results


