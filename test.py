import numpy as np


path_train = '../data/transform/train/'

visits_train = []
labels_train = []
file = '000000_008.txt'
visits_train.append(np.loadtxt(path_train + file).reshape(26, 24, 7))
labels_train.append(file[-7:-4])
X_train = np.array(visits_train)
y_train = np.array(list(map(int, labels_train)))
# c = np.hstack((X_train, y_train))
print(X_train.shape)
print(y_train.shape)