import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt


class visualization(object):
    def KMean(self, filePath):
        k = 4
        data = pd.read_table(filePath)
        value = data.values
        seed = 9  # 设置随机种子
        clf = KMeans(n_clusters=k, random_state=seed)  # 聚类
        clf.fit(value)  # 拟合模型
        label = clf.labels_
        for i in range(k):
            y = label == i  # 得到boolean矩阵
            z = label[y]
            print(z.size)  # 输出每一类数量
        y_pred = clf.fit_predict(value)
        plt.figure(1)
        plt.scatter(value[:, 0], value[:, 1], s=1, c=y_pred)
        plt.xlabel('AGC_Piston_OS (bar)')
        plt.ylabel('Acc_F3_Bot_WR_Z (g)')
        plt.savefig('KMean.png')

    def GM(self, filePath):
        data = pd.read_table(filePath)
        value = data.values
        k = 4  # 设置聚类数
        gmm = GaussianMixture(n_components=k)
        gmm.fit(value)
        labels = gmm.predict(value)

        for i in range(k):
            y = labels == i  # 得到boolean矩阵
            z = labels[y]
            print(z.size)  # 输出每一类数量
        plt.figure(1)
        plt.scatter(value[:, 0], value[:, 1], s=1, c=labels)
        plt.xlabel('AGC_Piston_OS (bar)')
        plt.ylabel('Acc_F3_Bot_WR_Z (g)')
        plt.savefig('GM.jpg')
