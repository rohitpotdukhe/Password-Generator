def keyConvert(key) :   #this function converts the entered key into  ascii format
    asciiKey = []
    for i in key :
        asciiKey.append(ord(i))
    return asciiKey

def asciiConvert(asciiKey) :    #this function converts the ascii list into a single digited list
    singularKey = []
    for i in asciiKey :
        number = int(i)
        #print(type(number))
        while number > 0 :
            singularKey.append(int(number % 10))
            number = int(number / 10)
    #print(singularKey)
    return singularKey

def passwordGenerator(singularKey , length) :   #In this function the password will be genrated 
    password = []
    lenSingular = len(singularKey)
    
    passwordLen = lenSingular / length
    while  length > 0:   
        for i in singularKey :
            

key = input("Enter what you want to convert into password: ") 
key = key.replace(" ","")

length = input("Enter how long the password is required: ")
#length = len(updatedKey)
#print(asciiKey)
    #print(len(asciiKey))
    #print(type(asciiKey))
asciiKey = keyConvert(key)  #asciiKey is a list which contains  converted ascii values
singularKey = asciiConvert(asciiKey)
#lenSingular = len(singularKey)
password = passwordGenerator(singularKey,length)
