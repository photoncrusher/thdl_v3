import re
import pandas as pd

f = open("E:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\product.json",encoding='utf-8')
data = f.read()
data = re.sub("\n\]\[",",",data)
f.close()

f2 = open("E:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\product.json",'w',encoding='utf-8')
f2.write(data)
f2.close()

df = pd.read_json ("E:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\product.json",encoding='utf-8')
df.to_csv ("E:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\product.csv", index = None)