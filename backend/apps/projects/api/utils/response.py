# -*- coding: utf-8 -*-
"""
Create by sandy at 16:58 23/12/2021
Description: ToDo
"""

import logging
import re

logger = logging.getLogger('django')


class Response(object):
    compare_result = []

    @classmethod
    def compare(cls, json_prod, json_test):
        assert isinstance(json_prod, dict)
        assert isinstance(json_test, dict)

        for key, value in json_prod.items():
            if key not in json_test.keys():
                cls.compare_result.append(f'{key}在 json_test中不存在')
                continue

            value_test = json_test[key]
            if type(value) != type(value_test):
                cls.compare_result.append(f'{key}: prod_type={type(value)}; test_type={type(value_test)}')

            if isinstance(value, (list, tuple)):
                if not value or not value_test:
                    continue

                value, value_test = value[0], value_test[0]
                if type(value) != type(value_test):
                    cls.compare_result.append(f'{key}: prod_type={type(value)}; test_type={type(value_test)}')
                    continue

            if isinstance(value, dict):
                cls.compare(value, value_test)

    @classmethod
    def query_json(cls, content: dict, query: str):
        try:
            for word in query.split('.'):
                if isinstance(content, dict):
                    content = content[word]
                elif isinstance(content, list):
                    content = content[int(word)]
            return content

        except Exception as error:
            logger.exception(error)
            return content

    @classmethod
    def regex(cls, content, pattern):
        try:
            content = str(content)
            return re.search(pattern, content).group()
        except Exception as error:
            logger.exception(error)
            return []


if __name__ == '__main__':
    json1 = {
        'name': 'wuchaofan',
        'info': {
            'age': 30,
            'hobbit': ['watching movie', 'swimming'],
            'favorites': [
                {
                    'book': ['lover'],
                    'movie': 'kung'
                }
            ]
        }
    }

    json2 = {
        'name': 'wuchaofan',
        'info': {
            'age': 30,
            'hobbit': [],
            'favorites': [
                {
                    'book': 'lover',
                    'movie': 'sunday'
                }
            ]
        }
    }

    Response.compare(json1, json2)
    print(Response.compare_result)
    print(Response.regex(json1, r'favorites.+?}'))
