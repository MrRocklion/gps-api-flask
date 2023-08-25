from flask import Flask,jsonify,request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tracker-app-233e4-default-rtdb.firebaseio.com/'
})
ref = db.reference('dispositivos')
app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message":"agregado"})

@app.route('/devices',methods=['GET'])
def getDevices():
    data = ref.get()
    return jsonify({"data":data})

@app.route('/update_device',methods=['POST'])
def setPosition():

    args = request.args
    args.to_dict()
    id = args.get("id")
    lat = args.get("lat")
    lon = args.get("lon")
    device_ref = ref.child(id)
    device_ref.update({
    'lat':lat,
    'lon':lon
    })

    return jsonify({"data":"ok"})




if __name__ == '__main__':
    app.run(debug=True,port=4000)