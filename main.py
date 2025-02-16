import functions
import createBus
import createPassager
from time import sleep
from connectDb import connectBD
from prettytable import PrettyTable
#cette fonction affiche un passager sur la console
db=connectBD()
if(db==0):
    print("-----------Echec de connexion à la base de donnée!!------------------")
    exit()
choix=functions.afficherMenu()
print("\n")
ListBus = []
ListPassager = []
while choix!="q" :
    if(choix.isdigit() and len(choix)<=2):
        if(choix=="1"):
           a= createBus.getListBus()
           #for i in a:
           #   ListBus.append(i)
           db["bus"].insert_many(a)
           choix=functions.afficherMenu()
        elif(choix=="2"):
            b=createPassager.getListPassager()
            #for k in b:
            #    ListPassager.append(k)
            db["passager"].insert_many(b)
            choix=functions.afficherMenu()
        elif(choix=="3"):
            bus=functions.getBusByMatricule()
            passager=functions.getPassagerById(False)
            data=functions.isPassagerIsIntoFlotte(passager)
            if(data==0 and passager!=0):
                if(functions.isPlaceAvailable(bus) and not functions.isPoidsOverFlow(passager,bus)):
                    functions.addPassagerTobus(passager,bus)
                else:
                    print("Manque de place ou d'espace pour les baggages!!")
            else :
                if(data!=0):
                    print("----Passager est deja dans le bus {}-----".format(data["bus"]["matricule"]))

            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="4"):
            bus=functions.getBusByMatricule()
            nbPlace=functions.numberOfAvailablePlace(bus)
            print("le nombre de place disponible pour le bus {} est {} ".format(bus["matricule"],nbPlace))
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="5"):
            bus=functions.getBusByMatricule()
            passager=functions.getPassagerById(False)
            functions.removePassagerInBus(passager,bus)
            sleep(6)
            choix=functions.afficherMenu()
        elif(choix=="6"):
            bus=functions.getBusByMatricule()
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
            ListBus=db["bus"].find({})
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
            passager=functions.getPassagerById(False)
            if(passager==0) :
                print("Passager nexiste pas !!".format())
                sleep(3)
                choix=functions.afficherMenu()
            else:
                count=0
                data=functions.isPassagerIsIntoFlotte(passager)
                if(data==0):
                    print("----Passager n'est dans la flotte!!-----")
                else:
                  print("------LE PASSAGER {} APPARTIENT AU BUS SUIVANT------".format(data["passager"]["Id"]))
                  functions.afficherBus(data["bus"])
                sleep(6)
                choix=functions.afficherMenu()
        elif(choix=="9"):
            bus=functions.getBusByMatricule()
            if(bus!=0):
                nbKg=functions.numberOfWeigthAvailable(bus)
                print("le nombre de KG reservé pour le bus {} est {} ".format(bus["matricule"],nbKg))
                sleep(6)
                choix=functions.afficherMenu()
            else:
                choix=functions.afficherMenu()
        elif(choix=="10"):
            ListBus=db["bus"].find({})
            x = PrettyTable()
            x.field_names = ["Matricule", "Place", "Poids max"]
            nbbus=0
            for bus in ListBus:
                #functions.afficherBus(bus)
                x.add_row([bus["matricule"], bus["nombrePlace"], bus["poidsMax"]])
                nbbus+=1
            if(nbbus==0):
                print("---------Pas de bus!!!!-----------")
            print(x)
            choix=input("taper ici____ ")
        elif(choix=="11"):
            ListPassager=db["passager"].find({})
            x = PrettyTable()
            x.field_names = ["ID", "Nom", "Prénom","Poids des baggages"]
            nbpas=0
            for pas in ListPassager:
                #functions.afficherPassager(pas)
                x.add_row([pas["Id"], pas["nom"], pas["prenom"],pas["poidsBaggage"]])
                nbpas+=1
            if(nbpas==0):
                print("---------Pas de passager!!!!-----------")
            print(x)
            choix=input("taper ici____ ")
        else:
            choix=functions.afficherMenu()