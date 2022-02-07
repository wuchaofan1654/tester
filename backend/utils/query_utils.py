# -*- coding: utf-8 -*-
"""
Create by sandy at 10:48 07/01/2022
Description: ToDo
"""

import os
import logging

logger = logging.getLogger('django')


class QueryUtil(object):
    @classmethod
    def grep_by_pattern(cls, pattern, path, recurse=True):
        shell = ['grep', '-n', pattern, path]

        if os.path.isdir(path) and recurse:
            shell.insert(1, '-r')

        return os.popen(' '.join(shell)).read()

    @classmethod
    def query_json(cls, content, query):
        try:
            for key in query.split('.'):
                if isinstance(content, dict):
                    content = content[key]
                elif isinstance(content, (list, tuple)):
                    content = content[int(key)]
                else:
                    logger.error(f'{key} error')
                    return None
            return content

        except Exception as err:
            logging.exception(err)
            return None

    @classmethod
    def compare_json_schema(cls, src: dict, dst: dict, result=None, pre=None) -> dict:
        try:
            if not result:
                result = {
                    "errors": [],
                    "warnings": []
                }

            if not isinstance(src, dict) or not isinstance(dst, dict):
                result["errors"].append(f'比较对象类型错误:  src: {type(src)}; dst: {type(dst)}')

            for key, value in src.items():
                if key not in dst.keys():
                    result["errors"].append(f'{key}在dst中不存在')
                    continue

                value_dst = dst[key]
                if type(value) != type(value_dst):
                    result["errors"].append(f'{key}类型不一致: src: {type(value)}; <dst: {type(value_dst)}')
                    continue

                if not value or not value_dst:
                    result["warnings"].append(f'{key}存在空值不能比较: src: {value}; dst: {value_dst}')
                    continue

                if isinstance(value, list):
                    value, value_dst = value[0], value_dst[0]
                    if type(value) != type(value_dst):
                        result["errors"].append(f'{key}类型不一致: src: {type(value)}; dst: {type(value_dst)}')
                        continue

                if isinstance(value, dict):
                    cls.compare_json_schema(value, value_dst, result)

        except Exception as err:
            logger.exception(err)

        finally:
            return result


if __name__ == '__main__':
    result_1 = QueryUtil.grep_by_pattern('class.*\\(.*\\)', './app.py')
    print(result_1)

    data_1 = {
        "errorCode": 200,
        "responseData": {
            "list": [
                {"username": "sandy", "sex": "male"},
                {"username": "sandy", "sex": "male"}
            ],
            "list_2": [
                {"username": "sandy", "sex": "male"},
                {"username": "sandy", "sex": "male"}
            ],
            "list_3": []
        }
    }

    data_2 = {
        "errorCode": 200,
        "responseData": {
            "list": [
                {"username": '18999890'}
            ],
            "list_2": [
                {"username": 188, "sex": "male"},
                {"username": "sandy", "sex": "male"}
            ],
            "list_3": [
                {"username": 188, "sex": "male"}
            ]
        }
    }
    result_2 = QueryUtil.query_json(data_1, 'responseData.list.0.sex')
    print(result_2)

    result_3 = QueryUtil.compare_json_schema(data_1, data_2)
    print(result_3)

