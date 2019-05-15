#!/usr/bin/env python
# coding=utf-8

import pandas as pd
import os

# 获取当前文件父目录路径
father_path = os.getcwd()

# 保存数据文件路径
path_csv = father_path + r'\data01\temp_city.csv'

# 写入数据
data = {"站点名": ["北京北", "北京东", "北京", "北京南", "北京西"],
        "代号": ["VAP", "BOP", "BJP", "VNP", "BXP"]}

# 数据初始化为dataframe对象
df = pd.DataFrame(data)

# 数据写入
df.to_csv(path_csv)
