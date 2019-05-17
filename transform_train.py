""" 
1.读取train_visit/train的每一个文件  os.dir
2.打开每一个文件，每个文件计算出自己的矩阵。存为一个txt或则npy
3.需不需要压缩成一个文件？
4.读取数据的时候，怎么拼接，占内存会不会很大
"""
import os
import numpy as np
import pandas as pd 
import datetime

origin_date = datetime.date(year=2018,month=10,day=1)
# print(origin_date)
path = '../data/train_visit/train/'# 没有就自己建

# print(target_array.shape) 
dict_strdate = {}# 这里没用到，可能后面有用，为了速度快
dict_all_date = {} # '20181001': 0, '20181002': 1, '20181003': 2, 用字典来读取，速度快
for i in range(182):
    date = origin_date + datetime.timedelta(days=i)
    date = str(date).replace('-', '')
    dict_strdate[date] = int(date)
    dict_all_date[date] = i

# print(dict_all_date)

def get_the_index(only_day_like_20181001):
    return dict_all_date[only_day_like_20181001] * 24


def getfilenames(path):
    files = os.listdir(path)
    return files

def get_array_this_visit(date_hour):
    date_hour = date_hour.split(',')
    array_this_visit = np.zeros((4368))
    for item in date_hour:
        item = item.split('&')
        hours = item[1].split('|')
        index = get_the_index(item[0])
        
        for hour in hours:
            array_this_visit[index + int(hour)] += 1
    return array_this_visit

# print(get_array_this_visit("20181004&15,20181009&11,20181012&14").shape)

# print(getfilenames(path))


filenames = getfilenames(path)


for filename in filenames:
    """
    每一个访问者，都对应自己的一个矩阵
    """
    file_path = path + filename
    target_array = np.zeros((4368))# 关键是要找到这个矩阵的索引，这个是目标矩阵
    content = pd.read_csv(file_path, sep='\t', usecols=[1])
    # print(len(content))
    for i in range(len(content)):
        # print(content.iloc[i][0])
        target_array += get_array_this_visit(content.iloc[i][0])# 目标矩阵找到在一个地区中，每一个访问者的矩阵并加起来
    
    np.savetxt('../data/transform/train/'+filename, target_array, fmt='%d')# 一个地区保存为一个txt

# print(target_array)


# f = open(file_path)
# file = f.read()
# user_visits = []
# user_visits = file.split('\n')
# for user_visit in user_visits
#     visit_times = []
#     visit_times = (user_visit.split('\t'))[1]
#     for visit_time in visit_times:
#        target_array += get_array_this_visit(str(visit_time))

# for _, date_hour in content.iterrows():
#     print(date_hour[0])
    
    # target_array += get_array_this_visit(str(date_hour))

# np.savetxt('c.txt',target_array,fmt='%d')
# print(target_array,target_array.shape)

    