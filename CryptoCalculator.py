import logging
logging.basicConfig(level = logging.DEBUG)


def calculateV2():
    #user input a number
    print("Enter number of investments you made")
    numOfInvestments = int(input())
    count = 1

    #Make an empty List
    investmentList = [numOfInvestments]

    # while loop from 1 to = number
    while(count <= numOfInvestments):
        print("Enter investment number " + str(int(count)))
        investment = int(input())
        investmentList.append(investment)
        count+=1




#logging.debug(calculateV2())


def calculate():
    print("Hello! How much money did you invest into bitcoin?")
    investment = int(input())
    print("At was price?")
    initialPrice = int(input())
    print("What is the current price of bitcoin") #Later on we'll implement a scraper to grab the current price of bitcoin or whichever crypto!
    finalPrice = int(input())

    percentage = findPercentage(initialPrice,finalPrice)
    currValue = ((percentage) * investment) + investment

    if(currValue > investment):
        print("You're current bitcoin is worth: " + str(float(currValue)) + " Currently a net profit!")
    elif(currValue == investment):
        print("You're current bitcoin is worth: " + str(float(currValue)) + " You broke even.")
    else:
        print("You're current bitcoin is worth: " + str(float(currValue)) + " Currently a net loss.")



def findPercentage(initialPrice,finalPrice):
    decrease = float(finalPrice) - float(initialPrice)
    perc = (decrease/initialPrice) # I have to fix the math here, i assume!
    return perc

def getAverage(*list):
    sum = 0
    counter = 0
    for x in list:
        counter += 1
        sum += x
    return sum/counter
    
#logging.debug(getAverage(5,66,2))



#calculate()