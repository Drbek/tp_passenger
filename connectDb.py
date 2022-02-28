import pymongo
#from defmodel import modelBus
#import copy
def connectBD(uri="mongodb://localhost:27017/"):
    myclient = pymongo.MongoClient(uri)
    mybd=myclient.list_database_names()
    if "agence_voyage" in myclient.list_database_names():
        mybd=myclient["agence_voyage"]
        return mybd
    else:
        return 0
