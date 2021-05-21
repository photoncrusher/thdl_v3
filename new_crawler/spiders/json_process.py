import json
import re
f = open('e:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\macbook.json')
data = f.read()
data = re.sub('\]\[',',',data)
f2 = open('e:\Working place\PROJECT 20202\AAATEST\\new_crawler\\new_crawler\macbook1.json',"w+")
f2.write(data)

