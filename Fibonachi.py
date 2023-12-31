#take an input and print the next few values that would follow that value in the fibbonachi sequence
#0,1,1,2,3,5,8,13,21... the sum of the two numbers before it.

pastFibNums = [0,1]

def findValue(value,currNum):
    pastFibNums.append(currNum)
    if currNum == value:
        return True
    else:
        return False
     
def findClosestValue(value):
    for num in range(len(pastFibNums)):
        counter = 0
        try:
            pastFibNums[num+1]
            while counter < (len(pastFibNums)-1):
                counter += 1
                if pastFibNums[num] < value and pastFibNums[num+1] > value:
                    p = value - pastFibNums[num]
                    q = pastFibNums[num+1] - value
                    if p < q:
                        print("The closest number to " + str(value) + " within the fibbonachi sequence is " + str(pastFibNums[num]) + ", which is the " + str(num-1)+ "th number in the series.")
                        quit()
                    elif q < p:
                        print("The closest number to " + str(value) + " within the fibbonachi sequence is " + str(pastFibNums[num+1]) + ", which is the " + str(num-1)+ "th number in the series.")
                        quit()
                else:
                    break
        except(IndexError):
            print("The closest number to " + str(value) + " within the fibbonachi sequence is " + str(pastFibNums[num]) + ", which is the last number in the series.")
            quit()

def fibsequence(value):
    x = 1
    y = 0
    if value == y:
        print(value, "was found in the first position of the fibbonachi sequence." )
        quit()
    elif value == x:
        print(value, "was duplicately found in the second and third position of the fibbonachi sequence." )
        quit()
    counter = 2
    while counter < 41:
        z = x + y
        y = x
        x = z
        counter += 1
        isValue = findValue(value,z)
        if isValue:
            print(value, "was found in the " + str(counter) + "th position of the fibbonachi sequence." )
            break
        elif counter == 40:
            print(value, "is not a member of the first 40 values in the fibbonachi sequence.")
            findClosestValue(value)
            quit()
        else:
            pass



inputVal = int(input("Enter the value you would like to find within the fibbonachi sequence.\n"))
fibsequence(inputVal)