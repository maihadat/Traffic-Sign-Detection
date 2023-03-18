import os
import random


lst = os.listdir('traffic_train/traffic_train/cropped/labels')
dic = {}
for file in lst:
    with open('traffic_train/traffic_train/cropped/labels/'+file) as f:
        line = f.readline().split(',')
        label = int(line[0])
        if label not in dic:
            dic[label] = [file]
        else:
            dic[label].append(file)
print(dic)
for label in dic:
    os.makedirs('traffic_train/traffic_train/final/labels/' + str(label))
    os.makedirs('traffic_train/traffic_train/final/images/' + str(label))
    if len(dic[label]) > 2500:
        lst = random.sample(range(0, len(dic[label])), 2500)
        for i in lst:
            os.replace('traffic_train/traffic_train/cropped/images/'+dic[label][i][:-3]+'png',
                       'traffic_train/traffic_train/final/images/'+str(label)+'/'+dic[label][i][:-3]+'png')
            os.replace('traffic_train/traffic_train/cropped/labels/' + dic[label][i],
                       'traffic_train/traffic_train/final/labels/' + str(label) + '/' + dic[label][i])
    else:
        for i in range(len(dic[label])):
            os.replace('traffic_train/traffic_train/cropped/images/'+dic[label][i][:-3]+'png',
                       'traffic_train/traffic_train/final/images/'+str(label)+'/'+dic[label][i][:-3]+'png')
            os.replace('traffic_train/traffic_train/cropped/labels/' + dic[label][i],
                       'traffic_train/traffic_train/final/labels/' + str(label) + '/' + dic[label][i])





