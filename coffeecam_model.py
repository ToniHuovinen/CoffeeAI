# -*- coding: utf-8 -*-

import numpy as np
import os
import pandas as pd
from keras.preprocessing import image
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense

# Use this script to create dataset consisting of each image in folder, and their respected yvalues
# You have to manually create a csv. I will turn that into automatic process eventually.
# For Dataset creation, run only the dataprocessing part. For training, run only the MODEL part

# DATAN PROCESSING
path = './coffeepic/'

dataset = np.empty((0,4096), int)
pathlist = os.listdir(path)


results = pd.read_csv("yvalues.csv")

# Transfer all the images in a folder to an array
for x in range(len(pathlist)):
    
    # Loads the image into a single row
    test_image = image.load_img('./coffeepic/' + str(pathlist[x]), grayscale=True, target_size = (1, 4096))

    dataset = np.append(dataset, test_image, axis=0)

# Combine the imagedata and yvalues, and after that shuffle the order
dataset = np.column_stack((dataset, results))
np.random.shuffle(dataset)

# At this spot I will add the csv-creation eventually so you don't have to do it manually



# ==========================================================================
# MODEL AND TRAINING. Using Keras
data_frame = pd.read_csv("dataset.csv")

# Separate data into training set results
X = data_frame.iloc[:,0:-1].values
y = data_frame.iloc[:,-1].values

# Create trainingset and testset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Scale the X values
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Model
model = Sequential()

# Input layer and first hidden layer
model.add(Dense(units=64, kernel_initializer='uniform', activation='relu', input_dim=4096))

# Second hidden layer
model.add(Dense(units=64, kernel_initializer='uniform', activation='relu'))

# Output layer. Result comes out as an continuous number. No need for activation functions
model.add(Dense(units=1, kernel_initializer= 'uniform'))

# Fit and Compile
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, verbose=1, batch_size=3, epochs=50)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
score = model.evaluate(X_test, y_test, verbose=0)

# Save the model. To be used in CoffeeAI.py
model.save("coffeemodel.h5")














