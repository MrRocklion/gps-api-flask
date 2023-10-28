data = "+CGPSINFO: 0252.951973,S,07859.715792,W,281023,212131.0,2570.9,,"
string_empty = data.replace(" ", "")
string_formated = string_empty[10:].split(",")
print(string_formated)
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
print(latitud)
print(longitud)
