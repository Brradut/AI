import matplotlib.pyplot as plt
import skimage.io as skio
import numpy as np
import sys
import random
import math
import tensorflow as tf
from keras import layers, models


def load_test_im():
    images = []
    for i in range(1, 1001):
        im = skio.imread('test/' + str(i) + '.png')
        images.append(im.tolist())
    return images

def load_test_labels():
    f = open('test/labels.txt')
    x = []
    for line in f.readlines():
        x.append(int(line[:-1]))
    return x


def load_training_im():
    images = []
    for i in range(1, 4001):
        im = skio.imread('training/' + str(i) + '.png')
        images.append(im.tolist())
    return images

def load_training_labels():
    f = open('training/labels.txt')
    x = []
    for line in f.readlines():
        x.append(int(line[:-1]))
    return x

def to_sepia(image):
    new_image = []
    for row in image:
        new_image.append([])
        for cell in row:
            r, g, b = cell[0], cell[1], cell[2]
            sr = 0.393 * r + 0.769 * g + 0.189 * b
            sg = 0.349 * r + 0.686 * g + 0.168 * b
            sb = 0.272 * r + 0.534 * g + 0.131 * b
            new_image[-1].append([int(sr), int(sg), int(sb)])
    return np.array(new_image)

#am folosit setul de date cifar 10 fiindca avea imagini de 32 pe 32
def create_db():
    folder = 'cat/'
    folder_save = 'img/'
    pre = '000'
    i = 1
    while i <= 5000:
        if i > 9:
            pre = '00'
        if i > 99:
            pre = '0'
        if i > 999:
            pre = ''
        filename = folder + pre + str(i) + '.png'
        im = skio.imread(filename)
        skio.imsave(folder_save + str(i) + '.png', im)
        im2 = to_sepia(im)
        skio.imsave(folder_save + str(i) + '_sepia.png', im2)
        i = i + 1

def separate_data(ratio = 0.8, dataSize = 5000):
    random.seed(5)
    indexes = [e for e in range(1, dataSize+1)]
    
    trainingSize = math.floor(dataSize * ratio)
    testSize = dataSize - trainingSize
    
    trainingIndexes = random.sample(indexes, trainingSize)
    testIndexes = [e for e in indexes if e not in trainingIndexes] 
    
    j = 1
    tn, ts, ten, tes = 0, 0, 0, 0
    f = open('training/labels.txt', 'w')
    for i in trainingIndexes:
        im = []
        if i % 2 == 0:
            im = skio.imread('img/'+str(i) + '.png')
            skio.imsave('training/' + str(j) + '.png', im)
            f.write('0\n')
            tn = tn + 1
        else:
            im = skio.imread('img/' + str(i) + '_sepia.png')
            skio.imsave('training/' + str(j) + '.png', im)
            f.write('1\n')
            ts = ts + 1
        j = j + 1
    
    j = 1 
    f = open('test/labels.txt', 'w')
    for i in testIndexes:
        im = []
        if i % 2 == 0:
            im = skio.imread('img/'+str(i) + '.png')
            skio.imsave('test/' + str(j) + '.png', im)
            f.write('0\n')
            ten = ten + 1
        else:
            im = skio.imread('img/' + str(i) + '_sepia.png')
            skio.imsave('test/' + str(j) + '.png', im)
            f.write('1\n')
            tes = tes + 1
        j = j + 1
    print(tn, ts, ten, tes)

def train():

    shape = (32, 32, 3)
    model = models.Sequential()
    #input
    model.add(layers.Conv2D(filters = 16, kernel_size =3, activation = 'relu', input_shape = shape))
    #hidden layer
    model.add(layers.Conv2D(32, 3, activation='relu'))
    #output
    model.add(layers.Flatten())
    model.add(layers.Dense(1, activation = 'sigmoid'))

    model.compile(loss = tf.keras.losses.BinaryCrossentropy(), optimizer = tf.optimizers.Adam(), metrics = ['accuracy'])
    model.summary()

    #train
    model.fit(load_training_im(), load_training_labels(), epochs=10, verbose =1, batch_size = 1)
    model.save('models/model')


    #test
    model = tf.keras.models.load_model('models/model')
    pred = model.predict(load_test_im())
    acc = 0
    testOut = load_test_labels()
    for i in range(len(testOut)):
        rez = 0
        if(pred[i] > 0.5):
           rez = 1 
        if rez == testOut[i]:
            acc = acc + 1

    print(acc/len(testOut))
def main():
    #create_db()
    #separate_data()
    train()

    

if __name__ == "__main__":
    main()
