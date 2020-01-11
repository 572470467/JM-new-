from flask import Flask, jsonify
import time
import mixer
GPIO.setmode(GPIO.BCM)

# GPIO setup
pump0 = Relay(10)
pump1 = Relay(22)

valve_air_mix = Relay(9)
mini_mix = Relay(20)
mix_powder = Relay(21)

mix_abrasives_on = Relay(17)
mix_abrasives_of = Relay(27)

vibrating_screen_powder = Relay(16)
vibrating_screen_powder_rotate_cyli = Relay(18)

upseal_cyli = Relay(12)
downseal_cyli = Relay(24)
up_avlv =Relay(25)
down_avlv =Relay(23)

hand_pump0 = Button(13)
hand_pump1 = Button(19)
mix=Mixer([8,7,1])
btnc0 = Button(8)
btnc1 = Button(7)
btnc2 = Button(1)

app = Flask(__name__)

@app.route('/mixer/<groupid>')
def button(groupid):
    B=mixer
    if groupid=='000':
        return str(B.block00prepare())
    elif groupid=='100':
        return str(B.reset_block00prepare())
    elif groupid=='200':
        return str(B.block10powderon())
    elif groupid=='300':
        return str(B.block20powderoff())
    elif groupid=='400':
        return str(B.block30feedandscreen())
    elif groupid=='500':
        return str(B.block40stopandreset())
    elif groupid=='600':
        return str(B.block50abrasiveson())
    elif groupid=='700':
        return str(B.block60abrasivesoff())
    elif groupid=='800':
        return str(B.erialtest())

@app.route('/status')
def op_mix_status():
    return str(mix.getstatus())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)


