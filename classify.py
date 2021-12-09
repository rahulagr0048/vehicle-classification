#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from glob import glob

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import csv


# In[8]:


new_model = tf.keras.models.load_model('saved_model/my_model')


# In[9]:


files = glob('{}/*/*_image.jpg'.format('test'))
files.sort()


# In[10]:


img_height = 180
img_width = 180
class_names = ['0', '1', '2']
name = '{}/test_labels.csv'.format('test')
with open(name, 'w') as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerow(['guid/image', 'label'])
    for file in files:
        guid = file.split('/')[-2]
        idx = file.split('/')[-1].replace('_image.jpg', '')
        img = tf.keras.utils.load_img(
        file, target_size=(img_height, img_width)
        )
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) # Create a batch

        predictions = new_model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        label = class_names[np.argmax(score)]
        writer.writerow(['{}/{}'.format(guid, idx), label])
    print('Wrote report file `{}`'.format(name))


# In[ ]:




