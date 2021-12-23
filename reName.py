#coding=utf-8
import os
from tqdm import tqdm
dir_path = 'D:/CLUST2015'

List = ['ICR-03_1','ICR-03_2','ICR-03_3','ICR-04_1','ICR-04_2','ICR-04_3','ICR-04_4','ICR-03_1']
# D:\CLUST2015\ICR-02_1
# D:\CLUST2015\ICR-03_1
def reName():
    for i in tqdm(List):
        # D:\CLUST2015\ICR - 04_4\Data
        for a in os.listdir(os.path.join(dir_path,i) + '/' + 'Data'):
            if 'ICR' in i:
                src = os.path.join(dir_path, i) + '/' + 'Data' + '/' + a
                dst = os.path.join(dir_path,i) + '/' + 'Data' + '/' + a[1:9]
                os.rename(src,dst)
a = reName()
