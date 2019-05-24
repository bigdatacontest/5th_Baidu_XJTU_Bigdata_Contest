import numpy as np
import os
import random

# path = "../data/train_data.txt"
# f = open(path)
# while 1:
#     lines = f.readlines(100000)
#     if not lines:
#         break
#     for line in lines:
#         print(line) # do something


path_train = '../data/transform/train/'
path_test = '../data/transform/test/'
visits_train = []
labels_train = []
visits_test = []
def getfilenames(path):
    files = os.listdir(path)
    return files

# print(getfilenames(path))
for file in getfilenames(path_train):
    visits_train.append(np.loadtxt(path_train + file).reshape(26, 24, 7))
    labels_train.append(file[-7:-4])
    # print(labels)

X_train = np.array(visits_train)
y_train = np.array(list(map(int, labels_train)))

np.save('../data/visit_npy/X_train.npy', X_train)
np.save('../data/visit_npy/y_train.npy', y_train)
# print(X)
# print(y)


for file in getfilenames(path_test):
    visits_test.append(np.loadtxt(path_test + file).reshape(26, 24, 7))

np.save('../data/visit_npy/visit_test.npy', visits_test)



def generate_batch_data_random(x, y, batch_size):
    """逐步提取batch数据到显存，降低对显存的占用"""
    ylen = len(y)
    loopcount = ylen // batch_size
    while (True):
        i = randint(0,loopcount)
        yield x[i * batch_size:(i + 1) * batch_size], y[i * batch_size:(i + 1) * batch_size]
