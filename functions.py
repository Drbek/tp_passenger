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