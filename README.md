# CoffeeAI
Deeplearning project for identifying the contents (volume) of coffeepot through webcam captured image

How this works:

The webcam has been set up so that it takes an image from the coffeepot every 30 second. Image is then saved into serverside. When the script CoffeeAI is run, it will scrape the website, looking for image tag, once it founds the tag it will then take whatever image is stored in the source attribute.

After that, image will be converted into grayscale and turned into array, with dimensions 1 x 4096 (essentially 64x64). When grayscale image is turned into array, what you get is a numerical value for each pixel ranging from 0 - 255. That data is then normalized and it will be inserted into trained deeplearning model for calculations.

Output is a approximation of coffee volume in the pot.


Training:

I have also included a script for training the model, so that you can use it on your own projects. What you need is a series of pictures from the thing you want to quantify. You can use the third script I have provided to do so or use your own methods.
