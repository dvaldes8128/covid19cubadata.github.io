import pandas as pd 
import json


cov_data=json.load(open("data/covid19-cuba.json"))
cov_data=cov_data['casos']['dias']

def get_event(_id,field):
    for day,data in cov_data.items():
        if data.get(field) and _id in data.get(field):
            return data['fecha']

def alta(_id):
    return get_event(_id,'recuperados_id')

def muerte(_id):
    return get_event(_id,'muertes_id')

def grave(_id):
    return get_event(_id,'graves_id')

def evac(_id):
    return get_event(_id,'evacuados_id')

subjects=[]

for day,data in cov_data.items() :
    if data.get("diagnosticados") is not None:
        for i in data["diagnosticados"]:
            i['deteccion']=data['fecha']
            i['alta']=alta(i["id"])
            i['muerte']=muerte(i["id"])
            i['grave_desde']=grave(i["id"])
            i['evacuación']=evac(i["id"])
            subjects.append(i)
    
cov_pd=pd.DataFrame(subjects)
cov_pd.to_csv("data/covid19-cuba.csv")
