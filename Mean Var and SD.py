import math

def sumSet(set):
    sumValue = sum(set)
    return sumValue

def findMean(set, sum):
    mean = sum/len(set)
    print("Mean of set =", mean)
    return mean

def findVariance(set, mean):
    sumval = 0
    for value in set:
        tempVal = value - mean
        sumval += tempVal**2
    sumvalSq = sumval
    var = sumvalSq/(len(set)-1)
    var = roundValue(var)
    print("Variance of set =", var)
    return var

def findSD(variance):
    sd = math.sqrt(variance)
    sd = roundValue(sd)
    print("Standard Deviation of the set =", sd)
    return sd

def roundValue(value):
    value = str(value)
    numLst = []
    pastDecimal = False
    numCount = 0
    index = 0
    for number in value:
        if number == ".":
            pastDecimal = True
            numLst.append(number)
            continue
        if pastDecimal == True:
            numCount+= 1
            if numCount == 8:
                #print("next", int(value[index+2]))
                #print("curr", int(value[index+1]))
                try:
                    value[index+2]
                except(IndexError):
                    numLst.append(number)
                    break
                if int(value[index+2]) >= 5:
                    number = int(number)
                    number += 1
                    number = str(number)
                    numLst.append(number)
                    break
                else:
                    numLst.append(number)
                    break
        index += 1
        numLst.append(number)
    #print(numLst)
    roundedNumber = ''
    for num in numLst:
        if num == ".":
            roundedNumber += "."
        else:
            roundedNumber += str(num)
    return(float(roundedNumber)) 


dataValue = input("Please enter a value or a list of values from the data set, seperated by a comma or space.\n")
for i in dataValue:
    if i.isdigit() == True:
        pass
    else:
        if i == " ":
            dataValues = dataValue.split(" ")
            break
        elif i == ",":
            dataValues = dataValue.split(",")
            break
#dataValues = dataValue.split(" ")
n = 0
for value in dataValues:
    dataValues[n] = float(value)
    n += 1
dataSum = sumSet(dataValues)
dataMean = findMean(dataValues, dataSum)
dataVariance = findVariance(dataValues, dataMean)
dataSD = findSD(dataVariance)
roundValue(dataSD)
