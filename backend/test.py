# -*- coding: utf-8 -*-
"""
Create by sandy at 17:37 30/12/2021
Description: ToDo
"""

data = [
    {'id': 1, 'parentId': 0, 'name': '1'},
    {'id': 2, 'parentId': 1, 'name': '1-2'},
    {'id': 3, 'parentId': 1, 'name': '1-3'},
    {'id': 4, 'parentId': 2, 'name': '1-2-4'},
    {'id': 5, 'parentId': 0, 'name': '1'},
    {'id': 6, 'parentId': 3, 'name': '1'},
    {'id': 7, 'parentId': 3, 'name': '1'},
    {'id': 8, 'parentId': 3, 'name': '1'},
    {'id': 9, 'parentId': 8, 'name': '1'},
    {'id': 10, 'parentId': 8, 'name': '1'},
    {'id': 11, 'parentId': 8, 'name': '1'},
    {'id': 12, 'parentId': 11, 'name': '1'},
    {'id': 13, 'parentId': 11, 'name': '1'},
    {'id': 14, 'parentId': 11, 'name': '1'},
    {'id': 15, 'parentId': 14, 'name': '1'},
    {'id': 16, 'parentId': 14, 'name': '1'},
    {'id': 17, 'parentId': 16, 'name': '1'},
    {'id': 18, 'parentId': 16, 'name': '1'},
]


result = set()


class GetTreeNode(object):
    def __init__(self):
        self._result_set = set()

    def result_set(self, start_id: int, include_start_id=True):
        self.__generate_children_ids(start_id=start_id, include_start_id=include_start_id)
        return self._result_set

    def all_objects(self):
        pass

    def __generate_children_ids(self, start_id=1, include_start_id=True):
        if include_start_id:
            self._result_set.add(start_id)

        children = [d for d in data if d['parentId'] == start_id]
        if children:
            [self._result_set.add(child['id']) for child in children]
            [self.__generate_children_ids(child.get('id')) for child in children]


print(GetTreeNode().result_set(1))
