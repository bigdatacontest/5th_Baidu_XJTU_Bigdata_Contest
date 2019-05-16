""" 
1.读取train_visit/train的每一个文件  os.dir
2.f.open(),打开每一个文件，每个文件计算出自己的矩阵。存为一个npy
3.多个npy压缩成一个npz?
4.怎么拼接成4维？
"""
import os
import numpy as np
import pandas as pd 
import datetime

origin_date = datetime.date(year=2018,month=10,day=1)
# print(origin_date)
path = '../data/test_visit/test/'

target_array = np.zeros((4368))
# print(target_array.shape) 
dict_strdate = {}
dict_all_date = {} # '20181001': 0, '20181002': 1, '20181003': 2, 
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
    file_path = path + filename
    content = pd.read_csv(file_path, sep='\t', usecols=[1])
    # print(len(content))
    for i in range(len(content)):
        # print(content.iloc[i][0])
        target_array += get_array_this_visit(content.iloc[i][0])
    
    np.savetxt('../data/transform/test/'+filename, target_array, fmt='%d')

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

    