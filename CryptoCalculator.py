import logging
logging.basicConfig(level=logging.DEBUG)

def calculateV2():
    # user input a number
    print("Enter number of investments you made")
    numOfInvestments = int(input())
    count = 1

    # Make an empty List
    cryptoPriceList = [numOfInvestments]
    investmentList = [numOfInvestments]

    # while loop from 1 to = number
    while (count <= numOfInvestments):
        print("What was the price of the Crypto currency at investment number " + str(int(count)))
        cryptoPrice = int(input())
        cryptoPriceList.append(cryptoPrice)
        print("How much did you invest at investment number " + str(int(count)))
        userInvestment = int(input())
        investmentList.append(userInvestment)
        count += 1

    #get the average from the lists
    aveCryptoPrice = getAverage(cryptoPriceList)
    aveUserInvestments = getAverage(investmentList)

    print(
        "What is the current price of Bitcoin?")  # Later on we'll implement a scraper to grab the current price of bitcoin or whichever crypto!
    finalPrice = int(input())
    percentage = findPercentage(aveCryptoPrice, finalPrice)
    currValue = ((percentage) * aveUserInvestments) + aveUserInvestments

    if (currValue > aveUserInvestments):
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net profit!".format(float(currValue)))
    elif (currValue == aveUserInvestments):
        print("Your current bitcoin is worth: ${:,.2f}. You broke even.".format(float(currValue)))
    else:
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net loss.".format(float(currValue)))


def calculate():
    print("Hello! How much money did you invest into Bitcoin?")
    investment = int(input())
    print("At what price?")
    initialPrice = int(input())
    print(
        "What is the current price of Bitcoin?")  # Later on we'll implement a scraper to grab the current price of bitcoin or whichever crypto!
    finalPrice = int(input())

    percentage = findPercentage(initialPrice, finalPrice)
    currValue = ((percentage) * investment) + investment

    if (currValue > investment):
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net profit!".format(float(currValue)))
    elif (currValue == investment):
        print("Your current bitcoin is worth: ${:,.2f}. You broke even.".format(float(currValue)))
    else:
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net loss.".format(float(currValue)))
def findPercentage(iPrice, fPrice):
    decrease = float(fPrice) - float(iPrice)
    perc = float(decrease / iPrice)  # I have to fix the math here, I assume!
    return perc
def getAverage(*list):
    ave = sum(*list)/len(*list)
    return ave
logging.debug(calculateV2())

