#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import yaml


def get_admintoken(yamlName = "admintoken.yaml"):
    yaml.warnings({'YAMLLoadWarning': False})
    # 从配置文件中读取token值，并返回
    p = os.path.join(r'/Users/youjia/Desktop/Test_framework-master/config/admintoken.yaml')
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    return t["appToken"]


if __name__ == "__main__":
    get_admintoken()
