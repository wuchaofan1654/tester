# -*- coding: utf-8 -*-
"""
Create by sandy at 11:35 23/12/2021
Description: ToDo
"""
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


AUTHOR_USER = get_user_model()


BOOL_CHOICES = {
    (0, _('否')),
    (1, _('是'))
}

STATUS_CHOICES = (
    (0, _('禁用')),
    (1, _('正常')),
    (2, _('仅自己可见')),
)

EXECUTE_STATUS_CHOICES = (
    (0, _('未执行')),
    (1, _('成功')),
    (2, _('失败')),
    (3, _('阻塞')),
    (4, _('部分失败'))
)

POINT_TYPE_CHOICES = (
    (1, _('事件')),
    (2, _('页面')),
)


