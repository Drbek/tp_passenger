import copy
from functions import getValidNumber
from functions import generateId
modelPassager={
    "Id":None,
    "nom":None,
    "prenom":None,
    "poidsBaggage":None
}
def getPassager(lastIndex):
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
#print(passa)

