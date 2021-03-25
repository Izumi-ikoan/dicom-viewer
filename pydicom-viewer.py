#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pydicom
import os
from matplotlib import pyplot as plt
import cv2
get_ipython().run_line_magic('matplotlib', 'inline')

root_dir = './dicomtest'
dcms = []
for curdir, dirs, files in os.walk(root_dir):
    for fl in files:
        if ".dcm" in fl.lower():
            dcms.append(os.path.join(curdir, fl))

for dcm in dcms:
    d_img = pydicom.read_file(dcm)
    d_raw_array = d_img.pixel_array
    max = d_raw_array.max()
    d_array = (d_raw_array / max) *255
    cv2.imwrite('./resulttest/01.png', d_array)

