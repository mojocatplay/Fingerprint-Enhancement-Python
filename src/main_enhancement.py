# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:42:58 2016

@author: utkarsh
"""

import numpy as np
import imageio
import skimage
from skimage.util import img_as_uint
#import cv2
import numpy as np;
import matplotlib.pylab as plt;
import scipy.ndimage
import sys

from image_enhance import image_enhance


if(len(sys.argv)<2):
    print('loading sample image');
    img_name = '2.jpg'
    img = imageio.imread('../images/' + img_name);
elif(len(sys.argv) >= 2):
    img_name = sys.argv[1];
    img = imageio.imread(sys.argv[1]);
    
if(len(img.shape)>2):
    # img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    img = np.dot(img[...,:3], [0.299, 0.587, 0.114]);

rows,cols = np.shape(img);
aspect_ratio = np.double(rows)/np.double(cols);

new_rows = 800;             # randomly selected number
new_cols = new_rows/aspect_ratio;

#img = cv2.resize(img,(new_rows,new_cols));
img = skimage.transform.resize(img,(np.int(new_rows),np.int(new_cols)));

enhanced_img = image_enhance(img);    

if(1):
    print('saving the image')
    imageio.imwrite('../enhanced/' + img_name,img_as_uint(enhanced_img));
else:
    plt.imshow(enhanced_img,cmap = 'Greys_r');
