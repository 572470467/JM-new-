import time
import json
import os
import pygame
import csv
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
Brack=[0,0,0]
White=[255,255,255]
Green=[0,255,0]
width=pygame.display.Info().current_w
height=pygame.display.Info().current_h
height0=int((height-117)/3)
size=(width-67)/20
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67,height0*2+87)
#screen = pygame.display.set_mode((width-67,height0))
screen = pygame.display.set_mode((width-67,height))
screen.fill(Brack)
pygame.display.update()
icon0={'0':'cgq0.jpg','1':'cgq1.jpg'}
icon1={'0':'dj0.jpg','1':'dj1.jpg'}
number0=["传感器0","传感器1","传感器2","传感器3","传感器4","传感器5","传感器6","传感器7"]
number1=["交流电机0","交流电机1","交流电机2","直流电机3","直流电机4","直流电机5","直流电机6"]
number2=["夹紧气缸","移动气缸","夹紧气缸","移动气缸","阻挡气缸","升降气缸","升降气缸(出)"]
number3=["热压机0","热压机1","热压机2"]
img=pygame.image.load('jxb.jpg')
img=pygame.transform.smoothscale(img,(int(size*1.2),int(size*1.2)))
screen.blit(img,(20,280))
text=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",18)
pygame.display.update()
def Icon_cgq(num,x,y,a):
    img=pygame.image.load(icon0[a])
    img=pygame.transform.smoothscale(img,(int(size*0.8),50))
    screen.blit(img,(x,y))
    text_fmt0=text.render(number0[num],3,White)
    screen.blit(text_fmt0,(x-5,y-25))
    pygame.display.update()
def Icon_dj(num,x,y,a):
    img=pygame.image.load(icon1[a])
    img=pygame.transform.smoothscale(img,(int(size*0.8),50))
    screen.blit(img,(x,y))
    text_fmt0=text.render(number1[num],3,White)
    screen.blit(text_fmt0,(x,y-20))
    pygame.display.update()
def Icon_qg(num,x,y):
    img=pygame.image.load('qg0.jpg')
    img=pygame.transform.smoothscale(img,(int(size*0.8),50))
    screen.blit(img,(x,y))
    text_fmt0=text.render(number2[num],3,White)
    screen.blit(text_fmt0,(x,y-25))
    pygame.display.update()
def Icon_cz(num,x,y,a):
    pygame.draw.rect(screen,Green,[x+size+20,y-19,80,30],2)
    text_fmt0=text.render('顶料',3,White)
    screen.blit(text_fmt0,(x+size-20,y-17))
    pygame.draw.rect(screen,Brack,[x+size+22,y-17,78,28],0)
    text_fmt0=text.render(a,3,White)
    screen.blit(text_fmt0,(x+size+30,y-15))
    pygame.draw.rect(screen,Green,[x+size+20,y+51,80,30],2)
    text_fmt0=text.render('底料',3,White)
    screen.blit(text_fmt0,(x+size-20,y+53))
    pygame.draw.rect(screen,Brack,[x+size+22,y+53,78,28],0)
    text_fmt0=text.render(a,3,White)
    screen.blit(text_fmt0,(x+size+30,y+55))
    img=pygame.image.load('cz.jpg')
    img=pygame.transform.smoothscale(img,(int(size*0.8),70))
    screen.blit(img,(x-20,y))
    img0=pygame.image.load('csd.jpg')
    img0=pygame.transform.smoothscale(img0,(int(size*0.8),70))
    screen.blit(img0,(x-20,y-70))
    pygame.display.update()
def Icon_ryj(num,x,y,wd):
    pygame.draw.rect(screen,Green,[x,y,40,40],3)
    text_fmt0=text.render(number3[num],3,White)
    screen.blit(text_fmt0,(x+50,y+5))
    text_fmt1=text.render('温度:',3,White)
    screen.blit(text_fmt1,(x+130,y+5))
    pygame.draw.rect(screen,Brack,[x+182,y+2,63,33],0)
    pygame.draw.rect(screen,Green,[x+180,y,65,35],2)
    text_fmt2=text.render('{}℃'.format(wd),3,White)
    screen.blit(text_fmt2,(x+190,y+5))
    pygame.display.update()
def Icon_gd(x,y,l):
    pygame.draw.rect(screen,Green,[x,y,l,90],5)
    pygame.display.update()
