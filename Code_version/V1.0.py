import cv2
import sys
import pygame as py
import numpy as np

# Constant

w,h = 2880,1800
moverange = 255
dmax,dmin = 240,15
blockwight = int(w/128)

fps = 20
clock = py.time.Clock()

default = np.zeros((64,48,3), np.uint8)
default.fill(0)
img1 = default
img2 = default

# Init

cap = cv2.VideoCapture(0)
py.init()
py.display.set_caption("before_mirro")
screen = py.display.set_mode((w,h),py.FULLSCREEN)

# Image Box

imagebox = []
pc = 30
for i in range(0,pc):
    imagebox.append(default)


# 480 640
# print(frame.shape)

# Camera read

def read():

    ret,frame = cap.read()
    frame = cv2.resize(frame, (64,48))
    frame = np.rot90(frame)
    return frame

# Detect Move

def detect():
    global imagebox

    move = img1-img2

    for i in range(0,64):
        for j in range(0,48):
            if detectbool(i,j,move):
                move[i][j] = [0,0,0]
            else:
                move[i][j] = [255,255,255]

    imagebox.append(move)
    del imagebox[0]

def detectbool(i,j,move):

    if (move[i][j][0] < dmin or move[i][j][0] > dmax) and (move[i][j][1] < dmin or move[i][j][1] > dmax) and (move[i][j][2] < dmin or move[i][j][2] > dmax):
        return True
    else:
        return False

# Add img

def addimg():

    sum = default

    for i in imagebox:
        sum = cv2.addWeighted(i,1,sum,0.9,0)
    
    return sum

# Draw

def draw():

    img = addimg()

    for i in range(0,64):
        for j in range(0,48):
            py.draw.rect(screen, img[i][j], py.Rect(i*blockwight, j*blockwight, blockwight, blockwight))

# Main loop

while True:
    for event in py.event.get():
        if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    sys.exit(0)
    
    img1 = read()
    
    detect()

    draw()

    py.display.update()

    img2 = img1

    clock.tick(fps)
