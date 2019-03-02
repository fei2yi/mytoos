import os
from PIL import Image
import pickle



with open('char_dict','rb') as man_file:
    a=pickle.load(man_file)


train_counter = 0
test_counter = 0
train_im_list=os.listdir('E:/Data/Images/train_img')
test_im_list=os.listdir('E:/Data/Images/test_img')
for train_im in train_im_list:
    char=train_im.split('_')[-1].split('.')[0]
    im_name=a.get(char)
    if im_name or im_name==0:
        class_name = './data/train/' + '%0.5d' % im_name
        if not os.path.exists(class_name):
            os.mkdir(class_name)
        try:
            im=Image.open('E:/Data/Images/train_img/%s'%train_im)
            im.resize((64,64),Image.ANTIALIAS).save(class_name+'/' + str(train_counter) + '.png')
            train_counter += 1
            print(train_im)
        except:
            continue

for train_im in test_im_list:
    char=train_im.split('_')[-1].split('.')[0]
    im_name=a.get(char)
    if im_name or im_name==0:
        class_name = './data/test/' + '%0.5d' % im_name
        if not os.path.exists(class_name):
            os.mkdir(class_name)
        try:
            im=Image.open('E:/Data/Images/test_img/%s'%train_im)
            im.resize((64,64),Image.ANTIALIAS).save(class_name+'/' + str(train_counter) + '.png')
            train_counter += 1
            print(train_im)
        except:
            continue


