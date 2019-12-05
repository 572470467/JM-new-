from flask import Flask, jsonify
import time
import B
#import Mix_group
#from common import Carrier
import random
app = Flask(__name__)
list=[{'pos':0,'sensors':[0,1,1,1,1]},{'pos':1,'sensors':[1,0,1,1,1]},{'pos':2,'sensors':[1,1,0,1,1]},{'pos':3,'sensors':[1,1,1,0,1]},{'pos':4,'sensors':[1,1,1,1,0]}]
list0=['motor0','motor1','motor2','motor3','sensor0','sensor1','sensor2','sensor3']
list1=['motor4','motor5','motor6','sensor4','sensor5','sensor6','sensor7']
list2=[[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
CGQ=[[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,0]]
releasestart = {'a':0, 'b':0}
releaseend = {'a':0, 'b':0}
releaseactive = {'a': False, 'b': False}

def random_A():
    dic = {}
    for i in range(2):
        dic[str(i)] = str(random.randrange(7))
    return list2[int(dic[str(i)])]

def random_status(cnt):
    dic = {}
    for i in range(cnt):
        dic[str(i)] = str(random.randrange(2)) + str(random.randrange(2))
    return dic

def random_carrier():
    dic = {}
    for i in range(2):
        dic[str(i)] = str(random.randrange(5))
    return dic[str(i)]

def random_s():
    dic = {}
    for i in range(8):
        dic[str(list0[i])] = str(random.randrange(2))
    return dic

def random_n():
    dic = {}
    for i in range(7):
        dic[str(list1[i])] = str(random.randrange(2))
    return dic

@app.route('/s/status/')
def status_s():
    d=random_s()
    return jsonify(d)

@app.route('/n/status/')
def status_n():
    d=random_n()
    return jsonify(d)

@app.route('/carrier/status')
def carrier():
    d=list[int(random_carrier())]
    return jsonify(d)

@app.route('/mixer/<groupid>')
def button(groupid):
    #d=groupid
    #return jsonify(d)
    #B=Mix_group
    if groupid=='000':
        return str(B.A())
        #return str(B.catch_powder())
    elif groupid=='100':
        return str(B.B())    
        #return str(B.mixed_powder())
    elif groupid=='200':
        return str(B.C())
        #return str(B.powder_feeding())
    elif groupid=='300':
        return str(B.D())
        #return str(B.mixed_abrasive())
    elif groupid=='400':
        return str(B.E())
        #return str(B.make_wetting_agent())
    elif groupid=='500':
        return str(B.F())
        #return str(B.add_wetting_agent())
    elif groupid=='600':
        return str(B.G())
        #return str(B.abrasive_feeding())

@app.route('/carrier/moveto/<groupid>')
def moveto(groupid):
    return str(B.A())
    #d=int(groupid)
    #return jsonify(d)
    #car=Carrier([13,6,5,0,11], 18, 23, 12, 25, 20, 24)
    #return str(car.moveto(d))

@app.route('/bucketgroup/a')
def group_a():
    d = random_status(5)
    return jsonify(d)

@app.route('/mixerstatus/')
def status_A():
    d={'status':random_A()}
    return jsonify(d)


@app.route('/bucketgroup/b')
def group_b():
    d = random_status(4)
    return jsonify(d)

@app.route('/feederon/<groupid>')
def feeder(groupid):
    if groupid in releasestart.keys():
        releasestart[groupid] = releaseend[groupid] = time.time()
        releaseactive[groupid] = True
        d = {'status': 'OK'}
    else:
       d = {'status': 'Error'}
    return jsonify(d)

@app.route('/feederoff/<groupid>')
def feeder_stop(groupid):
    if groupid in releasestart.keys():
        releaseend[groupid] = time.time()
        releaseactive[groupid] = False
        d = {'status': 'OK'}
    else:
        d = {'status': 'Error'}
    return jsonify(d)

@app.route('/scale/<groupid>')
def scale_read(groupid):
    if groupid in releasestart.keys():
        if releaseactive[groupid]:
            amt = time.time() - releasestart[groupid]
            print(time.time()-releasestart[groupid])
        else:
            amt = releaseend[groupid] - releasestart[groupid]
            print(releasestart[groupid])
        d = {'status': 'OK', 'reading': amt, 'started':releasestart[groupid]}
    else:
        d = {'status': 'Error', 'reading': -1, 'started': -1}
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)


