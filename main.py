import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time


midCoords = [960,540]

gameCoords = [900, 440, 1020, 560]

bobberCoords = [951,476,968,496]
# bobberCoords = [951,356+20,973,382+20]
menuCoords = [951+250,396-50,973+250,422-50]

def avgColor(screen):
    global bobberCoords
    num_x = bobberCoords[2]-bobberCoords[0]
    num_y = bobberCoords[3]-bobberCoords[1]
    sum = [0,0,0]
    for x in range(num_x):
        for y in range(num_y):
            sum[0] += screen[y][x][0]
            sum[1] += screen[y][x][1]
            sum[2] += screen[y][x][2]
    avg = [int(sum[0]/(num_x*num_y)),int(sum[1]/(num_x*num_y)),int(sum[2]/(num_x*num_y))]
    return avg

# while True:
#     mousePos = queryMousePosition()
#     print(str(mousePos.x) + ", " + str(mousePos.y), flush=True)
#     time.sleep(1.0)

while True:
    time.sleep(1)
    mousePos = queryMousePosition()
    # print(str(mousePos.x) + ", " + str(mousePos.y), flush=True)
    menu_screen = np.array(ImageGrab.grab(bbox=menuCoords))
    menu_color = avgColor(menu_screen)
    # print(menu_color)

    if not (menu_color[0]<120 and menu_color[0]>110 and
        menu_color[1]<120 and menu_color[1]>110 and
        menu_color[2]<120 and menu_color[2]>110):
        print("INSIDE", flush=True)
        bobber_screen = np.array(ImageGrab.grab(bbox=bobberCoords))
        # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        print(avgColor(bobber_screen), flush=True)
        # print(screen[393-bobberCoords[1]][959-bobberCoords[0]])
        print("Throw bobber", flush=True)
        click(mousePos.x,mousePos.y)
        time.sleep(2)
        print("Start checking for dip", flush=True)
        nodip = True
        while nodip:
            bobber_screen = np.array(ImageGrab.grab(bbox=bobberCoords))
            bobber_color = avgColor(bobber_screen)
            print(bobber_color, flush=True)
            if bobber_color[0]<40:
                print("Reel in", flush=True)
                click(mousePos.x,mousePos.y)
                nodip = False
