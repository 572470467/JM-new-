#coding = utf-8 
import time
from tkinter import*
import threading
import json
import os
import sys
name='  OPEN'
import socket
import csv ,sys,operator
import tkinter.filedialog
import pygame
import pandas as pd
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67,27)
Black=[0,0,0]
White=[255,255,255]
Red=[255,0,0]
Green=[0,255,0]
Gray=[169,169,169]
width=pygame.display.Info().current_w
height=pygame.display.Info().current_h
size0=(width-67)/9
color0=[Green,Green,Green,Green,Green]
number_a=["A0","A1","A2","A3","A4"]
icon={'11':'kz.jpg','01':'bz.jpg','00':'mz.jpg','10':'gz.jpg'}
screen = pygame.display.set_mode((int((width-67)/3),height))
text=pygame.font.SysFont("arial",24)
text1=pygame.font.SysFont("arial",16)
screen.fill(Black)
class Bottles(object):
    def Icon_a(num,x,y,a):  
        img=pygame.image.load(icon[a])
        img=pygame.transform.smoothscale(img,(90,90))
        screen.blit(img,(x,y))
        text_fmt0=text.render(number_a[num],3,White)
        screen.blit(text_fmt0,(x-50,y+25))
        pygame.display.update() 
    def WeightIcon(x,y,a): 
        img=pygame.image.load('cz0.jpg')
        img=pygame.transform.smoothscale(img,(90,90))
        screen.blit(img,(x,y))
        pygame.draw.rect(screen,Black,[x+100,y+30,size0-60,30],0)
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
        text_fmt0=text1.render(a,3,Black)
        screen.blit(text_fmt0,(x+2,y+4))
        pygame.display.update()
    def SJ(num,x,y,a): 
        text_fmt0=text1.render(a,3,White)
        screen.blit(text_fmt0,(x,y))
        pygame.draw.rect(screen,Green,[x,y+20,82,35],2)
        pygame.display.update()
    def PF():
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
            response=urllib.request.urlopen('http://192.168.10.200:5000/measure/{0}/{1}'.format(t[0],round(float(t[1])-float(t[2]),2)))
            print('http://192.168.10.200:5000/measure/{0}/{1}'.format(t[0],round(float(t[1])-float(t[2]),2)))
        color0[n]=Green
        mainloop()
    def State(num,n):   
        threads=[]
        threads.append(threading.Thread(target=Bottles.PF))
        for t in threads:
            t.setDaemon(True)
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
                                if t[3]=='FT_lifter' or t[3]=='FT_base':
                                    if color0[t[0]]==Green:
                                        color0[t[0]]=Red
                                        num=t[3]
                                        n=t[0]
                                        Bottles.State(num,n)
                                elif t[3]=='Reelect':
                                    python=sys.executable
                                    os.execl(python,python,*sys.argv)
                                elif t[3]=='  ZERO':
                                    response=urllib.request.urlopen("http://192.168.10.200:5000/zerosclae")                                       
                                elif t[0]==2:
                                    if color0[t[0]]==Green:
                                        color0[t[0]]=Red
                                        name=' CLOSE'
                                        response=urllib.request.urlopen("http://192.168.10.200:5000/valve/1")             
                                    elif color0[t[0]]==Red:
                                        color0[t[0]]=Green
                                        name='  OPEN'
                                        response=urllib.request.urlopen("http://192.168.10.200:5000/valve/0")
        response8=urllib.request.urlopen("http://192.168.10.200:5000/level")
        html8=response8.read().decode()
        a=(html8[2:-3].split('], ['))[0].split(', ')
        b=(html8[2:-3].split('], ['))[1].split(', ')        
        response10=urllib.request.urlopen("http://192.168.10.200:5000/scale")
        html10=response10.read()
        text10=json.loads(html10)
        B0=[[0,70,160,str(a[0])+str(b[0])],[1,70,30,str(a[1])+str(b[1])],[2,size0*2+20,240,str(a[2])+str(b[2])],[3,size0*2+20,120,str(a[3])+str(b[3])],[4,size0*2+20,0,str(a[4])+str(b[4])]]        
        #B0=[[0,70,160,str(html8[2])+str(html8[19])],[1,70,30,str(html8[5])+str(html8[22])],[2,size0*2+20,240,str(html8[8])+str(html8[25])],[3,size0*2+20,120,str(html8[11])+str(html8[28])],[4,size0*2+20,0,str(html8[14])+str(html8[31])]]
        list=[[0,size0*3-100,370,'FT_lifter'],[1,size0*3-100,490,'FT_base'],[2,size0+10,640,name],[3,size0*3-100,610,'Reelect'],[4,size0-120,640,'  ZERO']]
        for t in list:
            Bottles.AN(t[0],t[1],t[2],t[3])
        for i in B0:
            Bottles.Icon_a(i[0],i[1],i[2],i[3])
        Bottles.VibratoryFeeder(size0,370,'lx.jpg')
        Bottles.WeightIcon(size0,490,b'%0.2f' % text10)
