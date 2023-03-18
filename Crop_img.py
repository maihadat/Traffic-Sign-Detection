
from PIL import Image
import pandas as pd
import os 


def round_up(f):
    if f>int(f):
        return int(f)
    else:
        return int(f)+1


def crop_img(img_path, bouding_box, img_size, id, crop_size=(50, 50)):
    image = Image.open(img_path)
    x, y, w, h = bouding_box
    x0, y0 = img_size
    x1 = round_up(x-w/2-crop_size[0])
    x2 = round_up(x+w/2+crop_size[0])
    y1 = round_up(y-h/2-crop_size[1])
    y2 = round_up(y+h/2+crop_size[1])
    t1 = x1<0
    t2 = x2>x0
    t3 = y1<0
    t4 = y2>y0
    if t1:
        x1 = 0
    if t2:
        x2 = x0
    if t3:
        y1 = 0
    if t4:
        y2 = y0
    crop_img = image.crop((x1, y1, x2, y2))
    crop_img.save('traffic_train/traffic_train/cropped/images/'+str(id)+'.png')
    new_bbox = [(x-x1)/(x2-x1), (y-y1)/(y2-y1), w/(x2-x1), h/(y2-y1)]
    new_size = [(x2-x1), (y2-y1)]
    return new_bbox, new_size


def str_to_lst(s):
    s = s[1:-1]
    s = str.strip(s)
    s = str.split(s, ',')
    lst = []
    for i in s:
       lst.append(float(i))
    return lst


if __name__=='__main__':
    map = {
        1: 17,
        2: 43,
        3: 44,
        4: 45,
        5: 46,
        6: 47,
        7: 48
    }
    os.makedirs('traffic_train/traffic_train/cropped/images')
    os.makedirs('traffic_train/traffic_train/cropped/labels')
    annotation = pd.read_csv('traffic_train/traffic_train/annotation.csv')
    for i in range(len(annotation)):
        row = annotation.iloc[i]
        h = row['height']
        w = row['width']
        lst = str_to_lst(row['bbox'])
        new_bbox, new_size = crop_img('traffic_train/traffic_train/images/'+str(row['file_name']), lst, (w, h), i)
        s = str(map[row['category_id']]) + ',' + str(new_bbox)[1:-1]
        with open('traffic_train/traffic_train/cropped/labels/'+str(i)+'.txt', 'w') as f:
            f.write(s)




