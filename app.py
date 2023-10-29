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



@app.route('/')
def hello_world():
	return 'Hello World!'

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
    data = args.get("data")
    latitud = 0
    longitud = 0
    string_empty = data.replace(" ", "")
    string_formated = string_empty[9:].split(",")
    if string_formated[0]!="" and string_formated[2]!="":
        grados_lat = string_formated[0][0:2]
        grados_lon = string_formated[2][0:3]
        minutos_lat = float(string_formated[0][2:])
        minutos_lon = float(string_formated[2][3:])
        latitud = int(grados_lat) + ((minutos_lat) / 60)
        longitud =  int(grados_lon) + ((minutos_lon) / 60)
        if string_formated[1] =="S":
            latitud =  latitud*-1
        if string_formated[3] =="W":
            longitud =  longitud*-1
        device_ref = ref.child(id)
        device_ref.update({
        'lat':latitud,
        'lon':longitud
        })
    return jsonify({"latitud":latitud,"longitud":longitud})

@app.route('/track',methods=['POST'])
def setTrack():
    args = request.args
    args.to_dict()
    id = args.get("id")
    lat = args.get("lon")
    lon = args.get("lat")
    device_ref = ref.child(id)
    device_ref.update({
        'lat':lon,
        'lon':lat
        })
    return jsonify({"latitud":lat,"longitud":lon})




if __name__ == '__main__':
    app.run()