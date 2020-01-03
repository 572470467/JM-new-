#coding = utf-8 
import time
from tkinter import*
import threading
import json
import os
import socket
import csv ,sys,operator
import tkinter.filedialog
import pygame
import sys
import pandas as pd
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
Brack=[0,0,0]
White=[255,255,255]
Red=[255,0,0]
Green=[0,255,0]
Gray=[169,169,169]
name='  OPEN'
width=pygame.display.Info().current_w
height=pygame.display.Info().current_h
height0=int((height-117)/3)
size=int((width-67)/3)
size0=(width-67)/9
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67+size,27)
color0=[Green,Green,Green,Green]
number_b=["B0","B1","B2","B3"]
icon={'11':'kz.jpg','01':'bz.jpg','00':'mz.jpg','10':'gz.jpg'}
screen = pygame.display.set_mode((int((width-67)/3),height))
text=pygame.font.SysFont("arial",24)
text1=pygame.font.SysFont("arial",16)
screen.fill(Brack)
class Bottles(object):
    def Icon_b(num,x,y,a):    
        img=pygame.image.load(icon[a])
        img=pygame.transform.smoothscale(img,(90,90))
        screen.blit(img,(x,y))
        text_fmt0=text.render(number_b[num],3,White)
        screen.blit(text_fmt0,(x-50,y+25))
        pygame.display.update()
    def WeightIcon(x,y,a): 
        img=pygame.image.load('cz0.jpg')
        img=pygame.transform.smoothscale(img,(90,90))
        screen.blit(img,(x,y))
        pygame.draw.rect(screen,Brack,[x+100,y+30,size0-60,30],0)
        text_fmt0=text.render(a,3,White)
        screen.blit(text_fmt0,(x+100,y+30))
        pygame.display.update()
    def VibratoryFeeder(x,y,a): 
        img=pygame.image.load(a)
        img=pygame.transform.smoothscale(img,(90,90))
        screen.blit(img,(x,y))
        pygame.display.update()
    def AN(num,x,y,a):  
        pygame.draw.rect(screen,color0[num],[x,y,72,35],0)
        text_fmt0=text1.render(a,3,Brack)
        screen.blit(text_fmt0,(x+2,y+4))
        pygame.display.update()
    def SJ(num,x,y,a): 
        text_fmt0=text1.render(a,3,White)
        screen.blit(text_fmt0,(x,y))
        pygame.draw.rect(screen,Green,[x,y+20,82,35],2)
        pygame.display.update()    
    def csv():   
        root=tkinter.Tk()
        root.withdraw()
        fname= tkinter.filedialog.askopenfilename(title=u"Select formula",initialdir=num)
        f=open(fname)
        next(f)
        reader=csv.reader(f)
        lt=[]
        for a in reader:
            lt.append(a)
        for t in lt:
            response=urllib.request.urlopen('http://192.168.10.201:5000/measure/{0}/{1}'.format(t[0],round(float(t[1])-float(t[2]),2)))
            print('http://192.168.10.201:5000/measure/{0}/{1}'.format(t[0],round(float(t[1])-float(t[2]),2)))
        color0[n]=Green
        mainloop()
    def State(num,n):
        threads=[]
        threads.append(threading.Thread(target=Bottles.csv))
        for t in threads:
            t.start()
if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            elif event.type == QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        for t in list:
                            if t[1]<=pos[0]<=t[1]+82 and t[2]<=pos[1]<=t[2]+35:
                                if t[3]=='ML_lifter' or t[3]=='ML_base':
                                    if color0[t[0]]==Green:
                                        color0[t[0]]=Red
                                        num=t[3]
                                        n=t[0]
                                        Bottles.State(num,n)
                                elif t[3]=='Reelect':
                                    python=sys.executable
                                    os.execl(python,python,*sys.argv)
                                elif t[0]==2:
                                    if color0[t[0]]==Green:
                                        color0[t[0]]=Red
                                        name=' CLOSE'
                                        response=urllib.request.urlopen("http://192.168.10.201:5000/valve/1")
                                    elif color0[t[0]]==Red:
                                        color0[t[0]]=Green
                                        name='  OPEN'
                                        response=urllib.request.urlopen("http://192.168.10.201:5000/valve/0")
        response9=urllib.request.urlopen("http://192.168.10.201:5000/level")
        html9=response9.read().decode()
        response11=urllib.request.urlopen("http://192.168.10.201:5000/scale")
        html11=response11.read()
        text11=json.loads(html11)
        B1=[[0,size0-70,160,str(html9[2])+str(html9[16])],[1,size0-70,30,str(html9[5])+str(html9[19])],[2,size0*3-110,160,str(html9[8])+str(html9[22])],[3,size0*3-110,30,str(html9[11])+str(html9[25])]]
        list=[[0,size0-120,370,'ML_lifter'],[1,size0-120,490,'ML_base'],[2,size0*2-60,640,name],[3,size0-120,610,'Reelect']]
        for t in list:
            Bottles.AN(t[0],t[1],t[2],t[3])
        for v in B1:
            Bottles.Icon_b(v[0],v[1],v[2],v[3])
        Bottles.VibratoryFeeder(size0*2-70,370,'zd.jpg')
        Bottles.WeightIcon(size0*2-70,490,b'%0.2f' % text11)

