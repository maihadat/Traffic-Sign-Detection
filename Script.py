import os
import pandas as pd


def str_to_lst(s):
    s = s[1:-1]
    s = str.strip(s)
    s = str.split(s, ',')
    lst = []
    for i in s:
       lst.append(float(i))
    return lst


if __name__=='__main__':
    annotation = pd.read_csv('traffic_train/traffic_train/annotation.csv')
    processed = {}
    for i in range(len(annotation)):
        row = annotation.iloc[i]
        h = row['height']
        w = row['width']
        if row['file_name'] not in processed:
            processed[row['file_name']] = []
        lst = str_to_lst(row['bbox'])
        lst[0] /= w
        lst[2] /= w
        lst[1] /= h
        lst[3] /= h
        lst = [int(row['category_id'])] + lst
        processed[row['file_name']].append(lst)
    os.makedirs('traffic_train/traffic_train/labels')
    for file in processed:
        s = ''
        for line in processed[file][:-1]:
            s += str(line)[1:-1] + '\n'
        s += str(processed[file][-1])[1:-1]
        with open('traffic_train/traffic_train/labels/'+file+'.txt', 'w') as f:
            f.write(s)




