from connectDb import connectBD
#cette fonction permet de vverifier si un nombre est nombre est un floatant ou un entier
def is_float(str):
    result=False
    if str.count(".")<=1 :
        if str.replace(".","").isdigit() :
            result=True
    return result
# test
#print(is_float(input("Enter number : ")))
#cette function permet de obtenir un nombre valide de l'utiliszteur
def getValidNumber(str):
    number=input(str)
    while not is_float(number) :
        number=input(str)
    return number
# test
#print(getValidNumber("Enter number : "))
#cette fonction permet de generer un identifiant de bus ou d'un passager
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

import copy
from os import system, name
#cette fonction efface la console
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
#cette fonction ajoute un passager dans le bus
def addPassagerTobus(passager,bus):
    if(not isPassagerIntoBus(passager,bus)):
        bus["passagers"].append(passager)
        myquery = { "matricule":bus["matricule"] }
        newvalues = { "$set": { "passagers": bus["passagers"] } }
        db=connectBD()
        t = db["bus"].update_one(myquery,newvalues)
        print(t)
        print("Passager {} ({}) is added into bus {} ".format(passager["Id"],passager["nom"],bus["matricule"]))
    else:
        print("something wrong happened!!")
#cette fonction verifie s'il y'a de place disponible dans le bus
def isPlaceAvailable(bus):
    result=False
    if int(bus["nombrePlace"])>len(bus["passagers"]):
        result=True
    return result
#cette fonction verifie si un passager peut integrer un bus en calculant le poids
def isPoidsOverFlow(passager,bus) :
    result=False
    summe=0
    for x in bus["passagers"]:
        summe+=int(x["poidsBaggage"])
    if (int(bus["poidsMax"])<(summe+int(passager["poidsBaggage"]))):
        result=True
    return result
#cette fonction calcule le nombre de place disponible dans un bus
def numberOfAvailablePlace(bus):
    if int(bus["nombrePlace"])>len(bus["passagers"]):
        return (int(bus["nombrePlace"])-len(bus["passagers"]))
    else:
        return 0
#cette fonction calcule les poids en kg disponible dans un bus
def numberOfWeigthAvailable(bus):
    summe=0
    for x in bus["passagers"]:
        summe+=int(x["poidsBaggage"])
    if (int(bus["poidsMax"])>(summe)):
        return int(bus["poidsMax"])-(summe)
    else:
        return 0
#cette enlève un passager dans un bus
def removePassagerInBus(passager,bus):
    if(isPassagerIntoBus(passager,bus)):
        query={"matricule":bus["matricule"],"passagers":{"$elemMatch":{"Id":passager["Id"]}}}
        bus["passagers"].remove(passager)
        newValue={ "$set": {"passagers":bus["passagers"]}}
        db=connectBD()
        t=db["bus"].update_one(query,newValue)
        print(t)
        #bus["passagers"].remove(passager)
        print("Passager {} ({}) removed from bus {} ".format(passager["Id"],passager["nom"],bus["matricule"]))
    else:
        print("Passager doesnt exist on bus")
#cette fonction verifie si un passager est dans un bus
def isPassagerIntoBus(passager,bus):
    result=False
    db=connectBD()
    t=db["bus"].find_one({"matricule":bus["matricule"],"passagers":{"$elemMatch":{"Id":passager["Id"]}}})
    if(t!=None):
        result=True
    #for x in bus["passagers"]:
        #if x["Id"]==passager["Id"]:
            #result=True
            #break
    return result
#fonction qui permet d'obtenir un bus a partir du matricule . Elle retourne 0 si le bus nexiste pas
def getBusByMatricule():
    result=0
    choixBus=input("Entrer le matricule du bus : ")
    db=connectBD()
    result=db["bus"].find_one({"matricule":choixBus})
    while(result==None  and choixBus!="q"):
        choixBus=input("Entrer un matricule correct (BUS-XX)(bus {} inexistant) : ".format(choixBus))
        result=db["bus"].find_one({"matricule":choixBus})
    return result
#fonction qui permet d'obtenir un passager a partir de ID . Elle retourne 0 si le paasger nexiste pas
def getPassagerById(isOnTime):
    result=0
    choixPassager=input("Entrer l'ID du passager : ")
    #for x in listPassager:
        #if(x["Id"]==choixPassager):
            #result=x
    db=connectBD()
    result=db["passager"].find_one({"Id":choixPassager})

    while(result==None and isOnTime==False and choixPassager!="q"):
        choixPassager=input("Entrer ID correct (PAXX)(Passager {} inexistant) : ".format(choixPassager))
        result=db["passager"].find_one({"Id":choixPassager})
    #print(result)
    return result
#test 
#getBusByMatricule()
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

#cette fonction affiche le menu
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
    print("9. QUEL EST LE NOMBRE KG DISPONIBLE POUR UN BUS ? ")
    print("10. LISTE DES BUS ")
    print("11. LISTE DES PASSAGERS ")
    enter=input("taper Ici____ ")
    return enter
def afficherPassager(passager):
    print("-------{}----------".format(passager["Id"]))
    print("NOM : "+passager["nom"]+" "+passager["prenom"])
    print("POIDS BAGGAGE : "+passager["poidsBaggage"]+"KG")
    #print("-------------------")
#cette fonction affiche un bus sur la console
def afficherBus(bus):
    print("-------{}----------".format(bus["matricule"]))
    print("NOMBRE DE PLACE : "+bus["nombrePlace"])
    print("POIDS Max : "+bus["poidsMax"]+"KG")
   # print("-------------------")
#cette fonction verifi si un passager est dans la flotte puis returne les donnees du pasager dans le cas contraire elle retourne 0
def isPassagerIsIntoFlotte(passager):
    modelData={"bus":None,"passager":None}
    db=connectBD()
    ListBus=db["bus"].find({})
    myBus=None
    result=0
    count=0
    for bus in ListBus:
        for x in bus["passagers"]:
            if passager["Id"]==x["Id"]:
                modelData["passager"]=passager
                count+=1
                break
        if(count>0):
            modelData["bus"]=bus
            result=copy.deepcopy(modelData)
            break
    return result