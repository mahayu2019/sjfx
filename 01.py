#!/usr/bin/env python
# coding=utf-8

import pandas as pd
import os

# 获取当前文件父目录路径
father_path = os.getcwd()

# 原始数据文件路径
rpath_csv = father_path + r'\data01\city_station.csv'

# 读取数据
csv_read = pd.read_csv(rpath_csv)

#显示前10条数据
print(csv_read.head(10))
