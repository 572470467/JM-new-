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
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67,27)
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
size0=(width-67)/9
color0=[Green,Green,Green,Green,Green,Green]
number_a=["A0","A1","A2","A3","A4"]
number_b=["B0","B1","B2","B3"]
icon={'00':'img/kz.jpg','10':'img/bz.jpg','11':'img/mz.jpg','01':'img/gz.jpg'}
#screen = pygame.display.set_mode((width-67,height0))
screen = pygame.display.set_mode((width-67,640))
text=pygame.font.SysFont("arial",24)
text1=pygame.font.SysFont("arial",16)
screen.fill(Brack)
class Bottles(object):
    def Icon_a(num,x,y,a):  
        img=pygame.image.load(icon[a])
        img=pygame.transform.smoothscale(img,(90,90))
        screen.blit(img,(x,y))
        text_fmt0=text.render(number_a[num],3,White)
        screen.blit(text_fmt0,(x-50,y+25))
        pygame.display.update() 
    def Icon_b(num,x,y,a):    
        img=pygame.image.load(icon[a])
        img=pygame.transform.smoothscale(img,(90,90))
        screen.blit(img,(x,y))
        text_fmt0=text.render(number_b[num],3,White)
        screen.blit(text_fmt0,(x-50,y+25))
        pygame.display.update()
    def WeightIcon(x,y,a): 
        img=pygame.image.load('img/cz.jpg')
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
        fname= tkinter.filedialog.askopenfilename(title=u"Select formula",initialdir=(os.path.expanduser(default_dir)))
        f=open(fname)
        reader=csv.reader(f)
        lt=[]
        for a in reader:
            lt.append(a)
        for t in lt:
            root=tkinter.Tk()
            root.withdraw()
            response=urllib.request.urlopen(line[num].format(t[0],t[1]))
            print(line[num].format(t[0],t[1]))
        color0[n]=Green
    def State(num,n):    #多线程
        threads=[]
        threads.append(threading.Thread(target=Bottles.csv))
        for t in threads:
            t.daemon = True
            t.start()
