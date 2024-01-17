import cv2
import sys
import pygame as py
import numpy as np

cap = cv2.VideoCapture(0)
py.init()
py.display.set_caption("before_mirro")
screen = py.display.set_mode((2880,1800),py.FULLSCREEN)
gray = origin_img = np.zeros((1440,1080,3), np.uint8)
gray.fill(127)

imagebox = []

pc = 10
for i in range(0,pc):
    imagebox.append(gray)

h = 2880
w = 1800
time = 10001
fps = 20
clock = py.time.Clock()

# 480 640
# print(frame.shape)

def read():

    ret,frame = cap.read()
    frame = cv2.resize(frame, (1440,1080))
    frame = frame[0:h, 0:w]
    frame = np.rot90(frame)
    return frame

def output(frame):
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = py.surfarray.make_surface(img)
    return img

while True:
    for event in py.event.get():
        if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    sys.exit(0)
    
    if time > 10000:
        imagebox.append(read())
        del imagebox[0]
    else:
        time+=1

    frame =cv2.addWeighted(imagebox[0], 0.5, gray, 0.5, 0)

    for i in range(1,len(imagebox)): 
        frame = cv2.addWeighted(imagebox[i],0.5,frame,0.5,0)
    
    frame = cv2.addWeighted(read(),0.5,frame,0.5,0)

    frame = cv2.subtract(imagebox[-1], imagebox[-2])
    frame = output(frame)
    screen.blit(frame, (0, 0))
    py.display.update()
    clock.tick(fps)
