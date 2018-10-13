# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup  
from urllib.request import urlopen
import os
import time


url = ""

# Use this function to get images during coffee brewing.
# Parameters are number of pics, delay between pics in seconds
def get_image_for_training(num, delay):
    
    # Take a new picture in every loop
    for x in range(0, num):
        
        html = urlopen(url)
        soup = BeautifulSoup(html, features='lxml')

        # Save image
        for res in soup.findAll('img'):
            print(res.get('src'))
            list_var = url.split('/')
            resource = urlopen(list_var[0]+"//"+list_var[2]+res.get('src'))
            output = open(res.get('src').split('/')[-1],'wb')
            output.write(resource.read())
            output.close()
            
            # Rename the image from image.jpg to coffee[incrementnum].jpg
            os.rename('image.jpg', './coffeepic/coffee' + str(x) +'.jpg')
        
        time.sleep(delay)
        
get_image_for_training(1, 1)