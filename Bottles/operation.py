from flask import Flask, jsonify
import time
import mixer
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


