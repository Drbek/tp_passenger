import copy
from functions import getValidNumber
from functions import generateId
from functions import clear

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
    continueRegister=True
    while continueRegister :
        passager=getPassager(len(listPassager))
        listPassager.append(passager)
        confirm=input("Voulez ajouter un nouveau passager ? (oui/non) : ")
        if(confirm=="non") :
            continueRegister=False
            clear()
    return listPassager
#test
#listP=getListPassager()




