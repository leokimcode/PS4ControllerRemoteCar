import pygame
import json, os
import socket 
import time

   

################# UDP SEND RECEIVE ################
UDP_IP = "192.168.12.118"
port = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

def moveLeft():
    string = "l"
    string += 255(abs(analog_keys[2]))
    print((string))

def moveRight():
    string = "r"
    string += 255(abs(analog_keys[2]))
    print((string))

def moveUp():
    string = "u"
    string += 255(abs(analog_keys[1]))
    print((string))

def moveDown():
    string = "b"
    string += 255(abs(analog_keys[1]))
    print((string))

################################# LOAD UP ####################################
pygame.init()
running = True
LEFT, RIGHT, UP, DOWN = False, False, False, False
clock = pygame.time.Clock()
###########################################################################################

#######################Initialize /ntroller#################################
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

with open(os.path.join("ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)
# 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
# 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }

################################ START OF GAME LOOP####################################3
while running:
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass

        # HANDLES BUTTON PRESSES
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['left_arrow']:
                LEFT = True
                print("left button pressed")
            if event.button == button_keys['right_arrow']:
                RIGHT = True
                print("right button pressed")
            if event.button == button_keys['down_arrow']:
                DOWN = True
                print("down button pressed")
            if event.button == button_keys['up_arrow']:
                UP = True
                print("up button pressed")

        # HANDLES BUTTON RELEASES
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['left_arrow']:
                LEFT = False
                print("left button released")
            if event.button == button_keys['right_arrow']:
                RIGHT = False
                print("right button released")
            if event.button == button_keys['down_arrow']:
                DOWN = False
                print("down button released")
            if event.button == button_keys['up_arrow']:
                UP = False
                print("up button released")

        #HANDLES ANALOG INPUTS for left joyaxis
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            # print(analog_keys)
            #Vertical for left axis
            if abs(analog_keys[1]) > .1:
                if analog_keys[1] < -.5:
                    UP = True
                    moveUp()
                else:
                    UP = False
                if analog_keys[1] > .5:
                    DOWN = True
                    moveDown()
                else:
                    DOWN = False

        #HANDLES ANALOG INPUTS for right joyaxis
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            # print(analog_keys)
            #Horizontal for right axis
            if abs(analog_keys[2]) > .1:
                if analog_keys[2] > .5:
                    RIGHT = True
                    moveRight()
                else:
                    RIGHT = False
                if analog_keys[2] < -.5:
                    LEFT = True
                    moveLeft()
                else:
                    LEFT = False
