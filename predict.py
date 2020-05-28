import os
import sys
from tensorflow.keras import models as MODEL
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


def ext_frames(pth,pixel):
    frames=[]
    vcap=cv2.VideoCapture(pth)
    success, image=vcap.read()
    while success:
        image=cv2.resize(image,(pixel,pixel))
        frames.append(image)
        success, image=vcap.read()
    return np.asarray(frames)
    

def t_generator(arr):
    train_datagen= ImageDataGenerator(rescale=1./255)
    test_generator= train_datagen.flow(
        arr,
        shuffle=False,
        batch_size=1000)
    return test_generator

def predict_result(m,t_gen):
    result=m.predict(t_gen)
    return result

def predict(arr):
    length=len(arr)
    sp=int(4/5*length)
    arr=arr[sp:]
    length=len(arr)
    newarr=arr[arr<0.5]
    if len(newarr)>int(len(arr)*0.5):
        return True
    else:
        return False

def draw_graph(fn, arr):
    x=np.linspace(0, len(arr)/30.0, len(arr))
    y=arr
    ne=np.ma.masked_where(y>=0.5, y)
    po=np.ma.masked_where(y<0.5, y)
    plt.plot(x,ne,'bo',x,po,'ro',markersize=1.6)
    file_name= fn.split('/')[-1]
    plt.title(file_name)
    plt.xlabel('elapsed time in sec')
    plt.ylabel('value')
    plt.show()
    plt.clf()


def predict_file(path):
    frames=ext_frames(path,350)
    test_generator=t_generator(frames)
    model=MODEL.load_model('model.h5')
    result=model.predict(test_generator)
    #print(1)
    draw_graph(path, result)
    rst=predict(result)
  
    return rst
    

def main(arg):
    print(predict_file(arg))
    
if __name__ == "__main__":
    main(sys.argv[1])
    
