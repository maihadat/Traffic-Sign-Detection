
import os
import random

labels = [17, 43, 44, 45, 46, 47, 48]
'''
for label in labels:
    text_list = os.listdir('traffic_train/traffic_train/final/train/labels/'+str(label))
    taken_list = random.sample(range(len(text_list)), int(0.2*len(text_list)))
    os.makedirs('traffic_train/traffic_train/final/val/labels/'+str(label))
    os.makedirs('traffic_train/traffic_train/final/val/images/' + str(label))
    for i in taken_list:
        os.replace('traffic_train/traffic_train/final/train/labels/'+str(label)+'/'+text_list[i],
                   'traffic_train/traffic_train/final/val/labels/'+str(label)+'/'+text_list[i])
        os.replace('traffic_train/traffic_train/final/train/images/' + str(label) + '/' + text_list[i][:-3]+'png',
                   'traffic_train/traffic_train/final/val/images/' + str(label) + '/' + text_list[i][:-3]+'png')
'''
for label in labels:
    text_list1 = os.listdir('traffic_train/traffic_train/final/train/labels/'+str(label))
    text_list2 = os.listdir('traffic_train/traffic_train/final/val/labels/'+str(label))
    print(len(text_list2)/len(text_list1))


