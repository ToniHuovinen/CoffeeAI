# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:21:23 2018

@author: Toni Huovinen

This program fetches a picture from the websites server, analyzes it and returns
prediction of the contents (volume) of coffee pot
"""

from bs4 import BeautifulSoup  
from urllib.request import urlopen
import numpy as np
from keras.preprocessing import image
from sklearn.preprocessing import StandardScaler

# Loads the previously trained model
from keras.models import load_model

# Removed the url for obvious reasons
url = ""

html = urlopen(url)
soup = BeautifulSoup(html, features='lxml')

# Save the image from the webcam/server
for res in soup.findAll('img'):
    print(res.get('src'))
    list_var = url.split('/')
    resource = urlopen(list_var[0]+"//"+list_var[2]+res.get('src'))
    output = open(res.get('src').split('/')[-1],'wb')
    output.write(resource.read())
    output.close()
    

# Loads the trained model
model = load_model('coffeemodel.h5')

# Load the fetched image and process it
# Convert it to 1 x 4096 array
target = image.load_img('image.jpg', grayscale=True, target_size = (1, 4096))
target = np.array(target)
target = np.float64(target)

scaler = StandardScaler()

# Temporarily change the shape of array for scaling. After that change shape to previous
target = np.reshape(target, (4096,1))
target = scaler.fit_transform(target)
target = np.reshape(target, (1,4096))

# Prediction
pred = model.predict(target)

if pred[0][0] < 0.3:
    print("")
    print("Office is Closed")
else:
    print("")
    print("Pot is {0:.2f}% full.".format(pred[0][0]))











