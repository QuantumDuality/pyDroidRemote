import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time
mutable_object = {}

os.system('adb exec-out screencap -p > screen.png')
 
fig = plt.figure()
X_press_coordinate = np.array([0], dtype=np.float64)
Y_press_coordinate = np.array([0], dtype=np.float64)
X_release_coordinate = np.array([0], dtype=np.float64)
Y_release_coordinate = np.array([0], dtype=np.float64)


def onclick(event):
    global X_press_coordinate
    global Y_press_coordinate
    print('you pressed', event.key, event.xdata, event.ydata)
    X_press_coordinate = event.xdata
    #print type(X_press_coordinate)
    Y_press_coordinate = event.ydata
    #mutable_object['click'] = X_coordinate
    #os.system("adb shell input tap " + str(int(X_coordinate)) + " " + str(int(Y_coordinate)) )
    #os.system("adb exec-out screencap -p > screen.png")
    #plt.close()
    #fig = plt.figure()
    #cid = fig.canvas.mpl_connect('button_press_event', onclick)
    #screen =  mpimg.imread("screen.png", format=None)
    #plt.imshow(screen)
    #plt.show()
    #fig.canvas.mpl_disconnect(cid)
    cid = fig.canvas.mpl_connect('button_release_event', onrelease)



def onrelease(event):
    global X_release_coordinate
    global Y_release_coordinate
    print('you released on', event.key, event.xdata, event.ydata)
    X_release_coordinate = event.xdata
    Y_release_coordinate = event.ydata
    #mutable_object['click'] = X_coordinate
    os.system("adb shell input swipe " + str(int(X_press_coordinate)) + " " + str(int(Y_press_coordinate)) + " " + str(int(X_release_coordinate)) + " " + str(int(Y_release_coordinate))  )
    os.system("adb exec-out screencap -p > screen.png")
    #plt.close()
    screen =  mpimg.imread("screen.png", format=None)
    plt.clf()
    #fig.canvas.draw_idle()
    plt.imshow(screen)
    plt.show()

    global fig
    global cid
    fig = plt.figure()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)


cid = fig.canvas.mpl_connect('button_press_event', onclick)
screen =  mpimg.imread("screen.png", format=None)
plt.imshow(screen)
plt.show()




