import functions
import createBus
import createPassager
from time import sleep
choix=functions.afficherMenu()
print("\n")
ListBus=[]
ListPassager=[]
while choix!="q" :
    if(choix.isdigit() and len(choix)<=2):
        if(choix=="1"):
           ListBus= createBus.getListBus()
           choix=functions.afficherMenu()
        elif(choix=="2"):
            ListPassager=createPassager.getListPassager()
            choix=functions.afficherMenu()
        elif(choix=="3"):
           
            bus=functions.getBusByMatricule(ListBus)
            passager=functions.getPassagerById(ListPassager,False)
            if(functions.isPlaceAvailable(bus) and not functions.isPoidsOverFlow(passager,bus)):
                functions.addPassagerTobus(passager,bus)
            else:
                print("Manque de place ou d'espace pour les baggages!!")
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="4"):
            bus=functions.getBusByMatricule(ListBus)
            nbPlace=functions.numberOfAvailablePlace(bus)
            print("le nombre de place disponible pour le bus {} est {} ".format(bus["matricule"],nbPlace))
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="5"):
            bus=functions.getBusByMatricule(ListBus)
            passager=functions.getPassagerById(ListPassager,False)
            functions.removePassagerInBus(passager,bus)
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="6"):
            bus=functions.getBusByMatricule(ListBus)
            count=0
            for passager in bus["passagers"]:
                    functions.afficherPassager(passager)
                    count+=1
            if(count==0):
                print("--------Pas de passager dans ce bus!!!------------")
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="7"):
           # print(ListPassager)
            count=0
            for bus in ListBus:
                for passager in bus["passagers"]:
                    functions.afficherPassager(passager)
                    count+=1
            if(count==0):
                print("--------Pas de passager dans la flotte!!!------------")
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="8"):
            passager=functions.getPassagerById(ListPassager,True)
            if(passager==0) :
                print("Passager nexiste pas !!".format())
                sleep(3)
            else:
                count=0
                myBus=None
                for bus in ListBus:
                    for x in bus["passagers"]:
                        if passager["Id"]==x["Id"]:
                            functions.afficherPassager(passager)
                            sleep(3)
                            count+=1
                            break
                    myBus=bus
                if(count==0):
                    print("----Passager n'est dans la flotte!!-----")
            print("------LE PASSAGER {} APPARTIENT AU BUS SUIVANT------".format(passager["Id"]))
            choix=functions.afficherBus(myBus)
        elif(choix=="9"):
            bus=functions.getBusByMatricule(ListBus)
            if(bus!=0):
                nbKg=functions.numberOfWeigthAvailable(bus)
                print("le nombre de KG reservé pour le bus {} est {} ".format(bus["matricule"],nbKg))
                sleep(3)
                choix=functions.afficherMenu()
            else:
                choix=functions.afficherMenu()
        elif(choix=="10"):
            for bus in ListBus:
                functions.afficherBus(bus)
            if(len(ListBus)==0):
                print("---------Pas de bus!!!!-----------")
            sleep(6)
            choix=input("taper ici____ ")