if __name__ == '__main__':
    while True:
        time.sleep(1)
        y=open('press.csv','r')
        reader=csv.reader(y)
        lt=[]
        for a in reader:
            lt.append(a)
        f=open('amount.csv','r')
        reader=csv.reader(f)
        ls=[]
        for b in reader:
            ls.append(b)
        response0=urllib.request.urlopen('http://192.168.10.119:80/s/status/')
        html0=response0.read()
        text0=json.loads(html0)
        response1=urllib.request.urlopen('http://192.168.10.119:80/n/status/')
        html1=response1.read()
        text1=json.loads(html1)
        response2=urllib.request.urlopen("http://192.168.10.200:5000/scale")
        html2=response2.read()
        response3=urllib.request.urlopen("http://192.168.10.201:5000/scale")
        html3=response3.read()
        text2=json.loads(html2)
        text3=json.loads(html3)
        A0=[[0,size*18-10,192,text0['sensor0']],[1,size*15+20,192,text0['sensor1']],[2,size*12+10,192,text0['sensor2']],[3,size+40,192,text0['sensor3']],[4,size+40,449,text1['sensor4']],[5,size*14-20,449,text1['sensor5']],[6,size*19-10,449,text1['sensor6']]]
        A1=[[0,size*11+30,106,text0['motor0']],[1,size*9-10,106,text0['motor1']],[2,size*7-10,106,text0['motor2']],[3,size*2+40,106,text0['motor3']],[4,size*7+40,539,text1['motor4']],[5,size*9+40,539,text1['motor5']],[6,size*13+20,539,text1['motor6']]]
        A2=[[0,size*18-10,106],[1,size*18-10,25],[2,size*15+20,106],[3,size*15+20,25],[4,size*13-15,106],[5,size*10-10,192],[6,size*4,192]]
        A3=[[0,size*18-10,329,b'%0.2f' % text2],[1,size*15+20,329,b'%0.2f' % text3]]
        #A3=[[0,size*18-40,329,b'%0.2f' % text2['reading']],[1,size*15-30,329,b'%0.2f' % text3['reading']]]
        A4=[[0,size*2-20,265,lt[0][1]],[1,size*2-20,315,lt[1][1]],[2,size*2-20,365,lt[2][1]]]
        A5=[[size*11+25,165,size*9-30],[size*13+10,165,0],[size*11+5,165,10],[size*4-15,165,size*7+30],[size+20,165,size*2+45],[size+20,420,size*9+20],[size*11-45,420,size*3-50],[size*13+5,420,size*7-10]]
        text_fmt0=text.render('预压机在压数量：',3,White)
        screen.blit(text_fmt0,(size*6-15,285))
        pygame.draw.rect(screen,Brack,[size*7+62,282,58,33],0)
        pygame.draw.rect(screen,Green,[size*7+60,280,60,35],2)
        text_fmt2=text.render('{}件'.format(ls[0][1]),3,White)
        screen.blit(text_fmt2,(size*7+65,285))
        text_fmt1=text.render('压出产品的数量：',3,White)
        screen.blit(text_fmt1,(size*6-15,345))
        pygame.draw.rect(screen,Brack,[size*7+62,342,58,33],0)
        pygame.draw.rect(screen,Green,[size*7+60,340,60,35],2)
        text_fmt3=text.render('{}件'.format(ls[1][1]),3,White)
        screen.blit(text_fmt3,(size*7+65,345))
        for i in A0:
            Icon_cgq(i[0],i[1],i[2],i[3])
        for v in A1:
            Icon_dj(v[0],v[1],v[2],v[3])
            if int(v[3])==1 and 0<=v[0]<=3:
                img=pygame.image.load('jt1.jpg')
                img=pygame.transform.smoothscale(img,(int(size)-35,40))
                screen.blit(img,(v[1]-2,v[2]+80))
            elif int(v[3])==1 and 4<=v[0]<=6:
                img=pygame.image.load('jt0.jpg')
                img=pygame.transform.smoothscale(img,(int(size)-35,40))
                screen.blit(img,(v[1]-2,v[2]-90))
            else:
                pygame.draw.rect(screen,Brack,[v[1]-2,v[2]+80,int(size)-35,40],0)
                pygame.draw.rect(screen,Brack,[v[1]-2,v[2]-90,int(size)-35,40],0)
        for n in A2:
            Icon_qg(n[0],n[1],n[2])
        for m in A3:
            Icon_cz(m[0],m[1],m[2],m[3])
        for t in A4:
            Icon_ryj(t[0],t[1],t[2],t[3])
        for z in A5:
            Icon_gd(z[0],z[1],z[2])
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            elif event.type == QUIT:
                exit()
