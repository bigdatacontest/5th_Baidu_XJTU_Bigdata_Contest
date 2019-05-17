import os
import random

path = "../data/train_image/train/"
dirs = os.listdir(path)
files = {}# 一个超大字典

for dir in dirs:
    every_path = path + dir + "/"
    files[int(dir)] = []
    for file in os.listdir(every_path):
        files[int(dir)].append(every_path+file)
# print(files)


target_number = 10000

all_data = files
# 开始扩充数据集，每个到10000
for i in range(1, 10):
    for j in range(target_number - len(files[i])):
        all_data[i].append(files[i][random.randint(0, len(files[i]) - 1)])

# all_data是扩充后的总数据集，一共9万个
# print(len(all_data[9]))
#所有数据合并到一个列表中
finnal_all_data = []
for i in range(1, 10):
    finnal_all_data += all_data[i]

# print(len(finnal_all_data))
#扩充后的all_data，直接总体随机采样得到valid_data
# valid_data = []
valid_data = random.sample(finnal_all_data, 4500)
# for _ in range(4500):
#     temp = finnal_all_data[random.randint(0,90000)]
#     valid_data.append(temp)


# valid_data[random.randint(1, 10)] = random.sample(all_data[random.randint(1, 10)], 10)
# print(len(valid_data)) # 4500
# [ i for i in a if i not in b ]
# 这里的train_data每次的个数都不一样多，因为如果valid取走的数据，在all——data中有重复，那么train依然不能取这些重复的数据，一旦训练了就是背答案。
train_data = [i for i in finnal_all_data if i not in valid_data]
# print(len(train_data))


def write_data(path, data_name):
    f = open(path, "w+")
    for item in data_name:
        f.write(item+'\n')
    f.close()

write_data("../data/finnal_all_data.txt", finnal_all_data)
write_data("../data/train_data.txt", train_data)
write_data("../data/valid_data.txt", valid_data)


