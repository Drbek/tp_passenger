def is_float(str):
    result=False
    if str.count(".")<=1 :
        if str.replace(".","").isdigit() :
            result=True
    return result
# test
#print(is_float(input("Enter number : ")))

def getValidNumber(str):
    number=input(str)
    while not is_float(number) :
        number=input(str)
    return number
# test
#print(getValidNumber("Enter number : "))
def generateId(number,type):
    newNumber=str(number+1)
    nbchar=len(newNumber)
    if(nbchar==1):
        return "{}00{}".format(type,newNumber)
    elif(nbchar==2) :
        return "{}0{}".format(type,newNumber)
    else :
        return "{}{}".format(type,newNumber)
#test 
#print(generateId(int(input("Enter number : ")),input("Enter prefix : ")))

from os import system, name
from time import sleep
from unittest import result
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')
   # for mac and linux
   else:
    _ = system('clear')
#test
#print("Hi Learner!!")
#sleep(5)
#clear()

def addPassagerTobus(passager,bus):
    if(not isPassagerIntoBus(passager,bus)):
        bus["passagers"].append(passager)
        print("Passager {} ({}) is added into bus {} ".format(passager["Id"],passager["nom"],bus["matricule"]))
    else:
        print("something wrong happened!!")
def isPlaceAvailable(bus):
    result=False
    if int(bus["nombrePlace"])>len(bus["passagers"]):
        result=True
    return result
def isPoidsOverFlow(passager,bus) :
    result=False
    summe=0
    for x in bus["passagers"]:
        summe+=int(x["poidsBaggage"])
    if (int(bus["poidsMax"])<(summe+int(passager["poidsBaggage"]))):
        result=True
    return result
def numberOfAvailablePlace(bus):
    if int(bus["nombrePlace"])>len(bus["passagers"]):
        return (int(bus["nombrePlace"])-len(bus["passagers"]))
    else:
        return 0
def numberOfWeigthAvailable(bus):
    summe=0
    for x in bus["passagers"]:
        summe+=int(x["poidsBaggage"])
    if (int(bus["poidsMax"])>(summe)):
        return int(bus["poidsMax"])-(summe)
    else:
        return 0
def removePassagerInBus(passager,bus):
    if(isPassagerIntoBus(passager,bus)):
        bus["passagers"].remove(passager)
        print("Passager {} ({}) removed from bus {} ".format(passager["Id"],passager["nom"],bus["matricule"]))
    else:
        print("Passager doesnt exist on bus")
def isPassagerIntoBus(passager,bus):
    result=False
    for x in bus["passagers"]:
        if x["Id"]==passager["Id"]:
            result=True
            break
    return result
def getBusByMatricule(listBus):
    result=0
    choixBus=input("Entrer le matricule du bus : ")
    for x in listBus:
        if(x["matricule"]==choixBus):
            result=x
            break
    while(result==0):
        choixBus=input("Entrer un matricule correct (BUS-XX)(bus {} inexistant) : ".format(choixBus))
        for x in listBus:
            if(x["matricule"]==choixBus):
                result=x
                break
    return result
def getPassagerById(listPassager):
    result=0
    choixPassager=input("Entrer l'ID du passager : ")
    for x in listPassager:
        if(x["Id"]==choixPassager):
            result=x
    
    while(result==0):
        choixPassager=input("Entrer ID correct (PAXX)(Passager {} inexistant) : ".format(choixPassager))
        for x in listPassager:
            if(x["Id"]==choixPassager):
                result=x
    return result
#test 
""" Passager1={
    "Id":"PA001",
    "nom":"Bekono",
    "prenom":"Roland",
    "poidsBaggage":15
}
Passager2={
    "Id":"PA002",
    "nom":"Ngono",
    "prenom":"martin",
    "poidsBaggage":2
}
modelBus1={
    "matricule":"BUS-01",
    "nombrePlace":70,
    "poidsMax":18,
    "passagers":[Passager2]
}
modelBus2={
    "matricule":"BUS-02",
    "nombrePlace":10,
    "poidsMax":8,
    "passagers":[Passager1]
} """
#addPassagerTobus(Passager1,modelBus1)
#print(modelBus1)
#r=isPlaceAvailable(modelBus1)
#r=isPoidsOverFlow(Passager1,modelBus1)
#print(r)
#r=numberOfAvailablePlace(modelBus1)
#print(r)
#print(modelBus1)
#t=numberOfWeigthAvailable(modelBus1)
#print(t)
#print(modelBus1)
#removePassagerInBus(Passager2,modelBus1)
#print(modelBus1)
#r=isPassagerIntoBus(Passager1,modelBus1)
#print(r)
def afficherMenu():
    clear()
    print("----------------------------------------------------------------------")
    print("-------------------GESTION DES AGENCES DE VOYAGES---------------------")
    print("----------------------------------------------------------------------")
    print("1. CREER UN BUS")
    print("2. CREER UN PASSAGER")
    print("3. AJOUTER UN PASSAGER DANS UN BUS")
    print("4. VERIFIER LE NOMBRE DE PLACE D'UN BUS")
    print("5. RETIRER UN PASSAGER DANS BUS")
    print("6. LISTE DES PASSAGERS D'UN BUS")
    print("7. LISTE DES PASSAGERS DE LA FLOTTE")
    print("8. Y'A-TIL UN PASSAGER DANS MA FLOTTE ? ")
    enter=input("taper Ici____ ")
    return enter
    