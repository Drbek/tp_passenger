import functions

choix=functions.afficherMenu()
while choix !="q":
    if(choix.isdigit() and len(choix)==1):
        if(choix=="1"):
            pass