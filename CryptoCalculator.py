import logging
logging.basicConfig(level=logging.DEBUG)

def calculateV2():
    # user input a number
    print("Enter number of investments you made")
    numOfInvestments = int(input())
    count = 1
    # Make an empty List
    cryptoPriceList = []
    print("cryptoPriceList: " + str(cryptoPriceList))
    investmentList = []
    print("Investment List: " + str(investmentList))
    # while loop from 1 to = number
    while (count <= numOfInvestments):
        print("What was the price of the Crypto currency at investment number " + str(int(count)))
        cryptoPrice = float(input())
        print("cryptoPrice:" + str(cryptoPrice))
        cryptoPriceList.append(cryptoPrice)
        print("PriceList Append:" + str(cryptoPriceList.append(cryptoPrice)))
        print("How much did you invest at investment number " + str(int(count)))
        userInvestment = float(input())
        print("User Investment: " + str(userInvestment))
        investmentList.append(userInvestment)
        print("Investment List Append: " + str(investmentList.append(userInvestment)))
        count += 1
    #get the average from the lists
    aveCryptoPrice = getAverage(cryptoPriceList)
    print("Average Crypto Price: " + str(aveCryptoPrice))
    aveUserInvestments = getAverage(investmentList)
    print("Average User Investments: " + str(aveUserInvestments))
    print(
        "What is the current price of Bitcoin?")  # Later on we'll implement a scraper to grab the current price of bitcoin or whichever crypto!
    finalPrice = float(input())
    print("Final Price: ${:,.2f}".format(finalPrice))
    percentage = findPercentage(aveCryptoPrice, finalPrice)
    print("Percentage Growth: {:.2f}%".format(percentage*100))
    currValue = ((percentage) * aveUserInvestments) + aveUserInvestments
    
    results(currValue, aveUserInvestments)

def results(x, y):
    if (x > y):
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net profit!".format(float(x)))
    elif (x == y):
        print("Your current bitcoin is worth: ${:,.2f}. You broke even.".format(float(x)))
    else:
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net loss.".format(float(x)))

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
        print("Your current bitcoin is worth: ${:,2f}. You broke even.".format(float(currValue)))
    else:
        print("Your current bitcoin is worth: ${:,.2f}. Currently a net loss.".format(float(currValue)))
def findPercentage(iPrice, fPrice):
    decrease = float(fPrice) - float(iPrice)
    perc = float(decrease) / float(iPrice)  # I have to fix the math here, I assume!
    return perc
def getAverage(*list):
    ave = sum(*list)/len(*list)
    print(*list)
    return ave
logging.debug(calculateV2())
