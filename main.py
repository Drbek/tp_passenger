import functions
import createBus
import createPassager
from time import sleep
choix=functions.afficherMenu()
print(choix)
ListBus=[]
ListPassager=[]
while choix!="q" :
    if(choix.isdigit() and len(choix)==1):
        if(choix=="1"):
           ListBus= createBus.getListBus()
           choix=functions.afficherMenu()
        elif(choix=="2"):
            ListPassager=createPassager.getListPassager()
            choix=functions.afficherMenu()
        elif(choix=="3"):
           
            bus=functions.getBusByMatricule(ListBus)
            passager=functions.getPassagerById(ListPassager)
            
            if(functions.isPlaceAvailable(bus) and functions.isPoidsOverFlow(passager,bus)):
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
            passager=functions.getPassagerById(ListPassager)
            functions.removePassagerInBus(passager,bus)
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="6"):
            bus=functions.getBusByMatricule(ListBus)
            print(bus["passagers"])
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="7"):
            print(ListPassager)
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="8"):
            passager=functions.getPassagerById(ListPassager)
            sleep(6)
            choix=functions.afficherMenu()
        
            
    