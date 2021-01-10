from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/calcula',methods=['POST'])
def calcula():
    val=solution(request.json["roman"])
    res={"resultado":val}   
    return jsonify(res)

def solution(roman):
    romanDicOrd={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    romanDic={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    suma=[]
    for element in romanDic:
        if element in roman:
            suma.append(romanDic[element])
            roman=roman.replace(element,"")
    for element in roman:
        if element in romanDicOrd:
            suma.append(romanDicOrd[element])
    return sum(suma)