if __name__ == '__main__':
    while True:
        pygame.draw.rect(screen,Red,[size0*3+60,315,size0+110,100],2)
        pygame.draw.rect(screen,Red,[size0*3+60,435,size0+110,100],2)
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
                                if color0[t[0]]==Green:
                                    color0[t[0]]=Red
                                    if t[3]=='FT_lifter' or t[3]=='ML_lifter':
                                        color0[1]=Gray
                                        color0[3]=Gray
                                        if t[3]=='FT_lifter':
                                            num=0
                                            n=t[0]
                                            Bottles.State(num,n)
                                        elif t[3]=='ML_lifter':
                                            num=1
                                            n=t[0]
                                            Bottles.State(num,n)
                                    elif t[3]=='FT_base' or t[3]=='ML_base':
                                        color0[0]=Gray
                                        color0[2]=Gray
                                        if t[3]=='FT_base':
                                            num=0
                                            n=t[0]
                                            Bottles.State(num,n)
                                        elif t[3]=='ML_base':
                                            num=1
                                            n=t[0]
                                            Bottles.State(num,n) 
                                    elif t[3]=='   PAUSE' or t[3]=='   STOP':
                                        color0[0:4]=[Green,Green,Green,Green]
                                elif color0[t[0]]==Red:
                                    color0[t[0]]=Green
                            elif color0[0]==Green and color0[2]==Green:
                                color0[1]=Green
                                color0[3]=Green
                            elif color0[1]==Green and color0[3]==Green:
                                color0[0]=Green
                                color0[2]=Green
                        for i in B0:
                            if i[1]<=pos[0]<=i[1]+90 and i[2]<=pos[1]<=i[2]+90:
                                if state_a==['close','close','close','close','close']:
                                    if index ==0:
                                        state_a[i[0]]='open'
                                        #response0=urllib.request.urlopen('http://192.168.10.200:5000/feeder/{}/1'.format(i[0]))
                                        #html0=response0.read()
                                        #text0=json.loads(html0)
                                        print('http://192.168.10.200:5000/feeder/{}/1'.format(i[0]))
                                elif state_a[i[0]]=='open':
                                    if index ==2:
                                        state_a[i[0]]='close'
                                        #response1=urllib.request.urlopen('http://192.168.10.200:5000/feeder/{}/0'.format(i[0]))
                                        #html1=response1.read()
                                        #text1=json.loads(html1)
                                        print('http://192.168.10.200:5000/feeder/{}/0'.format(i[0]))
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
                        if size0+70<=pos[0]<=size0+160 and 490<=pos[1]<=580:
                            if index == 0:
                                response4=urllib.request.urlopen("http://192.168.10.200:5000/feederon")
                                html4=response4.read()
                                text4=json.loads(html4)
                            elif index==2:
                                response5=urllib.request.urlopen("http://192.168.10.200:5000/feederoff")
                                html5=response5.read()
                                text5=json.loads(html5)
                        elif size0*6+70<=pos[0]<=size0*6+160 and 490<=pos[1]<=580:
                            if index == 0:
                                response6=urllib.request.urlopen("http://192.168.10.201:5000/feederon")
                                html6=response6.read()
                                text6=json.loads(html6)
                            elif index==2:
                                response7=urllib.request.urlopen("http://192.168.10.201:5000/feederoff")
                                html7=response7.read()
                                text7=json.loads(html7)
        time.sleep(1/3)
        response8=urllib.request.urlopen("http://192.168.10.119:80/bucketgroup/a")
        html8=response8.read().decode()
        response9=urllib.request.urlopen("http://192.168.10.119:80/bucketgroup/b")
        html9=response9.read().decode()
        response10=urllib.request.urlopen("http://192.168.10.200:5000/scale")
        html10=response10.read()
        response11=urllib.request.urlopen("http://192.168.10.201:5000/scale")
        html11=response11.read()
        text8=json.loads(html8)
        text9=json.loads(html9)
        text10=json.loads(html10)
        text11=json.loads(html11)
        B0=[[0,70,160,text8['0']],[1,70,30,text8['1']],[2,size0*2+70,240,text8['2']],[3,size0*2+70,120,text8['3']],[4,size0*2+70,0,text8['4']]]
        B1=[[0,size0*5+70,160,text9['0']],[1,size0*5+70,30,text9['1']],[2,size0*7+70,160,text9['2']],[3,size0*7+70,30,text9['3']]]
        list=[[0,size0*3+80,350,'FT_lifter'],[1,size0*3+80,470,'FT_base'],[2,size0*4+80,350,'ML_lifter'],[3,size0*4+80,470,'ML_base'],[4,size0*5+85,350,'   PAUSE'],[5,size0*5+85,470,'   STOP']]
        list0=[[0,size0*3+20,550,'  plan:'],[1,size0*4+20,550,'complete:'],[2,size0*5+20,550,'coefficient:']]
        for k in list0:
            Bottles.SJ(k[0],k[1],k[2],k[3])
        for t in list:
            Bottles.AN(t[0],t[1],t[2],t[3])
        for i in B0:
            Bottles.Icon_a(i[0],i[1],i[2],i[3])
        for v in B1:
            Bottles.Icon_b(v[0],v[1],v[2],v[3])
        Bottles.VibratoryFeeder(size0+70,370,'img/lx.jpg')
        Bottles.WeightIcon(size0+70,490,b'%0.2f' % text10)
        #Bottles.WeightIcon(size0+70,490,b'%0.2f' % text10['reading'])
        Bottles.VibratoryFeeder(size0*6+70,370,'img/zd.jpg')
        Bottles.WeightIcon(size0*6+70,490,b'%0.2f' % text11)
        #Bottles.WeightIcon(size0*6+70,490,b'%0.2f' % text11['reading'])
