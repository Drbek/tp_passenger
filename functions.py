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