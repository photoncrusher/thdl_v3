from __future__ import division

import pandas as pd
import numpy as np


data = pd.read_csv("E:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\product.csv")
schema = pd.read_csv("E:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\\t1a.csv")

def jaccard_similarity(a, b):
    x = set(a)
    y = set(b)
    return len(x & y) / len(x | y)
def isNaN(string):
    return string != string

features = ["name","rom","ram"]
thresh_hold = 0.7
n_f = "status,resolution,screensize,screentech,cpu,gpu,size,rear_cam,front_cam,sim,tech,wifi,bluetooth,weigth,os,port".split(",")
for i in range(0,864):
  for j in range(0,87):
    simil_name = 0
    simil_rom = 0
    simil_ram = 0
    try:
      simil_name = jaccard_similarity(data["name"][i],schema["name"][j])
    except:
      simil_name = 0
    try:
      simil_rom = jaccard_similarity(data["rom"][i],schema["rom"][j])
    except:
      simil_rom = 0
    try:
      simil_ram = jaccard_similarity(data["ram"][i],schema["ram"][j])
    except:
      simil_ram = 0
    if simil_name >thresh_hold:
      for cols in n_f:
        if isNaN(data[cols][i]):
          print('filling data. ok!')
          data[cols][i] = schema[cols][j]
        continue

data.to_csv('E:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\data.csv')