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
    bus["passagers"].append(passager)
def isPlaceAvailable(bus):
    result=False
    if bus["nombrePlace"]>len(bus["passagers"]):
        result=True
    return result
def isPoidsOverFlow(passager,bus) :
    result=False
    summe=0
    for x in bus["passagers"]:
        summe+=x["poidsBaggage"]
    if (bus["poidsMax"]<(summe+passager["poidsBaggage"])):
        result=True
    return result
def numberOfAvailablePlace(bus):
    if bus["nombrePlace"]>len(bus["passagers"]):
        return (bus["nombrePlace"]-len(bus["passagers"]))
    else:
        return 0
def numberOfWeigthAvailable(bus):
    summe=0
    for x in bus["passagers"]:
        summe+=x["poidsBaggage"]
    if (bus["poidsMax"]>(summe)):
        return bus["poidsMax"]-(summe)
    else:
        return 0
def removePassagerInBus(passager,bus):
    if(isPassagerIntoBus(passager,bus)):
        bus["passagers"].remove(passager)
        print("Passager {} removed from bus {} ".format(passager["Id"],bus["Id"]))
    else:
        print("Passager doesnt exist on bus")
def isPassagerIntoBus(passager,bus):
    result=False
    for x in bus["passagers"]:
        if x["Id"]==passager["Id"]:
            result=True
            break
    return result