# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 21:12:47 2022

@author: Ark
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import docx

filePath = r'E:\OneDrive\NUS\CS5260\assignment 6/'
os.chdir(filePath)


text_file = open("col_step_SGD.txt", "r")
data = text_file.read()
text_file.close()
 
dataLst = data.split('/ Train')

loss_lr_DF_train = pd.DataFrame(columns=['loss','lr'])
for i in range(len(dataLst)):
    try:
        #i = 1
        #str1 = dataLst[i]
        lossStr = float(dataLst[i].split('Loss = ')[1].split(' ')[0].strip())
        lrStr = float(dataLst[i].split('LR = ')[1].split('\n')[1].strip())
        loss_lr_DF_train = loss_lr_DF_train.append({'loss':lossStr,'lr':lrStr},ignore_index=True)
    except:
        continue
    
dataLst = data.split('/ Test')

loss_lr_DF_test = pd.DataFrame(columns=['loss','lr'])
for i in range(len(dataLst)):
    try:
        #i = 1
        #str1 = dataLst[i]
        lossStr = float(dataLst[i].split('Loss = ')[1].split(' ')[0].strip())
        lrStr = float(dataLst[i].split('LR = ')[1].split('\n')[1].strip())
        loss_lr_DF_test = loss_lr_DF_test.append({'loss':lossStr,'lr':lrStr},ignore_index=True)
    except:
        continue    
    
    
fig = plt.figure()
ax = plt.axes()

ax.plot(loss_lr_DF_train.lr, loss_lr_DF_train.loss)
ax.plot(loss_lr_DF_test.lr, loss_lr_DF_test.loss)

