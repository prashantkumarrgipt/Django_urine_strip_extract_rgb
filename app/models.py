from django.db import models
from django.http import JsonResponse
from PIL import Image
import numpy as np
import cv2

class Upload(models.Model):
    image = models.ImageField(upload_to='images/')

    def get_image_data(self):
        i = cv2.imread(self.image.path)
        img = cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
        s = img.shape
        h = s[0]
        w = s[1]
        x = int(h/10)
        xh = int(x/2)
        w1 = int(w/6)
        w2 = int((w/6) + (w/3)) 
        w3 = int((w/6) + 2*(w/3)) 
        
        labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
        data = {}
        for i in range(0, 10):
            p1 = img[xh + i*x, w1]
            p2 = img[xh + i*x, w2]
            p3 = img[xh + i*x, w3]
            array1 = np.array(p1)
            array2 = np.array(p2)
            array3 = np.array(p3)
            average = np.mean([array1, array2, array3], axis=0)
            ans = average.astype(int)
            data[labels[i]] = ans.tolist()

        return data
