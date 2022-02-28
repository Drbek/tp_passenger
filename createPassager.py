import copy
from connectDb import connectBD
from functions import getValidNumber
from functions import generateId
from functions import clear
from defmodel import modelPassager
def getPassager(lastIndex):
    print("-----------------------------------------------------------")
    print("----------------AJOUTER UN NOUVEAU PASSAGER----------------")
    print("-----------------------------------------------------------")
    nom=input("Nom du passager : ")
    prenom=input("Prenom du passager : ")
    poidsBaggage=getValidNumber("Poids des baggages : ")
    passager=copy.deepcopy(modelPassager)
    passager["nom"]=nom
    passager["prenom"]=prenom
    passager["poidsBaggage"]=poidsBaggage
    passager["Id"]=generateId(lastIndex,"PA")
    return passager
#test
#passa=getPassager(0)
#clear()
#print(passa)
def getListPassager():
    listPassager=[]
    db=connectBD()
    lastDoc=db["passager"].find().limit(1).sort("_id",-1)
    leng=0
    for doc in lastDoc:
     index=doc["Id"].replace("PA","") 
     if index.isdigit() :
         leng=int(index)
    continueRegister=True
    while continueRegister :
        passager=getPassager(leng)
        listPassager.append(passager)
        confirm=input("Voulez ajouter un nouveau passager ? (oui/non) : ")
        if(confirm=="non") :
            continueRegister=False
        clear()
        leng+=1
    return listPassager
#test
#listP=getListPassager()




