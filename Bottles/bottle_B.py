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
import pandas as pd
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
state='closey'
state_a=['close','close','close','close','close']
state_b=['close','close','close','close']
line=['http://192.168.10.200:5000/measure/{0}/{1}','http://192.168.10.201:5000/measure/{0}/{1}']
Brack=[0,0,0]
White=[255,255,255]
Red=[255,0,0]
Green=[0,255,0]
Gray=[169,169,169]
width=pygame.display.Info().current_w
height=pygame.display.Info().current_h
height0=int((height-117)/3)
size=int((width-67)/2)
size0=(width-67)/9
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67+size,27)
color0=[Green,Green,Green,Green,Green,Green]
number_a=["A0","A1","A2","A3","A4"]
number_b=["B0","B1","B2","B3"]
icon={'00':'kz.jpg','10':'bz.jpg','11':'mz.jpg','01':'gz.jpg'}
#screen = pygame.display.set_mode((width-67,height0))
screen = pygame.display.set_mode((size,640))
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
        pygame.draw.rect(screen,Brack,[x+130,y+30,size0-40,30],0)
        text_fmt0=text.render(a,3,White)
        screen.blit(text_fmt0,(x+130,y+30))
        pygame.display.update()
    def VibratoryFeeder(x,y,a): 
        img=pygame.image.load(a)
        img=pygame.transform.smoothscale(img,(90,90))
        screen.blit(img,(x,y))
        pygame.display.update()
    def AN(num,x,y,a):  
        pygame.draw.rect(screen,color0[num],[x,y,82,35],0)
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
        default_dir= r"C:\Users\lenovo\Desktop\Bottles"  
        fname= tkinter.filedialog.askopenfilename(title=u"选择配方",initialdir=(os.path.expanduser(default_dir)))
        f=open(fname)
        reader=csv.reader(f)
        lt=[]
        for a in reader:
            lt.append(a)
        for t in lt:
            root.withdraw()
            response=urllib.request.urlopen(line[num].format(t[0],t[1]))
            print(line[num].format(t[0],t[1]))
        color0[n]=Green
        mainloop()
    def State(num,n):    #多线程
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
                                num=1
                                n=t[0]
                                if color0[t[0]]==Green:
                                    color0[t[0]]=Red
                                    Bottles.State(num,n)
                        for v in B1:
                            if v[1]<=pos[0]<=v[1]+90 and v[2]<=pos[1]<=v[2]+90:
                                if state_b==['close','close','close','close']:
                                    if index ==0:
                                        state_b[v[0]]='open'
                                        #response2=urllib.request.urlopen('http://192.168.10.201:5000/feeder/{}/1'.format(v[0]))
                                        #html2=response2.read()
                                        #text2=json.loads(html2)
                                        print('http://192.168.10.201:5000/feeder/{}/1'.format(v[0]))
                                elif state_b[v[0]]=='open':
                                    if index ==2:
                                        state_b[v[0]]='close'
                                        #response3=urllib.request.urlopen('http://192.168.10.201:5000/feeder/{}/0'.format(v[0]))
                                        #html3=response3.read()
                                        #text3=json.loads(html3)
                                        print('http://192.168.10.201:5000/feeder/{}/0'.format(v[0]))
                        if size0*6+70-size+70<=pos[0]<=size0*6+160-size+70 and 490<=pos[1]<=580:
                            if index == 0:
                                response6=urllib.request.urlopen("http://192.168.10.201:5000/feederon")
                                html6=response6.read()
                                text6=json.loads(html6)
                            elif index==2:
                                response7=urllib.request.urlopen("http://192.168.10.201:5000/feederoff")
                                html7=response7.read()
                                text7=json.loads(html7)
        time.sleep(1/3)
        response9=urllib.request.urlopen("http://192.168.10.119:80/bucketgroup/b")
        html9=response9.read().decode()
        response11=urllib.request.urlopen("http://192.168.10.201:5000/scale")
        html11=response11.read()
        text9=json.loads(html9)
        text11=json.loads(html11)
        B1=[[0,size0*5+70-size+70,160,text9['0']],[1,size0*5+70-size+70,30,text9['1']],[2,size0*7+70-size+70,160,text9['2']],[3,size0*7+70-size+70,30,text9['3']]]
        list=[[2,size0*4+80-size+70,350,'ML_lifter'],[3,size0*4+80-size+70,470,'ML_base']]
        for t in list:
            Bottles.AN(t[0],t[1],t[2],t[3])
        for v in B1:
            Bottles.Icon_b(v[0],v[1],v[2],v[3])
        Bottles.VibratoryFeeder(size0*6+70-size+70,370,'zd.jpg')
        Bottles.WeightIcon(size0*6+70-size+70,490,b'%0.2f' % text11)
