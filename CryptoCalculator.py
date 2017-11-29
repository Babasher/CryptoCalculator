import logging
logging.basicConfig(level = logging.DEBUG)

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
        print("You're current bitcoin is worth: " + str(float(currValue)) + " currently a net profit")
    elif(currValue == investment):
        print("You're current bitcoin is worth: " + str(float(currValue)) + " You broke even!")
    else:
        print("You're current bitcoin is worth: " + str(float(currValue)) + "currently a net loss")


def findPercentage(initialPrice,finalPrice):
    decrease = float(finalPrice) - float(initialPrice)
    perc = (decrease/initialPrice) # I have to fix the math here, i assume!
    return perc

logging.debug(calculate())
#logging.debug(findPercentage(9784,10236))