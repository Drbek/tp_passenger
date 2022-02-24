import copy
modelPassager={
    "Id":None,
    "nom":None,
    "prenom":None,
    "poidsBaggage":None
}
def getPassager():
    nom=input("Nom du passager : ")
    prenom=input("Prenom du passager : ")
    poidsBaggage=getValidNumber(input("Poids des baggages : "))
    passager=copy.deepcopy(modelPassager)
    passager["nom"]=nom
    passager["prenom"]=prenom
    passager["poidsBaggage"]=poidsBaggage
