import cv2
import sys
import numpy as np
import pygame as py

# Constant

w,h = 1440,900
error = 30
pc = 100
interval = 1
layer = 10

camera_wight = 48
camera_high = int(camera_wight*0.75)
blockwight = int(w/camera_wight)

fps = 20
clock = py.time.Clock()

default = np.zeros((camera_wight,camera_high,3), np.uint8)
default.fill(0)
img1 = default
img2 = default
imagebox = [default.copy() for _ in range(pc)]

# Init

cap = cv2.VideoCapture(0)
py.init()
py.display.set_caption("before_mirro")
# screen = py.display.set_mode((w,h))
screen = py.display.set_mode((w,h),py.FULLSCREEN)

# 480 640
# print(frame.shape)

# Camera read

def read():
    ret,frame = cap.read()
    return np.rot90(cv2.resize(frame, (camera_wight,camera_high)))

# Cv2 to pygame(photo)

def output(frame):
    img = cv2.resize(frame,(w,int(w*0.75)))
    img = img[0:w,0:h]
    img = py.surfarray.make_surface(img)
    return img

# Detect Move

def detect(img1,img2):
    move = np.abs(img1 - img2)
    mask = np.all((error > move) | (move > 255 - error), axis = 2)
    move[~mask] = blockwight
    move[mask] = 0
    imagebox.append(move)
    del imagebox[0]

# Add img

def addimg():

    start = max(0,len(imagebox) - (interval*layer))
    img = imagebox[start::interval]

    sum = default
    for i in range(layer):
        sum = cv2.addWeighted(img[i],1,sum,0.9,0)
    
    return sum

# Draw

def draw(img):
    for i in range(0,camera_wight):
        for j in range(0,camera_high):
            py.draw.rect(screen, (0,0,0), py.Rect(i*blockwight, j*blockwight, blockwight, blockwight))
            py.draw.rect(screen, (255,255,255), py.Rect(i*blockwight, j*blockwight, np.mean(img[i][j]), np.mean(img[i][j])))

# Main loop

while True:
    for event in py.event.get():
        if event.type == py.KEYDOWN and event.key == py.K_SPACE:
            sys.exit(0)
    
    img1 = read()
    detect(img1,img2)
    draw(addimg())

    py.display.update()

    img2 = img1

    clock.tick(fps)
