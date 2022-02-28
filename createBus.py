import copy
from functions import getValidNumber
from functions import generateId
from functions import clear
from defmodel import modelBus
def getBus(lastIndex):
    print("-----------------------------------------------------------")
    print("----------------AJOUTER UN NOUVEAU BUS---------------------")
    print("-----------------------------------------------------------")
    nombrePlace=getValidNumber("Quel est le nombre de place ? : ")
    poidsMax=getValidNumber("Quel est le poids max du bus ? : ")
    bus=copy.deepcopy(modelBus)
    bus["nombrePlace"]=nombrePlace
    bus["poidsMax"]=poidsMax
    bus["matricule"]=generateId(lastIndex,"BUS-")
    return bus
#test
#passa=getPassager(0)
#clear()
#print(passa)
from connectDb import connectBD
def getListBus():
    listBus=[]
    db=connectBD()
    lastDoc=db["bus"].find().limit(1).sort("_id",-1)
    leng=0
    for doc in lastDoc:
     index=doc["matricule"].replace("BUS-","") 
     if index.isdigit() :
         leng=int(index)
    continueRegister=True
    while continueRegister :
        bus=getBus(leng)
        listBus.append(bus)
        confirm=input("Voulez ajouter un nouveau bus ? (oui/non) : ")
        if(confirm=="non") :
            continueRegister=False
        clear()
        leng+=1
    return listBus
#test
#listP=getListBus()




