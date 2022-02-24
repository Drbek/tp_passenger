import copy
from functions import getValidNumber
from functions import generateId
from functions import clear
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
def getListBus():
    listBus=[]
    continueRegister=True
    while continueRegister :
        bus=getBus(len(listBus))
        listBus.append(bus)
        confirm=input("Voulez ajouter un nouveau bus ? (oui/non) : ")
        if(confirm=="non") :
            continueRegister=False
        clear()
    return listBus
#test
listP=getListBus()




